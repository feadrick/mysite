from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
import json
def index(request):
    r  = requests.get("http://www.uitm.edu.my/")
    data = r.text
    soup = BeautifulSoup(data)
    url_list=[]
    for link in soup.find_all('a'):
        url_list.append(link.get('href'))
    data={'data':url_list}
    return render(request,'polls/test.html',data)