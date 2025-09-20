"""
Programa: Calculadora de IMC (Índice de Masa Corporal)
Autor: [Tu nombre]
Materia: [nombre de la materia]

Descripción:
Este programa es una aplicación gráfica hecha en Python con PyQt5.
El objetivo es calcular el IMC de una persona a partir de su peso y altura,
mostrando en qué categoría se encuentra (bajo peso, normal, sobrepeso u obesidad).
Este es un problema de la vida real que se usa en salud y nutrición
para orientar decisiones médicas y hábitos saludables.
"""

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QFormLayout, QMessageBox, QFrame
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class CalculadoraIMC(QWidget):
    def __init__(self):
        super().__init__()

        # ---- Configuración de la ventana principal ----
        self.setWindowTitle("Calculadora de IMC")
        self.setGeometry(100, 100, 480, 420)

        # ---- Estilos generales (CSS para PyQt5) ----
        self.setStyleSheet("""
            QWidget {
                background-color: #f5f7fa;  /* Fondo suave */
            }
            QLineEdit {
                border: 2px solid #ccc;
                border-radius: 10px;
                padding: 8px;
                font-size: 14px;
            }
            QPushButton {
                background-color: #1abc9c;
                color: white;
                font-weight: bold;
                border-radius: 15px;
                padding: 10px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #16a085;
            }
            QLabel {
                color: #2c3e50;
            }
            QFrame {
                background-color: rgba(26, 188, 156, 0.2);
                border-radius: 15px;
                padding: 10px;
            }
        """)

        # ---- Fuentes personalizadas ----
        self.titulo_fuente = QFont("Segoe UI", 20, QFont.Bold)
        self.explicacion_fuente = QFont("Segoe UI", 12)
        self.labels_fuente = QFont("Segoe UI", 12)
        self.resultado_fuente = QFont("Segoe UI", 14, QFont.Bold)

        # ---- Título principal ----
        self.titulo = QLabel("Calculadora de IMC")
        self.titulo.setFont(self.titulo_fuente)
        self.titulo.setAlignment(Qt.AlignCenter)

        # ---- Explicación del IMC (problema de la vida real) ----
        self.explicacion = QLabel(
            "IMC (Índice de Masa Corporal): Es un valor que indica si tu peso "
            "es adecuado según tu altura. Se aplica en la vida real para identificar "
            "si una persona tiene bajo peso, peso normal, sobrepeso u obesidad, "
            "ayudando a personas a ver su estado de salud ."
        )
        self.explicacion.setFont(self.explicacion_fuente)
        self.explicacion.setWordWrap(True)
        self.explicacion.setAlignment(Qt.AlignCenter)

        # ---- Entradas de datos ----
        self.input_nombre = QLineEdit()
        self.input_nombre.setPlaceholderText("Nombre")

        self.input_peso = QLineEdit()
        self.input_peso.setPlaceholderText("Peso en kg")

        self.input_altura = QLineEdit()
        self.input_altura.setPlaceholderText("Altura en metros")

        # ---- Botones principales ----
        self.btn_calcular = QPushButton("Calcular IMC")
        self.btn_calcular.clicked.connect(self.calcular_imc)  # Llama a la función de cálculo

        self.btn_nuevo = QPushButton("Nuevo cálculo")
        self.btn_nuevo.clicked.connect(self.nuevo_calculo)  # Llama a la función de reinicio

        # ---- Panel de resultado ----
        self.resultado_frame = QFrame()
        self.resultado_label = QLabel("Resultado: ")
        self.resultado_label.setFont(self.resultado_fuente)
        self.resultado_label.setAlignment(Qt.AlignCenter)

        resultado_layout = QVBoxLayout()
        resultado_layout.addWidget(self.resultado_label)
        self.resultado_frame.setLayout(resultado_layout)

        # ---- Layout de formulario ----
        form_layout = QFormLayout()
        form_layout.addRow("Nombre:", self.input_nombre)
        form_layout.addRow("Peso (kg):", self.input_peso)
        form_layout.addRow("Altura (m):", self.input_altura)

        # ---- Layout principal ----
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.titulo)
        main_layout.addSpacing(5)
        main_layout.addWidget(self.explicacion)
        main_layout.addSpacing(10)
        main_layout.addLayout(form_layout)
        main_layout.addSpacing(15)
        main_layout.addWidget(self.btn_calcular)
        main_layout.addWidget(self.btn_nuevo)
        main_layout.addSpacing(20)
        main_layout.addWidget(self.resultado_frame)
        main_layout.setContentsMargins(40, 20, 40, 20)

        self.setLayout(main_layout)

    # ---- Función para calcular el IMC ----
    def calcular_imc(self):
        try:
            # Convertir entradas a números
            peso = float(self.input_peso.text())
            altura = float(self.input_altura.text())

            # Validar que sean valores positivos
            if peso <= 0 or altura <= 0:
                raise ValueError

            # Fórmula del IMC
            imc = peso / (altura ** 2)
            nombre = self.input_nombre.text() or "Usuario"

            # Clasificación del IMC
            if imc < 18.5:
                estado = "Bajo peso"
                color = "#3498db"  # azul
            elif 18.5 <= imc < 24.9:
                estado = "Normal"
                color = "#2ecc71"  # verde
            elif 25 <= imc < 29.9:
                estado = "Sobrepeso"
                color = "#f1c40f"  # amarillo
            else:
                estado = "Obesidad"
                color = "#e74c3c"  # rojo

            # Mostrar resultado en pantalla
            self.resultado_label.setText(f"{nombre}, tu IMC es {imc:.2f} ({estado})")
            self.resultado_frame.setStyleSheet(
                f"background-color: {color}; border-radius: 15px; padding: 10px; color: white;"
            )

        except:
            # Mensaje de error si se ingresan datos inválidos
            QMessageBox.warning(self, "Error", "Ingresa valores numéricos válidos mayores a cero.")

    # ---- Función para limpiar campos y reiniciar ----
    def nuevo_calculo(self):
        self.input_nombre.clear()
        self.input_peso.clear()
        self.input_altura.clear()
        self.resultado_label.setText("Resultado: ")

        # Restaurar color original del panel
        self.resultado_frame.setStyleSheet(
            "background-color: rgba(26, 188, 156, 0.2); border-radius: 15px; padding: 10px;"
        )
        self.input_nombre.setFocus()  # Poner el cursor en el campo nombre

# ---- Ejecución de la aplicación ----
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = CalculadoraIMC()
    ventana.show()
    sys.exit(app.exec_())