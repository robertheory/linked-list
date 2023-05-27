import requests
from bs4 import BeautifulSoup

def news():
    url='https://aisweb.decea.mil.br/?i=aerodromos&codigo=SBMT'
      
    resp=requests.get(url)

    if resp.status_code==200:
        print("Successfully opened the web page")
      
        soup=BeautifulSoup(resp.text,'html.parser')
        
        cartas = []

        sunrise = soup.find('sunrise').text
        print(sunrise)
        sunset = soup.find('sunset').text
        print(sunset)
        
        elements = soup.find_all('ul',class_='list list-icons list-primary list-icons-style-2')

        for element in elements:
            sibling = element.find_previous_sibling('h4')
            cartas.append(sibling.text)

        print(cartas)
      
    else:
        print("Error")
          
news()