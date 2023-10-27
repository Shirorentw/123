import tkinter as tk
import time
import _thread



key=''
key2=''
x=12
y=17
prex=11
prey=17
label=None
label2=None
label3=None
a=-1
b=-1
Options=True
Options2=False
map=0
premap=0
keep_moving=True
maze=[
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,0,1,1,1,0,0,0,1,0,0,0,0,0,0,1,1],
    [1,1,1,1,1,1,0,0,0,1,0,0,0,1,0,0,0,1,1,1,0,0,0,0,0,0,1,0,0,0,1,1],
    [1,1,1,1,1,1,1,0,1,1,1,0,0,1,1,1,0,0,0,1,0,0,0,1,0,1,1,1,0,0,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,0,1,0,0,0,1,1,1,1,1,1,0,1,1],
    [1,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,3,0,1,1,1,0,0,1,1],
    [1,1,1,0,0,0,0,0,0,1,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,1,0,0,0,1,1],
    [1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],]



def key_down(e):
    global key,key2
    key=e.keysym
    key2=e.keycode

def key_up(e):
    global key,key2
    key=''
    key2=''


def change_map():
    global maze,map,x,y,Options,Options2,a
    if map==0:

        if maze[x][y]==2 and Options==False:
            if key=='Down':
                canvas.delete(img_map)
                canvas.create_image(0,0,image=img_map1,anchor='nw',tag='img_map1')
                x=6
                y=10
                canvas.create_image(y*40,x*40,image=img1,anchor='nw',tag='img1')
                canvas.create_image(200,520,image=img2_1,anchor='nw',tag='img2_1')
                canvas.coords('img1',y*40,x*40)
                maze=[
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5],
                    [1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,0,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,4,0,0,0,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],]
                a=-1
                map=1
                dialogue_run_4()
                

        if maze[x][y]==2 and Options==True:
            if key=='Down':
                dialogue_run_3()
                

        if maze[x][y]==3:
            if key2==13:
                canvas.delete('img1')
                canvas.delete('img2')
                canvas.delete('img3')
                canvas.delete('img4')
                canvas.create_image(0,0,image=img2,anchor='nw',tag='img2')
                canvas.coords('img2',y*40,x*40)
                dialogue_2()
                a=-1
            
    elif map==1:

        if maze[x][y]==2 and Options==False:
            if key=='Up':
                dialogue_run_6()

        if maze[x][y]==3:
            if key=='Up':
                dialogue_run_9()        
            
        if maze[x][y]==2 and Options==True:
            if key=='Up':
                canvas.delete(img_map1)
                canvas.delete(img2)
                canvas.create_image(0,0,image=img_map2,anchor='nw',tag='img_map2')
                x=12
                y=0
                a=-1
                dialogue_run_8()
                canvas.create_image(y*40,x*40,image=img4,anchor='nw',tag='img4')
                canvas.coords('img4',y*40,x*40)
                maze=[
                    [1,1,1,1,1,1,1,1,1,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,0,0,0,0,0,0,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,0,0,0,0,0,0,1,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5],
                    [1,0,0,0,0,0,0,1,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5],
                    [1,0,0,0,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,0,0,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,0,0,0,0,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [3,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,4,4,4,4,0,0,0,0,0,0,0],
                    [1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],]
                map=2

        if maze[x][y]==4:
            if key2==13:
                canvas.delete('img1')
                canvas.delete('img2')
                canvas.delete('img3')
                canvas.delete('img4')
                canvas.create_image(0,0,image=img2,anchor='nw',tag='img2')
                canvas.coords('img2',y*40,x*40)
                dialogue_5()
                a=-1
            
        if maze[x][y]==5:
            dialogue_run_7()
            
    elif map==2:

        if maze[x][y]==2:
            if key=='Up':
                canvas.delete(img_map2)
                canvas.create_image(0,0,image=img_map3,anchor='nw',tag='img_map3')
                x=17
                y=9
                canvas.create_image(y*40,x*40,image=img2,anchor='nw',tag='img2')
                canvas.coords('img2',y*40,x*40)
                maze=[
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,3,3,3,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],]
                map=3

        if maze[x][y]==3:
            if key=='Left':
                dialogue_run_10()

        if maze[x][y]==4:
            if key2==13:
                canvas.delete('img1')
                canvas.delete('img2')
                canvas.delete('img3')
                canvas.delete('img4')
                canvas.create_image(0,0,image=img2,anchor='nw',tag='img2')
                canvas.coords('img2',y*40,x*40)
                dialogue_11()
                a=-1

        if maze[x][y]==5:
            if key=='Right':
                dialogue_run_12()

    elif map==3:
        if maze[x][y]==2:
            if key=='Up':
                canvas.delete(img_map3)
                canvas.create_image(0,0,image=img_map4,anchor='nw',tag='img_map4')
                x=16
                y=2
                canvas.create_image(y*40,x*40,image=img2,anchor='nw',tag='img2')
                canvas.coords('img2',y*40,x*40)
                maze=[
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1],
                    [1,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,2],
                    [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                    [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                    [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                    [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                    [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                    [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                    [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                    [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                    [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                    [1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],]
                map=4

        if maze[x][y]==3:
            if key=='Down':
                dialogue_run_10()

    elif map==4:
        if maze[x][y]==2:
            if key=='Right':
                dialogue_run_13()
        if maze[x][y]==3:
            if key=='Up':
                canvas.delete(img_map4)
                canvas.create_image(0,0,image=img_map6,anchor='nw',tag='img_map6')
                x=14
                if y==2:
                    y=2
                elif y==24:
                    y=24
                canvas.create_image(y*40,x*40,image=img2,anchor='nw',tag='img2')
                canvas.coords('img2',y*40,x*40)
                maze=[
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,0,1,1,0,0,1,0,0,1,0,1,1,1,0,0,0,1,1,0,0,0,1,1,1],
                    [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1],
                    [1,1,1,0,0,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,0,0,0,1,1,1],
                    [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1],
                    [1,1,1,0,0,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,0,1,0,0,1,1],
                    [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1],
                    [1,1,0,0,0,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,0,1,0,0,1,1],
                    [1,1,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
                    [1,1,0,0,0,3,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,0,0,0,0,1,1],
                    [1,1,0,0,0,0,3,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
                    [1,1,2,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,1,2,0,0,0,0,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],]
                canvas.create_image(240,480,image=img3_3,anchor='nw',tag='img3_3')
                map=5
                dialogue_run_14()

    elif map==5:
        if maze[x][y]==3:
            if key2==13:
                canvas.delete('img1')
                canvas.delete('img2')
                canvas.delete('img3')
                canvas.delete('img4')
                canvas.delete('img3_3')
                if x==11 and y==6:
                    canvas.create_image(y*40,x*40,image=img1,anchor='nw',tag='img1')
                    canvas.coords('img1',y*40,x*40)
                    canvas.create_image(240,480,image=img3_4,anchor='nw',tag='img3_4')
                elif x==12 and y==5:
                    canvas.create_image(y*40,x*40,image=img4,anchor='nw',tag='img4')
                    canvas.coords('img4',y*40,x*40)
                    canvas.create_image(240,480,image=img3_2,anchor='nw',tag='img3_2')
                elif x==13 and y==6:
                    canvas.create_image(y*40,x*40,image=img2,anchor='nw',tag='img2')
                    canvas.coords('img2',y*40,x*40)
                    canvas.create_image(240,480,image=img3_1,anchor='nw',tag='img3_1')
                dialogue_15()
                Options=True
        
        if maze[x][y]==2 and Options==True:
            if key=='Down':
                if x==14 and y==2:
                    x=3
                    y=2
                elif x==14 and y==24:
                    x=3
                    y=24
                canvas.delete(img_map6)
                canvas.create_image(0,0,image=img_map4,anchor='nw',tag='img_map4')
                canvas.create_image(y*40,x*40,image=img1,anchor='nw',tag='img1')
                canvas.coords('img1',y*40,x*40)
                maze=[
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,5,1,1,1,1],
                    [1,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,2],
                    [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                    [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                    [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                    [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                    [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                    [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                    [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                    [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                    [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                    [1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],]
                map=6

        if maze[x][y]==2 and Options==False:
            if key=='Down':
                dialogue_run_16()

    elif map==6:
        if maze[x][y]==3:
            if key=='Up':
                dialogue_run_17()
        if maze[x][y]==4:
            if key=='Down':
                dialogue_run_17()
        if maze [x][y]==2:
            if key=='Right':
                dialogue_run_17()

        if maze[x][y]==5:
            if key=='Up':
                canvas.delete(img_map4)
                canvas.create_image(0,0,image=img_map10,anchor='nw',tag='img_map10')
                x=8
                y=26
                canvas.create_image(y*40,x*40,image=img3,anchor='nw',tag='img3')
                canvas.coords('img3',y*40,x*40)
                maze=[
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,3,1,1,1,1,1],
                    [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,0,2,1,0,2,1,0,2,1,0,2,1,0,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],]
                map=7




    elif map==7:
        if maze[x][y]==2:
            if key2==13:
                dialogue_18()








def dialogue_run_1():
    _thread.start_new_thread(dialogue_1,())  

def dialogue_1():
    global label,label2

    canvas.create_image(250,543,image=dialog_box,anchor='nw',tag='dialog_box')
    label=tk.Label(form,text='叮铃铃 叮铃铃 叮铃铃',font=('俐方體11號',24),bg="#bababa")
    label.place(x=270,y=570)
    time.sleep(3)
    label.destroy()
    canvas.create_image(890,480,image=avatar2,anchor='nw',tag='avatar2')
    label=tk.Label(form,text='阿阿阿阿阿（起床中...）',font=('俐方體11號',24),bg='#bababa')
    label.place(x=270,y=570)
    time.sleep(1.8)
    label.destroy()
    label=tk.Label(form,text='又到了憂鬱的星期一...',font=('俐方體11號',24),bg='#bababa')
    label.place(x=270,y=570)
    time.sleep(1.75)
    label.destroy()
    label=tk.Label(form,text='快餓扁了 趕快起床吃東西再去學校吧...',font=('俐方體11號',24),bg='#bababa')
    label.place(x=270,y=570)
    time.sleep(3)
    label.destroy()
    label=tk.Label(form,text='我記得客廳那裡有一些麵包可以吃',font=('俐方體11號',24),bg='#bababa')
    label.place(x=270,y=570)
    time.sleep(3)
    canvas.delete('avatar2')
    label.destroy()
    label=tk.Label(form,text='使用 ↑ ↓ ← → 進行移動',font=('俐方體11號',24),bg='#bababa')
    label2=tk.Label(form,text='Enter:對話、調查、確定',font=('俐方體11號',24),bg='#bababa')
    label.place(x=270,y=570)
    label2.place(x=270,y=610)
    time.sleep(3)
    label.destroy()
    label2.destroy()
    label_name.destroy()
    canvas.delete('dialog_box')
    moving()

def dialogue_2():
    global key,key2,label,label2,label3,a,Options,maze,keep_moving

    keep_moving=False

    if key=='Up' and a==2:
        Options=True
    elif key=='Down' and a==2:
        Options=False

    if a==0:
        if label is not None:
            label.destroy()
        canvas.create_image(250,543,image=dialog_box,anchor='nw',tag='dialog_box')
        label=tk.Label(form,text='獲得麵包！',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)

    if a==1:
        if label is not None:
            label.destroy()
        canvas.create_image(890,480,image=avatar2,anchor='nw',tag='avatar2')
        label=tk.Label(form,text='這麵包還能吃嗎... 感覺放了好久',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)   
    
    if a==2 and Options==True:
        if label is not None:
            label.destroy()
        if label2 is not None:
            label2.destroy()
        if label3 is not None:
            label3.destroy()
        canvas.delete('avatar2')
        label=tk.Label(form,text='是否食用？　(使用↑　↓鍵選擇)',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)
        label2=tk.Label(form,text='是',font=('俐方體11號',24),bg='white')
        label2.place(x=270,y=610)
        label3=tk.Label(form,text='否',font=('俐方體11號',24),bg='#bababa')
        label3.place(x=270,y=650)

    if a==2 and Options==False:
        if label is not None:
            label.destroy()
        if label2 is not None:
            label2.destroy()
        if label3 is not None:
            label3.destroy()
        label=tk.Label(form,text='是否食用？　(使用↑　↓鍵選擇)',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)
        label2=tk.Label(form,text='是',font=('俐方體11號',24),bg='#bababa')
        label2.place(x=270,y=610)
        label3=tk.Label(form,text='否',font=('俐方體11號',24),bg='white')
        label3.place(x=270,y=650)

    if a==3 and Options==True:
        if label is not None:
            label.destroy()
        if label2 is not None:
            label2.destroy()
        if label3 is not None:
            label3.destroy()
        label=tk.Label(form,text='你吃下了一個外表帶有藍色斑點的麵包',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)

    if a==4 and Options==True:
        label.destroy()
        canvas.create_image(890,480,image=avatar2,anchor='nw',tag='avatar2')
        label=tk.Label(form,text='這麵包竟然發霉了...',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)

    if a==5 and Options==True:
        label.destroy()
        canvas.delete('avatar2')
        label=tk.Label(form,text='現在你的胃裡多了一份冒險的味道',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)

    if a==6 and Options==True:
        label.destroy()
        canvas.create_image(890,480,image=avatar2,anchor='nw',tag='avatar2')
        label=tk.Label(form,text='一大早就這麼雖...',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)

    if a==7 and Options==True:
        label.destroy()
        label=tk.Label(form,text='先出門去學校吧 希望等一下胃不會哭',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)

    if a==8 and Options==True:
        canvas.delete('avatar2')
        canvas.delete('dialog_box')
        label.destroy()
        maze=[
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,0,1,1,1,0,0,0,1,0,0,0,0,0,0,1,1],
                [1,1,1,1,1,1,0,0,0,1,0,0,0,1,0,0,0,1,1,1,0,0,0,0,0,0,1,0,0,0,1,1],
                [1,1,1,1,1,1,1,0,1,1,1,0,0,1,1,1,0,0,0,1,0,0,0,1,0,1,1,1,0,0,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,0,1,0,0,0,1,1,1,1,1,1,0,1,1],
                [1,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1,1],
                [1,1,1,0,0,0,0,0,0,1,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,1,0,0,0,1,1],
                [1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1],
                [1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1],
                [1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1],
                [1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1],
                [1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],]
        keep_moving=True
        Options=False
        return
    
    if a==3 and Options==False:
        if label is not None:
            label.destroy()
        if label2 is not None:
            label2.destroy()
        if label3 is not None:
            label3.destroy()
        label=tk.Label(form,text='你選擇不吃麵包 ',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)

    if a==4 and Options==False:
        if label is not None:
            label.destroy()
        if label2 is not None:
            label2.destroy()
        if label3 is not None:
            label3.destroy()
        label=tk.Label(form,text='然後你就餓死了',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)
    
    if a==5 and Options==False:
        label.destroy()
        form.quit()

    if key2==13:
        a+=1

    form.after(100,dialogue_2)

def dialogue_run_3():
    _thread.start_new_thread(dialogue_3,())  

def dialogue_3():
    global keep_moving
    keep_moving=False
    canvas.create_image(250,543,image=dialog_box,anchor='nw',tag='dialog_box')
    canvas.create_image(890,480,image=avatar2,anchor='nw',tag='avatar2')
    label=tk.Label(form,text='要先去客廳找麵包吃...',font=('俐方體11號',24),bg="#bababa")
    label.place(x=270,y=570)
    time.sleep(1.5)
    label.destroy()
    canvas.delete('avatar2')
    canvas.delete('dialog_box')
    keep_moving=True

def dialogue_run_4():
    _thread.start_new_thread(dialogue_4,())    

def dialogue_4():
    global maze,Options,keep_moving
    keep_moving=False
    canvas.create_image(250,543,image=dialog_box,anchor='nw',tag='dialog_box')
    canvas.create_image(890,480,image=avatar2,anchor='nw',tag='avatar2')
    label=tk.Label(form,text='肚子好痛 早知道就乾脆不要吃那塊麵包',font=('俐方體11號',24),bg="#bababa")
    label.place(x=270,y=570)
    time.sleep(2.3)
    label.destroy()
    label=tk.Label(form,text='去找一下王小明看看他有沒有胃藥吧',font=('俐方體11號',24),bg='#bababa')
    label.place(x=270,y=570)
    time.sleep(2.3)
    label.destroy()
    canvas.delete('dialog_box')
    canvas.delete('avatar2')
    Options=False
    keep_moving=True
      
def dialogue_5():
    global key2,a,label,label2,label3,maze,Options,keep_moving

    keep_moving=False

    if key=='Down' and a==6:
        Options=True
    elif key=='Up' and a==6:
        Options=False

    if a==0:
        if label is not None:
            label.destroy()
        canvas.create_image(250,543,image=dialog_box,anchor='nw',tag='dialog_box')
        canvas.create_image(890,480,image=avatar1,anchor='nw',tag='avatar1')
        label=tk.Label(form,text='王小明：早安',font=('俐方體11號',24),bg="#bababa")
        label.place(x=270,y=570)

    if a==1:
        if label is not None:
            label.destroy()
        label=tk.Label(form,text='王小明：現在都幾點了',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)

    if a==2:
        if label is not None:
            label.destroy()
        label=tk.Label(form,text='王小明：趕快去學校上課！',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)

    if a==3:
        if label is not None:
            label.destroy()
        canvas.delete('avatar1')
        label=tk.Label(form,text='好喔',font=('俐方體11號',24),bg='#bababa')
        canvas.create_image(890,480,image=avatar2,anchor='nw',tag='avatar2')
        label.place(x=270,y=570)

    if a==4:
        if label is not None:
            label.destroy()
        label=tk.Label(form,text='那個...',font=('俐方體11號',24),bg='#bababa')
        canvas.create_image(890,480,image=avatar2,anchor='nw',tag='avatar2')
        label.place(x=270,y=570)

    if a==5:
        if label is not None:
            label.destroy()
        canvas.delete('avatar2')
        canvas.create_image(890,480,image=avatar1,anchor='nw',tag='avatar1')
        label=tk.Label(form,text='王小明：甚麼事？',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)

    if a==6 and Options==False:
        if label is not None:
            label.destroy()
        if label2 is not None:
            label2.destroy()
        if label3 is not None:
            label3.destroy()
        canvas.delete('avatar1')
        canvas.create_image(890,480,image=avatar2,anchor='nw',tag='avatar2')
        label2=tk.Label(form,text='你有胃藥嗎？ 我肚子痛...',font=('俐方體11號',24),bg='white')
        label2.place(x=270,y=570)
        label3=tk.Label(form,text='沒事...',font=('俐方體11號',24),bg='#bababa')
        label3.place(x=270,y=620)

    if a==6 and Options==True:
        if label is not None:
            label.destroy()
        if label2 is not None:
            label2.destroy()
        if label3 is not None:
            label3.destroy()
        label2=tk.Label(form,text='你有胃藥嗎？ 我肚子痛...',font=('俐方體11號',24),bg='#bababa')
        label2.place(x=270,y=570)
        label3=tk.Label(form,text='沒事...',font=('俐方體11號',24),bg='white')
        label3.place(x=270,y=620)

    if a==7 and Options==False:
        if label is not None:
            label.destroy()
        if label2 is not None:
            label2.destroy()
        if label3 is not None:
            label3.destroy()
        canvas.delete('avatar2')
        canvas.create_image(890,480,image=avatar1,anchor='nw',tag='avatar1')
        label=tk.Label(form,text='王小明：胃藥嗎？ 等我一下',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)

    if a==8 and Options==False:
        if label is not None:
            label.destroy()
        canvas.delete('img2_1')
        canvas.delete('avatar1')
        canvas.create_image(200,520,image=img2_4,anchor='nw',tag='img2_4')
        canvas.create_image(890,480,image=avatar2,anchor='nw',tag='avatar2')
        label=tk.Label(form,text='...',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)

    if a==9 and Options==False:
        if label is not None:
            label.destroy()
        canvas.delete('img2_4')
        canvas.delete('avatar2')
        canvas.create_image(200,520,image=img2_1,anchor='nw',tag='img2_1')
        label=tk.Label(form,text='王小明：胃藥在這 趕快吃一吃去學校',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)
        canvas.create_image(890,480,image=avatar1,anchor='nw',tag='avatar1')

    if a==10 and Options==False:
        if label is not None:
            label.destroy()
        canvas.delete('avatar1')
        canvas.create_image(890,480,image=avatar2,anchor='nw',tag='avatar2')
        label=tk.Label(form,text='感謝感謝 我吃完就馬上去了',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)

    if a==11 and Options==False:
        if label is not None:
            label.destroy()
        canvas.delete('avatar2')
        label=tk.Label(form,text='~慢慢的把胃藥吞下肚~',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)

    if a==12 and Options==False:
        if label is not None:
            label.destroy()
        label=tk.Label(form,text='感覺有吃沒吃都一樣 你的胃依然在哭泣',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)

    if a==13 and Options==False:
        if label is not None:
            label.destroy()
        canvas.delete('dialog_box')
        maze=[
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5],
            [1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,0,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,0,0,0,0,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],]
        Options=True
        keep_moving=True
        return
    
    if a==7 and Options==True:
        if label is not None:
            label.destroy()
        if label2 is not None:
            label2.destroy()
        if label3 is not None:
            label3.destroy()
        canvas.delete('avatar2')
        canvas.create_image(890,480,image=avatar1,anchor='nw',tag='avatar1')
        label=tk.Label(form,text='王小明：沒事就趕快去學校上課',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)

    if a==8 and Options==True:
        if label is not None:
            label.destroy()
        canvas.delete('avatar1')
        canvas.create_image(890,480,image=avatar2,anchor='nw',tag='avatar2')
        label=tk.Label(form,text='(胃痛的問題晚點再解決吧 快遲到了)',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)

    if a==9 and Options==True:
        if label is not None:
            label.destroy()
        canvas.delete('dialog_box')
        canvas.delete('avatar2')
        maze=[
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5],
            [1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,0,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,0,0,0,0,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],]
        Options=True
        keep_moving=True
        return
    
    if key2==13:
        a+=1

    form.after(100,dialogue_5)

def dialogue_run_6():
    _thread.start_new_thread(dialogue_6,())    

def dialogue_6():
    global keep_moving
    keep_moving=False
    canvas.create_image(250,543,image=dialog_box,anchor='nw',tag='dialog_box')
    canvas.create_image(890,480,image=avatar2,anchor='nw',tag='avatar2')
    label=tk.Label(form,text='要先去找王小明，看看他有沒有胃藥',font=('俐方體11號',24),bg="#bababa")
    label.place(x=270,y=570)
    time.sleep(1.5)
    label.destroy()
    canvas.delete('avatar2')
    canvas.delete('dialog_box')
    keep_moving=True
    
def dialogue_run_7():
    _thread.start_new_thread(dialogue_7,()) 

def dialogue_7():
    global x,y,keep_moving
    keep_moving=False
    canvas.create_image(250,543,image=dialog_box,anchor='nw',tag='dialog_box')
    canvas.create_image(890,480,image=avatar2,anchor='nw',tag='avatar2')
    label=tk.Label(form,text='往學校的路不在這裡',font=('俐方體11號',24),bg="#bababa")
    label.place(x=270,y=570)
    time.sleep(1.5)
    label.destroy()
    canvas.delete('avatar2')
    canvas.delete('dialog_box')
    if x==16 and y==13:
        x=15
        canvas.delete('img1')
        canvas.create_image(0,0,image=img2,anchor='nw',tag='img2')
        canvas.coords('img2',y*40,x*40)
    if x==7 and y==31:
        y=30
        canvas.delete('img4')
        canvas.create_image(0,0,image=img3,anchor='nw',tag='img3')
        canvas.coords('img3',y*40,x*40)
    keep_moving=True

def dialogue_run_8():
    _thread.start_new_thread(dialogue_8,()) 

def dialogue_8():
    global keep_moving
    keep_moving=False
    canvas.create_image(250,543,image=dialog_box,anchor='nw',tag='dialog_box')
    canvas.create_image(890,480,image=avatar2,anchor='nw',tag='avatar2')
    label=tk.Label(form,text='還有五分鐘就要打鐘了',font=('俐方體11號',24),bg="#bababa")
    label.place(x=270,y=570)
    time.sleep(1.7)
    label.destroy()
    label=tk.Label(form,text='肚子感覺還是有點痛...',font=('俐方體11號',24),bg="#bababa")
    label.place(x=270,y=570)
    time.sleep(1.5) 
    label.destroy()
    label=tk.Label(form,text='要不要去找販賣機買一瓶水？',font=('俐方體11號',24),bg="#bababa")
    label.place(x=270,y=570)
    time.sleep(2) 
    label.destroy()
    canvas.delete('avatar2')
    canvas.delete('dialog_box')
    keep_moving=True

def dialogue_run_9():
    _thread.start_new_thread(dialogue_9,()) 

def dialogue_9():
    global keep_moving
    keep_moving=False
    canvas.create_image(250,543,image=dialog_box,anchor='nw',tag='dialog_box')
    canvas.create_image(890,480,image=avatar2,anchor='nw',tag='avatar2')
    label=tk.Label(form,text='先去學校吧...',font=('俐方體11號',24),bg="#bababa")
    label.place(x=270,y=570)
    time.sleep(1.5) 
    label.destroy()
    canvas.delete('avatar2')
    canvas.delete('dialog_box')
    keep_moving=True

def dialogue_run_10():
    _thread.start_new_thread(dialogue_10,()) 

def dialogue_10():
    global keep_moving
    keep_moving=False
    canvas.create_image(250,543,image=dialog_box,anchor='nw',tag='dialog_box')
    canvas.create_image(890,480,image=avatar2,anchor='nw',tag='avatar2')
    label=tk.Label(form,text='早知道就請假 好想回家',font=('俐方體11號',24),bg="#bababa")
    label.place(x=270,y=570)
    time.sleep(1.5) 
    label.destroy()
    canvas.delete('avatar2')
    canvas.delete('dialog_box')
    keep_moving=True

def dialogue_11():
    global key,key2,label,label2,label3,a,Options,keep_moving,maze

    keep_moving=False
    
    if key=='Up' and a==1:
        Options=True
    elif key=='Down' and a==1:
        Options=False

    if a==0:
        if label is not None:
            label.destroy()
        canvas.create_image(250,543,image=dialog_box,anchor='nw',tag='dialog_box')
        canvas.create_image(890,480,image=avatar2,anchor='nw',tag='avatar2')
        label=tk.Label(form,text='錢包裡只剩下20塊了',font=('俐方體11號',24),bg="#bababa")
        label.place(x=270,y=570)

    if a==1 and Options==True:
        if label is not None:
            label.destroy()
        if label2 is not None:
            label2.destroy()
        if label3 is not None:
            label3.destroy()
        canvas.delete('avatar2')
        label=tk.Label(form,text='是否購買礦泉水？',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)
        label2=tk.Label(form,text='是',font=('俐方體11號',24),bg='white')
        label2.place(x=270,y=610)
        label3=tk.Label(form,text='否',font=('俐方體11號',24),bg='#bababa')
        label3.place(x=270,y=650)
    if a==1 and Options==False:
        if label is not None:
            label.destroy()
        if label2 is not None:
            label2.destroy()
        if label3 is not None:
            label3.destroy()
        canvas.delete('avatar2')
        label=tk.Label(form,text='是否購買礦泉水？',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)
        label2=tk.Label(form,text='是',font=('俐方體11號',24),bg='#bababa')
        label2.place(x=270,y=610)
        label3=tk.Label(form,text='否',font=('俐方體11號',24),bg='white')
        label3.place(x=270,y=650)

    if a==2 and Options==True:
        label.destroy()
        label2.destroy()
        label3.destroy()
        label=tk.Label(form,text='(你購買了一瓶超冰的礦泉水 並喝下去)',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)

    if a==3 and Options==True:
        label.destroy()
        canvas.create_image(890,480,image=avatar2,anchor='nw',tag='avatar2')
        label=tk.Label(form,text='咕嚕咕嚕 啊啊啊啊啊',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)

    if a==4 and Options==True:
        label.destroy()
        label=tk.Label(form,text='我剛剛是不是買了一瓶液態氮？ 太冰了吧',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)

    if a==5 and Options==True:
        label.destroy()
        canvas.delete('avatar2')
        canvas.delete('dialog_box')
        maze=[
            [1,1,1,1,1,1,1,1,1,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,1,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5],
            [1,0,0,0,0,0,0,1,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5],
            [1,0,0,0,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,0,0,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,0,0,0,0,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [3,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],]
        keep_moving=True
        Options=False
        return
    
    if a==2 and Options==False:
        label.destroy()
        label2.destroy()
        label3.destroy()
        canvas.create_image(890,480,image=avatar2,anchor='nw',tag='avatar2')
        label=tk.Label(form,text='只剩20塊 先省起來感覺之後會用到',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)

    if a==3 and Options==False:
        label.destroy()
        canvas.delete('avatar2')
        canvas.delete('dialog_box')
        maze=[
            [1,1,1,1,1,1,1,1,1,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,1,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5],
            [1,0,0,0,0,0,0,1,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5],
            [1,0,0,0,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,0,0,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,0,0,0,0,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [3,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],]
        keep_moving=True
        Options=False
        return

    if key2==13:
        a+=1

    form.after(100,dialogue_11)

def dialogue_run_12():
    _thread.start_new_thread(dialogue_12,()) 

def dialogue_12():
    global x,y,keep_moving
    keep_moving=False
    canvas.create_image(250,543,image=dialog_box,anchor='nw',tag='dialog_box')
    canvas.create_image(890,480,image=avatar2,anchor='nw',tag='avatar2')
    label=tk.Label(form,text='往教室的路不在這裡',font=('俐方體11號',24),bg="#bababa")
    label.place(x=270,y=570)
    time.sleep(1.5)
    label.destroy()
    canvas.delete('avatar2')
    canvas.delete('dialog_box')
    if x==4 and y==31:
        x=4
        canvas.delete('img4')
        canvas.create_image(0,0,image=img3,anchor='nw',tag='img3')
        canvas.coords('img3',y*40,x*40)
    if x==5 and y==31:
        x=5
        canvas.delete('img4')
        canvas.create_image(0,0,image=img3,anchor='nw',tag='img3')
        canvas.coords('img3',y*40,x*40)
    keep_moving=True

def dialogue_run_13():
    _thread.start_new_thread(dialogue_13,()) 

def dialogue_13():
    global keep_moving
    keep_moving=False
    canvas.create_image(250,543,image=dialog_box,anchor='nw',tag='dialog_box')
    canvas.create_image(890,480,image=avatar2,anchor='nw',tag='avatar2')
    label=tk.Label(form,text='先進教室吧 ',font=('俐方體11號',24),bg="#bababa")
    label.place(x=270,y=570)
    time.sleep(1.5) 
    label.destroy()
    canvas.delete('avatar2')
    canvas.delete('dialog_box')
    keep_moving=True

def dialogue_run_14():
    _thread.start_new_thread(dialogue_14,()) 

def dialogue_14():
    global keep_moving,Options
    keep_moving=False
    canvas.create_image(250,543,image=dialog_box,anchor='nw',tag='dialog_box')
    canvas.create_image(890,480,image=avatar2,anchor='nw',tag='avatar2')
    label=tk.Label(form,text='恩？ 今天怎麼這麼只有一個人在教室？',font=('俐方體11號',24),bg="#bababa")
    label.place(x=270,y=570)
    time.sleep(2)
    label.destroy()
    label=tk.Label(form,text='去問問看他好了',font=('俐方體11號',24),bg="#bababa")
    label.place(x=270,y=570)
    time.sleep(1.5)
    label.destroy()
    canvas.delete('avatar2')
    canvas.delete('dialog_box')
    keep_moving=True
    Options=False

def dialogue_15():
    global keep_moving,key2,a,label,label2,maze

    keep_moving=False
    if a==0:
        label.destroy()
        canvas.create_image(250,543,image=dialog_box,anchor='nw',tag='dialog_box')
        canvas.create_image(890,480,image=avatar3,anchor='nw',tag='avatar3')
        label=tk.Label(form,text='？？？：早啊～ 你怎麼今天來學校呢？',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)

    if a==1:
        label.destroy()
        canvas.delete('avatar3')
        canvas.create_image(890,480,image=avatar2,anchor='nw',tag='avatar2')
        label=tk.Label(form,text='欸等等 你是誰？ 為什麼在我們的教室？',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)   

    if a==2:
        label.destroy()
        canvas.delete('avatar2')
        canvas.create_image(890,480,image=avatar3,anchor='nw',tag='avatar3')
        label=tk.Label(form,text='袁子畢：啊不好意思 我叫做袁子畢',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)  

    if a==3:
        label.destroy()
        canvas.delete('avatar3')
        canvas.create_image(890,480,image=avatar2,anchor='nw',tag='avatar2')
        label=tk.Label(form,text='袁子畢你好你好',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)  

    if a==4:
        label.destroy()
        label=tk.Label(form,text='等等 這甚麼鬼名字？？？',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570) 

    if a==5:
        label.destroy()
        canvas.delete('avatar2')
        canvas.create_image(890,480,image=avatar3,anchor='nw',tag='avatar3')
        label=tk.Label(form,text='袁子畢：啊哈哈哈...我爸媽取的',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)  

    if a==6:
        label.destroy()
        label=tk.Label(form,text='袁子畢：哈哈... ... ',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)  

    if a==7:
        label.destroy()
        label=tk.Label(form,text='袁子畢：...',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)  

    if a==8:
        label.destroy()
        canvas.delete('avatar3')
        canvas.create_image(890,480,image=avatar2,anchor='nw',tag='avatar2')
        label=tk.Label(form,text='抱歉...  恩...為什麼其他人都不在？',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)  

    if a==9:
        label.destroy()
        canvas.delete('avatar2')
        canvas.create_image(890,480,image=avatar3,anchor='nw',tag='avatar3')
        label=tk.Label(form,text='袁子畢：你難道不知道今天放颱風假嗎？',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)

    if a==10:
        label.destroy()
        canvas.delete('avatar3')
        canvas.create_image(890,480,image=avatar2,anchor='nw',tag='avatar2')
        label=tk.Label(form,text='...',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570) 

    if a==11:
        if label is not None:
            label.destroy()
        if label2 is not None:
            label2.destroy()
        label=tk.Label(form,text='早上忙著的處理胃痛的事然後就衝來學校',font=('俐方體11號',24),bg='#bababa')
        label2=tk.Label(form,text='忘記有颱風來這件事了...',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)
        label2.place(x=270,y=610) 

    if a==12:
        if label is not None:
            label.destroy()
        if label2 is not None:
            label2.destroy()
        canvas.delete('avatar2')
        canvas.create_image(890,480,image=avatar3,anchor='nw',tag='avatar3')
        label=tk.Label(form,text='袁子畢：哈哈沒關係啦 颱風下午才會來',font=('俐方體11號',24),bg='#bababa')
        label2=tk.Label(form,text='不過還是建議你早點回家比較好喔~',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)
        label2.place(x=270,y=610) 
        
    if a==13:
        label.destroy()
        label2.destroy()
        canvas.delete('avatar3')
        canvas.create_image(890,480,image=avatar2,anchor='nw',tag='avatar2')
        label=tk.Label(form,text='好喔',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)

    if a==14:
        label.destroy()
        label=tk.Label(form,text='那你來學校要幹嘛？',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)

    if a==15:
        if label is not None:
            label.destroy()
        if label2 is not None:
            label2.destroy()
        canvas.delete('avatar2')
        canvas.create_image(890,480,image=avatar3,anchor='nw',tag='avatar3')
        label=tk.Label(form,text='袁子畢：喔～我回來學校拿會計作業',font=('俐方體11號',24),bg='#bababa')
        label2=tk.Label(form,text='昨天忘記拿回家了',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)
        label2.place(x=270,y=610)

    if a==16:
        label.destroy()
        label2.destroy()
        canvas.delete('avatar3')
        label=tk.Label(form,text='你的胃發出了一聲哀號...',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)

    if a==17:
        label.destroy()
        canvas.create_image(890,480,image=avatar2,anchor='nw',tag='avatar2')
        label=tk.Label(form,text='... 我要去一下廁所',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)

    if a==18:
        label.destroy()
        canvas.delete('avatar2')
        canvas.create_image(890,480,image=avatar3,anchor='nw',tag='avatar3')
        label=tk.Label(form,text='袁子畢：OK 那我班鑰匙先放在講桌上',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)

    if a==19:
        label.destroy()
        label=tk.Label(form,text='袁子畢：等一下要離開的時候記得鎖門喔',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)

    if a==20:
        label.destroy()
        canvas.delete('avatar3')
        canvas.create_image(890,480,image=avatar2,anchor='nw',tag='avatar2')
        label=tk.Label(form,text='好的',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)

    if a==21:
        label.destroy()
        label=tk.Label(form,text='（先去廁所吧）',font=('俐方體11號',24),bg='#bababa')
        label.place(x=270,y=570)


    if a==22:
        label.destroy()
        canvas.delete('avatar2')
        canvas.delete('dialog_box')
        keep_moving=True
        a=-1
        maze=[
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,0,1,1,0,0,1,0,0,1,0,1,1,1,0,0,0,1,1,0,0,0,1,1,1],
            [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1],
            [1,1,1,0,0,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,0,0,0,1,1,1],
            [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1],
            [1,1,1,0,0,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,0,1,0,0,1,1],
            [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1],
            [1,1,0,0,0,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,0,1,0,0,1,1],
            [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
            [1,1,0,0,0,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,0,0,0,0,1,1],
            [1,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
            [1,1,2,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,1,2,0,0,0,0,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],]
        return


    if key2==13:
        a+=1

    form.after(100,dialogue_15)
    
def dialogue_run_16():
    _thread.start_new_thread(dialogue_16,()) 

def dialogue_16():
    global keep_moving
    keep_moving=False
    canvas.create_image(250,543,image=dialog_box,anchor='nw',tag='dialog_box')
    canvas.create_image(890,480,image=avatar2,anchor='nw',tag='avatar2')
    label=tk.Label(form,text='先去問問看那個人',font=('俐方體11號',24),bg="#bababa")
    label.place(x=270,y=570)
    time.sleep(2)
    label.destroy()
    canvas.delete('avatar2')
    canvas.delete('dialog_box')
    keep_moving=True

def dialogue_run_17():
    _thread.start_new_thread(dialogue_17,()) 

def dialogue_17():
    global keep_moving
    keep_moving=False
    canvas.create_image(250,543,image=dialog_box,anchor='nw',tag='dialog_box')
    canvas.create_image(890,480,image=avatar2,anchor='nw',tag='avatar2')
    label=tk.Label(form,text='先去廁所...',font=('俐方體11號',24),bg="#bababa")
    label.place(x=270,y=570)
    time.sleep(2)
    label.destroy()
    canvas.delete('avatar2')
    canvas.delete('dialog_box')
    keep_moving=True

def dialogue_18():
    global keep_moving,a,key2

    if a==0:
        keep_moving=False
        canvas.delete(img_map10)
        canvas.create_image(250,543,image=dialog_box,anchor='nw',tag='dialog_box')
        label=tk.Label(form,text='test',font=('俐方體11號',24),bg="#bababa")
        label.place(x=270,y=570)

    if a==1:
        label.destroy()
        canvas.delete('dialog_box')
    
    if key2==13:
        a+=1


    form.after(100,dialogue_18)






def moving():
    global x,y,key,key2,prex,prey,label,label2,label3,Options,Options2,maze,a,map,keep_moving,premap
    
    if keep_moving==True:
        change_map()
        prex=x
        prey=y

        if premap==map:
            if key=='Up':
                x-=1
                if x<0:x=0
                if maze[x][y]==1:
                    x=prex
                    y=prey
                canvas.delete('img1')
                canvas.delete('img2')
                canvas.delete('img3')
                canvas.delete('img4')
                canvas.create_image(0,0,image=img2,anchor='nw',tag='img2')
                canvas.coords('img2',y*40,x*40)
            if key=='Down':
                x+=1
                if x>17:x=17
                if maze[x][y]==1:
                    x=prex
                    y=prey
                canvas.delete('img1')
                canvas.delete('img2')
                canvas.delete('img3')
                canvas.delete('img4')
                canvas.create_image(0,0,image=img1,anchor='nw',tag='img1')
                canvas.coords('img1',y*40,x*40)
            if key=='Left':
                y-=1
                if y<0:y=0
                if maze[x][y]==1:
                    x=prex
                    y=prey
                canvas.delete('img1')
                canvas.delete('img2')
                canvas.delete('img3')
                canvas.delete('img4')
                canvas.create_image(0,0,image=img3,anchor='nw',tag='img3')
                canvas.coords('img3',y*40,x*40)
            if key=='Right':
                y+=1
                if y>31:y=31

                if maze[x][y]==1:
                    x=prex
                    y=prey
                canvas.delete('img1')
                canvas.delete('img2')
                canvas.delete('img3')
                canvas.delete('img4')
                canvas.create_image(0,0,image=img4,anchor='nw',tag='img4')
                canvas.coords('img4',y*40,x*40)

        elif premap!=map:
            premap=map


    form.after(100,moving)


form=tk.Tk()
form.geometry('1280x720+50+50')
form.resizable(False,False)
form.title('RPG GAME')

canvas=tk.Canvas(width=1280,height=720,bg='black')
canvas.pack()

img_map=tk.PhotoImage(file='C:/Users/yoren/Desktop/RPG GAME/room1.png')
canvas.create_image(0,0,image=img_map,anchor='nw',tag='img_map')
img_map1=tk.PhotoImage(file='C:/Users/yoren/Desktop/RPG GAME/map1.png')
img_map2=tk.PhotoImage(file='C:/Users/yoren/Desktop/RPG GAME/map2.png')
img_map3=tk.PhotoImage(file='C:/Users/yoren/Desktop/RPG GAME/map3.png')
img_map4=tk.PhotoImage(file='C:/Users/yoren/Desktop/RPG GAME/map4.png')
img_map5=tk.PhotoImage(file='C:/Users/yoren/Desktop/RPG GAME/map5.png')
img_map6=tk.PhotoImage(file='C:/Users/yoren/Desktop/RPG GAME/map6.png')
img_map7=tk.PhotoImage(file='C:/Users/yoren/Desktop/RPG GAME/map7.png')
img_map8=tk.PhotoImage(file='C:/Users/yoren/Desktop/RPG GAME/map8.png')
img_map9=tk.PhotoImage(file='C:/Users/yoren/Desktop/RPG GAME/map9.png')
img_map10=tk.PhotoImage(file='C:/Users/yoren/Desktop/RPG GAME/map10.png')


label=tk.Label(form,text='',font=('微軟正黑體',16),bg='white')
label2=tk.Label(form,text='',font=('微軟正黑體',16),bg='white')
label3=tk.Label(form,text='',font=('微軟正黑體',16),bg='white')
label_name=tk.Label(form,text='',font=('微軟正黑體',16),bg='white')



img1=tk.PhotoImage(file='C:/Users/yoren/Desktop/RPG GAME/1-1.png')
img2=tk.PhotoImage(file='C:/Users/yoren/Desktop/RPG GAME/1-2.png')
img3=tk.PhotoImage(file='C:/Users/yoren/Desktop/RPG GAME/1-3.png')
img4=tk.PhotoImage(file='C:/Users/yoren/Desktop/RPG GAME/1-4.png')
img2_1=tk.PhotoImage(file='C:/Users/yoren/Desktop/RPG GAME/2-1.png')
img2_2=tk.PhotoImage(file='C:/Users/yoren/Desktop/RPG GAME/2-2.png')
img2_3=tk.PhotoImage(file='C:/Users/yoren/Desktop/RPG GAME/2-3.png')
img2_4=tk.PhotoImage(file='C:/Users/yoren/Desktop/RPG GAME/2-4.png')
img3_1=tk.PhotoImage(file='C:/Users/yoren/Desktop/RPG GAME/3-1.png')
img3_2=tk.PhotoImage(file='C:/Users/yoren/Desktop/RPG GAME/3-2.png')
img3_3=tk.PhotoImage(file='C:/Users/yoren/Desktop/RPG GAME/3-3.png')
img3_4=tk.PhotoImage(file='C:/Users/yoren/Desktop/RPG GAME/3-4.png')
canvas.create_image(y*40,x*40,image=img1,anchor='nw',tag='img1')

dialog_box=tk.PhotoImage(file='C:/Users/yoren/Desktop/RPG GAME/dialog_box.png')

avatar1=tk.PhotoImage(file='C:/Users/yoren/Desktop/RPG GAME/avatar1.png')
avatar2=tk.PhotoImage(file='C:/Users/yoren/Desktop/RPG GAME/avatar2.png')
avatar3=tk.PhotoImage(file='C:/Users/yoren/Desktop/RPG GAME/avatar3.png')

form.bind('<KeyPress>',key_down)
form.bind('<KeyRelease>',key_up)




#dialogue_run_1()
moving()



form.mainloop()

