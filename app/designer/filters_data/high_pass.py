# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'high_pass.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HighPassData(object):
    def setupUi(self, HighPassData):
        HighPassData.setObjectName("HighPassData")
        HighPassData.resize(311, 408)
        self.gridLayout = QtWidgets.QGridLayout(HighPassData)
        self.gridLayout.setObjectName("gridLayout")
        self.label_9 = QtWidgets.QLabel(HighPassData)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 5, 0, 1, 2)
        self.stop_att = QtWidgets.QDoubleSpinBox(HighPassData)
        self.stop_att.setFrame(True)
        self.stop_att.setAlignment(QtCore.Qt.AlignCenter)
        self.stop_att.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.stop_att.setKeyboardTracking(True)
        self.stop_att.setDecimals(3)
        self.stop_att.setObjectName("stop_att")
        self.gridLayout.addWidget(self.stop_att, 5, 2, 1, 1)
        self.pass_freq = QtWidgets.QDoubleSpinBox(HighPassData)
        self.pass_freq.setFrame(True)
        self.pass_freq.setAlignment(QtCore.Qt.AlignCenter)
        self.pass_freq.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.pass_freq.setKeyboardTracking(True)
        self.pass_freq.setDecimals(3)
        self.pass_freq.setObjectName("pass_freq")
        self.gridLayout.addWidget(self.pass_freq, 2, 2, 1, 1)
        self.pass_att = QtWidgets.QDoubleSpinBox(HighPassData)
        self.pass_att.setFrame(True)
        self.pass_att.setAlignment(QtCore.Qt.AlignCenter)
        self.pass_att.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.pass_att.setKeyboardTracking(True)
        self.pass_att.setDecimals(3)
        self.pass_att.setObjectName("pass_att")
        self.gridLayout.addWidget(self.pass_att, 4, 2, 1, 1)
        self.gain = QtWidgets.QDoubleSpinBox(HighPassData)
        self.gain.setFrame(True)
        self.gain.setAlignment(QtCore.Qt.AlignCenter)
        self.gain.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.gain.setKeyboardTracking(True)
        self.gain.setDecimals(3)
        self.gain.setObjectName("gain")
        self.gridLayout.addWidget(self.gain, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(HighPassData)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(HighPassData)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 5, 3, 1, 1)
        self.label = QtWidgets.QLabel(HighPassData)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(HighPassData)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(HighPassData)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(HighPassData)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 2)
        self.label_8 = QtWidgets.QLabel(HighPassData)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 4, 3, 1, 1)
        self.label_12 = QtWidgets.QLabel(HighPassData)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 6, 3, 1, 1)
        self.label_13 = QtWidgets.QLabel(HighPassData)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 7, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(HighPassData)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 6, 0, 1, 1)
        self.order_fixed = QtWidgets.QCheckBox(HighPassData)
        self.order_fixed.setObjectName("order_fixed")
        self.gridLayout.addWidget(self.order_fixed, 7, 1, 1, 1)
        self.denorm_select = QtWidgets.QComboBox(HighPassData)
        self.denorm_select.setObjectName("denorm_select")
        self.denorm_select.addItem("")
        self.denorm_select.addItem("")
        self.denorm_select.addItem("")
        self.gridLayout.addWidget(self.denorm_select, 6, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(HighPassData)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 8, 0, 1, 1)
        self.denorm_perc = QtWidgets.QDoubleSpinBox(HighPassData)
        self.denorm_perc.setFrame(True)
        self.denorm_perc.setAlignment(QtCore.Qt.AlignCenter)
        self.denorm_perc.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.denorm_perc.setKeyboardTracking(True)
        self.denorm_perc.setDecimals(3)
        self.denorm_perc.setObjectName("denorm_perc")
        self.gridLayout.addWidget(self.denorm_perc, 6, 2, 1, 1)
        self.q_fixed = QtWidgets.QCheckBox(HighPassData)
        self.q_fixed.setObjectName("q_fixed")
        self.gridLayout.addWidget(self.q_fixed, 8, 1, 1, 1)
        self.order = QtWidgets.QDoubleSpinBox(HighPassData)
        self.order.setFrame(True)
        self.order.setAlignment(QtCore.Qt.AlignCenter)
        self.order.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.order.setKeyboardTracking(True)
        self.order.setDecimals(3)
        self.order.setObjectName("order")
        self.gridLayout.addWidget(self.order, 7, 2, 1, 1)
        self.q_max = QtWidgets.QDoubleSpinBox(HighPassData)
        self.q_max.setFrame(True)
        self.q_max.setAlignment(QtCore.Qt.AlignCenter)
        self.q_max.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.q_max.setKeyboardTracking(True)
        self.q_max.setDecimals(3)
        self.q_max.setObjectName("q_max")
        self.gridLayout.addWidget(self.q_max, 8, 2, 1, 1)
        self.stop_freq = QtWidgets.QDoubleSpinBox(HighPassData)
        self.stop_freq.setFrame(True)
        self.stop_freq.setAlignment(QtCore.Qt.AlignCenter)
        self.stop_freq.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.stop_freq.setKeyboardTracking(True)
        self.stop_freq.setDecimals(3)
        self.stop_freq.setObjectName("stop_freq")
        self.gridLayout.addWidget(self.stop_freq, 1, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(HighPassData)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(HighPassData)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 2)

        self.retranslateUi(HighPassData)
        QtCore.QMetaObject.connectSlotsByName(HighPassData)

    def retranslateUi(self, HighPassData):
        _translate = QtCore.QCoreApplication.translate
        HighPassData.setWindowTitle(_translate("HighPassData", "Form"))
        self.label_9.setText(_translate("HighPassData", "Stopband Att. (Aa):"))
        self.label_4.setText(_translate("HighPassData", "Hz"))
        self.label_10.setText(_translate("HighPassData", "dB"))
        self.label.setText(_translate("HighPassData", "Gain (G):"))
        self.label_2.setText(_translate("HighPassData", "dB"))
        self.label_7.setText(_translate("HighPassData", "Passband Att. (Ap):"))
        self.label_3.setText(_translate("HighPassData", "Passband freq. (fp):"))
        self.label_8.setText(_translate("HighPassData", "dB"))
        self.label_12.setText(_translate("HighPassData", "%"))
        self.label_13.setText(_translate("HighPassData", "Filter order:"))
        self.label_11.setText(_translate("HighPassData", "Denorm.:"))
        self.order_fixed.setText(_translate("HighPassData", "Fixed:"))
        self.denorm_select.setItemText(0, _translate("HighPassData", "fp"))
        self.denorm_select.setItemText(1, _translate("HighPassData", "fa"))
        self.denorm_select.setItemText(2, _translate("HighPassData", "Other freq."))
        self.label_15.setText(_translate("HighPassData", "Max Q:"))
        self.q_fixed.setText(_translate("HighPassData", "Fixed:"))
        self.label_6.setText(_translate("HighPassData", "Hz"))
        self.label_5.setText(_translate("HighPassData", "Stopband freq. (fa):"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HighPassData = QtWidgets.QWidget()
    ui = Ui_HighPassData()
    ui.setupUi(HighPassData)
    HighPassData.show()
    sys.exit(app.exec_())