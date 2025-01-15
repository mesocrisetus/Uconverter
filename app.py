from flask import Flask,render_template,request,send_from_directory
import os
import functions as fn

app = Flask(__name__)
app.secret_key =os.urandom(24)

@app.route("/")
def index():
    
    return render_template('index.html')


@app.route('/descargarVideo', methods=['POST'])
def descargarVideo():
    url = request.form['url']
    format = request.form['format']
    path = fn.convertir(url,format)
    if path:
        filename = os.path.basename(path)
        return render_template('index.html',filename=filename,format=format)
    else:
        return "Error al convertir el video", 500

@app.route('/download/<filename>')
def download_file(filename):
    folder = os.path.join(os.getcwd(), 'vids') 
    return send_from_directory(folder, filename, as_attachment=True)

if __name__ == '__main__':
    app.run() 