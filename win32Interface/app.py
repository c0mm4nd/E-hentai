# coding:utf8
from Tkinter import *
import sys
sys.path.append("..")
import ehentai

class Application(Frame):
    def start(self):
        url = self.url.get()
        rtn = ehentai.download_pics(url)
        if rtn is True:
            self.START["text"] = "开始下载"
            self.urlHere['text'] = '上一本下载好了，新本子Url写这里:'
        pass
    def createWidgets(self):
        self.urlHere = Label(self)
        self.urlHere['text'] = '本子Url写这里:'
        self.urlHere.pack({"side": "left"})

        self.url = Entry(self)
        self.url.pack({"side": "left"})

        self.START = Button(self)
        self.START["text"] = "开始下载",
        self.START["command"] = self.start
        self.START.pack({"side": "left"})

        self.QUIT = Button(self)
        self.QUIT["text"] = "退出"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack({"side": "right"})


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
root.title("无响应其实是在下载的不可名状工具")
app = Application(master=root)
app.mainloop()
root.destroy()