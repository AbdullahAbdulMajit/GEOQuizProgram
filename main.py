from tkinter import * #imports codes from tkinter library
from tkinter import messagebox #Import message box widget.
import re   
import random


background_color = "#DEBB74"
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
        self.quiz_frame = Frame(parent, bg = background_color, padx = 167, pady = 110)
        self.quiz_frame.grid()

        #TITLE
        self.heading_label = Label(self.quiz_frame, text = "GEOGRAPHY QUIZ", fg = "#A52A2A", font = ("TW Cent MT", "30", "bold"), bg = background_color)
        self.heading_label.grid(row = 0)

        #USER INFO
        self.user_label= Label(self.quiz_frame, text = "Enter your name:", fg = "#A52A2A", font = ("TW Cent MT","18"), bg = background_color)
        self.user_label.grid(row = 1, pady = 20) 
        
        #ENTRY BOX
        self.pattern = re.compile("^\\w{0,16}$") # '^' matches the start of this string, '\\' disallows special characters to be inputted, 'w' allows alphabets, num, and underscore, {0. 13} is character limit set to max 13 characters, $ matches the end of the string.
        user_validation = (self.quiz_frame.register(self.username_boundary), "%i", "%P") 
        self.entry_box= Entry(self.quiz_frame, background = 'Light Gray', borderwidth = 2, relief = SUNKEN, validate = "key", validatecommand = user_validation, invalidcommand = self.name_error)
        self.entry_box.grid(row = 2, pady = 20)
        self.name_input = self.entry_box.get()
        
        #BUTTON
        self.continue_button = Button(self.quiz_frame, text = "START", font = ("14"), fg = "White", bg = "#3F9D2F", command = self.empty)
        self.continue_button.grid(row = 3, pady = 20) 

        
    #User Entry Error Handling and Boundary. 
    def username_boundary(self, index, username): 
        return self.pattern.match(username) is not None #make sure user input matches requirements.
        
    def name_error(self):  #if user enters more than 13 characters or special characters, user gets error.
        self.error = Label(self.quiz_frame, text = "*Invalid character.*", fg = "red", padx = 100, bg = background_color)
        self.error.grid(row = 5)
        self.error.after(1500, self.error.destroy) #label appears then disappears after 2s.

    def empty(self): #if user inputs nothing, give error.
        self.name_input = self.entry_box.get()
        if self.name_input == "":
            self.error = Label(self.quiz_frame, text = "*You haven't entered a name.*", fg = "red", padx = 100, bg = background_color)
            self.error.grid(row = 5)
            self.error.after(1500, self.error.destroy) #label appears then disappears after 1.5s. 
        else:
            #If user inputs their name, their name is appended into a list in the self.name_collection() def method below, then display questions. 
            self.name_collection()

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
    self.quiz_frame = Frame(parent, bg = background_color)
    self.quiz_frame.grid()

    #Questions displayed from 'q_a' questions and answers list.
    self.question_label = Label(self.quiz_frame, text = q_a[quenum][0], font = ("Helvetica", "16", "bold"), width = 54, pady = 10)
    self.question_label.grid(row = 2, pady =20)

    #Selection options for each questions displayed using radio buttons.
    self.rb1 = Radiobutton(self.quiz_frame, text = q_a[quenum][1], value = 1, indicator = 0, variable = self.var1
    , command = self.test_progress, pady = 60, padx = 1, font = ("Verdana", "11"), relief = RAISED, width = 37, bg = "Orange", activebackground = "Dark Orange")
    self.rb1.grid(row = 3, pady = 8, sticky = W, column = 0)

    self.rb2 = Radiobutton(self.quiz_frame, text = q_a[quenum][2], value = 2, indicator = 0, variable = self.var1, command = self.test_progress, pady = 60, padx = 1, font = ("Verdana","11"), relief = RAISED, width = 37, bg = "Orange", activebackground = "Dark Orange")
    self.rb2.grid(row = 3,pady = 8, sticky = E, column = 0)

    self.rb3 = Radiobutton(self.quiz_frame, text = q_a[quenum][3], value = 3, indicator = 0, variable = self.var1, command = self.test_progress,  pady = 60, padx = 1, font = ("Verdana","11"), relief = RAISED, width = 37, bg = "Orange", activebackground = "Dark Orange")
    self.rb3.grid(row = 4, pady = 8, sticky = W, column = 0)

    self.rb4 = Radiobutton(self.quiz_frame, text = q_a[quenum][4], value = 4, indicator = 0, variable = self.var1, command = self.test_progress, pady = 60, padx = 1, font = ("Verdana","11"), relief = RAISED, width = 37, bg = "Orange", activebackground = "Dark Orange")
    self.rb4.grid(row = 4, pady = 8, sticky = E, column = 0)

    #Quit button if user wants to quit during the quiz.
    self.quit_button = Button(self.quiz_frame, text = "QUIT", bg = "Red", relief = RAISED, command = self.quit)
    self.quit_button.grid(row = 0, sticky = W, padx = 10, pady = (10))

    #Score display.
    self.score_update = Label(self.quiz_frame, text = "Score: " + str(score), bg = background_color, font = ("bold"))
    self.score_update.grid(row = 0, padx = 20, pady = (10), sticky = E)
        
  #If user wants to leave during the quiz in progress, user is asked to confirm, then taken to leaderboard.
  def quit(self):
    result = messagebox.askyesno("Exit", "Are you sure?") #Ask user to confirm
    if result == True: #if yes, then takes user to leaderboard.
      self.leader_board() 
    else: #or else continue quiz.
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
    if len(asked) > 4: #at the end of the quiz: 
      if selected == q_a[quenum][4]: #user is taken to the leaderboard to show their results. 
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
    
  #Initialising the leaderboard to list top 5 names with the highest scores so far from the stored_usernames.
  def leader_board(self):
    root.withdraw()
    name = stored_usernames[0]
    file = open("leaderBoard.txt", "a") #insert the leader file in here.

    if name == "admin":
      file = open("leaderBoard.txt", "w")
    else:
      file.write(str(score)) 
      file.write(" - ")
      file.write(name + "\n") #mention score along with user name inputted by the user.
      file.close()
        
    inputFile = open("leaderBoard.txt", 'r')
    lineList = inputFile.readlines()
    lineList.sort()
        
    inputFile = open("leaderBoard.txt", "r")
    lineList = inputFile.readlines()
    lineList.sort()
    top = []
    top5 = (lineList[-5:])
    for line in top5:
      point = line.split(" - ")
      top.append((int(point[0]), point[1]))
    file.close()
    top.sort()
    top.reverse()
    return_string = ""
    for i in range(len(top)):
      return_string += "{} - {}\n".format(top[i][0], top[i][1])
    print(return_string)

    #Display Leaderboard in new seperate window.
    open_leaderb = Leaderboardwindow(root)
    open_leaderb.num1.config(text = return_string)


