import requests
import bs4
from bs4 import BeautifulSoup
from bs4 import SoupStrainer

#print(page.text)
#print(soup.prettify())
#____________________________________________________________________________________________________________
#Mvideo
#Page1_Spb    
url = 'https://www.mvideo.ru/shops/store-list??storePickerList.json.jsp?page=1&tab=list?cityId=CityCZ_1638'
page = requests.get(url)
soup = bs4.BeautifulSoup(page.text, 'html.parser')
city2 = soup.find("div",class_="name")
#print (city2.get_text())

for link in soup.find_all('p'):
    print(link.get_text('p'))
    
#Page2_Spb
url = 'https://www.mvideo.ru/shops/store-list??storePickerList.json.jsp?page=2&tab=list?cityId=CityCZ_1638'
page = requests.get(url)
soup = bs4.BeautifulSoup(page.text, 'html.parser')

#city2 = soup.find("div",class_="name")
#print (city2.get_text())

for link in soup.find_all('p'):
    print(link.get_text('p'))
#____________________________________________________________________________________________________________

#Eldorado
url = 'https://www.eldorado.ru/info/shops/11279/'
page = requests.get(url)
print(page.status_code)
soup = bs4.BeautifulSoup(page.text, 'html.parser')


#city = soup.find(class_='metro')
#print (city.contents[1])


#city1 = soup.find_all("div",class_='metro')
#print (city1)

for link in soup.find_all("div",class_="metro"):
    print(link.get_text('p'))
#____________________________________________________________________________________________________________

#Mvideo
#Krasnodar   
url = 'https://www.mvideo.ru/shops/store-list??storePickerList.json.jsp?page=1&tab=list?cityId=CityCZ_2128'
page = requests.get(url)
soup = bs4.BeautifulSoup(page.text, 'html.parser')
city2 = soup.find("div",class_="name")
for link in soup.find_all('p'):
    print(link.get_text('p'))
#____________________________________________________________________________________________________________

#Mvideo
#Rostov  
url = 'https://www.mvideo.ru/shops/store-list??storePickerList.json.jsp?page=1&tab=list?cityId=CityCZ_2446'
page = requests.get(url)
soup = bs4.BeautifulSoup(page.text, 'html.parser')
city2 = soup.find("div",class_="name")
for link in soup.find_all('p'):
    print(link.get_text('p'))
#____________________________________________________________________________________________________________


