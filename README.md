# Proyecto Final: Parte 1
---
### Resumen
Este proyecto consiste en Face Spoofing Detection. Primero, se realiza el entrenamiento del modelo de Deep Learning usando un dataset de rostros de personas. Segundo, se ejecuta la aplicación, utilizando los pesos del modelo que nos ayudará a clasificar lás imágenes. Finalmente, se debe conectar a un celular que recibirá lás imágenes de la cámara como input, y marcará en un cuadro verde los rostros reales y color rojo los rostros no reales.
![Descripción de la imagen](/img/prueba.png "Face Spoofing Detection")

### Desarrollo

En el proyecto se ha utilizado un modelo de Deep Learning para la detección de rostros reales o no. Para ejecutar el proyecto no necesitar entrenar el modelo nuevamente. Los pesos del modelo se encuentra en **antispoofing_models/antispoofing_model.h5**. Por lo que, solo requiere ejecutar el archivo **app.py**. Y descomentar las siguientes líneas de código:

```sh
# video.open("http://192.168.1.101:8080/video")
# vs = VideoStream(src=0).start()
# time.sleep(2.0)
```

## Installation

```sh
opencv-python==4.6.0.66
tensorflow==2.11.0
```