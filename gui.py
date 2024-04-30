# Form implementation generated from reading ui file 'maze-game-gui.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Maze(object):
    def setupUi(self, Maze):
        Maze.setObjectName("Maze")
        Maze.resize(900, 800)
        Maze.setMinimumSize(QtCore.QSize(900, 800))
        Maze.setMaximumSize(QtCore.QSize(900, 800))
        self.centralwidget = QtWidgets.QWidget(parent=Maze)
        self.centralwidget.setObjectName("centralwidget")
        self.UpButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.UpButton.setGeometry(QtCore.QRect(320, 380, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.UpButton.setFont(font)
        self.UpButton.setObjectName("UpButton")
        self.RightButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.RightButton.setGeometry(QtCore.QRect(380, 410, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.RightButton.setFont(font)
        self.RightButton.setObjectName("RightButton")
        self.LeftButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.LeftButton.setGeometry(QtCore.QRect(260, 410, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.LeftButton.setFont(font)
        self.LeftButton.setObjectName("LeftButton")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(320, 440, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.maze = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.maze.setGeometry(QtCore.QRect(0, 0, 900, 341))
        self.maze.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.maze.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.maze.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.maze.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.maze.setAutoScroll(True)
        self.maze.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.maze.setShowGrid(True)
        self.maze.setGridStyle(QtCore.Qt.PenStyle.SolidLine)
        self.maze.setRowCount(68)
        self.maze.setColumnCount(140)
        self.maze.setObjectName("maze")
        self.maze.horizontalHeader().setVisible(False)
        self.maze.horizontalHeader().setDefaultSectionSize(2)
        self.maze.horizontalHeader().setMinimumSectionSize(5)
        self.maze.verticalHeader().setVisible(False)
        self.maze.verticalHeader().setDefaultSectionSize(2)
        self.maze.verticalHeader().setHighlightSections(True)
        self.maze.verticalHeader().setMinimumSectionSize(5)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 380, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 410, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        Maze.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Maze)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 18))
        self.menubar.setObjectName("menubar")
        Maze.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Maze)
        self.statusbar.setObjectName("statusbar")
        Maze.setStatusBar(self.statusbar)

        self.retranslateUi(Maze)
        QtCore.QMetaObject.connectSlotsByName(Maze)

    def retranslateUi(self, Maze):
        _translate = QtCore.QCoreApplication.translate
        Maze.setWindowTitle(_translate("Maze", "MainWindow"))
        self.UpButton.setText(_translate("Maze", "UP"))
        self.RightButton.setText(_translate("Maze", "Right"))
        self.LeftButton.setText(_translate("Maze", "Left"))
        self.pushButton_4.setText(_translate("Maze", "Down"))
        self.label.setText(_translate("Maze", "High Score:"))
        self.label_3.setText(_translate("Maze", "Current Time: 0:00"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Maze = QtWidgets.QMainWindow()
    ui = Ui_Maze()
    ui.setupUi(Maze)
    Maze.show()
    sys.exit(app.exec())
