from tkinter import * #imports codes from tkinter library
import random


stored_usernames = []


class StartingWindow:
    def __init__(self, parent):
 
        background_color = "#DEBB74"

        #FRAME
        self.quiz_frame = Frame(parent, bg = background_color, padx = 100, pady = 100)
        self.quiz_frame.grid()

        #TITLE
        self.heading_label = Label(self.quiz_frame, text = "GEOGRAPHY QUIZ", font = ("TW Cent MT", "18", "bold"), bg = background_color)
        self.heading_label.grid(row = 0)

        #USER INFO
        self.user_label= Label(self.quiz_frame, text = "Enter your name:", font = ("TW Cent MT","16"), bg = background_color)
        self.user_label.grid(row = 1, pady = 20) 
        
        #ENTRY BOX
        self.entry_box= Entry(self.quiz_frame)
        self.entry_box.grid(row = 2, pady = 20)
        
        #BUTTON
        self.continue_button = Button(self.quiz_frame, text = "START", bg = "#3F9D2F", command = self.name_collection)
        self.continue_button.grid(row = 3, pady = 20) 
       
    def name_collection(self):
        name = self.entry_box.get()
        stored_usernames.append(name) #stores input to the name list variable
        print(stored_usernames)
        self.quiz_frame.destroy()
        

if __name__ == "__main__": #Makes the file the starter file
    root = Tk() #Creates a pop up window
    root.title("Geography Quiz") 
    startingWindow_object = StartingWindow(root)
    root.mainloop() #Keeps the window on