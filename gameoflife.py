#game of life
#<2 nb dead || >3
# =3 birth
import random
from colorama import Fore, Back, Style
from os import system
import time
cho =[0,1]
palette= []
nN = int(input("Size of square:"))
ts = float(input("timeti wait"))
round =0

def start():
	for i in range(0,nN):
		row =[]
		for j in range(0,nN):
			row.append( random.choice(cho))
		palette.append(row)
def printer(text):
	if(text == 1):
		print(Back.GREEN + '\033[32m',text,'\033[0m', end='')
	else:
		print( Back.RED + '\033[31m',text,'\033[0m', end='')
start()
def printpal():
	_ = system('cls')
	print("This round is: " + str(round))
	for r in palette:
		for c in r:
			printer(c)
		print('')
printpal()


def nextR():
	temppalette = []
	for i in range(0,nN):
		row =[]
		for j in range(0,nN):
			k = getnb(i,j)
			if(palette[i][j]== 0):
				if(k == 3):
					row.append(1)
				else:
					row.append(0)
			else:
				if(k > 3 or k<2):
					row.append(0)
				else:
					row.append(1)
		temppalette.append(row)
	return temppalette

	
def getnb(r,c):
	e= [r,c]
	w =[r,c]
	s = [r,c]
	n = [r,c]
	if(r == nN-1):
		s[0]=0
	else:
		s[0]= r+1
	if(r == 0):
		n[0]= nN-1
	else:
		n[0] = r-1
	if(c==0):
		e[1]=nN-1
	else:
		e[1]= c-1
	if(c==nN-1):
		w[1]=0
	else:
		w[1]=c+1
	en = [n[0],e[1]]
	wn = [n[0],w[1]]
	es =[s[0],e[1]]
	ws =[s[0],w[1]]
	
	coords = [e,w,s,n,en,wn,es,ws]
	countl =0
	
	for i in coords:
		if(palette[i[0]][i[1]] ==1):
			countl = countl +1
	return countl

h = 'i'
while(True):
	#h = input("pressany")
	time.sleep(ts)
	round +=1
	if(h=='q'):
		break
	palette = nextR()
	printpal()
