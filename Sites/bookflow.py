from packages import *

def getBooksBookFlow(searcher):
    books = []

    url1 = "https://bookflow.in/search-results/?ad_title="
    url2 = "&cat_id=&location=&oETrwUWOK=BDermLiv6oE7qsO&cLdJhMkZSCvbWixo=2qv36L&CDlcvaiFSwOJ=NgG1%5BvXIOq4&oETrwUWOK=BDermLiv6oE7qsO&cLdJhMkZSCvbWixo=2qv36L&CDlcvaiFSwOJ=NgG1%5BvXIOq4"
    req = requests.get(url1 + searcher + url2)
    soup = BeautifulSoup(req.text, "html.parser")
    items = (soup.find_all(class_ = "ads-grid-container"))

    for item in items:
        # book = Book()
        urlString = str(item.a)

        titleString1 = str(item.find(class_ = "ads-grid-content").h3)
        titleString1 = titleString1[4 : - 5]

        titleString2 = str(item.find(class_ = "ads-grid-style").img)

        titleString2 = titleString2[10: titleString2.find("\"", 10)]

        if len(titleString2) > len(titleString1):
            titleString = titleString2
        else:
            titleString = titleString1
        
        priceString = str(item.find(class_ = "ads-grid-price"))
        priceString = priceString[priceString.find("<span>") + 6: priceString.find("<span class") - 1]

        if len(priceString) > 5:
            priceString = "call"
        
        title = titleString

        price = priceString
        
        url = urlString[9: urlString.find("\"", 9)]

        # books.append(book)
        books.append(
            {
                "title": title, 
                "price": price, 
                "url": url,
                "author": ""
            }
        )

    return books

if __name__ == "__main__":
    lst = getBooksBookFlow("dracula")
