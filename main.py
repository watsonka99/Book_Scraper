import requests
import bs4

f = open("books.csv", "a")
f.write("Title, price, url, img\n")

url = "http://books.toscrape.com/catalogue/"
base_url = "http://books.toscrape.com/catalogue/page-{}.html"

for i in range(1, 2):
    result = requests.get(base_url.format(str(i)))
    soup = bs4.BeautifulSoup(result.text, "lxml")
    books = soup.select(".product_pod")
    for j in range(0, len(books)):
        title = soup.select("h3")[j].contents[0]['title']
        price = soup.select(".price_color")[j].getText()
        book_url = soup.select("h3")[j].contents[0]['href']
        img = soup.select(".thumbnail")[j]['src']
        f.write(title + ", "+ price + ", " + url + book_url + ", " + "http:"+img +"\n")
        
f.close()
