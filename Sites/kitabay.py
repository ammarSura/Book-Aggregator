from packages import *


def getBooksKitabay(searcher):
    books = []

    url = "https://kitabay.com/search?type=product&q="
    req = requests.get(url + searcher)
    soup = BeautifulSoup(req.text, "html.parser")
    items = (soup.find_all(class_ = "prd-info"))

    for item in items:
        # book = Book()
        urlString = (str(item.find('a')))
        
        

        titleString = urlString
        helper1 = titleString.find("title=\"") + 7    
        
        authorString = str(item.find(class_ = "prd-tag prd-hidemobile"))

        priceString = str(item.find(class_ = "price-new"))


        author = authorString[authorString.find(">") + 1: authorString.find("</div>")]
        
        title = titleString[helper1:titleString.find("\"", helper1)]

        price = priceString[ priceString.find(">") + 5: priceString.find("</div>") - 3]
        
        url = "https://kitabay.com" + urlString[9:urlString.find("\"", 9)]

        # books.append(book)
        books.append(
            {
                "title": title, 
                "price": price, 
                "url": url
            }
        )

    return books
