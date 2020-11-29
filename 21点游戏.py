import tkinter #导入tkinter库
import tkinter.messagebox #导入弹窗库
import random #乱序牌堆用

def jieguo(c,zhuang): #比较点数和，显示游戏结果
    #弹出一个显示结果的窗口
    jieguo=tkinter.Tk() #建立窗口显示游戏结果
    jieguo.title('游戏结果') #给窗口起名字
    jieguo.geometry('600x400') #设定窗口的大小
    h0=tkinter.Label(jieguo,text='游戏结果',bg='red',font=30,width=15,height=3)
    h0.pack()
    
    #对比点数和并显示结果，如果玩家点数和为0，就说明他没玩
    if c[0]!=0: #如果点数和不是0，就说明他玩了，给他放一个位置
        h1=tkinter.Label(jieguo,text='玩家1：',font=30,width=6,height=2).place(x=60,y=80)
    if c[0]!=0 and zhuang>c[0]: #庄家点数大
        k1=tkinter.Label(jieguo,text='输了',bg='red',font=30,width=10,height=2).place(x=120,y=80)
    if c[0]!=0 and zhuang<c[0]: #玩家点数大
        k1=tkinter.Label(jieguo,text='赢了',bg='green',font=30,width=10,height=2).place(x=120,y=80)
    if zhuang==c[0]: #两个点数相同
        k1=tkinter.Label(jieguo,text='平局',font=30,width=10,height=2).place(x=120,y=80)
    if zhuang==c[0]==-1: #意味着玩家庄家都爆牌
        k1=tkinter.Label(jieguo,text='输了',bg='red',font=30,width=10,height=2).place(x=120,y=80)

    if c[1]!=0:
        h2=tkinter.Label(jieguo,text='玩家2：',font=30,width=6,height=2).place(x=360,y=80)
    if c[1]!=0 and zhuang>c[1]: #庄家点数大
        k2=tkinter.Label(jieguo,text='输了',bg='red',font=30,width=10,height=2).place(x=420,y=80)
    if c[1]!=0 and zhuang<c[1]: #玩家点数大
        k2=tkinter.Label(jieguo,text='赢了',bg='green',font=30,width=10,height=2).place(x=420,y=80)
    if zhuang==c[1]: #两个点数相同
        k2=tkinter.Label(jieguo,text='平局',font=30,width=10,height=2).place(x=420,y=80)
    if zhuang==c[1]==-1: #意味着玩家庄家都爆牌
        k2=tkinter.Label(jieguo,text='输了',bg='red',font=30,width=10,height=2).place(x=420,y=80)

    if c[2]!=0:
        h3=tkinter.Label(jieguo,text='玩家3：',font=30,width=6,height=2).place(x=60,y=140)
    if c[2]!=0 and zhuang>c[2]: #庄家点数大
        k3=tkinter.Label(jieguo,text='输了',bg='red',font=30,width=10,height=2).place(x=120,y=140)
    if c[2]!=0 and zhuang<c[2]: #玩家点数大
        k3=tkinter.Label(jieguo,text='赢了',bg='green',font=30,width=10,height=2).place(x=120,y=140)
    if zhuang==c[2]: #两个点数相同
        k3=tkinter.Label(jieguo,text='平局',font=30,width=10,height=2).place(x=120,y=140)
    if zhuang==c[2]==-1: #意味着玩家庄家都爆牌
        k3=tkinter.Label(jieguo,text='输了',bg='red',font=30,width=10,height=2).place(x=120,y=140)

    if c[3]!=0:
        h4=tkinter.Label(jieguo,text='玩家4：',font=30,width=6,height=2).place(x=360,y=140)
    if c[3]!=0 and zhuang>c[3]: #庄家点数大
        k4=tkinter.Label(jieguo,text='输了',bg='red',font=30,width=10,height=2).place(x=420,y=140)
    if c[3]!=0 and zhuang<c[3]: #玩家点数大
        k4=tkinter.Label(jieguo,text='赢了',bg='green',font=30,width=10,height=2).place(x=420,y=140)
    if zhuang==c[3]: #两个点数相同
        k4=tkinter.Label(jieguo,text='平局',font=30,width=10,height=2).place(x=420,y=140)
    if zhuang==c[3]==-1: #意味着玩家庄家都爆牌
        k4=tkinter.Label(jieguo,text='输了',bg='red',font=30,width=10,height=2).place(x=420,y=140)

    if c[4]!=0:
        h5=tkinter.Label(jieguo,text='玩家5：',font=30,width=6,height=2).place(x=60,y=200)
    if c[4]!=0 and zhuang>c[4]: #庄家点数大
        k5=tkinter.Label(jieguo,text='输了',bg='red',font=30,width=10,height=2).place(x=120,y=200)
    if c[4]!=0 and zhuang<c[4]: #玩家点数大
        k5=tkinter.Label(jieguo,text='赢了',bg='green',font=30,width=10,height=2).place(x=120,y=200)
    if zhuang==c[4]: #两个点数相同
        k5=tkinter.Label(jieguo,text='平局',font=30,width=10,height=2).place(x=120,y=200)
    if zhuang==c[4]==-1: #意味着玩家庄家都爆牌
        k5=tkinter.Label(jieguo,text='输了',bg='red',font=30,width=10,height=2).place(x=120,y=200)
        
    if c[5]!=0:
        h6=tkinter.Label(jieguo,text='玩家6：',font=30,width=6,height=2).place(x=360,y=200)
    if c[5]!=0 and zhuang>c[5]: #庄家点数大
        k6=tkinter.Label(jieguo,text='输了',bg='red',font=30,width=10,height=2).place(x=420,y=200)
    if c[5]!=0 and zhuang<c[5]: #玩家点数大
        k6=tkinter.Label(jieguo,text='赢了',bg='green',font=30,width=10,height=2).place(x=420,y=200)
    if zhuang==c[5]: #两个点数相同
        k6=tkinter.Label(jieguo,text='平局',font=30,width=10,height=2).place(x=420,y=200)
    if zhuang==c[5]==-1: #意味着玩家庄家都爆牌
        k6=tkinter.Label(jieguo,text='输了',bg='red',font=30,width=10,height=2).place(x=420,y=200)
        
    if c[6]!=0:
        h7=tkinter.Label(jieguo,text='玩家7：',font=30,width=6,height=2).place(x=60,y=260)
    if c[6]!=0 and zhuang>c[6]: #庄家点数大
        k7=tkinter.Label(jieguo,text='输了',bg='red',font=30,width=10,height=2).place(x=120,y=260)
    if c[6]!=0 and zhuang<c[6]: #玩家点数大
        k7=tkinter.Label(jieguo,text='赢了',bg='green',font=30,width=10,height=2).place(x=120,y=260)
    if zhuang==c[6]: #两个点数相同
        k7=tkinter.Label(jieguo,text='平局',font=30,width=10,height=2).place(x=120,y=260)
    if zhuang==c[6]==-1: #意味着玩家庄家都爆牌
        k7=tkinter.Label(jieguo,text='输了',bg='red',font=30,width=10,height=2).place(x=120,y=260)
        
    g17=tkinter.Button(window,font=30,width=15,height=2).place(x=420,y=450) #下方按钮
    g18=tkinter.Button(window,font=30,width=15,height=2).place(x=620,y=450)
 
    jieguo.mainloop() #循环显示

