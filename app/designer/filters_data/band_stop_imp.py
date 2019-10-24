# Third-party modules
import PyQt5.QtWidgets as QtWid

# filters-tool project modules
from app.designer.filters_data.band_stop import Ui_BandStopData
from app.approximators.butterworth import ButterworthApprox
from app.approximators.chebyshev_i import ChebyshevIAprrox
from app.approximators.chebyshev_ii import ChebyshevIIApprox
from app.approximators.legendre import LegendreApprox
from app.approximators.bessel import BesselApprox
from app.approximators.gauss import GaussApprox
from app.approximators.cauer import CauerApprox

class BandStopData(QtWid.QWidget, Ui_BandStopData):

    def __init__(self, *args, **kwargs):
        super(BandStopData, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Approximators for passing data to
        self.approximators = [ButterworthApprox(), ChebyshevIAprrox(), ChebyshevIIApprox(), LegendreApprox(), BesselApprox(), GaussApprox(), CauerApprox()]
        self.approx_index = 0

        # Signal and slot connections
        self.gain.valueChanged.connect(self.on_change)
        self.pass_freq_l.valueChanged.connect(self.on_change)
        self.pass_freq_r.valueChanged.connect(self.on_change)
        self.stop_freq_l.valueChanged.connect(self.on_change)
        self.stop_freq_r.valueChanged.connect(self.on_change)
        self.pass_att_l.valueChanged.connect(self.on_change)
        self.pass_att_r.valueChanged.connect(self.on_change)
        self.stop_att.valueChanged.connect(self.on_change)
        self.stop_att.valueChanged.connect(self.on_change)
        self.denorm_perc.valueChanged.connect(self.on_change)
        self.order.valueChanged.connect(self.on_change)
        self.q_max.valueChanged.connect(self.on_change)
        self.denorm_select.currentIndexChanged.connect(self.on_change)
        self.order_fixed.stateChanged.connect(self.on_change)
        self.q_fixed.stateChanged.connect(self.on_change)

        self.on_change()


    def on_change(self):
        if self.order_fixed.isChecked():
            self.order.setEnabled(True)
        else:
            self.order.setDisabled(True)

        if self.q_fixed.isChecked():
            self.q_max.setEnabled(True)
        else:
            self.q_max.setDisabled(True)

        if self.denorm_select.currentIndex() != 2:
            self.denorm_perc.setDisabled(True)
        else:
            self.denorm_perc.setEnabled(True)
        if self.denorm_select.currentIndex() == 0:
            self.denorm_perc.setValue(0)
        elif self.denorm_select.currentIndex() ==1:
            self.denorm_perc.setValue(100)

        self.approximators[self.approx_index].type = 'band-stop'
        self.approximators[self.approx_index].gain = self.gain.value()
        self.approximators[self.approx_index].fpl = self.pass_freq_l.value()
        self.approximators[self.approx_index].fpr = self.pass_freq_r.value()
        self.approximators[self.approx_index].fal = self.stop_freq_l.value()
        self.approximators[self.approx_index].far = self.stop_freq_r.value()
        self.approximators[self.approx_index].Apl = self.pass_att_l.value()
        self.approximators[self.approx_index].Apr = self.pass_att_r.value()
        self.approximators[self.approx_index].Aal = self.stop_att.value()
        self.approximators[self.approx_index].denorm = self.denorm_perc.value()
        self.approximators[self.approx_index].ord = self.order.value()
        self.approximators[self.approx_index].q = self.q_max.value()