import requests
from bs4 import BeautifulSoup
import smtplib # i can now send email
import time

URL = 'https://www.amazon.com.br/FITA-LED-FONTE-CONTROLE-REMOTO/dp/B07CGK4CFM/ref=sr_1_1?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=led&qid=1595348860&sr=8-1'


headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:5])

    if(converted_price < 60):
        send_email()
    print(converted_price)
    print(title)
   

def send_email():
    server = smtplb.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('fakeaccont@gmail.com', '123456789')
    body = 'Check your ptoduct in amazon, https://www.amazon.com.br/FITA-LED-FONTE-CONTROLE-REMOTO/dp/B07CGK4CFM/ref=sr_1_1?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=led&qid=1595348860&sr=8-1'
    msg = f"Subject: {Subject}\n\n{body}"

    server.sendmail(
        'fakeaccont@gmail.com',#from
        'anotherfakeaccont@gmail.com',#to
        msg
    )
    print("Email sent :)")

    server.quit()

    while(True):
        check_price()
        time.sleep(60 * 60)
