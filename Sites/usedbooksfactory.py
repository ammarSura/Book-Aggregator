from packages import *


def getBooksFactory(searcher):
    books = []

    url = "https://www.usedbooksfactory.com/buy-second-hand-old-books/search?titlepublisher="
    req = requests.get(url + searcher)
    soup = BeautifulSoup(req.text, "html.parser")
    items = (soup.find_all(class_ = "li_box"))

    for item in items:
        # book = Book()
        
        urlString = str(item.find(class_ = "aa-product-img"))

        titleString = str(item.find(class_ = "aa-add-card-btn add_to_cart"))
        helper1 = titleString.find("data-bookname=\"") + 15

        priceString = str(item.find(class_ = "aa-add-card-btn add_to_cart"))
        
        helper2 = priceString.find("data-price=\"") + 12

        title = titleString[helper1:titleString.find("\"", helper1)]

        author = title[title.find("-") + 1:]

        price = priceString[helper2:priceString.find("\"", helper2)]
        
        url = "https://www.usedbooksfactory.com" + urlString[32:urlString.find("\"", 32)]

        # books.append(book)
        books.append(
            {
                "title": title, 
                "price": price, 
                "url": url
            }
        )

    return books