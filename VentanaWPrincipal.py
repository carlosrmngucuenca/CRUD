# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WVentanaprincipal.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(808, 610)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 0, 611, 541))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("Imagenes/servicios_biblioteca_0.png")))
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 808, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMENU = QtGui.QMenu(self.menubar)
        self.menuMENU.setObjectName(_fromUtf8("menuMENU"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionMantenimiento_Personas = QtGui.QAction(MainWindow)
        self.actionMantenimiento_Personas.setObjectName(_fromUtf8("actionMantenimiento_Personas"))
        self.actionMantenimiento_Libros = QtGui.QAction(MainWindow)
        self.actionMantenimiento_Libros.setObjectName(_fromUtf8("actionMantenimiento_Libros"))
        self.actionSalir = QtGui.QAction(MainWindow)
        self.actionSalir.setObjectName(_fromUtf8("actionSalir"))
        self.actionMantenimiento_Personas_ToolBar = QtGui.QAction(MainWindow)
        self.actionMantenimiento_Personas_ToolBar.setObjectName(_fromUtf8("actionMantenimiento_Personas_ToolBar"))
        self.actionMantenimiento_Libros_ToolBar = QtGui.QAction(MainWindow)
        self.actionMantenimiento_Libros_ToolBar.setObjectName(_fromUtf8("actionMantenimiento_Libros_ToolBar"))
        self.actionPrestamo_De_Libros_Toolbar = QtGui.QAction(MainWindow)
        self.actionPrestamo_De_Libros_Toolbar.setObjectName(_fromUtf8("actionPrestamo_De_Libros_Toolbar"))
        self.actionPrestamo_Libros = QtGui.QAction(MainWindow)
        self.actionPrestamo_Libros.setObjectName(_fromUtf8("actionPrestamo_Libros"))
        self.actionMantenimiento_Categorias = QtGui.QAction(MainWindow)
        self.actionMantenimiento_Categorias.setObjectName(_fromUtf8("actionMantenimiento_Categorias"))
        self.actionMantenimiento_De_Categorias_ToolBar = QtGui.QAction(MainWindow)
        self.actionMantenimiento_De_Categorias_ToolBar.setObjectName(_fromUtf8("actionMantenimiento_De_Categorias_ToolBar"))
        self.menuMENU.addAction(self.actionMantenimiento_Personas)
        self.menuMENU.addAction(self.actionMantenimiento_Libros)
        self.menuMENU.addAction(self.actionMantenimiento_Categorias)
        self.menuMENU.addSeparator()
        self.menuMENU.addAction(self.actionPrestamo_Libros)
        self.menuMENU.addAction(self.actionSalir)
        self.menubar.addAction(self.menuMENU.menuAction())
        self.toolBar.addAction(self.actionMantenimiento_Personas_ToolBar)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionMantenimiento_Libros_ToolBar)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPrestamo_De_Libros_Toolbar)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionMantenimiento_De_Categorias_ToolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Ventana Principal", None))
        self.menuMENU.setTitle(_translate("MainWindow", "MENU", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionMantenimiento_Personas.setText(_translate("MainWindow", "Mantenimiento Personas", None))
        self.actionMantenimiento_Libros.setText(_translate("MainWindow", "Mantenimiento Libros", None))
        self.actionSalir.setText(_translate("MainWindow", "Salir", None))
        self.actionMantenimiento_Personas_ToolBar.setText(_translate("MainWindow", "Mantenimiento Personas", None))
        self.actionMantenimiento_Personas_ToolBar.setToolTip(_translate("MainWindow", "Mantenimiento Personas", None))
        self.actionMantenimiento_Libros_ToolBar.setText(_translate("MainWindow", "Mantenimiento Libros", None))
        self.actionMantenimiento_Libros_ToolBar.setToolTip(_translate("MainWindow", "Mantenimiento De Libros", None))
        self.actionPrestamo_De_Libros_Toolbar.setText(_translate("MainWindow", "Prestamo De Libros", None))
        self.actionPrestamo_De_Libros_Toolbar.setToolTip(_translate("MainWindow", "Prestamo Libros", None))
        self.actionPrestamo_Libros.setText(_translate("MainWindow", "Prestamo Libros", None))
        self.actionMantenimiento_Categorias.setText(_translate("MainWindow", "Mantenimiento Categorias", None))
        self.actionMantenimiento_De_Categorias_ToolBar.setText(_translate("MainWindow", "Mantenimiento De Categorias", None))
        self.actionMantenimiento_De_Categorias_ToolBar.setToolTip(_translate("MainWindow", "Mantenimiento Categorias", None))

