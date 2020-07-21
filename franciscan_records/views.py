# franciscan_records/views.py
from django.shortcuts import render, redirect
from .models import Record
from django.views.generic import ListView
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import urllib, base64

def index(request):
    search_term = ''

    if request.GET and request.GET['search']:
        search_term = request.GET['search']
        records = Record.objects.all().filter(text__icontains=search_term)
    else:
        records = None

    return render(request, 'franciscan_records/index.html', {'records' : records, 'search_term': search_term })

def wordcloud(request):
    df = pd.DataFrame(list(Record.objects.all().values()))
    text = " ".join(t for t in df.text)
    stopwords = set(STOPWORDS)
    stopwords.update(['franciscan'])
    wordcloud = WordCloud(width=1000, height=500, stopwords=stopwords, background_color="white").generate(text)
    plt.figure(figsize=(15, 10))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    image = io.BytesIO()
    plt.savefig(image, format='png')
    image.seek(0)  # rewind the data
    string = base64.b64encode(image.read())
    image_64 = 'data:image/png;base64,' + urllib.parse.quote(string)

    return render(request, 'franciscan_records/wordcloud.html', {'wordcloud': image_64})
