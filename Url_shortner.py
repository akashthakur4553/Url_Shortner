from tkinter import *
import requests
import pyperclip


def url_shortner():
    Api = '909fb5772552d48ae1be06daf7f41c7f21aef'
    base_url = 'https://cutt.ly/api/api.php'
    parameters = {'key': Api, 'short': url.get()}
    request = requests.get(base_url, params=parameters)
    data = request.json()
    try:
        short_link = data['url']['shortLink']
        shorturl.set(short_link)
    except Exception as e:
        error_code = data['url']['status']
        print("The sstatus is ", error_code)


def copy():
    if shorturl.get():
        pyperclip.copy(shorturl.get())


def reset():
    shorturl.set("")
    url.set("")


root = Tk()
root.title(" URL Shortner")
root.geometry("400x350")
root.resizable(False, False)
root.config(background="#BAD1C2")
photo = PhotoImage(file="link.png")
root.iconphoto(False, photo)

url = StringVar()
shorturl = StringVar()

Label(root, text="URL Shortner", bg="#BAD1C2",
      fg="#153462", font="verdana 22 ").place(x=80, y=10)
Label(root, text="-------------------------------------------------",
      bg="#BAD1C2", fg="#F6F6C9", font="verdana 12 ").place(x=15, y=50)

Label(root, text="Enter URL Here ", bg="#2C3E50", fg="#EAECEE",
      font="verdana 10 bold", padx=2, pady=2).place(x=7, y=100)
Entry(root, textvariable=url, font="verdana 12", width=30).place(x=7, y=120)

Button(root, text="Convert...", bg="#0081C9", fg="#000",
       font="verdana 12 ", command=url_shortner, relief=GROOVE).place(x=7, y=180)

Label(root, text="Shortened URL - Copy & Paste in browser", bg="#2C3E50",
      fg="#EAECEE", font="verdana 10 bold", padx=2, pady=2).place(x=7, y=250)
Entry(root, textvariable=shorturl, width=35,
      font="verdana 12").place(x=7, y=270)
Button(root, text="Copy Url", bg="#0081C9", fg="#000",
       font="verdana 12 ", command=copy, relief=GROOVE).place(x=7, y=310)


Button(root, text="Reset", bg="#0081C9", fg="#000",
       font="verdana 12 ", command=reset, relief=GROOVE).place(x=130, y=310)
root.mainloop()
