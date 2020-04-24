#! /usr/bin/python3
import colorama
from colorama import Fore, Back, Style
import os
import time
import random as rn
#from tkinter import *
from math import *
import pickle
import operator
from timeit import default_timer as timer
import re
import sys

os.system('clear')

colorama.init()

#Classes

class Opert:
    def __init__(self, oper, range1, range2):
        self.op = oper #1=+,2=-,3=x,4=/,5=no
        self.r1 = range1
        self.r2 = range2
    def gen_paire(self):
        if (self.op ==1): #plus 
            fs  = rn.randrange(1,self.r1+1)
            snd = rn.randrange(1,self.r2+1)
            res = fs+snd
            return [fs,snd,res]
        elif (self.op ==2): #minus
            fs=0
            snd=0
            while fs==snd:
                fs =rn.randrange(1,self.r1+1)
                snd=rn.randrange(1,min(fs,self.r2)+1)
            res = fs-snd
            return [fs,snd,res]
        elif (self.op ==3): #mult
            fs  = rn.randrange(2,self.r1+1)
            snd = rn.randrange(2,self.r2+1)
            res = fs*snd
            return [fs,snd,res]
        elif (self.op ==4): #div
            if self.r1>self.r2:
               rmax=self.r1
               rmin=self.r2
            else:
               rmax=self.r2
               rmin=self.r1
     
            fs  = rn.randrange(2,rmin+1)
            rem=rmax/(1.0*fs)
            rem=floor(rem)
            snd = rn.randrange(1,rem+1)
            resmult = fs*snd
            return [resmult, fs, snd]



    def op_sign(self):
        if (self.op ==1):  #---"+" 
            return '+'
        elif (self.op ==2):#---"-" 
            return '-'
        elif (self.op ==3):#---"x"
            return 'x'
        elif (self.op ==4):#---"/"
            return '/'
    def paire_pts (self, paire):
        fs,snd,res = paire
        if (self.op ==1):   #---"+"
            if (fs>10 and snd>10 and not (fs %10==0) and not (snd %10==0)):
                return 4
            elif (fs==snd or (fs<5 or snd <5)):
                return 1
            elif (fs>=5 or snd >=5):
                return 2
            else:
                 return 3
        elif (self.op ==2): #---"-"
            if ((fs % 10) < (snd % 10) and not (fs%10==0)):
                return 4
            elif (fs>10 and snd>10 and abs(fs-snd)>10):
                return 3
            elif (fs<10):
                 return 1
            else:
                return 2
        elif (self.op ==3):#---"x"
            if (fs > 10 and snd >10):
                return 5
            elif ((fs in [6,7,8,9] or snd in [6,7,8,9]) and (fs != snd)):
                return 4
            else:
                return 2
        elif (self.op ==4):#---"/"
            if (fs > 10 and snd >10):
                return 5
            elif (fs%2==0 or snd%2==0):
                return 3
            else:
                return 4


#List of scores
if (os.path.exists('scores.pickle')):
    with open ('scores.pickle', 'rb') as f_scores:
        scores_dict = pickle.load (f_scores)

else:
    scores_dict={} 

def disp_scores(scores_dict):
    print ("\n")
    sorted_scores = sorted(scores_dict.items(), key=operator.itemgetter(1))
    #print (sorted_scores)
    for ii in sorted_scores[::-1]:
        print (Back.GREEN+Fore.WHITE+'   {0:4d}] {1:20} ======> {2:.2f}'.format((ii[1][2]),ii[0],(ii[1][0])))
        #print (Back.GREEN+Fore.WHITE+"           "+str(ii[1][2])+"] "+ii[0] + ' -----> ' + str(ii[1][0]))
    print ("\n")

disp_scores(scores_dict)

#get config
if (os.path.exists('config.pickle')):
    with open ('config.pickle', 'rb') as f_conf:
        config_dict = pickle.load (f_conf)
else:
    config_dict={}

#general values
yess=['Yes', 'yes', 'y','YES','Y']
noo =['No','no','NO','n','N'] 
quit=['Q','q','quit','Quit','QUIT']

#Retrieve name from ID
def id2name (scores_dict,the_id):
    id2name=''
    for name, ent in scores_dict.items():
        if (ent[2]==the_id):
            id2name = name
            break
    return id2name

       

#Ask name
def rev_word(word):
    new_w=''
    for ii in word[::-1]:
        new_w = new_w+ii
    return new_w

heb=1
name=''
while (str(name)==''):
    #os.system('clear')
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    if (heb==1):    
        inp_user= input(Back.CYAN+Fore.WHITE + "Hey kid! What's your name/id [heb]? "+Back.RESET)
        if (inp_user.isdigit()):
            name= id2name(scores_dict,int(inp_user))
        else:
            name_tmp = inp_user
            name=rev_word(name_tmp)
        heb=0
    else:
        inp_user= input(Back.CYAN+Fore.WHITE + "Hey kid! What's your name/id [eng]? "+Back.RESET)
        if (inp_user.isdigit()):
            name= id2name(scores_dict,int(inp_user))
        else:
            name= inp_user
        heb=1

