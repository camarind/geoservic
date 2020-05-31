import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPixmap
# se importan las librerias
import webbrowser
import folium
# pedir lugar para geolocalizar
from geopy.geocoders import Nominatim
import time
import math

# esto es de PyQt5
title_font = QFont("Candara", 14)
title_results_font = QFont("Candara", 14)

#clase de PyQt5
class Window(QWidget):

    def __init__(self):
        super(). __init__()
        # titulo que se muestra en la venta
        self.setWindowTitle("GeoServi Buscando Mapas")
        self.setGeometry(950, 100, 350, 530)# location x, y - size x,y
        self.showGUI()

# Titulo que se muetra en la venta
    def showGUI(self):
        self.title = QLabel("Busca un lugar y genera su mapa", self)
        self.title.setFont(title_font)
        self.title.move(60, 10)
        # imágen
        self.image = QLabel(self)
        self.image.setPixmap(QPixmap('marca.png'))
        self.image.move(160,60) # x,y
        #Etiqueta y campo de texto Para el nombre del lugar
        self.label_lugar= QLabel("Lugar",self)
        self.label_lugar.move(10, 50)
        self.name_lugar= QLineEdit(self)
        self.name_lugar.move(10,65)
        self.name_lugar.setPlaceholderText("Digite un lugar")
        # Etiquetas y campos de texto notas
        self.label_grade1 = QLabel("1 Mapa a Color, 2: Mapa a Blanco y Negro", self)
        self.label_grade1.move(10,100)
        self.grade1 = QLineEdit(self)
        self.grade1.move(10,120)
        self.grade1.setPlaceholderText("Ingrese 1 o 2")
        #Etiqueta y campo de texto Para el nombre del mapa
        self.label_mapa= QLabel("Asignar nombre al mapa",self)
        self.label_mapa.move(10, 150)
        self.name_mapa= QLineEdit(self)
        self.name_mapa.move(10,170)
        self.name_mapa.setPlaceholderText("Asignar nombre al mapa")


        #Boton guardar
        self.save_button = QPushButton("Buscar", self)
        self.save_button.move(10,250)
        self.save_button.clicked.connect(self.get_values)

        # tabla resultados
        self.label_results = QLabel("Resultados de la busqueda", self)
        self.label_results.setFont(title_results_font)
        self.label_results.move(10, 290)
        self.results = QTableWidget(self)
        self.results.setRowCount(0)
        self.results.setColumnCount(2)
        self.results.setHorizontalHeaderItem(0, QTableWidgetItem("Lugar"))
        self.results.setHorizontalHeaderItem(1, QTableWidgetItem(" Opcion"))
        self.results.move(10, 310)
        self.show()
    #Evento del boton
    def message(self, msj):
        QMessageBox.information(self, "Advertencia", msj)

    def get_values(self):
        if(self.name_lugar.text()== "" or self.grade1.text() == "" or self.name_mapa.text() == ""):
            self.message("Todos los campos deben ser diligenciados")

        else:
            try:
                average = (float(self.grade1.text()))
                average = round(average,2)
                rowPosition = self.results.rowCount()
                self.results.insertRow(rowPosition)
                self.results.setItem(rowPosition, 0, QTableWidgetItem(self.name_lugar.text()))
                self.results.setItem(rowPosition, 1, QTableWidgetItem(str(average)))
                
                # Con esta funcion podemos ubicar cualqier lugar en el mapa
                geo = Nominatim(user_agent="MyApp")
                lugar = self.name_lugar.text()
                loc = geo.geocode(lugar)
                
                #print(loc)
                #print(loc.latitude, loc.longitude)
                ### voy a pasar los datos a la funcion con Folium para pintar los mapas
                latitud = loc.latitude
                longitud = loc.longitude
                resp = average
                eXten = '.html'
                if resp == 1.0:
                    #pinto el mapa a color
                    #print(" Usted Eligio la opcion 1 mapa a color ")
                    mapa = folium.Map(location=[latitud, longitud], zoom_start=12, control_scale=True)
                    #Marquilla en el mapas
                    tooltip = 'Marker'
                    folium.Marker([latitud, longitud], popup='Marker', tooltip=tooltip).add_to(mapa)
                    nombreMapaColor = self.name_mapa.text()
                    ruta = 'C:\\Users\\cesar\\Desktop\\MapasFolium\\'
                    rutaColor = ruta+nombreMapaColor+eXten
                    #Marquilla en el mapas
                    tooltip = nombreMapaColor
                    folium.Marker([latitud, longitud], popup=nombreMapaColor, tooltip=tooltip).add_to(mapa)
                    mapa.save(rutaColor)
                     #Para abrir el archivo automáticamente
                    webbrowser.open_new_tab(rutaColor)
                elif resp == 2.0:
                    #pinto el mapa a blanco y negro
                    #print(" Usted Eligio la opcion 2 mapa a Blancon y Negro ")
                    mapa= folium.Map(location=[latitud, longitud], zoom_start=12, control_scale=True, tiles='Stamen Toner')
                    nombreMapaBlancoNegro = self.name_mapa.text()
                    ruta ='C:\\Users\\cesar\\Desktop\\MapasFolium\\'
                    rutaNegro = ruta+nombreMapaBlancoNegro+eXten
                    tooltip = nombreMapaBlancoNegro
                    folium.Marker([latitud, longitud], popup=nombreMapaBlancoNegro, tooltip=tooltip).add_to(mapa)
                    mapa.save(rutaNegro)
                     #Para abrir el archivo automáticamente
                    webbrowser.open_new_tab(rutaNegro)
                else:
                    resp=0
                #se limpian los campos
                self.name_lugar.clear()
                self.grade1.clear()
                self.name_mapa.clear()
            except:
                self.message("Digite Lugares y campos válidos")




#Main del programa con PyQt5

def main():
    ''' Manejo de la GUI (Flujos y eventos)'''
    App = QApplication(sys.argv)
    window = Window()
    ''' Se evita cerrar la venta '''
    sys.exit(App.exec_())

main()