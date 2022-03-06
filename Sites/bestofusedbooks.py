from packages import *

#soldouts
def getBooksbest(searcher):
    books = []

    url1 = "https://bestofusedbooks.com/search?q="
    url2 = "&options%5Bprefix%5D=last"
    req = requests.get(url1 + searcher + url2)
    soup = BeautifulSoup(req.text, "html.parser")
    items = (soup.find_all(class_ = "product-card product-card--list"))

    for item in items:
        
        urlString = str(item.find(class_ = "full-width-link"))

        titleString = str(item.find(class_ = "product-card__title"))
        
        authorString = str(item.find(class_ = "list-view-item__title").find("small"))

        priceString = str(item.find(class_ = "price-item price-item--regular"))

        soldout = str(item)
        
        title = titleString[34:titleString.find("<", 34)]

        price = priceString[priceString.find("from Rs. ") + 9: priceString.find("</span>") - 4]
        
        url = "https://bestofusedbooks.com/" + urlString[33:urlString.find("\"", 33)]

        

        books.append(
            {
                "title": title, 
                "price": price, 
                "url": url,
                "author": "",
                "site": "bestofusedbooks.com"
            }
        )

    return books

if __name__ == "__main__":
    lst = getBooksbest("asimov")

    for b in lst:
        print(b.title, b.soldout)

