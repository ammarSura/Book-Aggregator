from packages import *

def getBooksHalf(searcher):
    books = []

    url = "https://halfpricebooks.in/search?type=product&q="
    req = requests.get(url + searcher)
    soup = BeautifulSoup(req.text, "html.parser")
    items = (soup.find_all(class_ = "product-grid-item"))

    for item in items:
        # book = Book()
        urlString = str(item)
        helper1 = urlString.find("class=\"product-grid-item\" href=\"") + 32


        titleString = str(item.p)
        
        helper3 = titleString.find(" by ")
        
        priceString = str(item.find(class_ = "product-item--price"))
        helper2 = priceString.find("<small aria-hidden=\"true\">Rs.") + 30
        author = ""
        if helper3 > - 1:
            author = (titleString[helper3 + 3: -4]).strip()
        
        title = titleString[3:-4]

        price = priceString[helper2: priceString.find("<", helper2) - 3]
        
        url = "https://halfpricebooks.in" + urlString[helper1: urlString.find("\"", helper1)]

        # books.append(book)

        books.append(
            {
                "title": title, 
                "price": price, 
                "url": url,
                "author": author,
                "site": "halfpricebooks.in"
            }
        )

    return books

if __name__ == "__main__":
    lst = getBooksHalf("asimov") 
    print(lst)