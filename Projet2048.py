import random
from random import randint
from tkinter import *
import math as m
import copy

def gauche (M):
    Bo=False
    for i in range (4):
        v=0
        p=0
        for j in range (4):
            if M[i][j]!=0:
                if p!=j:
                    if M[i][j]==v:
                        M[i][p-1]=2*v
                        v=2*v
                    else:
                        M[i][p]=M[i][j]
                        p=p+1
                        v=M[i][j]
                    M[i][j]=0
                    Bo=True
                elif M[i][j]==v:
                    M[i][j-1]=2*v
                    M[i][j]=0
                    v=2*v
                    Bo=True
                else:
                    p=p+1
                    v=M[i][j]
    return(Bo)

def droite (M):
    Bo=False
    for i in range (4):
        v=0
        p=3
        for j in range (4):
            if M[i][3-j]!=0:
                if p!=(3-j):
                    if M[i][(3-j)]==v:
                        M[i][p+1]=2*v
                        v=2*v
                    else:
                        M[i][p]=M[i][(3-j)]
                        p=p-1
                        v=M[i][(3-j)]
                    M[i][(3-j)]=0
                    Bo=True
                elif M[i][(3-j)]==v:
                    M[i][(4-j)]=2*v
                    M[i][3-j]=0
                    v=2*v
                    Bo=True
                else:
                    p=p-1
                    v=M[i][(3-j)]
    return(Bo)

def haut(M):
    Bo=False
    for j in range (4):
        v=0
        p=0
        for i in range (4):
            if M[i][j]!=0:
                if p!=i:
                    if M[i][j]==v:
                        M[p-1][j]=2*v
                        v=2*v
                    else:
                        M[p][j]=M[i][j]
                        p=p+1
                        v=M[i][j]
                    M[i][j]=0
                    Bo=True
                elif M[i][j]==v:
                    M[i-1][j]=2*v
                    M[i][j]=0
                    v=2*v
                    Bo=True
                else:
                    p=p+1
                    v=M[i][j]
    return(Bo)

def bas(M):
    Bo=False
    for j in range (4):
        v=0
        p=3
        for i in range (4):
            if M[3-i][j]!=0:
                if p!=(3-i):
                    if M[3-i][j]==v:
                        M[p+1][j]=2*v
                        v=2*v
                    else:
                        M[p][j]=M[3-i][j]
                        p=p-1
                        v=M[3-i][j]
                    M[3-i][j]=0
                    Bo=True
                elif M[3-i][j]==v:
                    M[4-i][j]=2*v
                    M[3-i][j]=0
                    v=2*v
                    Bo=True
                else:
                    p=p-1
                    v=M[3-i][j]
    return(Bo)

def rajout(M):
    l=[]
    for i in range (4):
        for j in range (4):
            if M[i][j]==0:
                l.append([i,j])
    n=len(l)
    a=random.randint(1,n)
    b=random.randint(1,2)
    M[l[a-1][0]][l[a-1][1]]=2*b
    
def score(M):
    s=0
    for i in range (4):
        for j in range (4):
            if M[i][j]!=0:
                s=s+(m.log(M[i][j],2))*M[i][j]
    return(s)

def paspossible(M):
    if not(bas(M)):
        if not(gauche(M)):
            if not(droite(M)):
                if not(haut(M)):
                    return(True)
    return(False)
    
 def explore(M):
    rajout(M)
    while not(paspossible(copy.deepcopy(M))):
        joue=True
        while joue:
            joue=False
            r=random.randint(1,4)
            if r==1:
                if not(bas(M)):
                    joue=True
            if r==2:
                if not(haut(M)):
                    joue=True
            if r==3:
                if not(gauche(M)):
                    joue=True
            if r==4:
                if not(droite(M)):
                    joue=True
        rajout(M)
    return(score(M))

def choixcoup(M,n):
    s1=0
    s2=0
    s3=0
    s4=0
    v=1
    s=0
    if bas(copy.deepcopy(M)):
        for i in range (n):
            B=copy.deepcopy(M)
            b=bas(B)
            s1=s1+explore(B)
    s=s1
    if haut(copy.deepcopy(M)):
        for i in range (n):
            B=copy.deepcopy(M)
            b=haut(B)
            s2=s2+explore(B)
    if s2>s:
        v=2
        s=s2
    if gauche(copy.deepcopy(M)):
        for i in range (n):
            B=copy.deepcopy(M)
            b=gauche(B)
            s3=s3+explore(B)
    if s3>s:
        v=3
        s=s3
    if droite(copy.deepcopy(M)):
        for i in range (n):
            B=copy.deepcopy(M)
            b=droite(B)
            s4=s4+explore(B)
    if s4>s:
        v=4
    return(v)
    
def Carlo (n):
    F = Tk()
    F.title("2048")
    C=Canvas(F, width=400, height=400)
    C.pack()
    M=[[0 for i in range (4)] for j in range (4)]
    H=[[C.create_text(i*100+50,j*100+50,text=M[i][j]) for i in range (4)] for j in range(4)]
    jeu=True
    for i in range (4):
        for j in range (4):
            C.create_rectangle((i*100,j*100,(i+1)*100,(j+1)*100))
            
    def aux ():
        rajout(M)
        if not(paspossible(copy.deepcopy(M))):
            v=choixcoup(M,n)
            if v==1:
                b=bas(M)
            elif v==2:
                b=haut(M)
            elif v==3:
                b=gauche(M)
            elif v==4:
                b=droite(M)
            for i in range (4):
                for j in range (4):
                    C.itemconfigure(H[i][j],text=M[i][j])
            F.after(1,aux)
        else:
            for i in range (4):
                for j in range (4):
                    C.itemconfigure(H[i][j],text=M[i][j])
    F.after(1,aux)
    F.mainloop()
    return(M)
