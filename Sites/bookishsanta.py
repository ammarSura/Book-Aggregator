from packages import *

#soldouts
#page changing


def getBooksSanta(searcher):
    books = []

    url = "https://www.bookishsanta.com/search?type=article%2Cpage%2Cproduct&q="
    req = requests.get(url + searcher)
    soup = BeautifulSoup(req.text, "html.parser")
    items = (soup.find_all(class_ = "productitem"))


    for item in items:
        # book = Book()
        urlString = str(item.find(class_ = "productitem--title").a)
        helper1 = urlString.find("href=\"") + 6

        titleString = urlString
        
        authorString = str(item.find(class_ = "productitem--info"))

        helper2 = authorString.find("style=\"text-decoration:none; font-size: 11px; font-weight:400; color:#335145\">by ") + 80
        

        priceString = str(item.find(class_ = "price productitem__price"))
        helper3 = priceString.find("class=\"money\" data-price") + 40

        author = authorString[ helper2 : authorString.find("<", helper2)].strip()

        title = titleString[titleString.find(">") + 1 : titleString.find("</a>") ].strip()

        price = priceString[ helper3: priceString.find("</span>", helper3)].strip()[: - 3]
        
        url = "https://www.bookishsanta.com" + urlString[helper1 : urlString.find("\"", helper1 )]
        
        books.append(
            {
                "title": title, 
                "price": price, 
                "url": url,
                "author": author,
                "site": "bookishsanta.com"
            }
        )
        
    return books

if __name__ == "__main__":
    lst = getBooksSanta("dracula")