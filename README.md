# Leccion de analisis de texto

En esta leccion se uso el texto de Alejandro Humboldt titulado "SITIOS DE LAS CORDILLERAS Y MONUMENTOS DE LOS PUEBLOS INDÍGENAS DE AMERICA" 

## Orden de trabajo: 

#### Paso 1
  - El documento de Python titulado __pdfajpeg.py__ convirtio el pdf de dicho texto a imagenes de cada pagina. 

#### Paso 2

 - El documento de Python titulado __ROCcompleto.py__ convierte todas las imagenes a un solo file en forma textual en este caso el documento __textocompleto.txt__. Para esto utilizamso la biblioteca llamada __pytesseract__ 

#### Paso 3 

 - _Bajo desarrollo_ El documento de Python titulado __Frecuenciasdepalabras.py__ estara utilizando el paquete __NLTK__ y __WordCloud__ para producir un analisis de las palabras no triviales mas comunes en este trabajo de Humboldt.