import requests
from bs4 import BeautifulSoup

url = "https://protein-shop-tunisia.tn/categorie-produit/nutrition-sportive/gainer-prise-de-poids/"

response = requests.get(url)

if response.status_code==200:
    soup = BeautifulSoup(response.content,'html.parser')

    Prot_Names = []
