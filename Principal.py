

from VentanaWMantenimientoPersona import Ui_FormMantPersonas
from VentanaWPrincipal import Ui_MainWindow
from VentanaWMantenimientoLibros import  Ui_FormMantLibros
from VentanaWPrestamos import Ui_FormPrestamoLibros
from VentanaWCategorias import Ui_FormMantenimientoCategorias
import time
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtNetwork import *
from PyQt4 import QtCore, QtGui



try:
    import cPickle as pickle
except ImportError:
    import pickle


class Categoria:
    def __init__(self, codigo, descripcion):
        self.codigo=codigo
        self.descripcion=descripcion
    def __str__(self):
        return str(self.codigo)+";"+str(self.descripcion)
class stock:
    def __init__(self, ISBN, nPag, idioma,lenguaje,autor,editorial,categoria=Categoria("",""),reserva=False,fecha="",ID=""):
        self.ISBN = ISBN
        self.nPag = nPag
        self.idioma = idioma
        self.lenguaje = lenguaje
        self.autor = autor
        self.editorial = editorial
        self.categoria = categoria
        self.reserva=reserva
        self.fecha=fecha
        self.ID=ID
    def __str__(self):
        return str(self.ISBN)+";"+str(self.nPag)+";"+str(self.idioma)+";"+str(self.lenguaje)+";"+str(self.autor)+";"+str(self.editorial)+";"+str(self.categoria.codigo)+";"+str(self.reserva)+";"+str(self.fecha)+";"+str(self.ID)

class Libro:
    def __init__(self, ISBN, nPag, idioma,lenguaje,autor,editorial,categoria=Categoria("","")):
        self.ISBN=ISBN
        self.nPag=nPag
        self.idioma=idioma
        self.lenguaje=lenguaje
        self.autor=autor
        self.editorial=editorial
        self.categoria=categoria
    def __str__(self):
        return str(self.ISBN)+";"+str(self.nPag)+";"+str(self.idioma)+";"+str(self.lenguaje)+";"+str(self.autor)+";"+str(self.editorial)+";"+str(self.categoria.codigo)
class Estudiante:
    def __init__(self, id, nombres, apellidos):
        self.id=id
        self.apellidos=apellidos
        self.nombres=nombres
    def __str__(self):
        return str(self.id)+";"+str(self.nombres)+";"+str(self.apellidos)
class Libreria:
    def __init__(self, libros,categorias,estudiantes,stock):
        self.categorias=categorias
        self.libros=libros
        self.estudiantes=estudiantes
        self.stock=stock

class VentanaMantenimientoPersona(QtGui.QMainWindow,Ui_FormMantPersonas):


    def __init__(self, parent=None):
        super(VentanaMantenimientoPersona,self).__init__(parent)
        self.setupUi(self)

class VentanaMantenimientoLibros(QtGui.QMainWindow,Ui_FormMantLibros):


    def __init__(self, parent=None):
        super(VentanaMantenimientoLibros,self).__init__(parent)
        self.setupUi(self)

class VentanaPrestamoDeLibros(QtGui.QMainWindow,Ui_FormPrestamoLibros):


    def __init__(self, parent=None):
        super(VentanaPrestamoDeLibros,self).__init__(parent)
        self.setupUi(self)


class VentanaMantenimientoDeCategorias(QtGui.QMainWindow,Ui_FormMantenimientoCategorias):


    def __init__(self, parent=None):
        super(VentanaMantenimientoDeCategorias,self).__init__(parent)
        self.setupUi(self)






class VentanaPrincipal(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(VentanaPrincipal,self).__init__(parent)
        self.setupUi(self)
        self.connect(self.actionMantenimiento_Personas_ToolBar,QtCore.SIGNAL("triggered()"),self.Mantenimiento_Personas)
        self.connect(self.actionMantenimiento_Libros_ToolBar, QtCore.SIGNAL("triggered()"), self.Mantenimiento_Libros)
        self.connect(self.actionPrestamo_De_Libros_Toolbar, QtCore.SIGNAL("triggered()"), self.Prestamo_Libros)
        self.connect(self.actionMantenimiento_De_Categorias_ToolBar, QtCore.SIGNAL("triggered()"), self.MantenimientoDe_Categorias)

        self.connect(self.actionMantenimiento_Personas, QtCore.SIGNAL("triggered()"),self.Mantenimiento_Personas)
        self.connect(self.actionMantenimiento_Libros, QtCore.SIGNAL("triggered()"), self.Mantenimiento_Libros)
        self.connect(self.actionPrestamo_Libros, QtCore.SIGNAL("triggered()"), self.Prestamo_Libros)
        self.connect(self.actionSalir, QtCore.SIGNAL("triggered()"), self.salir_VentanaPrincipal)
        self.connect(self.actionMantenimiento_Categorias, QtCore.SIGNAL("triggered()"), self.MantenimientoDe_Categorias)



    def Mantenimiento_Personas(self):
        self.v1=VentanaMantenimientoPersona()
        self.v1.show()
    def Mantenimiento_Libros(self):
        self.v2=VentanaMantenimientoLibros()
        self.v2.show()

    def Prestamo_Libros(self):
        self.v3=VentanaPrestamoDeLibros()
        self.v3.show()

    def MantenimientoDe_Categorias(self):
        self.v4=VentanaMantenimientoDeCategorias()
        self.v4.show()



    def salir_VentanaPrincipal(self):
        sys.exit(0)


app = QtGui.QApplication(sys.argv)
myapp = VentanaPrincipal()
myapp.show()
sys.exit(app.exec_())