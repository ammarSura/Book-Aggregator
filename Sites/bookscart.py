from packages import *
#url problem unfixable
#add timer
def getBooks99(searcher):
    books = []

    url = "https://99bookscart.com/search?q="
    req = requests.get(url + searcher)
    soup = BeautifulSoup(req.text, "html.parser")
    items = (soup.find_all(class_ = "product-card product-card--list"))


    for item in items:
        # book = Book()
        urlString = str(item.find(class_ = "full-width-link"))

        titleString = str(item.find(class_ = "product-card__title"))
        
        authorString = str(item.find(class_ = "list-view-item__title").find("small"))

        priceString = str(item.find(class_ = "price-item price-item--sale"))

        author = authorString[44:authorString.find("<", 44)]
        
        title = titleString[34:titleString.find("<", 34)]

        price = priceString[72:priceString.find("<", 72)]
        
        url = "https://99bookscart.com" + urlString[33:urlString.find("\"", 33)]

       
        if price != "":
            # books.append(book)
            books.append(
            {
                "title": title, 
                "price": price, 
                "url": url,
                "author": author,
                "site": "99bookscart.com"
            }
            )


    return books

if __name__ == "__main__":
    lst = getBooks99("asimov") 
    print(len(lst))
    for i in range(len(lst)):
        print(i, lst[i].price)
        print((lst[i].price) == "")