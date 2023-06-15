#luson basumatary
import keyboard
from playsound import playsound
import os
import random
import turtle
#setting up things
screen=turtle.Screen()
turtle.bgcolor("black")
text=turtle.Turtle()
text.penup()
text.goto(-10,100)
text.color("white")
tt=turtle.Turtle()
tt.color("cyan")
tt.hideturtle()
tt.speed(20)
a=0
#program loop
while True:
    tt.penup()
    tt.goto(-100,0)
    forDis=0 
    dR=0
    tt.pendown()
    #another loop :)
    while True:
        h=0
        no=0
        if a==200:
            tt.penup()
            tt.goto(-100,0)
            a=0
            tt.clear()
            tt.pendown()
        if keyboard.is_pressed('q'):
            no=1
            h=10
        if keyboard.is_pressed('w'):
            no=2
            h=20
        if keyboard.is_pressed('e'):
            no=3
            h=30
        if keyboard.is_pressed('r'):
            no=4
            h=40
        if keyboard.is_pressed('t'):
            no=5
            h=50
        if keyboard.is_pressed('y'):
            no=6
            h=60
        if keyboard.is_pressed('u'):
            no=7
            h=70
        if keyboard.is_pressed('i'):
            no=8
            h=80
        if keyboard.is_pressed('o'):
            no=9
            h=90
        if keyboard.is_pressed('p'):
            no=10
            h=100
        if keyboard.is_pressed('a'):
            no=11
            h=110
        if keyboard.is_pressed('s'):
            no=12
            h=120
        if keyboard.is_pressed('d'):
            no=13
            h=130
        if keyboard.is_pressed('f'):
            no=14
            h=140
        if keyboard.is_pressed('g'):
            no=15
            h=150
        if keyboard.is_pressed('h'):
            no=16
            h=160
        if keyboard.is_pressed('j'):
            no=17
            h=170
        if keyboard.is_pressed('k'):
            no=18
            h=180
        if keyboard.is_pressed('l'):
            no=19
            h=190
        if keyboard.is_pressed('z'):
            no=20
            h=200
        if keyboard.is_pressed('x'):
            no=21
            h=210
        if keyboard.is_pressed('c'):
            no=22
            h=220
        if keyboard.is_pressed('v'):
            no=23
            h=230
        if keyboard.is_pressed('b'):
            no=24
            h=240  
        a+=1
        try:
            playsound(os.getcwd()+"/tones/key"+str(no)+".mp3",False)
            tt.goto(tt.xcor()+1,h)
        except Exception:
            tt.goto(tt.xcor()+1,tt.ycor())
            continue
#hope, by now you've figured out how it's running :)
