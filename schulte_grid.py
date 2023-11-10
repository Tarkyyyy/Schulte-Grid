import random
import time
from tkinter import*

#控制台测试代码
# cunt = 0
# for i in range(25):
#     print(main_list[i],end="\t")
#     cunt += 1
#     if cunt % 5 == 0:
#         print()

root = Tk()
root.geometry('300x200')
root.title('Schulte Grid_司马万轶')
def clicked(n):     #点击按钮事件
    global sttime
    global edtime
    if n == 0:
        sttime = time.time()
        # print(sttime)
    elif n == 24:
        edtime = time.time()
        # print(edtime-sttime)
        lab.config(text= round(edtime-sttime,3))       #刷新text显示时间
    buttonlist[n].config(bg= "grey",fg = "white")
    return 0

#随机打乱列表
main_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
random.shuffle(main_list)

buttonlist = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    #储存按钮信息
for i in range(25):     #放置按钮
    buttonlist[i] = Button(root, text=main_list[i],command=lambda n=main_list[i]-1:clicked(n),width=5)
    buttonlist[i].grid(column=i%5+1,row= i//5)
lab = Label(root,text="none")
lab.grid(column=6)
root.mainloop()

    