def pai(a): #把牌换算成点数
    if a=='♠2' or a=='♥2' or a=='♦2' or a=='♣2':
        return 2
    if a=='♠3' or a=='♥3' or a=='♦3' or a=='♣3':
        return 3
    if a=='♠4' or a=='♥4' or a=='♦4' or a=='♣4':
        return 4
    if a=='♠5' or a=='♥5' or a=='♦5' or a=='♣5':
        return 5
    if a=='♠6' or a=='♥6' or a=='♦6' or a=='♣6':
        return 6
    if a=='♠7' or a=='♥7' or a=='♦7' or a=='♣7':
        return 7
    if a=='♠8' or a=='♥8' or a=='♦8' or a=='♣8':
        return 8
    if a=='♠9' or a=='♥9' or a=='♦9' or a=='♣9':
        return 9
    if a=='♠10' or a=='♥10' or a=='♦10' or a=='♣10' or a=='♠J' or a=='♥J' or a=='♦J' or a=='♣J' or a=='♠Q' or a=='♥Q' or a=='♦Q' or a=='♣Q' or a=='♠K' or a=='♥K' or a=='♦K' or a=='♣K':
        return 10
    if a=='♠A' or a=='♥A' or a=='♦A' or a=='♣A': #A先按11
        return 11
    
