from django.shortcuts import render
import requests
from requests_oauthlib import OAuth1
import os
from dotenv import load_dotenv

def index(request):
    home_page_data = { 
        "park": 'info'
    }
    return render(request, "pages/index.html", home_page_data)

def about(request):
    auth = OAuth1(os.environ['key'])
    endpoint = f"https://developer.nps.gov/api/v1/alerts"
    response = requests.get(endpoint, auth=auth)
    responseJSON = response.json()
    print(responseJSON)
    np_data = { 
        "key": 'value'
    }
    return render(request, "pages/about.html", np_data)

def contact(request):
    return render(request, "pages/contact.html")