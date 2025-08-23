# Youtube-mp3 DOWNLOADER

## Objetivo de la aplicación
Creada con el fin de utilizarlo en ambientes personales. En este caso dentro de un Ubuntu server y exponiendolo con Docker dentro de la red.

## Funcionamiento
Utiliza como base el comado:
`yt-dlp -x --audio-format mp3 "URL_DEL_VIDEO"`
La descarga se guarda localmente en el servidor dentro de /MUSIC/Youtube. Ademas, cuando se descarga desde la interfaz web, el navegador permite elegir dónde guardar el archivo MP3 en el equipo del usuario. 

## Uso
Al exponer la aplicación con el siguiente comando:
`sudo docker build youtube-mp3 .`
`sudo docker run -d --name youtubemp3 -p 5500:5500 -v ~/Music/Youtube:/downloads --restart unless-stopped youtube-mp3`

Parámetros explicados:

- -d: ejecuta el contenedor en segundo plano.

- --name youtubemp3: asigna un nombre al contenedor.

- -p 5500:5500: expone el puerto 5500 del contenedor al puerto 5500 del host.

- -v ~/Music/Youtube:/downloads: mapea la carpeta local donde se guardarán los MP3.

- --restart unless-stopped: hace que el contenedor se reinicie automáticamente si el servidor se reinicia.

Una vez levantado, la aplicación estará disponible en tu navegador en:

http://IP_DEL_SERVIDOR:5500

## Descargar música desde línea de comando (opcional)

Si querés descargar música directamente sin usar la web, podés ejecutar:
`yt-dlp -x --audio-format mp3 "URL_DEL_VIDEO" `

Los archivos se guardarán en la carpeta donde ejecutes el comando, o en la ruta que especifiques usando -o.

## Notas

- Recomendado solo para uso personal dentro de redes privadas.
- Asegúrate de tener suficiente espacio en disco para guardar tus descargas.
- Esta aplicación no almacena los MP3 dentro del contenedor, solo en la ruta mapeada en el host.