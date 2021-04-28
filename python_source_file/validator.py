from tkinter import *
import tkinter as tk
from ttkthemes import themed_tk as tk
from tkinter import ttk
import tkinter.filedialog,tkinter.messagebox
from ttkthemes import themed_tk as tk
from PIL import Image , ImageTk


#ROOT
root = tk.ThemedTk()

root.geometry("350x450")
root.get_themes()
root.set_theme("plastik")
root.configure(bg="white")

root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)

#NAVIGATION FUNCTION
def show_frame(frame):
    frame.tkraise()

#PAGES    
page1 =Frame(root,bg="white")
page2 =Frame(root,bg="blue")
page3 =Frame(root,bg="pink")

login_image = ImageTk.PhotoImage(Image.open("UI/SUDOKO.png"))


# CREATING PAGE OBJECT
for frame in (page1,page2,page3):
    frame.grid(row=0,column=0,sticky='nsew')

    
# NAVIGATION FUNC FOR 2nd PAGE
def nexts():
    show_frame(page2)

# PAGE1:------------------------------------------------------------------------------

login_panel = Label(page1,image=login_image)
login_panel.pack(fill='both',expand=True)
    

                                                                 
enter_button = ttk.Button(page1,text="ENTER",command= nexts,width=10)
enter_button.place(x=140,y=300)


cr_button = ttk.Button(page1,text="ABOUT-US",command=lambda:show_frame(page3),width=10)
cr_button.place(x=140,y=350)

#PAGE3:--------------------------------------------------------------------------------

Credit_label = Label(page3,text="CREATED BY : SUSHMA",bg="yellow",fg="black",font=("caliberi",10,"bold"))
Credit_label.pack(side=LEFT,anchor=CENTER,expand=True,fill=BOTH)


#PAGE2:--------------------------------------------------------------------------------
mainframe = Frame(page2)
mainframe.grid(row=0,column=0,padx=50,pady=50)

title2 = Label(page2,text="CREATE SUDUKO",bg="yellow",fg="black",font=("caliberi",10,"bold"))
title2.place(x=130,y=0)

#COLUMNS & ROWS:
a1 = Entry(mainframe,width=4)
a1.grid(row=1,column=0)


a2 = Entry(mainframe,width=4)
a2.grid(row=2,column=0)

a3 = Entry(mainframe,width=4)
a3.grid(row=3,column=0)


a4 = Entry(mainframe,width=4)
a4.grid(row=4,column=0)


a5 = Entry(mainframe,width=4)
a5.grid(row=5,column=0)


a6 = Entry(mainframe,width=4)
a6.grid(row=6,column=0)


a7 = Entry(mainframe,width=4)
a7.grid(row=7,column=0)


a8 = Entry(mainframe,width=4)
a8.grid(row=8,column=0)

a9 = Entry(mainframe,width=4)
a9.grid(row=9,column=0)


b1 = Entry(mainframe,width=4)
b1.grid(row=1,column=1)


b2 = Entry(mainframe,width=4)
b2.grid(row=2,column=1)

b3 = Entry(mainframe,width=4)
b3.grid(row=3,column=1)


b4 = Entry(mainframe,width=4)
b4.grid(row=4,column=1)


b5 = Entry(mainframe,width=4)
b5.grid(row=5,column=1)


b6 = Entry(mainframe,width=4)
b6.grid(row=6,column=1)


b7 = Entry(mainframe,width=4)
b7.grid(row=7,column=1)


b8 = Entry(mainframe,width=4)
b8.grid(row=8,column=1)

b9 = Entry(mainframe,width=4)
b9.grid(row=9,column=1)

c1 = Entry(mainframe,width=4)
c1.grid(row=1,column=2)


c2 = Entry(mainframe,width=4)
c2.grid(row=2,column=2)

c3 = Entry(mainframe,width=4)
c3.grid(row=3,column=2)


c4 = Entry(mainframe,width=4)
c4.grid(row=4,column=2)


c5 = Entry(mainframe,width=4)
c5.grid(row=5,column=2)


c6 = Entry(mainframe,width=4)
c6.grid(row=6,column=2)


c7 = Entry(mainframe,width=4)
c7.grid(row=7,column=2)


c8 = Entry(mainframe,width=4)
c8.grid(row=8,column=2)

c9 = Entry(mainframe,width=4)
c9.grid(row=9,column=2)


d1 = Entry(mainframe,width=4)
d1.grid(row=1,column=3)


d2 = Entry(mainframe,width=4)
d2.grid(row=2,column=3)

d3 = Entry(mainframe,width=4)
d3.grid(row=3,column=3)


d4 = Entry(mainframe,width=4)
d4.grid(row=4,column=3)


d5 = Entry(mainframe,width=4)
d5.grid(row=5,column=3)


d6 = Entry(mainframe,width=4)
d6.grid(row=6,column=3)