print ("Shalom " + name + "! \n")
time.sleep(1)


#Configuration screen
def config_proc():
    print ("\n\nWhat do you want to work out?")
    
    op_plus_inp=''
    while (op_plus_inp not in yess and op_plus_inp not in noo):
        op_plus_inp = input('Do you want "+" ? ')
        op_plus = 5
        op_plus_range1 = 0
        op_plus_range2 = 0
        if op_plus_inp in yess:
            print('Ok let''s do "+"')
            op_plus_range1 = input('Choose a range for first operator from 1 to ? :')
            op_plus_range2 = input('Choose a range for second operator from 1 to ? :')
            op_plus=1
        elif op_plus_inp in noo:
            print('Ok, no "+"')
        else:
            print('You need to choose between Y or N!')
    
        print ("\n")
    
    op_minus_inp=''
    while (op_minus_inp not in yess and op_minus_inp not in noo):
        op_minus_inp = input('Do you want "-" ? ')
        op_minus = 5
        op_minus_range1 = 0
        op_minus_range2 = 0
        if op_minus_inp in yess:
            print('Ok let''s do "-"')
            op_minus_range1 = input('Choose a range for first operator from 1 to ? :')
            op_minus_range2 = input('Choose a range for second operator from 1 to ? :')
            op_minus=2
        elif op_minus_inp in noo:
            print('Ok, no "-"')
        else:
            print('You need to choose between Y or N!')
    
        print ("\n")
    
    
    op_mult_inp=''
    while (op_mult_inp not in yess and op_mult_inp not in noo):
        op_mult_inp = input('Do you want "x" ? ')
        op_mult = 5
        op_mult_range1 = 0
        op_mult_range2 = 0
        if op_mult_inp in yess:
            print('Ok let''s do "x"')
            op_mult_range1 = input('Choose a range for first operator from 1 to ? :')
            op_mult_range2 = input('Choose a range for second operator from 1 to ? :')
            op_mult=3
        elif op_mult_inp in noo:
            print('Ok, no "x"')
        else:
            print('You need to choose between Y or N!')
    
        print ("\n")

    op_div_inp=''
    while (op_div_inp not in yess and op_div_inp not in noo):
        op_div_inp = input('Do you want "/" ? ')
        op_div = 5
        op_div_range1 = 0
        op_div_range2 = 0
        if op_div_inp in yess:
            print('Ok let''s do "/"')
            op_div_range1 = input('Choose a range for first operator from 1 to ? :')
            op_div_range2 = input('Choose a range for second operator from 1 to ? :')
            op_div=4
        elif op_div_inp in noo:
            print('Ok, no "/"')
        else:
            print('You need to choose between Y or N!')
    
        print ("\n")
    return [op_plus, op_plus_range1, op_plus_range2, op_minus, op_minus_range1, op_minus_range2,op_mult, op_mult_range1, op_mult_range2, op_div, op_div_range1, op_div_range2]

def conv_class_config(parm):
    op_plus, op_plus_range1, op_plus_range2, op_minus, op_minus_range1, op_minus_range2,op_mult, op_mult_range1, op_mult_range2 ,op_div, op_div_range1, op_div_range2= parm
    op1 = Opert(op_plus,int(op_plus_range1),int(op_plus_range2))
    op2 = Opert(op_minus,int(op_minus_range1),int(op_minus_range2))
    op3 = Opert(op_mult,int(op_mult_range1),int(op_mult_range2))
    op4 = Opert(op_div,int(op_div_range1),int(op_div_range2))

    opr = [op1, op2, op3,op4]
    return opr    


#Check DB and configure
new_config=0
bd=0
if (config_dict.get(name,None)):
    load_conf = input ('\nI see, you already have a config, do you want to load it? ')
    if (load_conf in yess):
        opr=config_dict[name]
    elif (re.search('mmm\d+',load_conf)):
        num_bd= re.sub(r'm*',"",load_conf)
        bd=1
        opr=config_dict[name]
    else:
        rep_conf = config_proc()
        opr = conv_class_config(rep_conf)
        new_config = 1
else:
    rep_conf = config_proc()
    opr = conv_class_config(rep_conf)
    new_config = 1

        
os.system('clear')

#save config
if new_config :
    config_dict.update({name:opr})
    with open('config.pickle', 'wb') as f_conf:
        pickle.dump(config_dict,f_conf)


vld_opr=[]
for op in opr:
    if (op.op<5):
       vld_opr.append(op) 
        
