# def f(x):
#     return x*x
# r = map(f,[1,2,3,4,5,6,7,8,9])
# list(r)


# 时间模块属性
# timezone:当前时区和UTC时间相差的描述，在没有夏令时的情况下的间隔
# print(time.timezone)
# print(time.altzone)
# print(time.daylight)
# time.time()
# t = time.localtime()
# print(type(t))
# print(t.tm_hour)
# import time
# for i in range(10):
#     print(i)
#     time.sleep(1)



# # 导入tkinter模块下面所有方法
# from tkinter import *
# # 创建一个主窗口
# root = Tk()
# # 是设置最小大小
# root.minsize(300,300)
# # 创建一个button,加入主窗口中
# btn1 = Button(root,text="按钮1")
# btn1.grid(row=0,column=0,columnspan=2,ipadx=30)
# btn2 = Button(root,text="按钮2")
# btn2.grid(row=0,column=2)
# btn3 = Button(root,text="按钮3")
# btn3.grid(row=0,column=3)
# btn4 = Button(root,text="按钮4")
# btn4.grid(row=1,column=0)
# btn5 = Button(root,text="按钮5")
# btn5.grid(row=1,column=1,rowspan=2,ipady=15)
# btn6 = Button(root,text="按钮6")
# btn6.grid(row=1,column=2,columnspan=2,ipadx=30)
# btn7 = Button(root,text="按钮7")
# btn7.grid(row=2,column=0)
# btn8 = Button(root,text="按钮8")
# btn8.grid(row=2,column=2,ipadx=30)
# # 加入消息循环
# root.mainloop()
# from tkinter import *
# root = Tk()
# root.minsize(300,300)
# but1 = Button(root,text='按钮1')
# but1.place(x=0,y=0,height=30)
# but2 = Button(root,text='按钮2')
# but2.place(x=60,y=0,height=30)
# but3 = Button(root,text='按钮3')
# but3.place(x=120,y=0,height=30)
# but4 = Button(root,text='按钮4')
# but4.place(x=0,y=30,height=30)
# but5 = Button(root,text='按钮5')
# but5.place(x=60,y=30,height=30)
# but6 = Button(root,text='按钮6')
# but6.place(x=120,y=30,height=30)
# root.mainloop()
# from tkinter import *
# root = Tk()
# root.minsize(300,300)
# but1 = Button(root,text='按钮1')
# but1.place(relx=0,rely=0,relheight=0.1)
# but2 = Button(root,text='按钮2')
# but2.place(relx=0.2,rely=0,relheight=0.1)
# but3 = Button(root,text='按钮3')
# but3.place(relx=0.4,rely=0,relheight=0.1)
# but4 = Button(root,text='按钮4')
# but4.place(relx=0,rely=0.1,relheight=0.1)
# but5 = Button(root,text='按钮5',font=20,bg="blue")
# but5.place(relx=0.2,rely=0.1,relheight=0.1,relwidth=0.4)
# but6 = Button(root,text='按钮6')
# but6.place()
# root.mainloop()
# from tkinter import *
# root = Tk()
# #定义点击菜单触发的方法
# def hello():
#     print("hello!")
# def open_f():
#     print("正在打开文件")
# #创建总菜单
# menubar = Menu(root,bg="pink")
# # 创建一个下拉菜单，并且加入文件菜单
# filemenu = Menu(menubar)
# #创建下来菜单的选项
# filemenu.add_command(label="Open", command=open_f)
# filemenu.add_command(label="Save", command=hello)
# #创建下拉菜单的分割线
# filemenu.add_separator()
# filemenu.add_command(label="Exit", command=root.quit)
# #将文件菜单作为下拉菜单添加到总菜单中，并且将命名为File
# menubar.add_cascade(label="File", menu=filemenu)
# # 显示总菜单
# root.config(menu=menubar)
# root.mainloop()
# # 导入tkinter模块下面所有方法
# from tkinter import *
# import tkinter.messagebox
# # 创建一个主窗口
# root = Tk()
# # 是设置最小大小
# root.minsize(300,300)
# # 定义一个函数
# def info():
#     resault = tkinter.messagebox.askretrycancel('友情提示','你的机器已超载,请更换机器')
#     print(resault)
# # 创建一个button,加入主窗口中
# btn1 = Button(root,text="显示信息对话框",height=2,bg="#999",command=info)
# btn1.grid(row=0,column=0,columnspan=2,ipadx=30)
# btn2 = Button(root,text="按钮2")
# btn2.grid(row=0,column=2)
# btn3 = Button(root,text="按钮3")
# btn3.grid(row=0,column=3)
# btn4 = Button(root,text="按钮4")
# btn4.grid(row=1,column=0)
# btn5 = Button(root,text="按钮5")
# btn5.grid(row=1,column=1,rowspan=2,ipady=15)
# btn6 = Button(root,text="按钮6")
# btn6.grid(row=1,column=2,columnspan=2,ipadx=30)
# btn7 = Button(root,text="按钮7")
# btn7.grid(row=2,column=0)
# btn8 = Button(root,text="按钮8")
# btn8.grid(row=2,column=2)
# # 加入消息循环
# root.mainloop()
# from tkinter import *
# root=Tk()
# root.minsize(400,400)
# frame1 = Frame(root,bg="red",width=150,height=80)
# btn1 = Button(frame1,text="按钮1").pack()
# label = Label(frame1,text="hhhhhh").pack()
# frame1.pack(side="left")
# frame2 = Frame(root,bg="blue",width=200,height=200)
# label = Label(frame2,text="ooooooo").pack()
# frame2.pack()
# root.mainloop()

