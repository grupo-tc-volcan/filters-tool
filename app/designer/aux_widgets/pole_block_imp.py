# Third-party modules
import PyQt5.QtWidgets as QtWid
import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore

# filters-tool project modules
from app.designer.aux_widgets.pole_block import Ui_PoleBlock

class PoleBlock(QtWid.QWidget, Ui_PoleBlock):

    def __init__(self, *args, **kwargs):
        super(PoleBlock, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.pass_data_action = self.ignore_data_action


    def ignore_data_action(self, *args, **kwargs):
        pass


    def mousePressEvent(self, ev):
        super(PoleBlock, self).mousePressEvent(ev)

        data_dragged = {
            'fp': self.fp.text(),
            'q': self.q_val.text(),
            'n': self.order.text()
        }
        self.pass_data_action(data_dragged, self)