#Start excercises
if len(vld_opr) >=1:
    if (bd==1):
        num_op = num_bd
    else:
        num_op = 25;#input('How many operations you want? ')

    again='y'

    while (again in yess):
        rn.seed()
        good_res=0
        list_good_res = []
        list_weak_res = []
        list_bad_res  = []
        sum_delta=0
        for ii in range(1,int(num_op)+1): 
            opernid = rn.randrange(1,len(vld_opr)+1)
            opern=vld_opr[opernid-1]
            rn.seed()
            paire =[]
            rnd_gen=0
            while ((paire in list_good_res and paire not in list_weak_res) or paire==[]) and rnd_gen<25:
                paire = opern.gen_paire()
                rnd_gen+=1
            signe = opern.op_sign()
    
            start = timer()
            if (bd==1):
                print (Back.CYAN+Fore.WHITE +'Compute: '+ str(paire[0]) + ' ' + signe + ' ' +str(paire[1]) + ' = ' + str(paire[2]))
                resul = str(paire[2])
            else:
                resul="g"
                while (not resul.isdigit()):
                    resul = input (Back.CYAN+Fore.WHITE +str(ii)+'- Compute: '+ str(paire[0]) + ' ' + signe + ' ' +str(paire[1]) + ' = ')
                    if (resul in quit):
                        break
            end=timer()
            if (resul in quit):
                break
            delta = end-start
            if (int(resul) == paire[2]): #good answer
                list_good_res.append(paire)
                if (delta > 5): # too slow!
                    list_weak_res.append(paire)
                pts = opern.paire_pts(paire)
                good_res=good_res+pts
                sum_delta = sum_delta + delta 
                print (Back.GREEN+Fore.WHITE+"YESSSSSSSSSSSS!! "+ "you gain " + str(pts) + " points!! you are the best " +name+" !!")
            else: #bad answer
                list_bad_res.append(paire)
                sum_delta = sum_delta + 5
                print (Back.RED+Fore.WHITE+"WRONG!"+Back.GREEN+Fore.WHITE+" The good answer is: "+str(paire[0]) + ' ' + signe + ' ' +str(paire[1])+' = '+str(paire[2]))
        
        #previous score
        prev_score=[]
        if(name in scores_dict):
            prev_score = scores_dict[name]

        if (resul in quit):
            print ("\nBye.")
        else:
            time_per_answer = sum_delta/(int(num_op)+1)
            #absolute bonus
            bonus_fact = 1
            bonus_rel=1
            print ("Your time is: "+str(round(time_per_answer)))
            
            #bonus abs
            #if (time_per_answer < 1):
            #    bonus_fact = 4
            #elif (time_per_answer  < 2):
            #    bonus_fact = 3
            #elif (time_per_answer < 3):
            #    bonus_fact = 2
            
            #linear bonus
            if (time_per_answer<=5):
                bonus_fact = 4+(0.1-time_per_answer)/1.63
            #relative bonus
            #print(time_per_answer)
            #print(prev_score)
            if(name in scores_dict):
                if (time_per_answer < prev_score[1]):
                    print (Back.GREEN+Fore.WHITE+"You do it faster, goooood!")
                    bonus_rel=1.1

            good_res = int(good_res*bonus_rel)
            print (Back.CYAN+Fore.WHITE + '\nYour score is: ' + str(good_res))
            if (bonus_fact > 1):
                good_res = round(good_res*bonus_fact)
                print (Back.GREEN+Fore.WHITE+"You get a bonus!!!! of ....."+str(round(bonus_fact))+" and now your score is: "+str(good_res))



        #Register the scores
        if (name in scores_dict):
            if (prev_score[0] >= good_res):
                print (Back.RED+Fore.WHITE+"\n"+name+", well, you did a lower or same score than your best one: "+ str(prev_score[0]))
            else:
                print (Back.GREEN+Fore.WHITE+"Ohhh YES "+name+"!! you beat your own score!!")
                name_pos = prev_score[2]
                scores_dict.update({name:[good_res,time_per_answer,name_pos]})
                disp_scores(scores_dict)

        else:
            print (Back.GREEN+Fore.WHITE+"Good score")
            name_pos = len(scores_dict)+1
            scores_dict.update({name:[good_res,time_per_answer,name_pos]})

        with open ('scores.pickle', 'wb') as f_scores:
           pickle.dump(scores_dict, f_scores)

        again = 'p'
        while (again not in yess and again not in noo):
            again = input(Back.BLUE+Fore.WHITE+"\nDo you want to play again? ")
            if (again=='s'):
                disp_scores(scores_dict)
                #kk=input ("keyy....")
                try:
                    input("Press enter to continue")
                except SyntaxError:
                    pass
                #os.system('read -s -n 1 -p "Press any key to continue..."')
                #print
                os.system('clear')
                
        os.system('clear')

    print ("Bye!"+Back.RESET+Fore.RESET)











