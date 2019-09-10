from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtPrintSupport import*
import sys
import sqlite3
import time
import os

class InsertDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(InsertDialog, self).__init__(*args, **kwargs)

        self.setWindowIcon(QIcon('icon/g3.png'))
        self.QBtn = QPushButton()
        self.QBtn.setText('Registrar: ')

        self.setWindowTitle("Add Aluno: ")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        self.setWindowTitle("Dados do Aluno: ")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        self.QBtn.clicked.connect(self.addStudent)

        layout = QVBoxLayout()

        self.nameinput = QLineEdit()
        self.nameinput.setPlaceholderText('Nome')
        layout.addWidget(self.nameinput)

        self.branchinput = QComboBox()
        self.branchinput.addItem("Eng. Quimica")
        self.branchinput.addItem("Civil")
        self.branchinput.addItem("Eletronica")
        self.branchinput.addItem("Comunicação")
        self.branchinput.addItem("Computação")
        self.branchinput.addItem("Tecnologia da Informação")

        layout.addWidget(self.branchinput)

        self.seminput = QComboBox()
        self.seminput.addItem("1")
        self.seminput.addItem("2")
        self.seminput.addItem("3")
        self.seminput.addItem("4")
        self.seminput.addItem("5")
        self.seminput.addItem("6")
        self.seminput.addItem("7")
        self.seminput.addItem("8")

        layout.addWidget(self.seminput)

        self.mobileinput = QLineEdit()
        self.mobileinput .setPlaceholderText('Telefone')
        layout.addWidget(self.mobileinput)

        self.addressinput = QLineEdit()
        self.addressinput.setPlaceholderText('Endereco')
        layout.addWidget(self.addressinput)

        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def addStudent(self):
        name = ''
        branch = ''
        sem = -1
        mobile = ''
        address = ''

        name = self.nameinput.text()
        branch = self.branchinput.itemText(self.branchinput.currentIndex())
        sem = self.seminput.itemText(self.seminput.currentIndex())
        mobile = self.mobileinput.text()
        address = self.addressinput.text()
        try:
            self.conn = sqlite3.connect('database.db')
            self.c = self.conn.cursor()
            self.c.execute('INSERT INTO students (name,branch,sem,Mobile,address)VALUES (?,?,?,?,?)', (name,branch,sem,mobile,address))

            self.conn.commit()
            self.c.close()
            self.conn.close()

            QMessageBox.information(QMessageBox(), 'Cadastro', 'ESTUDANTE CADASTRADO COM SUCESSO')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'anfisope10@hotmIL.com', 'Não foi possivel realizar seu cadastro')



class SearchDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(SearchDialog, self).__init__(*args, **kwargs)
        self.setWindowIcon(QIcon('icon/g3.png'))
        self.QBtn = QPushButton()
        self.QBtn.setText('Pesquisar: ')

        self.setWindowTitle("Pesquisar Aluno: ")
        self.setFixedWidth(300)
        self.setFixedHeight(100)

        self.QBtn.clicked.connect(self.searchstudent)

        layout = QVBoxLayout()

        self.searchinput = QLineEdit()
        self.onlyInt = QIntValidator()
        self.searchinput.setValidator(self.onlyInt)
        self.searchinput.setPlaceholderText('Inscrição ')
        layout.addWidget(self.searchinput)

        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def searchstudent(self):
        searchrol = ''
        searchrol = self.searchinput.text()


        try:
            self.conn = sqlite3.connect('database.db')
            self.c = self.conn.cursor()
            result = self.c.execute('SELECT * from students WHERE roll =' + str(searchrol))
            row = result.fetchone()
            searchresult = 'INSCRICAO: '+str(row[0])+'\n'+'NOME : '+str(row[1])+'\n'+'CURSO : '+str(row[2])+'\n'+'SEMESTRE : '+str(row[3])+'\n'+'TELEFONE : '+str(row[4])+'\n'+'ENDERECO : '+str(row[5])
            QMessageBox.information(QMessageBox(), 'Sucesso na pesquisa', searchresult)
            self.conn.commit()
            self.c.close()
            self.conn.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'anfisope10@hotmIL.com', 'Sua pesquisa não foi encontrada')

class DeleteDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(DeleteDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText('Deletar: ')

        self.setWindowTitle("Deletar Inscricao: ")
        self.setFixedWidth(300)
        self.setFixedHeight(100)

        self.QBtn.clicked.connect(self.deletestudent)

        layout = QVBoxLayout()

        self.deleteinput = QLineEdit()
        self.onlyInt = QIntValidator()
        self.deleteinput.setValidator(self.onlyInt)
        self.deleteinput.setPlaceholderText('Delete ')
        layout.addWidget(self.deleteinput)

        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def deletestudent(self):
        delrol = ''
        delrol = self.deleteinput.text()

        try:
            self.conn = sqlite3.connect('database.db')
            self.c = self.conn.cursor()
            self.c.execute('DELETE from students WHERE roll =' + str(delrol))

            self.conn.commit()
            self.c.close()
            self.conn.close()

            QMessageBox.information(QMessageBox(), 'anfisope10@hotmail.com', 'DELETADO COM SUCESSO')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'anfisope10@hotmIL.com', 'Não foi possivel deletar')
class AboutDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)
        self.setWindowIcon(QIcon('icon/g3.png'))
        self.setFixedWidth(500)
        self.setFixedHeight(500)

        QBtn = QDialogButtonBox.Ok
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.accepted.connect(self.reject)

        layout = QVBoxLayout()


        self.setWindowTitle("Sobre")
        title = QLabel('Cadastro de Alunos Em PYQT5')
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)

        labelpic = QLabel()
        pixmap = QPixmap('icon/san.png')
        pixmap = pixmap.scaledToWidth(275)
        labelpic.setPixmap(pixmap)
        labelpic.setFixedHeight(150)

        layout.addWidget(title)

        layout.addWidget(QLabel('V5.0'))
        layout.addWidget(QLabel("Sistema da Computação UFF"))
        layout.addWidget(QLabel("Copyright AndersonFSP 2019"))
        layout.addWidget(labelpic)

        layout.addWidget(self.buttonBox)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowIcon(QIcon('icon/g3.png'))
        #Conexão BANCO DE DADOS#
        self.conn = sqlite3.connect('database.db')
        self.c = self.conn.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS students(roll INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, branch TEXT, sem INTEGER, mobile INTEGER, address TEXT)")
        self.c.close()

        fileMenu = self.menuBar().addMenu('&File')
        help_menu = self.menuBar().addMenu('&Ajuda')
        self.setWindowTitle('CADASTRO DE ALUNOS EM PYQT5')
        self.setMinimumSize(800, 600)

        self.tableWidget = QTableWidget()
        self.setCentralWidget(self.tableWidget)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)

        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.tableWidget.setHorizontalHeaderLabels(('Inscrição No', 'Nome', 'Filial', 'Semestre', 'Telefone', 'Endereço'))

        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        statusbar = QStatusBar()
        self.setStatusBar(statusbar)

        btn_ac_adduser = QAction(QIcon("icon/add1.png"), "Add Aluno", self)
        btn_ac_adduser.triggered.connect(self.insert)
        btn_ac_adduser.setStatusTip("add Aluno")
        toolbar.addAction(btn_ac_adduser)

        btn_ac_refresh = QAction(QIcon("icon/refresh.png"), "Atualizar Dados", self)
        btn_ac_refresh.triggered.connect(self.loaddata)
        btn_ac_refresh.setStatusTip("Atualizar Dados")
        toolbar.addAction(btn_ac_refresh)

        btn_ac_search = QAction(QIcon("icon/search.png"), "Pesquisar por Aluno", self)
        btn_ac_search.triggered.connect(self.search)
        btn_ac_search.setStatusTip("Pesquisar Alunos")
        toolbar.addAction(btn_ac_search)

        btn_ac_delete = QAction(QIcon("icon/delete.png"), "Deletar cadastro", self)
        btn_ac_delete.triggered.connect(self.delete)
        btn_ac_delete.setStatusTip("Deletar Alunos")
        toolbar.addAction(btn_ac_delete)

        #######################################
        adduser_action = QAction(QIcon("icon/add1.png"), "Add Aluno", self)
        adduser_action.triggered.connect(self.insert)
        fileMenu.addAction(adduser_action)

        searchuser = QAction(QIcon("icon/search.png"), "Pesquisar ", self)
        searchuser.triggered.connect(self.search)
        fileMenu.addAction(searchuser)

        deluser = QAction(QIcon("icon/delete.png"), "Deletar cadastro", self)
        deluser.triggered.connect(self.delete)
        fileMenu.addAction(deluser)
        #######################################

        about_action = QAction(QIcon("icon/about.png"), "Desenvolvedor", self)
        about_action.triggered.connect(self.about)
        help_menu.addAction(about_action)

    def loaddata(self):
        self.connection = sqlite3.connect('database.db')
        query = 'SELECT * FROM students'
        result = self.connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number,row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for columm_number,data in enumerate(row_data):
                    self.tableWidget.setItem(row_number,columm_number, QTableWidgetItem(str(data)))
        self.connection.close()
    def insert(self):
        dlg = InsertDialog()
        dlg.exec_()

    def delete(self):
        dlg = DeleteDialog()
        dlg.exec_()

    def search(self):
        dlg = SearchDialog()
        dlg.exec_()

    def about(self):
        dlg = AboutDialog()
        dlg.exec_()

app = QApplication(sys.argv)
if(QDialog.Accepted == True):
    window = MainWindow()
    window.show()
    window.loaddata()
sys.exit(app.exec_())

