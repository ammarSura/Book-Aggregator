import tkinter as tk
from tkinter import ttk
import sys

sys.path.insert(1, '../Sites')

from searcher import *

from Book import *

import webbrowser

def checkBoxes(root):
    names = ["bookchor", "99bookscart", "usedbooksfactory", "kitabay", "bookishsanta", "halfpricebooks", "bestofusedbooks", "pustakkosh", "bookflow","worthing"]
    boxes = []

    for name in names:
        var = tk.IntVar()
        boxes.append([name, var])

    # print(boxes)

    for i in range(len(boxes)):
        tk.Checkbutton(root, text = boxes[i][0], variable = boxes[i][1], font=("Courier", 15,)).place(x = 5, y = 170 + 30 * i, width = 200)

    return boxes

# def minPriceGetter(x):
#   a = x.get()
  
#   x.delete(0, tk.END)

#   print(a)

# def maxPriceGetter(x):
#   a = x.get()
  
#   x.delete(0, tk.END)

#   print(a)
  
def priceGetter(x1, x2, allboxes, searchLst):
  a = x1.get()
  
  x1.delete(0, tk.END)

  b = x2.get()
  
  x2.delete(0, tk.END)

  if a == "":
    a = 0
  else:
    a = int(a)

  if b == "":
    b = 100000
  else:
    b = int(b)

    if a > b:
      b = 100000
  
  # for i in searchLst:
  #   print(i)

  print(searchLst, allboxes)

  






def pricer(f, allboxes, searchLst):
  tk.Label(f, text="Min: ", font=("Courier", 25, "bold"), foreground='#000000').place(x = 5, y = 500)
  x1 = tk.Entry(f, font=("Courier", 25, "bold"), foreground = "#4d4d4d")

  x1.place(x = 100, y = 500, height = 35, width = 100)
  # f.bind('<Return>', (lambda event : minPriceGetter(x1) ) )

  tk.Label(f, text="Max: ", font=("Courier", 25, "bold"), foreground='#000000').place(x = 5, y = 550)
  x2 = tk.Entry(f, font=("Courier", 25, "bold"), foreground = "#4d4d4d")
  x2.place(x = 100, y = 550, height = 35, width = 100)
  # f.bind('<Return>', (lambda event : maxPriceGetter(x1) ))

  return x1, x2

  

  #command = lambda c = allboxes: culler(c)

def lstManager(boxes):
    lst = []
    for b in boxes:
        if b[1].get() == 1:
            lst.append(b[0])

    print(lst)
    return lst

class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = tk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 300 ), window=self.scrollable_frame)

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

def openweb(url):
  print(url)
  webbrowser.open(url, new=1)

def texter(string, cutoff):
  
  if len(string) > cutoff:
    return string[:cutoff] + "..."
  return string 


def printBooks(L, allboxes, flst, frame_width, frame_height):
  box = ScrollableFrame(flst[1])

  pad = (0, 0)

  fsize = 20

  for i in L:
    all = []
    helper = tk.IntVar()
    check = tk.Checkbutton(box.scrollable_frame, text = "Title: " + texter(str(i.title), 80), variable = helper, font=("Courier", fsize, "bold"))

    
    check.pack(side = "top", anchor="center", padx = pad)
    author = tk.Label(box.scrollable_frame, text = "Author: " + texter(str(i.author), 80), font=("Courier", fsize, "bold"), background="#fff")

    author.pack(side = "top", anchor="center", padx = pad)
    
    price = tk.Label(box.scrollable_frame, text = "Price: " + texter(str(i.price), 80), font=("Courier", fsize, "bold"), background="#fff")

    price.pack(side = "top", anchor="center",padx = pad)
    
    site = tk.Label(box.scrollable_frame, text = "Site: " + texter(str(i.url[8 : str(i.url).find(".",13)]), 50), font=("Courier", fsize, "bold"), background="#fff")

    site.pack(side = "top", anchor="center",padx = pad)
    link = tk.Button(box.scrollable_frame, text = "link", font=("Courier", fsize, "bold"), height = 2, width = 10, command = lambda m = i.url: openweb(m) )

    link.pack(anchor="center", padx = pad)
    
    space = tk.Label(box.scrollable_frame, text=" ", font=("Courier", fsize, "bold"), background="#fff")

    space.pack(side = "top", anchor="center", padx = pad)

    allboxes.append([check, author, price, site, link, space, helper, 1])
    
  box.place(x = 10, y = 10, width = frame_width - 20, height = int(frame_height * 0.6) - 20)

  tk.Label(flst[0], text="Done!", font=("Courier", 40, "bold"), foreground='#ff3333').place(x = 10, y = int(frame_height * 0.1 + 110))

