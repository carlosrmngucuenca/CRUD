# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WMantenimientoCategorias.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_FormMantenimientoCategorias(object):
    def setupUi(self, FormMantenimientoCategorias):
        FormMantenimientoCategorias.setObjectName(_fromUtf8("FormMantenimientoCategorias"))
        FormMantenimientoCategorias.resize(790, 662)
        self.tabWidget = QtGui.QTabWidget(FormMantenimientoCategorias)
        self.tabWidget.setGeometry(QtCore.QRect(30, 80, 731, 341))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.BotonModificar_MC = QtGui.QPushButton(self.tab)
        self.BotonModificar_MC.setGeometry(QtCore.QRect(450, 90, 75, 23))
        self.BotonModificar_MC.setObjectName(_fromUtf8("BotonModificar_MC"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(180, 90, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEditNroP_MC = QtGui.QLineEdit(self.tab)
        self.lineEditNroP_MC.setGeometry(QtCore.QRect(290, 130, 113, 20))
        self.lineEditNroP_MC.setObjectName(_fromUtf8("lineEditNroP_MC"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(180, 130, 81, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEditIISBN_MC = QtGui.QLineEdit(self.tab)
        self.lineEditIISBN_MC.setGeometry(QtCore.QRect(290, 90, 113, 20))
        self.lineEditIISBN_MC.setObjectName(_fromUtf8("lineEditIISBN_MC"))
        self.BotonBorrar_MC = QtGui.QPushButton(self.tab)
        self.BotonBorrar_MC.setEnabled(True)
        self.BotonBorrar_MC.setGeometry(QtCore.QRect(450, 60, 75, 23))
        self.BotonBorrar_MC.setObjectName(_fromUtf8("BotonBorrar_MC"))
        self.BotonCrear_MC = QtGui.QPushButton(self.tab)
        self.BotonCrear_MC.setGeometry(QtCore.QRect(450, 120, 75, 23))
        self.BotonCrear_MC.setObjectName(_fromUtf8("BotonCrear_MC"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.frame = QtGui.QFrame(FormMantenimientoCategorias)
        self.frame.setGeometry(QtCore.QRect(30, 440, 731, 161))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.tabWidget_2 = QtGui.QTabWidget(self.frame)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 10, 701, 111))
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.BotonBuscar_MC = QtGui.QPushButton(self.tab_2)
        self.BotonBuscar_MC.setGeometry(QtCore.QRect(460, 30, 75, 23))
        self.BotonBuscar_MC.setObjectName(_fromUtf8("BotonBuscar_MC"))
        self.label_6 = QtGui.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(210, 30, 46, 13))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEditID_MP_2 = QtGui.QLineEdit(self.tab_2)
        self.lineEditID_MP_2.setGeometry(QtCore.QRect(290, 30, 113, 20))
        self.lineEditID_MP_2.setObjectName(_fromUtf8("lineEditID_MP_2"))
        self.tabWidget_2.addTab(self.tab_2, _fromUtf8(""))
        self.BotonSalir_MC = QtGui.QPushButton(FormMantenimientoCategorias)
        self.BotonSalir_MC.setEnabled(True)
        self.BotonSalir_MC.setGeometry(QtCore.QRect(10, 590, 75, 23))
        self.BotonSalir_MC.setObjectName(_fromUtf8("BotonSalir_MC"))
        self.label_4 = QtGui.QLabel(FormMantenimientoCategorias)
        self.label_4.setGeometry(QtCore.QRect(250, 20, 281, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(17)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.frame.raise_()
        self.tabWidget.raise_()
        self.BotonSalir_MC.raise_()
        self.label_4.raise_()

        self.retranslateUi(FormMantenimientoCategorias)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(FormMantenimientoCategorias)

    def retranslateUi(self, FormMantenimientoCategorias):
        FormMantenimientoCategorias.setWindowTitle(_translate("FormMantenimientoCategorias", "Ventana Categorias", None))
        self.BotonModificar_MC.setText(_translate("FormMantenimientoCategorias", "Modificar", None))
        self.label.setText(_translate("FormMantenimientoCategorias", "Codigo", None))
        self.label_2.setText(_translate("FormMantenimientoCategorias", "Descripcion ", None))
        self.BotonBorrar_MC.setText(_translate("FormMantenimientoCategorias", "Borrar", None))
        self.BotonCrear_MC.setText(_translate("FormMantenimientoCategorias", "Crear", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("FormMantenimientoCategorias", "Mantenimiento", None))
        self.BotonBuscar_MC.setText(_translate("FormMantenimientoCategorias", "Buscar", None))
        self.label_6.setText(_translate("FormMantenimientoCategorias", "Codigo", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("FormMantenimientoCategorias", "Mantenimiento", None))
        self.BotonSalir_MC.setText(_translate("FormMantenimientoCategorias", "SALIR", None))
        self.label_4.setText(_translate("FormMantenimientoCategorias", "MANTENIMIENTO DE CATEGORIAS", None))

