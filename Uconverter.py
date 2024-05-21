import os
import sys
#modulos de pyQT
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5.uic import loadUi

# Modulos youtube 

from pytube import YouTube
from pytube.cli import on_progress



class DlgIniciar(QDialog):
    def __init__(self): #traer el usuario
        super(DlgIniciar, self).__init__()
        loadUi('ui/form.ui',self)
        # self.b_ingresar.clicked.connect(self.crud)
        self.progressBar.hide()
        self.b_youtube.clicked.connect(self.convertir)

    def convertir(self):
        if self.combo_youtube.currentText() == 'MP4':
            self.progressBar.show()
            bar = self.progressBar
            bar.setValue(20)
            url = self.t_url_youtube.text()
            path = os.getcwd()

            youtubeObject = YouTube(url)
            youtubeObject = youtubeObject.streams.get_highest_resolution()
            bar.setValue(60)
            try:
                youtubeObject.download(path)            

                bar.setValue(80)

                bar.setValue(100)
                msg = QMessageBox()        
                msg.setWindowTitle("Completado")
                msg.setText("Se ha descargado el video!!")
                msg.exec() 
                self.progressBar.hide()
            
            except:
                print("Error al descargar MP4")   

        elif self.combo_youtube.currentText() == 'MP3':
             self.progressBar.show()
             bar = self.progressBar
             bar.setValue(20)
             
             url = self.t_url_youtube.text() 
             
             
             youtubeObject = YouTube(url)
             youtubeObject = youtubeObject.streams.filter(only_audio=True).first()
             bar.setValue(60)
             try:
                path = os.getcwd()
                print(path)          
                out = youtubeObject.download(path)  
                
                #Cambiar a MP3
                base,ext = os.path.splitext(out)
                new = youtubeObject.title + '.mp3'
                
                bar.setValue(80)
                
                os.rename(out,new)
                bar.setValue(100)
                
                msg = QMessageBox()        
                msg.setWindowTitle("Completado")
                msg.setText("Se ha descargado el audio!!")
                msg.exec() 
                self.progressBar.hide()
                
             except:
                print("Error al descargar MP3")

                  

#prgrama o ejecucion principal de ejecucion
app = QApplication(sys.argv)#'argv'#la aplicacion se encarga de minimizar o max la ventana
dlgIniciar = DlgIniciar()  
dlgIniciar.show()
sys.exit(app.exec_())#ejecutar una salida        