# from tkinter import *
# root = Tk()
# root.minsize(300,300)
# def openwindow():
#     resault = Toplevel(bg="yellow",height=100,width=100)
#     resault.title('这是一个新窗口')
#     resault['bg']="red"
#     print(resault)

# btn = Button(root,text="弹出一个新窗口",command=openwindow).pack()
# root.mainloop()







# from turtle import *
# from random import *
# from math import *

# def tree(n, l):
#     pd() # 下笔
#     # 阴影效果
#     t = cos(radians(heading() + 45)) / 8 + 0.25
#     pencolor(t, t, t)
#     pensize(n / 3)
#     forward(l) # 画树枝


#     if n > 0:
#         b = random() * 15 + 10 # 右分支偏转角度
#         c = random() * 15 + 10 # 左分支偏转角度
#         d = l * (random() * 0.25 + 0.7) # 下一个分支的长度
#         # 右转一定角度，画右分支
#         right(b)
#         tree(n - 1, d)
#         # 左转一定角度，画左分支
#         left(b + c)
#         tree(n - 1, d)

#         # 转回来
#         right(c)
#     else:
#         # 画叶子
#         right(90)
#         n = cos(radians(heading() - 45)) / 4 + 0.5
#         pencolor(n, n*0.8, n*0.8)
#         circle(3)
#         left(90)

#         # 添加0.3倍的飘落叶子
#         if(random() > 0.7):
#             # 飘落
#             t = heading()
#             an = -30 + random()*10
#             setheading(an)
#             pu()
#             dis = int(600*random()*0.5 + 300*random()*0.3 + 150*random()*0.2)
#             forward(dis)
#             pd()
#             setheading(t)


#             # 画叶子
#             right(90)
#             n = cos(radians(heading() - 45)) / 4 + 0.5
#             pencolor(n*0.5+0.5, 0.4+n*0.4, 0.4+n*0.4)
#             circle(2)
#             left(90)

#             #返回
#             t = heading()
#             setheading(an)
#             pu()
#             backward(dis)
#             pd()
#             setheading(t)

#     pu() # 抬笔
#     backward(l)# 退回

# bgcolor(0.5, 0.5, 0.5) # 背景色
# ht() # 隐藏turtle
# speed(0) # 速度，1-10渐进，0最快
# tracer(20000, 0)
# pu() # 抬笔
# backward(100)
# left(90) # 左转90度
# pu() # 抬笔
# backward(300) # 后退300
# tree(12, 100) # 递归7层
# done()





# 作者：杨航锋
# 链接：https://www.zhihu.com/question/271643290/answer/362608527
# 来源：知乎
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。








# import turtle
# import random
# from turtle import *
# from time import sleep

# t = turtle.Turtle()
# w = turtle.Screen()


# def tree(branchLen, t):
#     if branchLen > 3:
#         if 8 <= branchLen <= 12:
#             if random.randint(0, 2) == 0:
#                 t.color('snow')
#             else:
#                 t.color('lightcoral')
#             t.pensize(branchLen / 3)
#         elif branchLen < 8:
#             if random.randint(0, 1) == 0:
#                 t.color('snow')
#             else:
#                 t.color('lightcoral')
#             t.pensize(branchLen / 2)
#         else:
#             t.color('sienna')
#             t.pensize(branchLen / 10)

#         t.forward(branchLen)
#         a = 1.5 * random.random()
#         t.right(20*a)
#         b = 1.5 * random.random()
#         tree(branchLen-10*b, t)
#         t.left(40*a)
#         tree(branchLen-10*b, t)
#         t.right(20*a)
#         t.up()
#         t.backward(branchLen)
#         t.down()


# def petal(m, t):  # 树下花瓣
#     for i in range(m):
#         a = 200 - 400 * random.random()
#         b = 10 - 20 * random.random()
#         t.up()
#         t.forward(b)
#         t.left(90)
#         t.forward(a)
#         t.down()
#         t.color("lightcoral")
#         t.circle(1)
#         t.up()
#         t.backward(a)
#         t.right(90)
#         t.backward(b)


# def main():
#     t = turtle.Turtle()
#     myWin = turtle.Screen()
#     getscreen().tracer(5, 0)
#     turtle.screensize(bg='wheat')
#     t.left(90)
#     t.up()
#     t.backward(150)
#     t.down()
#     t.color('sienna')
#     tree(60, t)
#     petal(100, t)

#     myWin.exitonclick()


# main()


import math
for i in range(10000):
    x = int(math.sqrt(i + 100))
    y = int(math.sqrt(i + 268))
    if(x * x == i + 100)and((y * y == i + 100):
        print(i)


