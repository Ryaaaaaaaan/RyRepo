#Environmentally friendly program
#By Ryan 
#5/03/19

#Get GUI funtional 
from random import shuffle
from appJar import gui
app=gui()
questions = []

class Question:
        #inilitilse the class
        def __init__(self,answer1, answer2, answer3, answer4, questionText):
                self.answer1 = answer1
                self.answer2 = answer2
                self.answer3 = answer3
                self.answer4 = answer4
                self.questionText = questionText

def launch(win):
        if win == "Start":
                question1()
        if win == "Exit":
                app.stop()
app.setTitle("Trash removal")
app.addLabel ("Quiz Full of Trash")
app.addButtons(["Start", "Exit"], launch)
app.go()