d7 = Entry(mainframe,width=4)
d7.grid(row=7,column=3)


d8 = Entry(mainframe,width=4)
d8.grid(row=8,column=3)

d9 = Entry(mainframe,width=4)
d9.grid(row=9,column=3)


e1 = Entry(mainframe,width=4)
e1.grid(row=1,column=4)


e2 = Entry(mainframe,width=4)
e2.grid(row=2,column=4)

e3 = Entry(mainframe,width=4)
e3.grid(row=3,column=4)


e4 = Entry(mainframe,width=4)
e4.grid(row=4,column=4)


e5 = Entry(mainframe,width=4)
e5.grid(row=5,column=4)


e6 = Entry(mainframe,width=4)
e6.grid(row=6,column=4)


e7 = Entry(mainframe,width=4)
e7.grid(row=7,column=4)


e8 = Entry(mainframe,width=4)
e8.grid(row=8,column=4)

e9 = Entry(mainframe,width=4)
e9.grid(row=9,column=4)

l1 = Entry(mainframe,width=4)
l1.grid(row=1,column=5)


l2 = Entry(mainframe,width=4)
l2.grid(row=2,column=5)

l3 = Entry(mainframe,width=4)
l3.grid(row=3,column=5)


l4 = Entry(mainframe,width=4)
l4.grid(row=4,column=5)


l5 = Entry(mainframe,width=4)
l5.grid(row=5,column=5)


l6 = Entry(mainframe,width=4)
l6.grid(row=6,column=5)


l7 = Entry(mainframe,width=4)
l7.grid(row=7,column=5)


l8 = Entry(mainframe,width=4)
l8.grid(row=8,column=5)

l9 = Entry(mainframe,width=4)
l9.grid(row=9,column=5)

s1 = Entry(mainframe,width=4)
s1.grid(row=1,column=6)


s2 = Entry(mainframe,width=4)
s2.grid(row=2,column=6)

s3 = Entry(mainframe,width=4)
s3.grid(row=3,column=6)


s4 = Entry(mainframe,width=4)
s4.grid(row=4,column=6)


s5 = Entry(mainframe,width=4)
s5.grid(row=5,column=6)


s6 = Entry(mainframe,width=4)
s6.grid(row=6,column=6)


s7 = Entry(mainframe,width=4)
s7.grid(row=7,column=6)


s8 = Entry(mainframe,width=4)
s8.grid(row=8,column=6)

s9 = Entry(mainframe,width=4)
s9.grid(row=9,column=6)

x1 = Entry(mainframe,width=4)
x1.grid(row=1,column=7)


x2 = Entry(mainframe,width=4)
x2.grid(row=2,column=7)

x3 = Entry(mainframe,width=4)
x3.grid(row=3,column=7)


x4 = Entry(mainframe,width=4)
x4.grid(row=4,column=7)


x5 = Entry(mainframe,width=4)
x5.grid(row=5,column=7)

x6 = Entry(mainframe,width=4)
x6.grid(row=6,column=7)


x7 = Entry(mainframe,width=4)
x7.grid(row=7,column=7)


x8 = Entry(mainframe,width=4)
x8.grid(row=8,column=7)

x9 = Entry(mainframe,width=4)
x9.grid(row=9,column=7)


z1 = Entry(mainframe,width=4)
z1.grid(row=1,column=8)


z2 = Entry(mainframe,width=4)
z2.grid(row=2,column=8)

z3 = Entry(mainframe,width=4)
z3.grid(row=3,column=8)


z4 = Entry(mainframe,width=4)
z4.grid(row=4,column=8)


z5 = Entry(mainframe,width=4)
z5.grid(row=5,column=8)


z6 = Entry(mainframe,width=4)
z6.grid(row=6,column=8)


z7 = Entry(mainframe,width=4)
z7.grid(row=7,column=8)


z8 = Entry(mainframe,width=4)
z8.grid(row=8,column=8)

z9 = Entry(mainframe,width=4)
z9.grid(row=9,column=8)




#VALIDATOR

