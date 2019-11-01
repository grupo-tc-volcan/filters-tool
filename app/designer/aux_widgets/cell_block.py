# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cell_block.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CellBlock(object):
    def setupUi(self, CellBlock):
        CellBlock.setObjectName("CellBlock")
        CellBlock.resize(300, 200)
        CellBlock.setMaximumSize(QtCore.QSize(300, 200))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        CellBlock.setFont(font)
        CellBlock.setAcceptDrops(True)
        CellBlock.setAutoFillBackground(False)
        self.gridLayout = QtWidgets.QGridLayout(CellBlock)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(CellBlock)
        self.frame.setAcceptDrops(False)
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(1)
        self.frame.setMidLineWidth(1)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 3, 3, 1, 1)
        self.label_74 = QtWidgets.QLabel(self.frame)
        self.label_74.setMaximumSize(QtCore.QSize(93, 16777215))
        self.label_74.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_74.setObjectName("label_74")
        self.gridLayout_2.addWidget(self.label_74, 5, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 3, 1, 1)
        self.label_78 = QtWidgets.QLabel(self.frame)
        self.label_78.setMaximumSize(QtCore.QSize(93, 16777215))
        self.label_78.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_78.setObjectName("label_78")
        self.gridLayout_2.addWidget(self.label_78, 5, 0, 1, 1)
        self.fp = QtWidgets.QLabel(self.frame)
        self.fp.setObjectName("fp")
        self.gridLayout_2.addWidget(self.fp, 2, 1, 1, 1)
        self.n0 = QtWidgets.QLabel(self.frame)
        self.n0.setObjectName("n0")
        self.gridLayout_2.addWidget(self.n0, 3, 4, 1, 1)
        self.v_min = QtWidgets.QDoubleSpinBox(self.frame)
        self.v_min.setMaximumSize(QtCore.QSize(93, 16777215))
        self.v_min.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.v_min.setDecimals(2)
        self.v_min.setObjectName("v_min")
        self.gridLayout_2.addWidget(self.v_min, 5, 1, 1, 1)
        self.v_max = QtWidgets.QDoubleSpinBox(self.frame)
        self.v_max.setMaximumSize(QtCore.QSize(93, 16777215))
        self.v_max.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.v_max.setDecimals(2)
        self.v_max.setObjectName("v_max")
        self.gridLayout_2.addWidget(self.v_max, 5, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.f0 = QtWidgets.QLabel(self.frame)
        self.f0.setMaximumSize(QtCore.QSize(16777215, 20))
        self.f0.setObjectName("f0")
        self.gridLayout_2.addWidget(self.f0, 2, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.type = QtWidgets.QLabel(self.frame)
        self.type.setObjectName("type")
        self.gridLayout_2.addWidget(self.type, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 3, 1, 1)
        self.q_val = QtWidgets.QLabel(self.frame)
        self.q_val.setObjectName("q_val")
        self.gridLayout_2.addWidget(self.q_val, 0, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 3, 0, 1, 1)
        self.np = QtWidgets.QLabel(self.frame)
        self.np.setObjectName("np")
        self.gridLayout_2.addWidget(self.np, 3, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setAcceptDrops(True)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 6, 0, 1, 1)
        self.dynamic_range = QtWidgets.QLabel(self.frame)
        self.dynamic_range.setObjectName("dynamic_range")
        self.gridLayout_2.addWidget(self.dynamic_range, 6, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 6, 3, 1, 1)
        self.gain = QtWidgets.QDoubleSpinBox(self.frame)
        self.gain.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.gain.setDecimals(2)
        self.gain.setMinimum(-300.0)
        self.gain.setMaximum(300.0)
        self.gain.setObjectName("gain")
        self.gridLayout_2.addWidget(self.gain, 6, 4, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)

        self.retranslateUi(CellBlock)
        QtCore.QMetaObject.connectSlotsByName(CellBlock)

    def retranslateUi(self, CellBlock):
        _translate = QtCore.QCoreApplication.translate
        CellBlock.setWindowTitle(_translate("CellBlock", "Form"))
        self.label_5.setText(_translate("CellBlock", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt; font-weight:600;\">n</span><span style=\" font-size:10pt; font-weight:600; vertical-align:sub;\">0</span><span style=\" font-size:10pt; font-weight:600;\">:</span></p></body></html>"))
        self.label_74.setText(_translate("CellBlock", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt; font-weight:600;\">V</span><span style=\" font-size:10pt; font-weight:600; vertical-align:sub;\">max</span></p></body></html>"))
        self.label_7.setText(_translate("CellBlock", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt; font-weight:600;\">f</span><span style=\" font-size:10pt; font-weight:600; vertical-align:sub;\">0</span><span style=\" font-size:10pt; font-weight:600;\">:</span></p></body></html>"))
        self.label_78.setText(_translate("CellBlock", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt; font-weight:600;\">V</span><span style=\" font-size:10pt; font-weight:600; vertical-align:sub;\">min</span></p></body></html>"))
        self.fp.setText(_translate("CellBlock", "<html><head/><body><p><span style=\" font-size:10pt;\">...</span></p></body></html>"))
        self.n0.setText(_translate("CellBlock", "<html><head/><body><p><span style=\" font-size:10pt;\">...</span></p></body></html>"))
        self.v_min.setSuffix(_translate("CellBlock", "V"))
        self.v_max.setSuffix(_translate("CellBlock", "V"))
        self.label_3.setText(_translate("CellBlock", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt; font-weight:600;\">f</span><span style=\" font-size:10pt; font-weight:600; vertical-align:sub;\">p</span><span style=\" font-size:10pt; font-weight:600;\">:</span></p></body></html>"))
        self.f0.setText(_translate("CellBlock", "<html><head/><body><p><span style=\" font-size:10pt;\">...</span></p></body></html>"))
        self.label_2.setText(_translate("CellBlock", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt; font-weight:600;\">Type:</span></p></body></html>"))
        self.type.setText(_translate("CellBlock", "<html><head/><body><p><span style=\" font-size:10pt;\">...</span></p></body></html>"))
        self.label_4.setText(_translate("CellBlock", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt; font-weight:600;\">Q:</span></p></body></html>"))
        self.q_val.setText(_translate("CellBlock", "<html><head/><body><p><span style=\" font-size:10pt;\">...</span></p></body></html>"))
        self.label.setText(_translate("CellBlock", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt; font-weight:600;\">n</span><span style=\" font-size:10pt; font-weight:600; vertical-align:sub;\">p</span><span style=\" font-size:10pt; font-weight:600;\">:</span></p></body></html>"))
        self.np.setText(_translate("CellBlock", "<html><head/><body><p><span style=\" font-size:10pt;\">...</span></p></body></html>"))
        self.label_6.setText(_translate("CellBlock", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt; font-weight:600;\">DR:</span></p></body></html>"))
        self.dynamic_range.setText(_translate("CellBlock", "<html><head/><body><p><span style=\" font-size:10pt;\">...</span></p></body></html>"))
        self.label_8.setText(_translate("CellBlock", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt;\">Gain:</span></p></body></html>"))
        self.gain.setSuffix(_translate("CellBlock", "dB"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CellBlock = QtWidgets.QWidget()
    ui = Ui_CellBlock()
    ui.setupUi(CellBlock)
    CellBlock.show()
    sys.exit(app.exec_())
