import sys

sys.path.append('./Sites')


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
    functions = {"bookchor": getBooksChor, "99bookscart": getBooks99, "usedbooksfactory": getBooksFactory, "kitabay": getBooksKitabay, "bookishsanta": getBooksSanta, "halfpricebooks": getBooksHalf, "bestofusedbooks": getBooksbest, "bookflow": getBooksBookFlow, "worthing": getBooksWorthing, "pustakkosh": getBooksPustakkosh}

    # "pustakkosh": getBooksPustakkosh

    results = []
    if l == None:
        for funct in functions:
            # print(json.dumps(functions[funct](string)))
            results.extend(functions[funct](string))


    else:
        for i in l:
            
            results.extend(functions[i](string))
    
    return results

if __name__ == "__main__":   
    # s = str(sys.stdin.read() )[1:-2]
    # file1 = open("x.txt", "w") 
    # file1.write(s)
    # x = (search(str(sys.stdin.read() )[1:-2]))
    x = search("romila")
    # print(json.dumps(sys.stdin.read()))

    # for i in x:
    #     print(json.dumps(i))
    # print(len(x))
    print(len(x))
    print(json.dumps(x))
    # # print(len(x))
    # sys.stdout("hi")
    # print(x[0].title)
    

    # print(json.dumps([{"ammar": "name"}]))
    