def culler(allboxes):
   
  for a in allboxes:
    if a[6].get() == 0 :
      for i in range(1, 6):
        a[i].pack_forget()
        a[7] = 0
    
def fetch(boxes, allboxes, e1, flst, frame_width, frame_height, searchLst):
  entered = e1.get()
  e1.delete(0, tk.END)
  lst = lstManager(boxes)

  print(entered)

  if len(lst) > 0:
    searchLst = search(entered, lst)
    printBooks(searchLst, allboxes, flst, frame_width, frame_height)
  else:
    searchLst = search(entered)
    printBooks(searchLst, allboxes, flst, frame_width, frame_height)

def frame1(root, boxes, allboxes, window_width, window_height):

  flst = []

  f = tk.Frame(root, bg = "#fff")

  flst.append(f)
  
  frame_width = window_width - int(window_width * 0.15)
  frame_height = window_height
  f.place(x = int(window_width * 0.15), y = 0, height = frame_height, width = frame_width)

  title = tk.Label(f, text="Used Book Aggregator", font=("Courier", 60, "bold"), background="#00b3b3", foreground='#ffcc33') 
  title.place(x = 0, y = 0, width = frame_width, height = int(frame_height * 0.1))

  tk.Button(f, text = 'Quit', font=("Courier", 20, "bold"), command = root.quit).place(x = int(frame_width / 3 ), y = int(frame_height * 0.2), height = 40, width = 100)

  f2 = frame2(f, frame_width, frame_height)
  flst.append(f2)

  tk.Label(f, text="Search: ", font=("Courier", 40, "bold"), foreground='#ffcc33').place(x = 10, y = int(frame_height * 0.1 + 20))
  e1 = tk.Entry(f, font=("Courier", 40, "bold"), foreground = "#4d4d4d")
  e1.place(x = 200, y = int(frame_height * 0.1 + 20), height = 42, width = frame_width - int(frame_width * 0.2))

  searchLst = None
  root.bind('<Return>', (lambda event : fetch(boxes, allboxes, e1, flst, frame_width, frame_height, searchLst)))

  
  tk.Button(f, text = 'Enter', font=("Courier", 20, "bold"), command = lambda b = boxes, c = allboxes, e = e1, g = flst, h = frame_height, w = frame_width, v = searchLst: fetch(b, c, e, g, w, h, v)).place(x = int(1.8 * frame_width / 3 ), y = int(frame_height * 0.2), height = 40, width = 100)

  tk.Button(f, text = 'Cull', font=("Courier", 20, "bold"), command = lambda c = allboxes: culler(c)).place(x = int(2.6 * frame_width / 3 ), y = int(frame_height * 0.2), height = 40, width = 100)

  x1, x2 = pricer(root, allboxes, searchLst)

  tk.Button(root, text = 'Filter', font=("Courier", 20, "bold"), command = lambda a = x1, b = x2, c = allboxes, d = searchLst: priceGetter(a, b, c, d)).place(x = 55, y = 600, height = 40, width = 100)

  return f, frame_width, frame_height, e1

def frame2(f, frame_width, frame_height):
  f2 = tk.Frame(f, bg = "#dcf")
  f2.place(x = 0, y = int(frame_height * 0.2) + 70, height = frame_height - int(frame_height * 0.4), width = frame_width)

  return f2
  

def gui():
  root = tk.Tk()

  #boxes
  boxes = checkBoxes(root)
  
  allboxes = []
  

  #main window
  window_width, window_height = root.winfo_screenwidth(), root.winfo_screenheight()
  root.geometry(str(window_width) + "x" + str(window_height))
  root.configure(background="#ccc")

  #first frame
  f1, frame_width, frame_height, e1 = frame1(root, boxes, allboxes, window_width, window_height)

  # tk.Label(f1, text="Done!", font=("Courier", 40, "bold"), foreground='#ffcc33').place(x = 10, y = int(frame_height * 0.1 + 100))

  root.mainloop()

if __name__ == "__main__":
  gui()

