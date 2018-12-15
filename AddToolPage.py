import MainMenu as mm
from addTool import addTool
import tkinter as tk
import ReadFile as rf
import util
import csv
from tkinter.filedialog import askopenfilename

class AddToolPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.login = master.login

        master.minsize('300','400')
        master.geometry("300x400+%d+%d" % ((self.winfo_screenwidth()/2)-150, (self.winfo_screenheight()/2)-200))
        master.title('Add new Tool')

        ###########################
        # HEADER frame start here
        ###########################
        header=tk.Frame(self,bg="red")
        header.grid(row=0,column=0,columnspan=2,sticky=tk.N+tk.E+tk.W)
        header.grid_columnconfigure(0, weight=1)
        header.grid_rowconfigure(0,weight=1)

        Label = tk.Label(header ,text = "Main menu for user: "+self.login).grid(row=0,column=0, sticky=tk.W)
        b_logout = tk.Button(header, text="Log Out",command=lambda : master.log_out()).grid(row=0,column=5, sticky=tk.E)

        ###########################
        # MID frame start here
        ###########################
        mid=tk.Frame(self)
        mid.grid(row=1,column=0)
        mid.grid_columnconfigure(0, weight=1)
        mid.grid_rowconfigure(0,weight=1)

        tk.Label(mid ,text = "Title").grid(row = 0, column = 0, sticky="E")
        tk.Label(mid ,text = "Description").grid(row = 1, column = 0, sticky="E")
        tk.Label(mid ,text = "Price per Day").grid(row = 2, column = 0, sticky="E")
        tk.Label(mid ,text = "Price per Half Day").grid(row = 3, column = 0, sticky="E")
        #k.Label(mid ,text = "Image").grid(row = 4, column = 0, sticky="E")

        self.tool_title = tk.StringVar(self)
        self.tool_description = tk.StringVar(self)
        self.tool_priceFullDay = tk.StringVar(self)
        self.tool_priceHalfDay = tk.StringVar(self)
        self.tool_imgPath = tk.StringVar(self)
        
        self.titleEntry = tk.Entry(mid, textvariable = self.tool_title)
        self.titleEntry.grid(row = 0, column = 1)
        self.descriptionEntry = tk.Entry(mid, textvariable = self.tool_description).grid(row = 1, column = 1)         #Prabobly text box instad of entry box
        self.priceFullDayEntry = tk.Entry(mid, textvariable = self.tool_priceFullDay).grid(row = 2, column = 1)
        self.priceHalfDay = tk.Entry(mid, textvariable = self.tool_priceHalfDay).grid(row = 3, column = 1)
        self.imgPath = tk.Entry(mid, textvariable = self.tool_imgPath, state = 'disabled').grid(row = 4, column = 1)                  #Prabobly something else than entry box

        ###########################
        # BOTTOM frame start here
        ###########################
        bot=tk.Frame(self)
        bot.grid(row=2,column=0)
        bot.grid_columnconfigure(0, weight=1)
        bot.grid_rowconfigure(0,weight=1)

        createToolButton = tk.Button (bot, text = "Add tool", command=lambda : self.checkTool()).grid(row = 6, column =0)
        backButton = tk.Button (bot, text = "Back",command=lambda : master.change_frame(mm.MainMenu)).grid(row = 6, column =1)
        img_btn = tk.Button(mid, text="Image", command=lambda: self.setImagePath()).grid(row=4, column=0, sticky="E")

    def setImagePath(self):
        filename = askopenfilename()
        self.tool_imgPath.set(filename)

    def checkTool(self):
        tool = []
        tool.append(self.tool_title.get())
        tool.append(self.tool_description.get())
        tool.append(self.tool_priceFullDay.get())
        tool.append(self.tool_priceHalfDay.get())
        tool.append(self.tool_imgPath.get())

        isCorrect = util.verifyTool(tool)
        if isCorrect:
            add = addTool(self.login)
            add.add(tool)
            self.tool_title.set("")
            self.tool_description.set("")
            self.tool_priceFullDay.set("")
            self.tool_priceHalfDay.set("")
            self.tool_imgPath.set("")
            self.titleEntry.focus()

