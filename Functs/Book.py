import webbrowser

class Book:
    title = None
    site = None
    author = None
    price = None
    url = None
    soldout = False
    img = None
    pub = None
    pages = None

    def linker():
        webbrowser.open(url, new=1)


def printer(lst):
    stringer = []
    for b in lst:
        # print(b.author)
        string = str(b.title) + " \n" + str(b.author) + " \n" + str(b.price) + " \n" + str(b.url) + " \n"
        # print(string)
        stringer.append(string)
        stringer.append("--------------------------------------------------------- \n")
        # print(string)
        # print(b.title)
        # print(b.author)
        # print(b.price)
        # print(b.url)

    return stringer



