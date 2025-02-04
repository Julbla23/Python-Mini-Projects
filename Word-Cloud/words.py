#moduł który tworzy wykresy i wizualizacje
import matplotlib.pyplot as plt

"""
    WordCloud: generuje chmury słów.
    STOPWORDS: zbiór często występujących, mało znaczących słów, które można wykluczyć z chmury słów.
    ImageColorGenerator: pozwala na kolorowanie chmury słów na podstawie obrazka. 
"""
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

#biblioteka używana do pracy z tablicami (array) i operacjami matematycznymi
import numpy as np

#biblioteka która służy do pracy z obrazami
from PIL import Image

#Moduł sys i os: używane do pracy z systemem operacyjnym np. zmiana katalogu roboczego
import sys, os

"""
    sys.path[0]: zwraca ścieżkę do katalogu, w którym znajduje się plik skryptu
    os.chdir(...): dzięki temu skrypt zawsze działa we właściwym folderze, niezależnie od tego, skąd został uruchomiony.
"""
os.chdir(sys.path[0])

# Read text. Encoding='utf-8' zapewnia poprawne odczytywanie znaków specjalnych (np. polskich liter)
text = open('../text-files/ode-to-joy.txt', mode='r', encoding='utf-8').read()

#przypisuje zbiór słów stop do zmiennej stopwords, co później pozwoli na ich automatyczne pominięcie podczas geenrowania chmury słów
stopwords = STOPWORDS

"""
    np.array: zamienia obraz na tablicę NumPy, gdzie każdy piksel ma wartość od 0 do 255
    .convert('L'): konwertuje obraz na skalę szarości (L oznacza luminację, czyli jasnkość piksela od 0 = czarny do 255 = biały).
"""
mask = np.array(Image.open('../Images/tree.jpg').convert('L'))
mask = np.where(mask > 128, 255, 0)

# .convert('RBG'): konwertuje obraz do kolorowego formatu RGB (każdy piksel ma trzy wartości: R (czerwony), G (zielony), B (niebieski)
color_image =np.array(Image.open('../Images/tree.jpg').convert('RGB'))

print(len(stopwords))

wc = WordCloud(
    background_color='white',
    stopwords=stopwords,
    mask=mask,
    height = 600,
    width=400,
    contour_width=1,
)

# generuje chmurę słów na podstawie wczytanego tekstu text
wc.generate(text)

# tworzy obiekt image_colors, który pobiera kolory bezpośrednio z obrazu color_image
image_colors = ImageColorGenerator(color_image)

#zamienia domyślny kolor chmury słów na kolory pobrane z color_image, słowa pokolorowane tak aby pasowały do kolorystyki
wc.recolor(color_func=image_colors)

#store to file
wc.to_file('wordcloud8_output.png')

#tworzy nowy obiekt wykresu o rozmiarze 10x6 cali. Pomaga ustawić odpowiednie proporcje wyświetlanej chmury słów. Bez tej linijki obraz mógłby być domyślnie zbyt mały lub źle dopasowany do ekranu
plt.figure(figsize=(10, 6))

#wyświetla chmurę słów i wygładza krawędzi i sprawia że obraz wygląda bardziej naturalnie, bez tego krawędzie mogłyby być bardziej poszarpane.
plt.imshow(wc, interpolation='bilinear')

#usuwa osie X i Y dzięki temu chmura słów wygląda jak czysty obraz bez zbędnych znaczeń
plt.axis('off')