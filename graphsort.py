import random
from Tkinter import * 
import time

class numbers(object):
    
    def __init__(self):
        self.genNumbers(50)
    
    
    # Fill list with random numbers
    def genNumbers(self, num):
        self.numberList = []
        for i in range(num):
            self.numberList.append(random.randint(1,290))
        appWindow.drawGraph(self.numberList)           
    
    # Bubble Sort
    def bubbleSort(self):
        for i in range(len(self.numberList)):
            for j in range(len(self.numberList)):
                if self.numberList[j] > self.numberList[i]:
                    #swap
                    self.numberList[j], self.numberList[i] = self.numberList[i], self.numberList[j]
                    # wait and update
                    time.sleep(0.1)
                    appWindow.drawGraph(self.numberList)
                    root.update_idletasks()
                    
    def selectionSort(self):
        for i in range(len(self.numberList)-1,0,-1):
            positionOfMax=0
            for j in range(1,i+1):
                if self.numberList[j]>self.numberList[positionOfMax]:
                    positionOfMax = j
            
            temp = self.numberList[i]
            self.numberList[i] = self.numberList[positionOfMax]
            self.numberList[positionOfMax] = temp
            
            # wait and update
            time.sleep(0.1)
            
            appWindow.drawGraph(self.numberList)
            root.update_idletasks()
  
class controller(object):
    
    def __init__(self, num):
        self.bubble = Button(frame,text ="Bubble Sort", command = num.bubbleSort)
        self.bubble.pack(side=BOTTOM)
        
        self.selection = Button(frame, text = "Selection Sort", command = num.selectionSort)
        self.selection.pack(side=BOTTOM)
        
        self.genButton = Button(frame,text ="New Numbers", command = self.genButtonEvent)
        self.genButton.pack(side=BOTTOM)
        
        self.entry = Entry(frame, width = 20)
        self.entry.pack(side=BOTTOM)
    
    def genButtonEvent(self):
        if self.entry.get().strip() == "":
            num.genNumbers(50)
        else:
            num.genNumbers(int(self.entry.get()))
            
                     
   
class view(object):
    def __init__(self):
        self.canvas = Canvas(frame, height=400, width=600, relief=RAISED, bg='white')
        self.canvas.pack(side=TOP)
        self.leftRect = self.canvas.create_rectangle(10,10,580,300, fill = "white", outline="black")

    
    #Draw the graph
    def drawGraph(self, numList):
        self.canvas.delete(ALL)
        self.leftRect = self.canvas.create_rectangle(10,10,580,300, fill = "white", outline="black")
        x = 10
        spacing = 550 / len(numList)
        for i in range(len(numList)):
            x += spacing
            self.canvas.create_rectangle(x, 300-numList[i], x+5, 300, fill = "red")
    
    #Moves Label
         
root = Tk()
frame = Frame(root)
frame.pack()
appWindow = view()
num = numbers()
c = controller(num)
root.mainloop()
root.destroy()
