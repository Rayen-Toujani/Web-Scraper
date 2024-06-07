import requests
from bs4 import BeautifulSoup

url = "https://protein-shop-tunisia.tn/categorie-produit/nutrition-sportive/gainer-prise-de-poids/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    Prot_Names = []

    for prot in soup.find_all('h3'):
        # Extract the text from the <a> tag within the <h3> tag
        isem_prot = prot.find('a').get_text()
        Prot_Names.append(isem_prot)

    for idx, isem_prot in enumerate(Prot_Names):
        print(f"{idx + 1}. {isem_prot}")

else:
    print("Failed to fetch")
