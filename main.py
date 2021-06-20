from tkinter import * #imports codes from tkinter library
from tkinter import messagebox #Import message box widget.
import random


stored_usernames = []
global q_a
asked = []
score = 0

q_a = {

  1 : ["Where is Mount Everest located in?", 'Nepal', 'Japan', 'New Zealand', 'Africa', 'Nepal', 1],

  2 : ["How many continents are there?", '8', '7', '10', '2', '7', 2],

  3 : ["Which country has the highest population?", 'USA', 'Russia', 'China', 'India', 'China', 3],

  4 : ["Which is the world’s smallest country?", 'UK', 'Australia', 'New Zealand', 'Vatican City', 'Vatican City', 4],

  5 : ["Which is the coldest continent in the world?", 'Antartica', 'Oceania', 'Asia', 'Africa', 'Antartica', 1],
}


#RANDOMISE
def randomiser():
  global quenum
  quenum = random.randint(1,5)
  if quenum not in asked:
    asked.append(quenum)
  elif quenum in asked:
    randomiser()


randomiser()

class Startingwindow:
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
        Questionwindow(root)
        



#QUIZ QUESTION PAGES
class Questionwindow:
  def __init__(self, parent):

    background_color = "#DEBB74"
    self.var1 = IntVar()

    #Set frame for questions.
    self.quiz_frame = Frame(parent, bg = background_color, pady = 6, width = 600, height = 700)
    self.quiz_frame.grid()

    #Questions displayed from 'q_a' questions and answers list.
    self.question_label = Label(self.quiz_frame, text = q_a[quenum][0], font = ("Helvetica", "10", "bold"), width = 90, pady = 30, wraplength = 600)
    self.question_label.grid(row = 2, pady = (20, 20))

    #Selection options for each questions displayed using radio buttons.
    self.rb1 = Radiobutton(self.quiz_frame, text = q_a[quenum][1], value = 1, indicator = 0, variable = self.var1, command = self.test_progress, pady = 60, font = ("Verdana", "11"), relief = RAISED, wraplength = 88, width = 40, bg = "Orange", activebackground = "Dark Orange")
    self.rb1.grid(row = 3, sticky = W, column = 0)

    self.rb2 = Radiobutton(self.quiz_frame, text = q_a[quenum][2], value = 2, indicator = 0, variable = self.var1, command = self.test_progress, pady = 60, font = ("Verdana","11"), relief = RAISED, wraplength = 88, width = 40, bg = "Orange", activebackground = "Dark Orange")
    self.rb2.grid(row = 3,  sticky = E, column = 0)

    self.rb3 = Radiobutton(self.quiz_frame, text = q_a[quenum][3], value = 3, indicator = 0, variable = self.var1, command = self.test_progress,  pady = 60, font = ("Verdana","11"), relief = RAISED, wraplength = 88, width = 40, bg = "Orange", activebackground = "Dark Orange")
    self.rb3.grid(row = 4,sticky = W, column = 0)

    self.rb4 = Radiobutton(self.quiz_frame, text = q_a[quenum][4], value = 4, indicator = 0, variable = self.var1, command = self.test_progress, pady = 60, font = ("Verdana","11"), relief = RAISED, wraplength = 88, width = 40, bg = "Orange", activebackground = "Dark Orange")
    self.rb4.grid(row = 4,  sticky = E, column = 0)

    #Quit button if user wants to quit during the game.
    self.quit_button = Button(self.quiz_frame, text = "QUIT", padx = 2, pady =1, bg = "Red", relief = RAISED, command = self.quitButton)
    self.quit_button.grid(row = 0, sticky = W, padx = 10, pady = (10,4))

    #Score display.
    self.score_update = Label(self.quiz_frame, text = "Score: " + str(score), bg = background_color, font = ("bold"))
    self.score_update.grid(row = 0, padx = 20, pady = (10,4), sticky = E)
        
  #If user wants to leave during the game in progress, user is asked to confirm, then taken to leaderboard.
  def quitButton(self):
    result = messagebox.askyesno("Exit Game", "Are you sure?") #Ask user to confirm
    if result == True: #if yes, then takes user to leaderboard.
      self.leader_board()
    else: #or else continue game.
      pass 

  def radioEvent(self): #Change answers for each question after user selects answer.
    randomiser()
    self.var1.set(0)
    self.question_label.config(text = q_a[quenum][0])
    self.rb1.config(text = q_a[quenum][1])
    self.rb2.config(text = q_a[quenum][2])
    self.rb3.config(text = q_a[quenum][3])
    self.rb4.config(text = q_a[quenum][4])
                
  #Setting up score system.
  def test_progress(self):
    global score
    score_label = self.score_update
    selected = self.var1.get()
    if len(asked) > 6: #at the end of the quiz: 
      if selected == q_a[quenum][6]: #user is taken to the leaderboard to show their results. 
        score += 10
        score_label.config(text = "Score: " + str(score))
        self.leader_board()
      else: #user is corrected with the right answer while they movce on to the next question
        print(selected)
        score += 0
        score_label.config(text = "Score: " + str(score))
        score_label.config(text = "Incorrect! The correct answer was " + q_a[quenum][5] + "\nScore:"  + str(score))
        self.leader_board()
    else: #during this quiz:
      if selected == q_a[quenum][6]: #if user selects right answer, gets 10 points and moves on to the next question.
        score += 10
        score_label.config(text = "Score: " + str(score))
        self.radioEvent()
      else: #if the user gets it incorrect, then user is corrected and moves on to next question.
        print(selected)
        score += 0
        score_label.config(text = "Oops! The correct answer was " + q_a[quenum][5] + "\nScore:"  + str(score))
        self.radioEvent()
    
    #Initialising the leaderboard to list top 20 names with the highest scores so far from the stored_usernames.
    def leader_board(self):
        root.withdraw()
        name = stored_usernames[0]
        file = open("leaderBoard.txt", "a") #insert the leader file in here.

        if name == "admin":
            file = open("leaderBoard.txt", "w")
        else:
            file.write(str(score)) #mention score along with user name inputted by the user.
            file.write(" - ")
            file.write(name + "\n") 
            file.close()
        
        inputFile = open("leaderBoard.txt", 'r')
        lineList = inputFile.readlines()
        lineList.sort()
        
        highest = [] #highest scores saved in this list
        highest_20 = (lineList[-20:])#top 20 highest scores will e displayed.
        for line in highest_20:
            point = line.split(" - ") #format each line.
            highest.append((int(point[0]), point[1]))
        file.close()
        highest.sort()
        highest.reverse()
        return_string = ""
        for i in range(len(highest)):
            return_string += "{} - {}\n".format(highest[i][0], highest[[i][0]])
        print(return_string)

        #Display Leaderboard in new seperate window.
        open_leaderb = Leaderboard(root)
        open_leaderb.num1.config(text = return_string)





        










 
    



##################################################################################
if __name__ == "__main__": #Makes the file the starter file
    root = Tk() #Creates a pop up window
    root.title("Geography Quiz") 
    startingwindow_object = Startingwindow(root)
    root.mainloop() #Keeps the window on
