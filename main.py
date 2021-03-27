import requests
import smtplib
import lxml
from bs4 import BeautifulSoup

amazon_product_end_point = "https://www.amazon.in/Rider-Republic-Womens-Cargo-305165-32_Blue_32/dp/B07GWWSZPN/ref=sr_1_5?dchild=1&keywords=cargo+pants+for+women&qid=1616764446&sr=8-5"

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url = amazon_product_end_point, headers = headers)
response.raise_for_status()
# print(response.text)

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

price = soup.find(id="priceblock_ourprice").get_text()
min_price = float(price.split('₹')[1].split('\xa0')[1].split(' -')[0])
print(min_price)

if min_price <=500:
   with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user = "oiji2504@gmail.com", password="your_password")
        connection.sendmail(
            from_addr="oiji2504@gmail.com", 
            to_addrs= "oiji2504@gmail.com",
            msg = f"Subject:Cargo Pants Sale!!\n\nlink: {amazon_product_end_point}\n\nNow at a discount price of Rs {min_price}!"
        )