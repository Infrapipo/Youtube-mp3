from flask import Flask, render_template, request, send_file
import yt_dlp
import os

app = Flask(__name__)
DOWNLOAD_FOLDER = "/downloads"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        if url:
            # Configuración para descargar en MP3
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
                'quiet': True,
                'noplaylist': True,
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=True)
                    filename = ydl.prepare_filename(info)
                    # yt-dlp crea el mp3 con mismo nombre pero extensión .mp3
                    mp3_file = os.path.splitext(filename)[0] + ".mp3"

                # Enviar archivo al usuario
                response = send_file(mp3_file, as_attachment=True)
                
                # Borrar archivo del contenedor después de enviarlo
                os.remove(mp3_file)
                
                return response
            except Exception as e:
                return f"Error: {e}"

    return render_template("index.html")

if __name__ == "__main__":
    os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)
    app.run(host="0.0.0.0", port=5000)
