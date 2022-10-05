from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def article(request):

    # caso queira procurar sobre um tema deve-se colocar como string na variavel abaixo, chamada subject_to_find, por exemplo

    # subject_to_find = 'bitcoin'

    subject_to_find = ""

    about = subject_to_find or "keyword"

    url = f"https://newsapi.org/v2/everything?q={about}&apiKey=76418f5dd1ad48939d1b1e17bcd7c824"

    response = requests.get(url)

    json = response.json()

    return render(request, "articles.html", {"articles": json["articles"]})
