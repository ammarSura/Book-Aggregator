import sys

sys.path.insert(1, './Sites')

from bookscart import *

from bestofusedbooks import *

from bookchor import *

from bookishsanta import *

from halfpricebooks import *

from kitabay import *

from pustakkosh import *

from usedbooksfactory import *

from worthing import *

from bookflow import *



import json


def search(string, l = None):
    functions = {"bookchor": getBooksChor, "99bookscart": getBooks99, "usedbooksfactory": getBooksFactory, "kitabay": getBooksKitabay, "bookishsanta": getBooksSanta, "halfpricebooks": getBooksHalf, "bestofusedbooks": getBooksbest, "pustakkosh": getBooksPustakkosh, "bookflow": getBooksBookFlow, "worthing": getBooksWorthing}

    results = []
    if l == None:
        for funct in functions:
            results.extend(functions[funct](string))

    else:
        for i in l:
            results.extend(functions[i](string))
    
    return results

if __name__ == "__main__":    
    x = (search(sys.stdin.read()))

    print(json.dumps(x))
    # print(x[0].title)
    

    # print(json.dumps([{"ammar": "name"}]))
    

