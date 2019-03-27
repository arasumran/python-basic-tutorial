import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.hebele.com/preo-p-watch-3-akilli-saat-akilli-bileklik-p-145056438')
soup = BeautifulSoup(page.text, 'html.parser')

image_url = soup.find(class_='product-image-gallery').contents[1].find('img')
image_new_price = soup.find(class_='discount-rate-tag-sticky').findAll(class_='new-price')[0].string
print("Product Name :  ", image_url['alt'])
print("Product source : ", image_url['src'])
print("Product Image :", image_new_price.split('\t')[-1])
