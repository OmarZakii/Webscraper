from os import name
from urllib import request
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from urllib.request import Request
import requests
import re
import validators
import lxml.html 
import mysql.connector
import random
# db =mysql.connector.connect(
#     host ="localhost",
#     user ="root",
#     passwd="12345678",
#     database="Medicine"
#     #passwd="210650@marcos"
# )
# mycursor =db.cursor()
headers_list = [
    # 1. Headers
    {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0', 
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0'},
    # 2. Headers
    {'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/89.0.4389.82 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,'
                  'image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-US,en;q=0.9'},
]

proxies = "78.189.20.150:5678"

url = NULL
req = Request(
    url, 
    data=None, 
    
    headers=random.choice(headers_list),
    pro
)
# req = requests.get(url,proxies={'http':proxy,'https':proxy})

page = uReq(req)

page_html = page.read()
page.close()

page_soup = soup(page_html,"html.parser")

soup1 = soup(page_html, "xml")
#tree = lxml.html.parse(page_html)
# page_soup3 = soup(page_html,"Xpath")
# page_soup.h1
# print(page_soup.body.span)
# boxes=page_soup.find_all("div",{"class":"title-wrapper"})

# page_soup2 = soup(page_html,features= "xml")
# prices = page_soup2.select("bdi")
# title =page_soup2.find_all("a",{"class":"woocommerce-LoopProduct-link woocommerce-loop-product__link"})
# #img = tree.xpath("section[@id='section_632197323']")
# img =page_soup.select("section.section")
# id =page_soup2.find_all("div",{"class":"add-to-cart-button"}) 

# for count in range(len(boxes)):
#     print(prices[count].text.strip("span").strip("EGP"))
#     print(title[count].text.strip("a"))
#     print(id[count].a["data-product_id"])
#     print(img[count])


        # # print(y.get('href'))
        # # print("1")
        # url1=y.get('href')
        
        # page1 = uReq(url1)
        # html = page1.read()
        # page.close()
        # page_soup3 = soup(html,features= "lxml")
        # mylinks =page_soup3. find_all("div",{"class":"product-category col product"})
        # if mylinks:
        #     print("hi")

        
        # for comp in mylinks:
        #   a=comp.find_all('a')
        #   for z in a:
        #     x=z.get('href')
        #     myread=uReq(x)
        #     html_pro = myread.read()
        #     page.close()
        #     page_soup9 = soup(html_pro,"xml")
        #     boxes=page_soup9.find_all("div",{"class":"title-wrapper"})
        #     page_soup4 = soup(html_pro,features= "xml")
        #     prices = page_soup4.select("bdi")
        #     title =page_soup4.find_all("a",{"class":"woocommerce-LoopProduct-link woocommerce-loop-product__link"})
        #     #img = tree.xpath("section[@id='section_632197323']")
        #     img =page_soup9.select("section.section")
        #     id =page_soup4.find_all("div",{"class":"add-to-cart-button"}) 
        #     print (len(boxes))
        #     print(len(title))

            # for count in range(len(boxes)):
                # print(prices[count].text.strip("span").strip("EGP"))
                # print(title[count].text.strip("a"))
                # print(id[count].a["data-product_id"])
                # print(img[count])
        


def get_products(links):

   for cnt in range (len(links)):
        navigate_links = links[cnt].find_all('a') 
        for link in navigate_links:
            url=link.get('href')
            print(url)
            page = uReq(url)
            page_html = page.read()
            page.close()
            page_soup3 = soup(page_html,features= "lxml")
            #mylinks =page_soup3. find_all("div",{"class":"product-category col product*"})
            mylinks =page_soup3.find_all('div', attrs={'class': re.compile('^product-category col product*')})
            title_page = page_soup9.find_all("div",attrs={"class":re.compile('^flex-col flex-grow*')})
            print(title_page.text.strip("h1"))
            title_db1 =title_page.text.strip("h1")
            # mycursor.execute("CREATE TABLE "+title_db+"(name VARCHAR(100),id INT PRIMARY KEY AUTO_INCREMENT")
          
            
            if  (mylinks) :
                get_products(mylinks)
            else:
                page_soup9 = soup(page_html,"html.parser")
                boxes=page_soup9.find_all("div",{"class":"title-wrapper"})
                page_soup4 = soup(page_html,features= "xml")
                prices = page_soup9.select("bdi")
                title =page_soup9.find_all("a",{"class":"woocommerce-LoopProduct-link woocommerce-loop-product__link"})
                #img = tree.xpath("section[@id='section_632197323']")
                # img =page_soup4.select("section.section")
                id =page_soup9.find_all("div",{"class":"add-to-cart-button"}) 
                title_page = page_soup9.find_all("div",attrs={"class":re.compile('^flex-col flex-grow*')})
                print(title_page.text.strip("h1"))
                title_db2=title_page.text.strip("h1")
                # mycursor.execute("INSERT INTO"+title_db1+"(name) VALUES (%s)"
                    # ,(name))
                # mycursor.execute("CREATE TABLE "+title_db2+"(name VARCHAR(100),id INT  PRIMARY KEY,price DOUBLE)")
                for count in range(len(boxes)):
                    print(pro_id=id[count].a["data-product_id"])
                    pro_id=id[count].a["data-product_id"]
                    print(name=title[count].text.strip("a"))
                    name=title[count].text.strip("a")
                    print(prices[count].text.strip("span").strip("EGP"))
                    price =prices[count].text.strip("span").strip("EGP")
                    # mycursor.execute("INSERT INTO"+title_db2+"(name,id,price) VALUES (%s,%s,%s)"
                    # ,(name,pro_id, price))

                    
                    
#                     # print(img[count])   

        
links =page_soup. find_all("ul",attrs={'class':re.compile('^sub-menu nav-dropdown*')})
# for cnt in links:
#     navigate_links = links[cnt].find_all('a')
    
    
get_products(links)


# # dom =  lxml.html.fromstring(page.read())

# # for link in dom.xpath('//a/@href'): # select the url in href for all a tags(links)
# #     print (link)
    
  


    




# # print(box[8])


# # print(box[0].div.span) 
