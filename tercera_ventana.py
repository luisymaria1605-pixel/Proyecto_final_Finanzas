
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel


from instr import txt_finalwin, txt_index, txt_workheart


class FinalWin(QWidget):
    # Inicialización con todos los datos del usuario
    def __init__(self, name, age,profesion,ingresos, gastos, fondo):
        super().__init__()

        self.name = name
        self.age = age
        self.profesion = profesion
        self.ingresos = ingresos
        self.gastos = gastos
        self.fondo = fondo

        self.initUI()
        self.set_appear()
        self.show()


    def _calculate_finanzas_index(self):
        return ((self.ingresos - self.gastos )+ self.fondo) / 2500
    





    def _health_level(self, finanzas_index):
        # CAMBIO REALIZADO: Se ordenaron las condiciones de mayor a menor para evaluar correctamente el índice financiero.
        # En esta prueba financiera, a mayor índice, mejor salud financiera y capacidad de ahorro.
        if finanzas_index  > 15:
            return 'Finanzas solidas, tienes capacidad de ahorro'
        if finanzas_index  >= 10:
            return 'Llegas a fin de mes, pero no tienes margen de ahorro'
        if finanzas_index >= 5:
            return 'Promedio'
        if finanzas_index >= 0:
            return 'Bajo'
        return 'Muy bajo'


    def initUI(self):
        # Calcular valores
        finanzas_index = self._calculate_finanzas_index()
        health_level = self._health_level(finanzas_index)

      
        self.lbl_title = QLabel(f'Resultados de tus finanzas, {self.name}')
        self.lbl_title.setWordWrap(True)

    
        self.lbl_age = QLabel(f'Edad: {self.age} años')
        self.lbl_age.setWordWrap(True)


        self.lbl_ingresos = QLabel(f'Ingresos: ${self.ingresos:.2f}')
        self.lbl_ingresos.setWordWrap(True)

        self.lbl_gastos = QLabel(f'Gastos: ${self.gastos:.2f}')
        self.lbl_gastos.setWordWrap(True)

        self.lbl_fondo = QLabel(f'Fondo: ${self.fondo:.2f}')
        self.lbl_fondo.setWordWrap(True)

        self.lbl_index = QLabel(f'{txt_index}{finanzas_index:.2f}')
        self.lbl_index.setWordWrap(True)


        # CAMBIO REALIZADO: Se eliminó el widget 'self.lbl_workheart' y el cálculo cardíaco 'workheart'
        # ya que no corresponden a una aplicación de capacidad de ahorro/finanzas.
        # (Originalmente causaba NameError por no estar definido 'workheart').

        
        self.lbl_health_level = QLabel(f'Nivel de rendimiento: {health_level}')
        self.lbl_health_level.setWordWrap(True)

   
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.lbl_title)
        main_layout.addWidget(self.lbl_age)
        main_layout.addWidget(self.lbl_ingresos)
        main_layout.addWidget(self.lbl_gastos)
        main_layout.addWidget(self.lbl_fondo)
        main_layout.addWidget(self.lbl_index)
        # CAMBIO REALIZADO: Se eliminó la inserción de 'self.lbl_workheart' del layout.
        main_layout.addWidget(self.lbl_health_level)
        main_layout.addStretch()

        self.setLayout(main_layout)

   
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(1000, 600)
        self.move(200, 100)


# Punto de entrada de la aplicación (para pruebas independientes)
if __name__ == '__main__':
    try:
        app = QApplication([])
        # CAMBIO REALIZADO: Se actualizaron los argumentos para que correspondan con los nuevos parámetros del constructor de FinalWin (finanzas).
        mw = FinalWin(name='Usuario', age=20, profesion='profesional', ingresos=3000, gastos=2500, fondo=5000)
        app.exec_()
    except Exception as e:
        print(f'Error: {e}')