def jisuan(a1,count): #用于计算点数和
    count=count+pai(a1)
    if a1=='♠A' or a1=='♥A' or a1=='♦A' or a1=='♣A':
        if count>21:
            count=count-10 #相当于把A从11改成了1
    if count>21: #如果大于21，就说明爆牌了
        count=-1 #爆牌的一律改成-1
    return count

def zhuangmo(c,z,x,zhuang): #最后庄家来摸牌
    for i in range(2,8):
        if zhuang>=17: #如果起始就大于17，直接就不拿牌
            break
        z.append(x[0]) #给庄家发牌
        del x[0]
        a1=z[i]
        zhuang=jisuan(a1,zhuang)
        if zhuang>=17 or zhuang==-1: #如果大于17，下次拿牌就有很大几率爆牌，就别拿了
            break
    d80.set(z) #显示庄家的牌
    if zhuang==-1: #爆牌了
        f80.set('爆牌了')
    else:
        f80.set(zhuang) #显示庄家的点数和
    jieguo(c,zhuang) #去显示结果

def mo1(b,c,x,z,zhuang): #拿牌
    b[0].append(x[0])
    a1=x[0] #算点数和
    del x[0]
    c[0]=jisuan(a1,c[0])
    d10.set(b[0]) #输出到标签
    f10.set(c[0])
    if c[0]==-1: #就说明爆牌了
        f10.set('爆牌了')
        mopai2(b,c,x,z,zhuang) #结束此玩家的摸牌
    if c[0]==21: #如果凑够了21点
        mopai2(b,c,x,z,zhuang) #结束此玩家的摸牌
def mopai1(b,c,x,z,zhuang): #摸牌，b是玩家牌，c是点数和，x是牌堆
    g10.set('*玩家 1 选择*')
    g2=tkinter.Button(window,text='[ 拿牌 ]',font=30,width=15,height=2,command=lambda:mo1(b,c,x,z,zhuang)).place(x=420,y=450) #下方按钮
    g3=tkinter.Button(window,text='[ 不拿牌 ]',font=30,width=15,height=2,command=lambda:mopai2(b,c,x,z,zhuang)).place(x=620,y=450)

def mo2(b,c,x,z,zhuang): #拿牌
    b[1].append(x[0])
    a1=x[0] #算点数和
    del x[0]
    c[1]=jisuan(a1,c[1])
    d20.set(b[1]) #输出到标签
    f20.set(c[1])
    if c[1]==-1: #就说明爆牌了
        f20.set('爆牌了')
        mopai3(b,c,x,z,zhuang) #结束此玩家的摸牌
    if c[1]==21: #如果凑够了21点
        mopai3(b,c,x,z,zhuang) #结束此玩家的摸牌
