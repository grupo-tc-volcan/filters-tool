# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'band_pass.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BandPassData(object):
    def setupUi(self, BandPassData):
        BandPassData.setObjectName("BandPassData")
        BandPassData.resize(290, 408)
        BandPassData.setMaximumSize(QtCore.QSize(290, 16777215))
        self.gridLayout = QtWidgets.QGridLayout(BandPassData)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(BandPassData)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 6, 1, 1)
        self.label_14 = QtWidgets.QLabel(BandPassData)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 1, 0, 1, 2)
        self.label = QtWidgets.QLabel(BandPassData)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(BandPassData)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 3, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(BandPassData)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 6, 1, 1)
        self.label_3 = QtWidgets.QLabel(BandPassData)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 2)
        self.label_16 = QtWidgets.QLabel(BandPassData)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 1, 6, 1, 1)
        self.label_20 = QtWidgets.QLabel(BandPassData)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 7, 0, 1, 2)
        self.denorm_select = QtWidgets.QComboBox(BandPassData)
        self.denorm_select.setObjectName("denorm_select")
        self.denorm_select.addItem("")
        self.denorm_select.addItem("")
        self.denorm_select.addItem("")
        self.gridLayout.addWidget(self.denorm_select, 11, 1, 1, 1)
        self.q_fixed = QtWidgets.QCheckBox(BandPassData)
        self.q_fixed.setAutoExclusive(False)
        self.q_fixed.setObjectName("q_fixed")
        self.gridLayout.addWidget(self.q_fixed, 13, 1, 1, 1)
        self.stop_freq_l = QtWidgets.QDoubleSpinBox(BandPassData)
        self.stop_freq_l.setFrame(True)
        self.stop_freq_l.setAlignment(QtCore.Qt.AlignCenter)
        self.stop_freq_l.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.stop_freq_l.setKeyboardTracking(True)
        self.stop_freq_l.setDecimals(3)
        self.stop_freq_l.setMaximum(1000000000000.0)
        self.stop_freq_l.setProperty("value", 100.0)
        self.stop_freq_l.setObjectName("stop_freq_l")
        self.gridLayout.addWidget(self.stop_freq_l, 1, 3, 1, 1)
        self.label_15 = QtWidgets.QLabel(BandPassData)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 13, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(BandPassData)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 3)
        self.label_11 = QtWidgets.QLabel(BandPassData)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 11, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(BandPassData)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 6, 1, 1)
        self.label_12 = QtWidgets.QLabel(BandPassData)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 11, 6, 1, 1)
        self.label_13 = QtWidgets.QLabel(BandPassData)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 12, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(BandPassData)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 6, 0, 1, 2)
        self.gain = QtWidgets.QDoubleSpinBox(BandPassData)
        self.gain.setFrame(True)
        self.gain.setAlignment(QtCore.Qt.AlignCenter)
        self.gain.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.gain.setKeyboardTracking(True)
        self.gain.setDecimals(3)
        self.gain.setMaximum(300.0)
        self.gain.setProperty("value", 5.0)
        self.gain.setObjectName("gain")
        self.gridLayout.addWidget(self.gain, 0, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(BandPassData)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 6, 6, 1, 1)
        self.order_fixed = QtWidgets.QCheckBox(BandPassData)
        self.order_fixed.setAutoExclusive(False)
        self.order_fixed.setObjectName("order_fixed")
        self.gridLayout.addWidget(self.order_fixed, 12, 1, 1, 1)
        self.stop_freq_r = QtWidgets.QDoubleSpinBox(BandPassData)
        self.stop_freq_r.setFrame(True)
        self.stop_freq_r.setAlignment(QtCore.Qt.AlignCenter)
        self.stop_freq_r.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.stop_freq_r.setKeyboardTracking(True)
        self.stop_freq_r.setDecimals(3)
        self.stop_freq_r.setMaximum(1000000000000.0)
        self.stop_freq_r.setProperty("value", 100000.0)
        self.stop_freq_r.setObjectName("stop_freq_r")
        self.gridLayout.addWidget(self.stop_freq_r, 4, 3, 1, 1)
        self.pass_freq_l = QtWidgets.QDoubleSpinBox(BandPassData)
        self.pass_freq_l.setFrame(True)
        self.pass_freq_l.setAlignment(QtCore.Qt.AlignCenter)
        self.pass_freq_l.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.pass_freq_l.setKeyboardTracking(True)
        self.pass_freq_l.setDecimals(3)
        self.pass_freq_l.setMaximum(1000000000000.0)
        self.pass_freq_l.setProperty("value", 1000.0)
        self.pass_freq_l.setObjectName("pass_freq_l")
        self.gridLayout.addWidget(self.pass_freq_l, 2, 3, 1, 1)
        self.label_18 = QtWidgets.QLabel(BandPassData)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 3, 6, 1, 1)
        self.pass_freq_r = QtWidgets.QDoubleSpinBox(BandPassData)
        self.pass_freq_r.setFrame(True)
        self.pass_freq_r.setAlignment(QtCore.Qt.AlignCenter)
        self.pass_freq_r.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.pass_freq_r.setKeyboardTracking(True)
        self.pass_freq_r.setDecimals(3)
        self.pass_freq_r.setMaximum(10000000000000.0)
        self.pass_freq_r.setProperty("value", 10000.0)
        self.pass_freq_r.setObjectName("pass_freq_r")
        self.gridLayout.addWidget(self.pass_freq_r, 3, 3, 1, 1)
        self.q_max = QtWidgets.QDoubleSpinBox(BandPassData)
        self.q_max.setFrame(True)
        self.q_max.setAlignment(QtCore.Qt.AlignCenter)
        self.q_max.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.q_max.setKeyboardTracking(True)
        self.q_max.setDecimals(3)
        self.q_max.setMaximum(100.0)
        self.q_max.setObjectName("q_max")
        self.gridLayout.addWidget(self.q_max, 13, 3, 1, 1)
        self.stop_att_r = QtWidgets.QDoubleSpinBox(BandPassData)
        self.stop_att_r.setFrame(True)
        self.stop_att_r.setAlignment(QtCore.Qt.AlignCenter)
        self.stop_att_r.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.stop_att_r.setKeyboardTracking(True)
        self.stop_att_r.setDecimals(3)
        self.stop_att_r.setMaximum(300.0)
        self.stop_att_r.setProperty("value", 40.0)
        self.stop_att_r.setObjectName("stop_att_r")
        self.gridLayout.addWidget(self.stop_att_r, 7, 3, 1, 1)
        self.label_19 = QtWidgets.QLabel(BandPassData)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 7, 6, 1, 1)
        self.stop_att_l = QtWidgets.QDoubleSpinBox(BandPassData)
        self.stop_att_l.setFrame(True)
        self.stop_att_l.setAlignment(QtCore.Qt.AlignCenter)
        self.stop_att_l.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.stop_att_l.setKeyboardTracking(True)
        self.stop_att_l.setDecimals(3)
        self.stop_att_l.setMaximum(300.0)
        self.stop_att_l.setProperty("value", 30.0)
        self.stop_att_l.setObjectName("stop_att_l")
        self.gridLayout.addWidget(self.stop_att_l, 6, 3, 1, 1)
        self.denorm_perc = QtWidgets.QDoubleSpinBox(BandPassData)
        self.denorm_perc.setFrame(True)
        self.denorm_perc.setAlignment(QtCore.Qt.AlignCenter)
        self.denorm_perc.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.denorm_perc.setKeyboardTracking(True)
        self.denorm_perc.setDecimals(3)
        self.denorm_perc.setMaximum(100.0)
        self.denorm_perc.setObjectName("denorm_perc")
        self.gridLayout.addWidget(self.denorm_perc, 11, 3, 1, 1)
        self.pass_att = QtWidgets.QDoubleSpinBox(BandPassData)
        self.pass_att.setFrame(True)
        self.pass_att.setAlignment(QtCore.Qt.AlignCenter)
        self.pass_att.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.pass_att.setKeyboardTracking(True)
        self.pass_att.setDecimals(3)
        self.pass_att.setMaximum(300.0)
        self.pass_att.setProperty("value", 1.0)
        self.pass_att.setObjectName("pass_att")
        self.gridLayout.addWidget(self.pass_att, 8, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(BandPassData)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 8, 6, 1, 1)
        self.label_7 = QtWidgets.QLabel(BandPassData)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 8, 0, 1, 2)
        self.order = QtWidgets.QSpinBox(BandPassData)
        self.order.setFrame(True)
        self.order.setAlignment(QtCore.Qt.AlignCenter)
        self.order.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.order.setKeyboardTracking(True)
        self.order.setMaximum(20)
        self.order.setObjectName("order")
        self.gridLayout.addWidget(self.order, 12, 3, 1, 1)

        self.retranslateUi(BandPassData)
        QtCore.QMetaObject.connectSlotsByName(BandPassData)

    def retranslateUi(self, BandPassData):
        _translate = QtCore.QCoreApplication.translate
        BandPassData.setWindowTitle(_translate("BandPassData", "Form"))
        self.label_2.setText(_translate("BandPassData", "dB"))
        self.label_14.setText(_translate("BandPassData", "Stopband freq. - (fa-):"))
        self.label.setText(_translate("BandPassData", "Gain (G):"))
        self.label_17.setText(_translate("BandPassData", "Passband freq. + (fp+):"))
        self.label_4.setText(_translate("BandPassData", "Hz"))
        self.label_3.setText(_translate("BandPassData", "Passband freq. - (fp-):"))
        self.label_16.setText(_translate("BandPassData", "Hz"))
        self.label_20.setText(_translate("BandPassData", "Stopband Att. + (Aa+):"))
        self.denorm_select.setItemText(0, _translate("BandPassData", "fp"))
        self.denorm_select.setItemText(1, _translate("BandPassData", "fa"))
        self.denorm_select.setItemText(2, _translate("BandPassData", "Other freq."))
        self.q_fixed.setText(_translate("BandPassData", "Fixed:"))
        self.label_15.setText(_translate("BandPassData", "Max Q:"))
        self.label_5.setText(_translate("BandPassData", "Stopband freq. + (fa+):"))
        self.label_11.setText(_translate("BandPassData", "Denorm.:"))
        self.label_6.setText(_translate("BandPassData", "Hz"))
        self.label_12.setText(_translate("BandPassData", "%"))
        self.label_13.setText(_translate("BandPassData", "Filter order:"))
        self.label_9.setText(_translate("BandPassData", "Stopband Att. - (Aa-):"))
        self.label_10.setText(_translate("BandPassData", "dB"))
        self.order_fixed.setText(_translate("BandPassData", "Fixed:"))
        self.label_18.setText(_translate("BandPassData", "Hz"))
        self.label_19.setText(_translate("BandPassData", "dB"))
        self.label_8.setText(_translate("BandPassData", "dB"))
        self.label_7.setText(_translate("BandPassData", "Passband Att. (Ap):"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BandPassData = QtWidgets.QWidget()
    ui = Ui_BandPassData()
    ui.setupUi(BandPassData)
    BandPassData.show()
    sys.exit(app.exec_())