class Solution(object):
   def isValidSudoku(self, board):
      """
      :type board: List[List[str]]
      :rtype: bool
      """
      for i in range(9):
         row = {}
         column = {}
         block = {}
         row_cube = 3 * (i//3)
         column_cube = 3 * (i%3)
         for j in range(9):
             if board[i][j]!='.' and board[i][j] in row:
                return False
             row[board[i][j]] = 1
             if board[j][i]!='.' and board[j][i] in column:
                return False
             column[board[j][i]] = 1
             rc= row_cube+j//3
             cc = column_cube + j%3
             if board[rc][cc] in block and board[rc][cc]!='.':
                return False
             block[board[rc][cc]]=1
      return True
ob1 = Solution()

def clearing():
    result_label.delete(0,END)


def valid():
         result_label.delete(0,END)
         result_label.configure(fg="green")
         result_label.insert(0,"VALID BOARD")
def invalid():
         result_label.delete(0,END)
         result_label.configure(fg="red")
         result_label.insert(0,"INVALID BOARD")

# RESULT FUNCTION:----------------------------------------------------------------
def checker():
    if tkinter.messagebox.askyesno("Confirmation","Confirm Validate?"):
      result_label.insert(0,(ob1.isValidSudoku([
            [a1.get(),b1.get(),c1.get(),d1.get(),e1.get(),l1.get(),s1.get(),x1.get(),z1.get()],
            [a2.get(),b2.get(),c2.get(),d2.get(),e2.get(),l2.get(),s2.get(),x2.get(),z2.get()],
            [a3.get(),b3.get(),c3.get(),d3.get(),e3.get(),l3.get(),s3.get(),x3.get(),z3.get()],
            [a4.get(),b4.get(),c4.get(),d4.get(),e4.get(),l4.get(),s4.get(),x4.get(),z4.get()],
            [a5.get(),b5.get(),c5.get(),d5.get(),e5.get(),l5.get(),s5.get(),x5.get(),z5.get()],
            [a6.get(),b6.get(),c6.get(),d6.get(),e6.get(),l6.get(),s6.get(),x6.get(),z6.get()],
            [a7.get(),b7.get(),c7.get(),d7.get(),e7.get(),l7.get(),s7.get(),x7.get(),z7.get()],
            [a8.get(),b8.get(),c8.get(),d8.get(),e8.get(),l8.get(),s8.get(),x8.get(),z8.get()],
            [a9.get(),b9.get(),c9.get(),d9.get(),e9.get(),l9.get(),s9.get(),x9.get(),z9.get()]
            ])))
    
      if result_label.get() == "1":
             valid()
      elif result_label.get() == "0":
             invalid()


def pdf_saver():     
    data = [["S","_","U","D","_","U","K","_","O",],
            [a1.get(),b1.get(),c1.get(),d1.get(),e1.get(),l1.get(),s1.get(),x1.get(),z1.get()],
            [a2.get(),b2.get(),c2.get(),d2.get(),e2.get(),l2.get(),s2.get(),x2.get(),z2.get()],
            [a3.get(),b3.get(),c3.get(),d3.get(),e3.get(),l3.get(),s3.get(),x3.get(),z3.get()],
            [a4.get(),b4.get(),c4.get(),d4.get(),e4.get(),l4.get(),s4.get(),x4.get(),z4.get()],
            [a5.get(),b5.get(),c5.get(),d5.get(),e5.get(),l5.get(),s5.get(),x5.get(),z5.get()],
            [a6.get(),b6.get(),c6.get(),d6.get(),e6.get(),l6.get(),s6.get(),x6.get(),z6.get()],
            [a7.get(),b7.get(),c7.get(),d7.get(),e7.get(),l7.get(),s7.get(),x7.get(),z7.get()],
            [a8.get(),b8.get(),c8.get(),d8.get(),e8.get(),l8.get(),s8.get(),x8.get(),z8.get()],
            [a9.get(),b9.get(),c9.get(),d9.get(),e9.get(),l9.get(),s9.get(),x9.get(),z9.get()]
            ]
    global fileName
    fileName ="validated_boards/validated.pdf"

    from reportlab.platypus import SimpleDocTemplate
    from reportlab.lib.pagesizes import letter

    pdf = SimpleDocTemplate(
        fileName,
        pagesize=letter
    )
    
    from reportlab.platypus import Table
    table = Table(data)
    from reportlab.platypus import TableStyle
    from reportlab.lib import colors

    ts = TableStyle(
        [
        ('BOX',(0,0),(-1,-1),2,colors.black),

        ('LINEBEFORE',(2,1),(2,-1),2,colors.red),
        ('LINEABOVE',(0,2),(-1,2),2,colors.green),

        ('GRID',(0,1),(-1,-1),2,colors.black),
        ]
    )
    table.setStyle(ts)


    elems = []
    elems.append(table)

    pdf.build(elems)
    

def dest():
    root.destroy()
# BUTTONS OF PAGE2----------------------------------------------
buttons = ttk.Button(page2,text="VALIDATE",command=checker)
buttons.grid(row=10,column=0,columnspan=2)

result_label = Entry(page2,text="",fg="red")
result_label.grid(row=11,column=0,pady=10,columnspan=2)


clbuttons = ttk.Button(page2,text="CLEAR",command=clearing)
clbuttons.grid(row=12,column=0,pady=10)


elbuttons = ttk.Button(page2,text="SAVE",command=pdf_saver)
elbuttons.grid(row=13,column=0,pady=10)

#INITIAL NAV TO PAGE1:
show_frame(page1)
root.mainloop()
#_-----------------------------------------------------END-------------------------------------------------------------------------------------------