def mopai2(b,c,x,z,zhuang): #玩家2摸牌
    if c[1]==0: #如果这个玩家没参加，就跳到庄家摸牌
        zhuangmo(c,z,x,zhuang)
    else:
        g10.set('*玩家 2 选择*')
        g4=tkinter.Button(window,text='[ 拿牌 ]',font=30,width=15,height=2,command=lambda:mo2(b,c,x,z,zhuang)).place(x=420,y=450) #下方按钮
        g5=tkinter.Button(window,text='[ 不拿牌 ]',font=30,width=15,height=2,command=lambda:mopai3(b,c,x,z,zhuang)).place(x=620,y=450)

def mo3(b,c,x,z,zhuang): #拿牌
    b[2].append(x[0])
    a1=x[0] #算点数和
    del x[0]
    c[2]=jisuan(a1,c[2])
    d30.set(b[2]) #输出到标签
    f30.set(c[2])
    if c[2]==-1: #就说明爆牌了
        f30.set('爆牌了')
        mopai4(b,c,x,z,zhuang) #结束此玩家的摸牌
    if c[2]==21: #如果凑够了21点
        mopai4(b,c,x,z,zhuang) #结束此玩家的摸牌
def mopai3(b,c,x,z,zhuang): #玩家3摸牌
    if c[2]==0: #如果这个玩家没参加，就跳到庄家摸牌
        zhuangmo(c,z,x,zhuang)
    else:
        g10.set('*玩家 3 选择*')
        g6=tkinter.Button(window,text='[ 拿牌 ]',font=30,width=15,height=2,command=lambda:mo3(b,c,x,z,zhuang)).place(x=420,y=450) #下方按钮
        g7=tkinter.Button(window,text='[ 不拿牌 ]',font=30,width=15,height=2,command=lambda:mopai4(b,c,x,z,zhuang)).place(x=620,y=450)

def mo4(b,c,x,z,zhuang): #拿牌
    b[3].append(x[0])
    a1=x[0] #算点数和
    del x[0]
    c[3]=jisuan(a1,c[3])
    d40.set(b[3]) #输出到标签
    f40.set(c[3])
    if c[3]==-1: #就说明爆牌了
        f40.set('爆牌了')
        mopai5(b,c,x,z,zhuang) #结束此玩家的摸牌
    if c[3]==21: #如果凑够了21点
        mopai5(b,c,x,z,zhuang) #结束此玩家的摸牌
def mopai4(b,c,x,z,zhuang): #玩家4摸牌
    if c[3]==0: #如果这个玩家没参加，就跳到庄家摸牌
        zhuangmo(c,z,x,zhuang)
    else:
        g10.set('*玩家 4 选择*')
        g8=tkinter.Button(window,text='[ 拿牌 ]',font=30,width=15,height=2,command=lambda:mo4(b,c,x,z,zhuang)).place(x=420,y=450) #下方按钮
        g9=tkinter.Button(window,text='[ 不拿牌 ]',font=30,width=15,height=2,command=lambda:mopai5(b,c,x,z,zhuang)).place(x=620,y=450)

def mo5(b,c,x,z,zhuang): #拿牌
    b[4].append(x[0])
    a1=x[0] #算点数和
    del x[0]
    c[4]=jisuan(a1,c[4])
    d50.set(b[4]) #输出到标签
    f50.set(c[4])
    if c[4]==-1: #就说明爆牌了
        f50.set('爆牌了')
        mopai6(b,c,x,z,zhuang) #结束此玩家的摸牌
    if c[4]==21: #如果凑够了21点
        mopai6(b,c,x,z,zhuang) #结束此玩家的摸牌
def mopai5(b,c,x,z,zhuang): #玩家5摸牌
    if c[4]==0: #如果这个玩家没参加，就跳到庄家摸牌
        zhuangmo(c,z,x,zhuang)
    else:
        g10.set('*玩家 5 选择*')
        g11=tkinter.Button(window,text='[ 拿牌 ]',font=30,width=15,height=2,command=lambda:mo5(b,c,x,z,zhuang)).place(x=420,y=450) #下方按钮
        g12=tkinter.Button(window,text='[ 不拿牌 ]',font=30,width=15,height=2,command=lambda:mopai6(b,c,x,z,zhuang)).place(x=620,y=450)

