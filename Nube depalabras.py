from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import string
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')



# Cargar las palabras comunes
palabras_comunes_espanol = set(stopwords.words('spanish'))

# Anadiendo palabras comunes particulares a este texto

palabras_comunes_espanol.add('á')
palabras_comunes_espanol.add('ma')
palabras_comunes_espanol.add('ó')
palabras_comunes_espanol.add('si')
palabras_comunes_espanol.add('p')
palabras_comunes_espanol.add('segun')
palabras_comunes_espanol.add('tambien')
palabras_comunes_espanol.add('solo')
palabras_comunes_espanol.add('tre')
palabras_comunes_espanol.add('mismo')
palabras_comunes_espanol.add('sino')
palabras_comunes_espanol.add('despues')
palabras_comunes_espanol.add('cada')
palabras_comunes_espanol.add('cuya')
palabras_comunes_espanol.add('parte')
palabras_comunes_espanol.add('tan')
palabras_comunes_espanol.add('cuyo')
palabras_comunes_espanol.add('pue')
palabras_comunes_espanol.add('parece')
palabras_comunes_espanol.add('aun')


def mostrar_nube_de_palabras(datos, titulo=None):
    nube_de_palabras = WordCloud(
        background_color='white',
        stopwords=palabras_comunes_espanol,
        max_words=200,
        max_font_size=40,
        scale=3,
        random_state=1  
    ).generate(str(datos))

    fig = plt.figure(1, figsize=(12, 12))
    plt.axis('off')
    if titulo:
        fig.suptitle(titulo, fontsize=20)
        fig.subplots_adjust(top=2.3)

    plt.imshow(nube_de_palabras)
    plt.savefig("nube_de_palabras_editada2")



# Leer el texto desde 'textocompleto.txt'
with open('textocompleto.txt', 'r', encoding='utf-8') as archivo:
    datos_texto = archivo.read()

# Crear la nube de palabras
mostrar_nube_de_palabras(datos_texto)
