from tkinter import *

Madlibs_root = Tk()
Madlibs_root.geometry('300x300')
Madlibs_root.title('Madlibs Generator')
Label(text= 'Madlibs Generator \n by Ab Chatterjee',font='arial 12 bold',bg='yellow').pack()
Label(text= 'Click any one: ',font='arial 10 bold',bg='magenta').place(x=90, y=80)

def madlibs1():
    name = input('Your name: ')
    dob = input('Enter your Dob: ')
    place = input('Your city: ')
    
    print(f'My name is {name}.I was born on {dob}, in {place}. ')

def madlibs2():
    adj = input("Adjective: ")  
    verb1 = input("Verb: ")
    verb2  = input("Verb: ")
    famous_person = input("Famous person: ")

    print(f"Computer programming is so {adj} ! it makes me so exicited all the time because \
i love to {verb1}.Stay hydearted and {verb2} like your are {famous_person} ! ")

Button(Madlibs_root, text = 'Introduction', font='arial 10', command=madlibs1,bg='light green').place(x=90, y=100)  
Button(Madlibs_root, text = 'Lets Play', font='arial 10', command=madlibs2,bg='light green').place(x=90, y=130)  

Madlibs_root.mainloop()