def mo6(b,c,x,z,zhuang): #拿牌
    b[5].append(x[0])
    a1=x[0] #算点数和
    del x[0]
    c[5]=jisuan(a1,c[5])
    d60.set(b[5]) #输出到标签
    f60.set(c[5])
    if c[5]==-1: #如果大于21，就说明爆牌了
        f60.set('爆牌了')
        mopai7(b,c,x,z,zhuang) #结束此玩家的摸牌
    if c[5]==21: #如果凑够了21点
        mopai7(b,c,x,z,zhuang) #结束此玩家的摸牌
def mopai6(b,c,x,z,zhuang): #玩家6摸牌
    if c[5]==0: #如果这个玩家没参加，就跳到庄家摸牌
        zhuangmo(c,z,x,zhuang)
    else:
        g10.set('*玩家 6 选择*')
        g13=tkinter.Button(window,text='[ 拿牌 ]',font=30,width=15,height=2,command=lambda:mo6(b,c,x,z,zhuang)).place(x=420,y=450) #下方按钮
        g14=tkinter.Button(window,text='[ 不拿牌 ]',font=30,width=15,height=2,command=lambda:mopai7(b,c,x,z,zhuang)).place(x=620,y=450)

def mo7(b,c,x,z,zhuang): #拿牌
    b[6].append(x[0])
    a1=x[0] #算点数和
    del x[0]
    c[6]=jisuan(a1,c[6])
    d70.set(b[6]) #输出到标签
    f70.set(c[6])
    if c[6]==-1: #就说明爆牌了
        f70.set('爆牌了')
        zhuangmo(c,z,x,zhuang) #跳到庄家摸牌
    if c[6]==21: #如果凑够了21点
        zhuangmo(c,z,x,zhuang) #跳到庄家摸牌
def mopai7(b,c,x,z,zhuang): #玩家7摸牌
    if c[6]==0: #如果这个玩家没参加，就跳到庄家摸牌
        zhuangmo(c,z,x,zhuang)
    else:
        g10.set('*玩家7 选择*')
        g15=tkinter.Button(window,text='[ 拿牌 ]',font=30,width=15,height=2,command=lambda:mo7(b,c,x,z,zhuang)).place(x=420,y=450) #下方按钮
        g16=tkinter.Button(window,text='[ 不拿牌 ]',font=30,width=15,height=2,command=lambda:zhuangmo(c,z,x,zhuang)).place(x=620,y=450)
      
def chushi(a): #起始每人分两张牌
    b=[[],[],[],[],[],[],[],[]] #用来储存牌
    c=[0,0,0,0,0,0,0] #用来储存点数和
    x1=['♠A','♠2','♠3','♠4','♠5','♠6','♠7','♠8','♠9','♠10','♠J','♠Q','♠K']
    x2=['♥A','♥2','♥3','♥4','♥5','♥6','♥7','♥8','♥9','♥10','♥J','♥Q','♥K']
    x3=['♦A','♦2','♦3','♦4','♦5','♦6','♦7','♦8','♦9','♦10','♦J','♦Q','♦K']
    x4=['♣A','♣2','♣3','♣4','♣5','♣6','♣7','♣8','♣9','♣10','♣J','♣Q','♣K']
    x=x1+x2+x3+x4
    random.shuffle(x) #将牌堆乱序
    z=[] #储存庄家的牌
    zhuang=0 #庄家点数和
    for i in range(2):
        z.append(x[0]) #给庄家发牌
        del x[0]
    d80.set(z) #显示庄家的牌
    for i in range(2): #算点数和
        zhuang=zhuang+pai(z[i]) #庄家的点数和
    if zhuang==22: #假如正巧摸到了两张A，那一张A就按1
        zhuang=12
    f80.set(zhuang) #显示庄家的点数和
    if zhuang==21: #如果庄家拿到21，就弹窗
        tkinter.messagebox.showinfo(title='提示',message='庄家拿到了21点！')
    for i in range(a): #给每个玩家发牌
        b[i].append(x[0])
        del x[0]
        b[i].append(x[0])
        del x[0]
    for i in range(a):
        a1,a2=b[i][0],b[i][1] #算点数和
        a1=pai(a1)
        a2=pai(a2)
        count=a1+a2
        if count==22: #假如正巧摸到了两张A，那一张A就按1
            count=12
        c[i]=count
    #输出到标签，标签显示每个玩家的牌以及点数和
    d10.set(b[0])
    f10.set(c[0])
    d20.set(b[1])
    f20.set(c[1])
    d30.set(b[2])
    f30.set(c[2])
    d40.set(b[3])
    f40.set(c[3])
    d50.set(b[4])
    f50.set(c[4])
    d60.set(b[5])
    f60.set(c[5])
    d70.set(b[6])
    f70.set(c[6])
    mopai1(b,c,x,z,zhuang) #第一个玩家开始摸牌
    
