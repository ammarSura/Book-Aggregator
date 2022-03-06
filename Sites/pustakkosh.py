from packages import *


def getBooksPustakkosh(searcher):

    books = []

    url = "https://pustakkosh.com/rent_or_buy_books.php?s="
    req = requests.get(url + searcher)
    soup = BeautifulSoup(req.text, "html.parser")
    items = (soup.find_all(class_ = "grid-product__wrap-inner"))

    for item in items:
        # book = Book()
        urlString = str(item.find(class_ = "grid-product__title"))
        helper1 = urlString.find("href=\"") + 6

        titleString = str(item.find(class_ = "grid-product__title-inner"))
        
        authorString = titleString

        priceString = str(item.find(class_ = "grid-product__price-amount"))

        author = authorString[authorString.find(" by ") + 3 : authorString.find("</div>")].strip()
        
        title = titleString[titleString.find(">") + 1 : titleString.find("</div>")]

        price = priceString[priceString.find(">") + 1 : priceString.find(".00INR")].replace(" ", "")
        
        url = urlString[helper1:urlString.find("\"", helper1)]

        # books.append(book)
        books.append(
            {
                "title": title, 
                "price": price, 
                "url": url,
                "author": author,
                "site": "pustakkosh.com"
            }
        )

    return books
