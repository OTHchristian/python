from random import randint
from math import sqrt
from tkinter import *
class Move() :

    def __init__(self,window,canvas,x,y,rond,x1,y1,food,label2) -> None:
        self.direction = ['Up', 'Down', 'Left', 'Right']
        self.window=window
        self.canvas = canvas
        self.vitesse = 5
        self.x = x
        self.y = y
        self.rond = rond
        self.x1 = x1
        self.y1 = y1
        self.food = food
        self.collision = False
        self.tmp = ''
        index = randint(0,3)
        self.label = label2
        self.score = 0
        self.event = self.direction[index]
        self.game()

    def replay(self):
        self.x= randint(50,450)
        self.y= randint(50,450)
        self.x1= randint(50,450)
        self.y1= randint(50,450)
        self.vitesse = 5
        self.canvas.coords(self.food,self.x1-3,self.y1-3,self.x1+3,self.y1+3)
        self.canvas.coords(self.rond,self.x-7,self.y-7,self.x+7,self.y+7)
        index = randint(0,3)
        self.collision = False
        self.event = self.direction[index]
        self.tmp = ''
        self.score = 0
        self.popup.destroy()
        self.game()

    def end(self):
        self.popup.destroy()
        self.window.destroy()
    
    def game(self) :
        self.collision_wall()
        self.collision_food()
        self.return_score()
        self.move()
        if not self.collision :
            self.canvas.after(100,self.game)
        else:
            popup = Tk()
            popup.title('serpent')
            popup.geometry(f'200x200+{str(self.window.winfo_x() + 150)}+{str(self.window.winfo_y() + 160)}')
            popup.minsize(width='200', height='200')
            popup.maxsize(width='200', height='200')
            popup.config(background='black')
            self.popup = popup
            label = Label(popup,text='GAME OVER',font='bolder',border=2,bg='red')
            label2 = Label(popup, text=f'SCORE : {self.score}',fg='white',bg='black',font='bolder')
            button1 = Button(popup, text='fermer', bg='white', fg='black',width='40',command=self.end)
            button = Button(popup, text='rejouer', bg='white', fg='black',width='40', command=self.replay)
            label.pack(pady=10)
            label2.pack(pady= 5)
            button.pack(pady=10)
            button1.pack(pady=3)
            popup.mainloop()

    def take_event(self,event) :
        self.event = event.keysym

    def move(self) :
        if self.event == 'Up' :
            self.tmp = 'Up'
            self.move_up()
        elif self.event == 'Down':
            self.tmp = 'Down'
            self.move_down()
        elif self.event == 'Left' :
            self.tmp = 'Left'
            self.move_left()
        elif self.event == 'Right' :
            self.tmp = 'Right'
            self.move_right()
        else :  
            pass

    def collision_food (self) :
        
        dist = (self.x - self.x1)**2 + (self.y-self.y1)**2
        dist = sqrt(dist)
        if  dist <= 7+0.2:
            self.x1 = randint(50,450)
            self.y1 = randint(50,450)
            self.canvas.coords(self.food,self.x1-3,self.y1-3,self.x1+3,self.y1+3)
            self.score += 1
            if self.score%4 == 0 :
                self.vitesse += 2 
        else :
            pass
    
    def collision_wall(self):

        if self.x+8  < 0 or self.x+8 >= 500 or  self.y+8 < 0 or self.y+8 >= 470 or self.x-8  < 0 or self.x-8 >= 500 or  self.y-8 < 0 or self.y-7 >= 470:
            self.collision = True

            
    def move_up(self):
        self.y -= self.vitesse 
        self.canvas.move(self.rond,0,-self.vitesse)
    def move_down(self):
        self.y += self.vitesse
        self.canvas.move(self.rond,0,+self.vitesse)
    def move_left(self):
        self.x -= self.vitesse
        self.canvas.move(self.rond,-self.vitesse,0)
    def move_right(self):
        self.x += self.vitesse
        self.canvas.move(self.rond,+self.vitesse,0)

    def return_score(self):
        self.label.configure(text=str(self.score))

