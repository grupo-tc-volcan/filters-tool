# Third-party modules
import PyQt5.QtWidgets as QtWid
import PyQt5.QtCore as QtCore

import numpy as np

# filters-tool project modules
from app.designer.aux_widgets.cells_settings import Ui_CellsSettings
from app.designer.aux_widgets.comp_par_block_imp import CompParBlock
from app.cells.sallen_key import SallenKey, CellGroup
from app.cells.fleischer_tow import FleischerTow
from app.cells.active_first_order import ActiveFirstOrder

class CellsSettings(QtWid.QWidget, Ui_CellsSettings):

    def __init__(self, cell_data, display_action=None, report_action=None, *args, **kwargs):
        super(CellsSettings, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.cell_data = cell_data
        self.cell_designers = [ActiveFirstOrder(), SallenKey(), FleischerTow(), None, None, None, None, None]

        # Callback for displaying circuit
        if display_action is None:
            self.display_circuit_action = self.ignore_data_action
        else:
            self.display_circuit_action = display_action
        if display_action is None:
            self.report_action = self.ignore_data_action
        else:
            self.report_action = report_action


        self.check_available_cells()
        self.design_cell()

        # Signal and slot connections
        self.cell_selector.currentIndexChanged.connect(self.design_cell)
        self.report_button.released.connect(self.generate_report)


    def ignore_data_action(self, *args, **kwargs):
        pass


    def check_available_cells(self):
        cell_type = self.cell_data['type']
        gain = 10**(self.cell_data['gain_data']/20)

        # ActiveFirstOrder are inverters, therefore their module gain is negative 
        if self.cell_designers[0].is_valid_gain_mode(cell_type, -gain) and self.cell_data['pole']['n'] == 1:
            # Enable Compensated Derivator and Integrator
            variant_enable = QtCore.QVariant(1 | 32)
            self.cell_selector.setItemData(0, variant_enable, QtCore.Qt.UserRole - 1)
            self.cell_selector.setCurrentIndex(0)
        else:
            # Disable Compensated Derivator and Integrator
            variant_disable = QtCore.QVariant(0)
            self.cell_selector.setItemData(0, variant_disable, QtCore.Qt.UserRole - 1)

        if self.cell_designers[1].is_valid_gain_mode(cell_type, gain) and self.cell_data['pole']['n'] == 2:
            # Enable Sallen Key
            variant_enable = QtCore.QVariant(1 | 32)
            self.cell_selector.setItemData(1, variant_enable, QtCore.Qt.UserRole - 1)
            self.cell_selector.setCurrentIndex(1)
        else:
            # Disable Sallen Key
            variant_disable = QtCore.QVariant(0)
            self.cell_selector.setItemData(1, variant_disable, QtCore.Qt.UserRole - 1)

        if self.cell_designers[2].is_valid_gain_mode(cell_type, gain) and self.cell_data['pole']['n'] == 2:
            # Enable Fleischer Tow
            variant_enable = QtCore.QVariant(1 | 32)
            self.cell_selector.setItemData(2, variant_enable, QtCore.Qt.UserRole - 1)
            self.cell_selector.setCurrentIndex(2)
        else:
            # Disable Fleischer Tow
            variant_disable = QtCore.QVariant(0)
            self.cell_selector.setItemData(2, variant_disable, QtCore.Qt.UserRole - 1)

        # Disabeling the rest
        for i in range(self.cell_selector.count()):
            if i != 0 and i != 1 and i!= 2:
                # Disable
                variant_disable = QtCore.QVariant(0)
                self.cell_selector.setItemData(i, variant_disable, QtCore.Qt.UserRole - 1)


    def design_cell(self):
        # Designing cell
        cell_selected = self.cell_selector.currentIndex()
        cell_type = self.cell_data['type']
        gain = 10**(self.cell_data['gain_data']/20)
        if cell_selected == 0 or (cell_selected == 2 and cell_type != 'band-pass'):
            gain = -gain
        if self.cell_data['zero'] is not None:
            zeros = {
                'wz': self.cell_data['zero']['f0'] * 2*np.pi,
                'nz': self.cell_data['zero']['n'] 
            }
        else:
            zeros = None
        poles = {
            'wp': self.cell_data['pole']['fp'] * 2*np.pi,
            'qp': self.cell_data['pole']['q'] 
        }


        self.cell_designers[cell_selected].set_cell(cell_type, gain)
        self.cell_designers[cell_selected].design_components(zeros, poles, gain)

        # Adding components
        components = self.cell_designers[cell_selected].get_components()
        self.add_components(components)

        # Adding parameters and sensitivities
        zeros, poles, gain = self.cell_designers[cell_selected].get_parameters()
        sensitivities = self.cell_designers[cell_selected].get_sensitivities()
        self.add_parameters_and_sensitivies(zeros, poles, gain, sensitivities)

        # Displaying circuit
        path_to_circuit = self.cell_designers[cell_selected].get_circuit()
        self.display_circuit_action(path_to_circuit)

        
    def add_components(self, components):
        self.cell_components.clear()

        for component in components.keys():
            new_component_block = CompParBlock(self.update_components)
            new_component_block.comp.setText(component + ':')
            new_component_block.val.setValue(components[component] if components[component] is not None else 0)

            index = self.cell_components.count()

            new_item = QtWid.QListWidgetItem()
            new_item.setSizeHint(new_component_block.sizeHint())
            self.cell_components.insertItem(index, new_item)
            self.cell_components.setItemWidget(new_item, new_component_block)

    
    def add_parameters_and_sensitivies(self, zeros, poles, gain, sensitivities):
        self.cell_sensitivities.clear()
        
        if self.cell_data['zero'] is not None and zeros != {}:
            new_parameter_block = CompParBlock(self.update_components)
            new_parameter_block.comp.setText('f0:')
            new_parameter_block.val.setValue(zeros['wz'] / 2*np.pi)
            new_parameter_block.val.setReadOnly(True)
            new_item = QtWid.QListWidgetItem()
            new_item.setSizeHint(new_parameter_block.sizeHint())
            self.cell_sensitivities.insertItem(0, new_item)
            self.cell_sensitivities.setItemWidget(new_item, new_parameter_block)

        new_parameter_block = CompParBlock(self.update_components)
        new_parameter_block.comp.setText('fp:')
        new_parameter_block.val.setValue(poles['wp'] / 2*np.pi)
        new_parameter_block.val.setReadOnly(True)
        new_item = QtWid.QListWidgetItem()
        new_item.setSizeHint(new_parameter_block.sizeHint())
        self.cell_sensitivities.insertItem(1, new_item)
        self.cell_sensitivities.setItemWidget(new_item, new_parameter_block)

        if self.cell_data['pole']['n'] == 2:
            new_parameter_block = CompParBlock(self.update_components)
            new_parameter_block.comp.setText('Q:')
            new_parameter_block.val.setValue(poles['qp'])
            new_parameter_block.val.setReadOnly(True)
            new_item = QtWid.QListWidgetItem()
            new_item.setSizeHint(new_parameter_block.sizeHint())
            self.cell_sensitivities.insertItem(2, new_item)
            self.cell_sensitivities.setItemWidget(new_item, new_parameter_block)

        for sensitivity in sensitivities.keys():
            for parameter in sensitivities[sensitivity]:
                new_component_block = CompParBlock(self.update_components)
                new_component_block.comp.setText('S' + sensitivity + '->' + parameter + ':')
                new_component_block.val.setValue(sensitivities[sensitivity][parameter])
                new_component_block.val.setReadOnly(True)

                index = self.cell_sensitivities.count()

                new_item = QtWid.QListWidgetItem()
                new_item.setSizeHint(new_component_block.sizeHint())
                self.cell_sensitivities.insertItem(index, new_item)
                self.cell_sensitivities.setItemWidget(new_item, new_component_block)


    def update_components(self, component, value):
        cell_selected = self.cell_selector.currentIndex()

        components = self.cell_designers[cell_selected].get_components()
        components[component.split(':')[0]] = value

        # Adding parameters and sensitivities
        zeros, poles, gain = self.cell_designers[cell_selected].get_parameters()
        sensitivities = self.cell_designers[cell_selected].get_sensitivities()
        self.add_parameters_and_sensitivies(zeros, poles, gain, sensitivities)

        # Displaying circuit
        path_to_circuit = self.cell_designers[cell_selected].get_circuit()
        self.display_circuit_action(path_to_circuit)


    def generate_report(self):
        self.report_action()