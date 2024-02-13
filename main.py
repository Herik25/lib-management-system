from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *
from ViewIssuedBooks import *
# Add your own database name and password here to reflect in the code
mypass = ""
mydatabase="db"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

root = Tk()
root.title("Library")
root.minsize(width=400,height=400)
root.geometry("600x500")

# Take n greater than 0.25 and less than 5
same=True
n=1.7

# Adding a background image
background_image =Image.open("lib.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size # retrive the height and width of the image

newImageSizeWidth = int(imageSizeWidth*n) #These variables calculate the new size of the image based on the resizing factor n
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 
    
background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.LANCZOS) # This resizes the image to the new size calculated.
img = ImageTk.PhotoImage(background_image) #This converts the resized image to a format that Tkinter can use.

Canvas1 = Canvas(root)

Canvas1.create_image(300,340,image = img) # give the image
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight) # set the image
Canvas1.pack(expand=True,fill="both")

headingFrame1 = Frame(root,bg="#FFBB00",bd=5, relief="solid", borderwidth=2)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to \n Library Management System", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="Add Book Details",bg='black', fg='white', command=addBook)
btn1.place(relx=0.28,rely=0.35, relwidth=0.45,relheight=0.1)
    
btn2 = Button(root,text="Delete Book",bg='black', fg='white', command=delete)
btn2.place(relx=0.28,rely=0.45, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="View Book List",bg='black', fg='white', command=View)
btn3.place(relx=0.28,rely=0.55, relwidth=0.45,relheight=0.1)
    
btn4 = Button(root,text="Issue Book to Student",bg='black', fg='white', command = issueBook)
btn4.place(relx=0.28,rely=0.65, relwidth=0.45,relheight=0.1)
    
btn5 = Button(root,text="Return Book",bg='black', fg='white', command = returnBook)
btn5.place(relx=0.28,rely=0.75, relwidth=0.45,relheight=0.1)
    
btn6 = Button(root,text="view Issued Book List",bg='black', fg='white', command = ViewIssuedBookList)
btn6.place(relx=0.28,rely=0.85, relwidth=0.45,relheight=0.1)

root.mainloop()
