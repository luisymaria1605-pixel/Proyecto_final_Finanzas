from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QRadioButton, QButtonGroup
from PyQt5.QtCore import Qt
from instr import txt_hinttest1, txt_hinttest2, txt_hinttest3, txt_sendresults, txt_test1, txt_test2, txt_test3, txt_title,txt_instruction
from tercera_ventana import FinalWin
from PyQt5.QtGui import QFont, QPixmap

class TestWin(QWidget):
    def __init__(self, name, age,profesion):
        super().__init__()

        self.name = name
        self.age = age
        self.profesion = profesion

        self.initUI()
        self.connects()
        self.set_appear()
        self.show()

    def initUI(self):
        # CAMBIO REALIZADO: Se definió 'self_estilo' al inicio para que esté disponible para todas las etiquetas que lo usan.
        self_estilo = "background-color: transparent; color: white;"
        fuente_campo = QFont("Times New Roman",12,QFont.Bold)



        self.lbl_test1 = QLabel(txt_test1)
        self.lbl_test1.setWordWrap(True)
        self.lbl_test1.setFont(fuente_campo)
        self.txt_test1_result = QLineEdit()
        self.txt_test1_result.setPlaceholderText(txt_hinttest1)
        self.lbl_test1.setStyleSheet(self_estilo)



        self.lbl_test2 = QLabel(txt_test2)
        self.lbl_test2.setWordWrap(True)
        self.lbl_test2.setFont(fuente_campo)
        self.txt_test2_result = QLineEdit()
        self.txt_test2_result.setPlaceholderText(txt_hinttest2)
        self.lbl_test2.setStyleSheet(self_estilo)
       
        self.lbl_test3 = QLabel(txt_test3)
        self.lbl_test3.setWordWrap(True)
        self.lbl_test3.setFont(fuente_campo)
        self.txt_test3_result = QLineEdit()
        self.txt_test3_result.setPlaceholderText(txt_hinttest3)
        self.lbl_test3.setStyleSheet(self_estilo)

        self.lbl_error = QLabel()
        self.lbl_error.setWordWrap(True)
        self.btn_next = QPushButton(txt_sendresults)


        self.lbl_image = QLabel(self)
        # CAMBIO REALIZADO: Se cambió la ruta absoluta del usuario anterior a la imagen local "fondooscuro.png" del proyecto.
        self.pixmap = QPixmap("fondooscuro.png")


        if not self.pixmap.isNull():
            self.lbl_image.setPixmap(self.pixmap)
        else:
            print("Error: No se pudo cargar la imagen")


        self.lbl_image.setScaledContents(True)
        self.lbl_image.lower()

        # CAMBIO REALIZADO: Se eliminó la definición local duplicada de 'self_estilo' de aquí ya que se movió al inicio de initUI().

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.lbl_test1)
        main_layout.addWidget(self.txt_test1_result)
        main_layout.addWidget(self.lbl_test2)
        main_layout.addWidget(self.txt_test2_result)
        main_layout.addWidget(self.lbl_test3)
        main_layout.addWidget(self.txt_test3_result)
        main_layout.addWidget(self.lbl_error)

    
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.btn_next)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def resizeEvent(self, event):
        self.lbl_image.setGeometry(0,0, self.width(), self.height())
        super().resizeEvent(event)

    # Conexión de señales y slots
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    # Configuración de apariencia de la ventana
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(1000, 800)
        self.move(100, 150)

    # Método auxiliar para validar y leer valores de pulso
    def _read_finance(self, line_edit):
        text = line_edit.text().strip()

        try:
            value = float(line_edit.text())
        except ValueError:
            self.lbl_error.setText('Por favor, introduzca un monto numerico valido.')
            self.lbl_error.setStyleSheet('color: red;')
            line_edit.setFocus()
            return None

        # Validación: el valor debe ser mayor que cero
        if value <= 0 :
            self.lbl_error.setText('Los montos financieros no pueden ser negativos.')
            self.lbl_error.setStyleSheet('color: red;')
            line_edit.setFocus()
            return None
        
        if value > 500000:
            self.lbl_error.setText('Los montos financieros no pueden ser mayores a 500,000.')
            self.lbl_error.setStyleSheet('color: red;')
            line_edit.setFocus()
            return None
        return value

    def next_click(self):
       
       
        self.lbl_error.clear()


        ingresos = self._read_finance(self.txt_test1_result)
        if ingresos is None:
            return

        gastos = self._read_finance(self.txt_test2_result)
        if gastos is None:
            return

        fondo = self._read_finance(self.txt_test3_result)
        if fondo is None:
            return

        self.lbl_error.clear()
        # CAMBIO REALIZADO: Se corrigió 'profesion' a 'self.profesion' ya que es un atributo de clase y no una variable local.
        self.final_win = FinalWin(
            name=self.name,
            age=self.age,
            profesion=self.profesion,
            ingresos=ingresos,
            gastos=gastos,
            fondo=fondo,
        )
        self.hide()


# Punto de entrada de la aplicación (para pruebas independientes)
if __name__ == '__main__':
    try:
        app = QApplication([])
        mw = TestWin(name='Usuario', age=30, profesion='estudiante')
        app.exec_()
    except Exception as e:
        print(f'Error: {e}')
