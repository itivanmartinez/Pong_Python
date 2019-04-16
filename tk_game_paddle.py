#Created By Ivan Martinez
#GitHub https://github.com/itivanmartinez
#Enjoy!

from tkinter import *
import random
import time

class Ball:
    def __init__(self,canvas,paddle,bricks,color):
        self.canvas = canvas
        self.paddle = paddle
        self.bricks = bricks
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,400,100)
        starts=[-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x=starts[0]
        self.y=-3
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        self.hit_bottom=False

    def moveball(self):
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y=3
        if pos[3]>=self.canvas_height:
            self.hit_bottom=True
        if pos[0]<=0:
            self.x=3
        if pos[2]>=self.canvas_width:
            self.x=-3
        if self.hit_paddle(pos)==True:
            self.y=-3
        for br in self.bricks:
            if self.hit_brick(pos,br)==True:
                self.y=3
                if br.hits==0:
                    canvas.delete(br.id)
                    bricks.remove(br)
    def hit_paddle(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2]>= paddle_pos[0] and pos[0]<=paddle_pos[2]:
            if pos[3]>=paddle_pos[1] and pos[3]<=paddle_pos[3]:
                return True
        return False
        
    def hit_brick(self,pos,br):
        brick_pos=self.canvas.coords(br.id)
        if pos[0]>= brick_pos[0] and pos[2]<=brick_pos[2]:
            if pos[1]<=brick_pos[3]:
                br.hits=br.hits-1
                br.change_color()
                return True
        return False
            
                
    
class Paddle:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id=canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,500)
        self.x=0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<Button-1>',self.slide_left)
        self.canvas.bind_all('<Button-3>',self.slide_right)

    def movepaddle(self):
        self.canvas.move(self.id,self.x,0)
        pos=self.canvas.coords(self.id)
        if pos[0]<=0:
            self.x = 0
        elif pos[2]>=self.canvas_width:
            self.x=0

    def slide_left(self,evt):
        self.x=-2
    def slide_right(self,evt):
        self.x=2
        
class Brick:
    def __init__(self, canvas,color,x,y):
        self.canvas=canvas
        self.x=x
        self.y=y
        self.hits=3
        self.id=canvas.create_rectangle(0,0,200,30,fill=color)
        self.canvas.move(self.id,self.x,self.y)
        self.canvas_width = self.canvas.winfo_width()
    def change_color(self):
        if self.hits==2:
            self.canvas.itemconfig(self.id,fill='blue')
        if self.hits==1:
            self.canvas.itemconfig(self.id,fill='red')

        

def create_bricks(x,y,bricks):
    for i in range(3):
        bricks.append(Brick(canvas,'gray',x,y))
        x=x+200
        
windows=Tk()
windows.title("My First Game")
windows.resizable(0,0)
windows.wm_attributes("-topmost",1)

canvas=Canvas(windows,width=600,height=600,bd=0,highlightthickness=0)
canvas.pack()
windows.update()

paddle=Paddle(canvas,'red')
bricks=[]
x=0
y=0
for i in range(3):
    create_bricks(x,y,bricks)
    y=y+30
ball=Ball(canvas,paddle,bricks,'blue')

while 1:
    ball.moveball()
    paddle.movepaddle()
    windows.update_idletasks()
    windows.update()
    time.sleep(0.01)
    
