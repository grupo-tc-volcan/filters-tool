# Third-party modules
import PyQt5.QtWidgets as QtWid

# filters-tool project modules
from app.designer.filters_data.group_delay import Ui_GroupDelayData
from app.approximators.butterworth import ButterworthApprox
from app.approximators.chebyshev_i import ChebyshevIApprox
from app.approximators.chebyshev_ii import ChebyshevIIApprox
from app.approximators.legendre import LegendreApprox
from app.approximators.bessel import BesselApprox
from app.approximators.gauss import GaussApprox
from app.approximators.cauer import CauerApprox

class GroupDelayData(QtWid.QWidget, Ui_GroupDelayData):

    def __init__(self, *args, **kwargs):
        super(GroupDelayData, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Approximators for passing data to
        self.approximators = [ButterworthApprox(), ChebyshevIApprox(), ChebyshevIIApprox(), LegendreApprox(), BesselApprox(), GaussApprox(), CauerApprox()]
        self.approx_index = 4

        # Signal and slot connections
        self.gain.valueChanged.connect(self.on_change)
        self.stop_freq.valueChanged.connect(self.on_change)
        self.stop_att.valueChanged.connect(self.on_change)
        self.group_delay_freq.valueChanged.connect(self.on_change)
        self.group_delay.valueChanged.connect(self.on_change)
        self.tol.valueChanged.connect(self.on_change)
        self.order.valueChanged.connect(self.on_change)
        self.q_max.valueChanged.connect(self.on_change)
        self.order_fixed.stateChanged.connect(self.on_change)
        self.q_fixed.stateChanged.connect(self.on_change)

        self.on_change()


    def on_change(self):
        if self.order_fixed.isChecked():
            if self.approx_index == 6:
                # Cauer filter needs the stopband attenuation data
                self.stop_att.setEnabled(True)
            elif self.approx_index == 2:
                # Cheby 2 needs the stopband attenuation instead of the passband attenuation
                self.stop_att.setEnabled(True)
            else:
                self.stop_att.setDisabled(True)

            if self.approx_index == 2:
                # Cheby 2 needs the stopband frequency instead of the passband frequency
                self.stop_freq.setEnabled(True)
            else:
                self.stop_freq.setDisabled(True)

            self.tol.setDisabled(True)
            self.order.setEnabled(True)
            self.q_fixed.setDisabled(True)

        elif self.q_fixed.isChecked():
            if self.approx_index == 6:
                # Cauer filter needs the stopband attenuation data
                self.stop_att.setEnabled(True)
            elif self.approx_index == 2:
                # Cheby 2 needs the stopband attenuation instead of the passband attenuation
                self.stop_att.setEnabled(True)
            else:
                self.stop_att.setDisabled(True)

            if self.approx_index == 2:
                # Cheby 2 needs the stopband frequency instead of the passband frequency
                self.stop_freq.setEnabled(True)
            else:
                self.stop_freq.setDisabled(True)

            self.tol.setDisabled(True)
            self.q_max.setEnabled(True)
            self.order_fixed.setDisabled(True)

        else:
            self.tol.setEnabled(True)
            self.order.setDisabled(True)
            self.q_max.setDisabled(True)
            self.stop_freq.setEnabled(True)
            self.stop_att.setEnabled(True)
            self.order_fixed.setEnabled(True)
            self.q_fixed.setEnabled(True)
            self.q_max.setValue(0)
            self.order.setValue(0)

        self.approximators[self.approx_index].type = 'group-delay'
        self.approximators[self.approx_index].gain = self.gain.value()
        self.approximators[self.approx_index].fa = self.stop_freq.value()
        self.approximators[self.approx_index].Aa = self.stop_att.value()
        self.approximators[self.approx_index].ft = self.group_delay_freq.value()
        self.approximators[self.approx_index].group_delay = self.group_delay.value()
        self.approximators[self.approx_index].tol = self.tol.value()
        self.approximators[self.approx_index].ord = self.order.value()
        self.approximators[self.approx_index].q = self.q_max.value()