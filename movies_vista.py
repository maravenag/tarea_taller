#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, controller, os
from PySide import QtGui, QtCore
from movies import Ui_MainWindow


class Movies(QtGui.QMainWindow):


    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.load_data()
        self.signals()
        self.show()

    def signals(self):
        self.ui.tableView.clicked.connect(self.actualiza)
        self.ui.btn_up.clicked.connect(self.arriba)
        self.ui.btn_down.clicked.connect(self.abajo)

    def arriba(self):
        model = self.ui.tableView.model()
        index = self.ui.tableView.currentIndex()
        pelicula = model.index(index.row(), 0, QtCore.QModelIndex()).data()
        controller.arriba_ranking(pelicula)
        self.load_data()
        self.ui.tableView.selectRow(index.row()-1)

    def abajo(self):
        model = self.ui.tableView.model()
        index = self.ui.tableView.currentIndex()
        pelicula = model.index(index.row(), 0, QtCore.QModelIndex()).data()
        controller.abajo_ranking(pelicula)
        self.load_data()
        self.ui.tableView.selectRow(index.row()+1)


    def actualiza(self):

        model = self.ui.tableView.model()
        index = self.ui.tableView.currentIndex()
        informacion = model.index(index.row(), 0, QtCore.QModelIndex()).data()
        self.pelicula = controller.obtener_una_pelicula(informacion)
        self.ui.lbl_reparto.setText(self.pelicula[0][6])
        self.ui.lbl_descripcion.setText(self.pelicula[0][7])
        self.ancho = self.ui.lbl_imagen.width()
        self.largo = self.ui.lbl_imagen.height()
        self.direc = "/db_movies/{0}".format(self.pelicula[0][2])
        self.myPixmap = QtGui.QPixmap(os.getcwd() + self.direc)
        self.ui.lbl_imagen.setPixmap(self.myPixmap.scaled(self.ancho,self.largo,QtCore.Qt.KeepAspectRatio))

    def load_data(self):
        peliculas = controller.obtener_peliculas()
        self.model = QtGui.QStandardItemModel(len(peliculas),5)
        self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"Titulo"))
        self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Año"))
        self.model.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Director"))
        self.model.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"Pais"))
        self.model.setHorizontalHeaderItem(4, QtGui.QStandardItem(u"Ranking"))

        r = 0
        for row in peliculas:
            index = self.model.index(r, 0, QtCore.QModelIndex())
            self.model.setData(index, row['title'])
            index = self.model.index(r, 1, QtCore.QModelIndex())
            self.model.setData(index, row['release_year'])
            index = self.model.index(r, 2, QtCore.QModelIndex())
            self.model.setData(index, row['director'])
            index = self.model.index(r, 3, QtCore.QModelIndex())
            self.model.setData(index, row['country'])
            index = self.model.index(r, 4, QtCore.QModelIndex())
            self.model.setData(index, row['ranking'])
            r = r + 1

        self.ui.tableView.setModel(self.model)
        self.ui.tableView.setColumnWidth(0, 100)
        self.ui.tableView.setColumnWidth(1, 50)
        self.ui.tableView.setColumnWidth(2, 150)
        self.ui.tableView.setColumnWidth(3, 50)
        self.ui.tableView.setColumnWidth(4, 80)
        self.ui.tableView.horizontalHeader().setResizeMode(0,self.ui.tableView.horizontalHeader().Stretch)
        self.ui.tableView.sortByColumn(4, QtCore.Qt.AscendingOrder)
def run():
    app = QtGui.QApplication(sys.argv)
    main = Movies()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()