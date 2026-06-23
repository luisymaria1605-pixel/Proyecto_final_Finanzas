from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton

from instr import txt_age, txt_hello, txt_hintname, txt_hintage, txt_instruction, txt_name, txt_next, txt_title, txt_profesion

from segunda_ventana import TestWin

class MainWin(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
        self.connects()
        self.set_appear()
        self.show()

  
    def initUI(self):
        # Etiqueta de bienvenida
        self.lbl_hello = QLabel(txt_hello)
        self.lbl_hello.setWordWrap(True)

       
        self.lbl_instruction = QLabel(txt_instruction)
        self.lbl_instruction.setWordWrap(True)

     
        self.lbl_name = QLabel(txt_name)
        self.txt_name = QLineEdit()
        self.txt_name.setPlaceholderText(txt_hintname)

      
        self.lbl_age = QLabel(txt_age)
        self.txt_age = QLineEdit()
        self.txt_age.setPlaceholderText(txt_hintage)

        self.lbl_profesion = QLabel(txt_profesion)
        self.txt_profesion = QLineEdit()

      
        self.lbl_error = QLabel()
        self.lbl_error.setWordWrap(True)

  
        self.btn_next = QPushButton(txt_next)
        # CAMBIO REALIZADO: Se eliminó la conexión duplicada de la señal clicked aquí.
        # Ya se conecta correctamente en el método connects() (abajo).

   
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.lbl_hello)
        main_layout.addWidget(self.lbl_instruction)
        main_layout.addWidget(self.lbl_name)
        main_layout.addWidget(self.txt_name)
        main_layout.addWidget(self.lbl_age)
        main_layout.addWidget(self.txt_age)
        main_layout.addWidget(self.lbl_profesion)
        main_layout.addWidget(self.txt_profesion)
        main_layout.addWidget(self.lbl_error)

        
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.btn_next)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(1000, 800)
        self.move(100, 150)

    def next_click(self):
        
        name = self.txt_name.text().strip()
        age_text = self.txt_age.text().strip()
        profesion = self.txt_profesion.text().strip()

       
        if not name:
            self.lbl_error.setText('El nombre no puede estar vacío.')
            self.lbl_error.setStyleSheet('color: red;')
            self.txt_name.setFocus()
            return

       
        try:
            age = int(age_text)
        except ValueError:
            self.lbl_error.setText('La edad debe ser un número entero.')
            self.lbl_error.setStyleSheet('color: red;')
            self.txt_age.setFocus()
            return


        if age <= 0:
            self.lbl_error.setText('La edad debe ser mayor que cero.')
            self.lbl_error.setStyleSheet('color: red;')
            self.txt_age.setFocus()
            return
        
        
        self.lbl_error.clear()
        self.segunda_ventana = TestWin(name=name, age=age, profesion=profesion) # type: ignore
        self.segunda_ventana.show()
        self.hide()



if __name__ == '__main__':
    try:
        app = QApplication([])
        mw = MainWin()
        app.exec_()
    except Exception as e:
        print(f'Error: {e}')