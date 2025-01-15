from pytubefix import YouTube
from pytubefix.cli import on_progress
import os,shutil



def convertir(url,format):
    cPath = os.getcwd()
    folder = 'vids'
    path = os.path.join(cPath,folder)
    checkAndCreateDirectory(path)

    deleteFiles(path)


    if format == 'MP4':
        youtubeObject = YouTube(url, 'WEB')
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        try:
            object = youtubeObject.download(path)  
            print(object)
            return  object         
        except:
            print("Error al descargar MP4")   

    elif format == 'MP3':
        youtubeObject = YouTube(url, 'WEB')
        youtubeObject = youtubeObject.streams.filter(only_audio=True).first()
        try:       
            out = youtubeObject.download(path)  
            base,ext = os.path.splitext(out)
            new = os.path.join(path, youtubeObject.title + '.mp3')  
            os.rename(out,new)
            return new
            
            
        except:
            print("Error al descargar MP3")


def checkAndCreateDirectory(folder):
    # Comprobar si el directorio existe
    if not os.path.exists(folder):
        # Crear el directorio si no existe
        os.makedirs(folder)
        print(f"El directorio {folder} ha sido creado.")
    else:
        print(f"El directorio {folder} ya existe.")

def deleteFiles(folder):
    try:
        for file in os.listdir(folder):
            file_path = os.path.join(folder,file)

            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        print('Files deleted')
    except Exception as e:
        print(f"File cann't be deleted: {e}")

cPath = os.getcwd()
folder = 'vids'
path = os.path.join(cPath,folder)
print(path)

deleteFiles(path)