def p1(): #选完玩家人数之后
    chushi(1) #给分牌函数传递玩家人数
def p2():
    chushi(2)
def p3():
    chushi(3)
def p4():
    chushi(4)
def p5():
    chushi(5)
def p6():
    chushi(6)
def p7():
    chushi(7)

window=tkinter.Tk() #建立窗口window
window.title('21点游戏') #给窗口起名字
window.geometry('1200x600')  #设定窗口的大小
a1=tkinter.Label(window,text='21点游戏',bg='green',font=15,width=30,height=2) #设定一个标签
#bg为背景，font为字大小，width为长，height为高
a1.pack() #放置标签
a2=tkinter.Label(window,text='选择玩家人数：',font=15,width=30,height=2).place(x=150,y=35) #放标签

#每个玩家的标签框放置
d10=tkinter.StringVar() #保证标签内容的变更可以显示到页面上
f10=tkinter.StringVar()
c1=tkinter.Label(window,text='玩家1：',bg='green',font=30,width=6,height=2).place(x=20,y=100) #放标签
d1=tkinter.Label(window,textvariable=d10,bg='yellow',font=30,width=20,height=2).place(x=100,y=100)
e1=tkinter.Label(window,text='点数和:',font=30,width=8,height=2).place(x=280,y=100)
f1=tkinter.Label(window,textvariable=f10,font=30,width=6,height=2).place(x=350,y=100)

d20=tkinter.StringVar() #保证标签内容的变更可以显示到页面上
f20=tkinter.StringVar()
c2=tkinter.Label(window,text='玩家2：',bg='green',font=30,width=6,height=2).place(x=20,y=200) #放标签
d2=tkinter.Label(window,textvariable=d20,bg='yellow',font=30,width=20,height=2).place(x=100,y=200)
e2=tkinter.Label(window,text='点数和:',font=30,width=8,height=2).place(x=280,y=200)
f2=tkinter.Label(window,textvariable=f20,font=30,width=6,height=2).place(x=350,y=200)

d30=tkinter.StringVar() #保证标签内容的变更可以显示到页面上
f30=tkinter.StringVar()
c3=tkinter.Label(window,text='玩家3：',bg='green',font=30,width=6,height=2).place(x=20,y=300) #放标签
d3=tkinter.Label(window,textvariable=d30,bg='yellow',font=30,width=20,height=2).place(x=100,y=300)
e3=tkinter.Label(window,text='点数和:',font=30,width=8,height=2).place(x=280,y=300)
f3=tkinter.Label(window,textvariable=f30,font=30,width=6,height=2).place(x=350,y=300)

