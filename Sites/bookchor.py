from packages import *
#soldouts
#page changing
def getBooksChor(searcher):
    books = []

    url = "https://www.bookchor.com/search/?query="
    req = requests.get(url + searcher)
    soup = BeautifulSoup(req.text, "html.parser")
    items = (soup.find_all(class_ = "product-item"))

    for item in items:
        # book = Book()
        urlString = str(item.find('h3').find('a'))
        
        titleString = str(item.find(class_ = "pi-img-wrapper hidden-xs").select("img"))
        
        authorString = str(item.select('p'))

        priceString = str(item.find(class_ = "pi-price"))
        
        author = authorString[11:authorString.find("\"", 11)]
        
        title = titleString[11:titleString.find("\"", 11)]

        price = priceString[48:priceString.find("<", 48)]
        
        url = "https://www.bookchor.com" + urlString[9:urlString.find("\"", 9)]

        if price != "":
            # books.append(book)
            books.append(
            {
                "title": title, 
                "price": price, 
                "url": url,
                "author": author,
                "site": "bookchor.com"
            }
        )


    return books

if __name__ == "__main__":
    lst = getBooksChor("freedom at midnight")
    for x in lst:
        print(x.title, x.price)



