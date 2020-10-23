# import tkinter module
from tkinter import *     
# import you tube module
from pytube import *		# pip install pytube3
# initializing tkinter
root = Tk()
# setting the geometry of the GUI
root.geometry("400x350")
# setting the title of the GUI
root.title("Linux YouTube Downloader Application")
# defining download function
def download():
	try:
		myVar.set("Downloading")
		root.update()
		YouTube(link.get()).streams.first().download()
		link.set("video downloaded successfully")
	except Exception as e:
		myVar.set("Mistake")
		root.update()
		link.set("Enter correct link")

# widget
Label(root, text="Welcome to youtube\nDownloader Application", font="Consolas 15 bold").pack()
# Declaring myVar
myVar = StringVar()
myVar.set("Enter the link below")
Entry(root, textvariable=myVar, width=40).pack(pady=10)
link = StringVar()
Entry(root, textvariable=link, width=40).pack(pady=10)
Button(root, text="Download video", command=download).pack()
root.mainloop()