d40=tkinter.StringVar() #保证标签内容的变更可以显示到页面上
f40=tkinter.StringVar()
c4=tkinter.Label(window,text='玩家4：',bg='green',font=30,width=6,height=2).place(x=420,y=300) #放标签
d4=tkinter.Label(window,textvariable=d40,bg='yellow',font=30,width=20,height=2).place(x=500,y=300)
e4=tkinter.Label(window,text='点数和:',font=30,width=8,height=2).place(x=680,y=300)
f4=tkinter.Label(window,textvariable=f40,font=30,width=6,height=2).place(x=750,y=300)

d50=tkinter.StringVar() #保证标签内容的变更可以显示到页面上
f50=tkinter.StringVar()
c5=tkinter.Label(window,text='玩家5：',bg='green',font=30,width=6,height=2).place(x=820,y=300) #放标签
d5=tkinter.Label(window,textvariable=d50,bg='yellow',font=30,width=20,height=2).place(x=900,y=300)
e5=tkinter.Label(window,text='点数和:',font=30,width=8,height=2).place(x=1080,y=300)
f5=tkinter.Label(window,textvariable=f50,font=30,width=6,height=2).place(x=1150,y=300)

d60=tkinter.StringVar() #保证标签内容的变更可以显示到页面上
f60=tkinter.StringVar()
c6=tkinter.Label(window,text='玩家6：',bg='green',font=30,width=6,height=2).place(x=820,y=200) #放标签
d6=tkinter.Label(window,textvariable=d60,bg='yellow',font=30,width=20,height=2).place(x=900,y=200)
e6=tkinter.Label(window,text='点数和:',font=30,width=8,height=2).place(x=1080,y=200)
f6=tkinter.Label(window,textvariable=f60,font=30,width=6,height=2).place(x=1150,y=200)

d70=tkinter.StringVar() #保证标签内容的变更可以显示到页面上
f70=tkinter.StringVar()
c7=tkinter.Label(window,text='玩家7：',bg='green',font=30,width=6,height=2).place(x=820,y=100) #放标签
d7=tkinter.Label(window,textvariable=d70,bg='yellow',font=30,width=20,height=2).place(x=900,y=100)
e7=tkinter.Label(window,text='点数和:',font=30,width=8,height=2).place(x=1080,y=100)
f7=tkinter.Label(window,textvariable=f70,font=30,width=6,height=2).place(x=1150,y=100)

d80=tkinter.StringVar() #保证标签内容的变更可以显示到页面上
f80=tkinter.StringVar()
c8=tkinter.Label(window,text='庄家',bg='red',font=50,width=10,height=2).place(x=540,y=100) #放庄家标签
d8=tkinter.Label(window,textvariable=d80,bg='yellow',font=30,width=20,height=2).place(x=500,y=150)
e8=tkinter.Label(window,text='点数和:',font=30,width=8,height=2).place(x=520,y=200)
f8=tkinter.Label(window,textvariable=f80,font=30,width=6,height=2).place(x=590,y=200)

g10=tkinter.StringVar() #保证标签内容的变更可以显示到页面上
g1=tkinter.Label(window,textvariable=g10,font=30,width=15,height=2).place(x=520,y=380) #下方按钮标签

b1=tkinter.Radiobutton(window,text=('1个'),value=1,command=p1).place(x=400,y=40) #选择玩家数,放置
b2=tkinter.Radiobutton(window,text=('2个'),value=2,command=p2).place(x=500,y=40)
b3=tkinter.Radiobutton(window,text=('3个'),value=3,command=p3).place(x=600,y=40)
b4=tkinter.Radiobutton(window,text=('4个'),value=4,command=p4).place(x=700,y=40)
b5=tkinter.Radiobutton(window,text=('5个'),value=5,command=p5).place(x=800,y=40)
b6=tkinter.Radiobutton(window,text=('6个'),value=6,command=p6).place(x=900,y=40)
b7=tkinter.Radiobutton(window,text=('7个'),value=7,command=p7).place(x=1000,y=40)

window.mainloop() #循环显示

