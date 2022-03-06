from packages import *

def getBooksWorthing(searcher):
    books = []

    url = "https://www.worthing.in/search?type=product&options%5Bprefix%5D=last&options%5Bunavailable_products%5D=hide&q="

    req = requests.get(url + searcher)
    soup = BeautifulSoup(req.text, "html.parser")
    items = (soup.find_all(class_ = "product-item product-item--vertical 1/3--tablet 1/4--lap-and-up"))

    for item in items:
        # book = Book()
        urlString = str(item.a)

        titleString = str(item.find(class_ = "product-item__title text--strong link"))

        priceString = str(item.find(class_ = "price"))
        
        helper1 = priceString.find("Rs. ") + 4
        
        title = titleString[titleString.find("\">") + 2: titleString.find("|")]

        helper = title.find(" by ")
        author = ""

        if helper > -1 :
            author = title[helper + 4: title.find("|")].strip()


        price = priceString[helper1 : priceString.find("</span>", helper1) - 3].replace(",", "")
        
        url = "https://www.worthing.in" + urlString[urlString.find("href=\"") + 6: urlString.find("\"><div")]

        # books.append(book)
        books.append(
            {
                "title": title, 
                "price": price, 
                "url": url,
                "author": author,
                "site": "worthing.in"
            }
        )
    return books