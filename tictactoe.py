from random import randint
bd=['']*10
def disc(bd):
  brd=['']*10
  print(bd[9]+'\t|'+bd[8]+'\t|'+bd[7])
  print(brd[9]+'\t|'+brd[8]+'\t|'+brd[7])
  print('-------------------------')
  print(brd[6]+'\t|'+brd[5]+'\t|' +brd[4])
  print(bd[6]+'\t|'+bd[5]+'\t|' +bd[4])
  print('-------------------------')
  print(brd[3]+'\t|'+brd[2]+'\t|' +brd[1])
  print(bd[3]+'\t|'+bd[2]+'\t|' +bd[1])
  
def inp1():
    a=True
    while a:
       p1=str(input(' player 1 enter your choice of x or o:'))
       if p1=='x' or p1=='o':
           if p1=='x':
               p1marker='x'
               p2marker='o'
               break
           else :
               p1marker='o'
               p2marker='x'
               break
           a=False
       else :
           pass  
    return (p1marker,p2marker)

def inp2():
    a=True
    while a:
       p2=str(input(' player 2 enter your choice of x or o:'))
       if p2=='x' or p2=='o':
           if p2=='x':
               p2marker='x'
               p1marker='o'
               break
           else :
               p2marker='o'
               p1marker='x'
               break
           a=False
       else :
           pass  
    return (p1marker,p2marker)

def placemarker(bd,marker,pos) :
    bd[pos]=marker

def checkwin(bd,mark):
     if bd[7]==mark and bd[8]==mark and bd[9]==mark: return True
     elif bd[6]==mark and bd[5]==mark and bd[4]==mark: return True
     elif bd[3]==mark and bd[2]==mark and bd[1]==mark: return True
     elif bd[7]==mark and bd[4]==mark and bd[1]==mark: return True
     elif bd[8]==mark and bd[5]==mark and bd[2]==mark: return True
     elif bd[9]==mark and bd[3]==mark and bd[6]==mark: return True
     elif bd[1]==mark and bd[5]==mark and bd[9]==mark: return True
     elif bd[7]==mark and bd[5]==mark and bd[3]==mark: return True
     else : return False

def choosefirst():
    flip=randint(0,1)
    if flip==1:
        return 'p1'
    else:
        return 'p2'
def spck(bd,pos):
    return bd[pos]==''
def fullck(bd):
    for i in range(1,10):
        if spck(bd,i):
            return False 
    return True
def plrchc(bd):
       pos=0
       
       pos=int(input('enter a pos from 1 to 9:'))
       return pos

def replay():
    ch=input('Play again ?? enter a choice yes or no:')
    return ch=='yes'
game=True
h=0    
while game :
  j=choosefirst()
  if j=='p1':
   (p1mark,p2mark)=inp1()
  else :
     (p1mark,p2mark)=inp2()
  for i in range(1,10):
      if fullck(bd)!=True:
        if i==1 or i==3 or i==5  or i==7 or i==9:
            pos1=plrchc(bd)
            placemarker(bd,p1mark,pos1)
            disc(bd)
            k=checkwin(bd,p1mark)

        else :
            pos1=plrchc(bd)
            placemarker(bd,p2mark,pos1)
            disc(bd)
            k=checkwin(bd,p2mark)
        if k==True :
              if i==1 or i==3 or i==5  or i==7 or i==9:
                 print('player 1 won')
                 h=1
                 break
              else :
                   print('player 2 won')
                   h=1
                   break
        else :
             continue
  if h !='1':    
   print(' \n it is a tie')
  t=replay()
  if t==True:
      bd=['']*10
      game=True
  else :

    game=False    