##Display Leaderboard in this class:
class Leaderboardwindow:

  #Format using a Toplevel widget for a new window.
  def __init__(self, parent):
    background_color = "#DEBB74"
    self.endbox = Toplevel(root)
    self.endbox.title("Quiz Leaderboard")
    self.endbox.resizable(False, False)

    #Leaderboard frame
    self.leaderb_frame = Frame(self.endbox, bg = background_color, padx = 220, pady = 50)
    self.leaderb_frame.grid()

    #Congratulate user.
    self.leaderb_heading = Label(self.leaderb_frame, text = "Leaderboard\n---", bg = background_color, fg = "Dark Red", font = ("Times New Roman", "14", "bold"))
    self.leaderb_heading.grid(row = 0)

    #Display personal score.
    self.score_results = Label(self.leaderb_frame, text = "Your Score:           " + str(score), bg = background_color, fg = "Dark Red", font = ("13"))
    self.score_results.grid(row = 1, pady = (0, 20))

    #Display top 5 highest scores from quiz.
    self.num1 = Label(self.leaderb_frame, text = "1st place..", bg = background_color, fg = "Dark Red", font=("Helvetica", "10"))
    self.num1.grid(row =2)

    #Quit button to exit quiz.
    quit_program = Button(self.leaderb_frame, text = "END", command = self.endbox_destroy, padx = 10, pady = 10 ,bg = "Red")
    quit_program.grid(row=4)


  #End quiz when user presses end button.
  def endbox_destroy(self):
    self.endbox.destroy()
    root.destroy()


##################################################################################
if __name__ == "__main__": #Makes the file the starter file
    root = Tk() #Creates a pop up window
    root.title("Geography Quiz") 
    startingwindow_object = Startingwindow(root)
    root.geometry("700x450")
    root.resizable(False, False)
    root.mainloop() #Keeps the window on

