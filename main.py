import requests
import bs4

f = open("books.csv", "a")
f.write("Title, price, url, img\n")

url = "http://books.toscrape.com"
base_url = "http://books.toscrape.com/catalogue/page-{}.html"

for i in range(1, 21):
    result = requests.get(base_url.format(str(i)))
    soup = bs4.BeautifulSoup(result.text, "lxml")
    books = soup.select(".product_pod")
    for book in books:
        title = book.select("h3")[0].select("a")[0]['title']
        price = book.select(".price_color")[0].getText()
        price = price[1 : : ]
        img = book.select(".thumbnail")[0]['src']
        img = img[2: : ]
        img = url + img
        book_url = book.select("h3")[0].select("a")[0]['href']
        f.write('"' +title +'"' + ", "+ price + ", " + url + book_url + ", " + img +"\n")
f.close()
