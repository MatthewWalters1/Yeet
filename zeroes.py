from time import sleep
from random import randint
check = False
print("(Z): Hello!\n")
sleep(3)
name = input("(Z): What is your name?\n")
sleep(4)
print("(Z): Nice to meet you,", name)
sleep(2)
print("(Z): I am Zeroes")
sleep(4)
mood = input("(Z): how are you feeling today?\n")
if mood.find('not bad') != -1 or mood.find('all right') != -1 or mood.find('alright') != -1 or mood.find('ok') != -1:
    sleep(6)
    print("(Z): Cool, I'm doing all right too!")
elif mood.find('bad') != -1 or mood.find('terrible') != -1 or mood.find('not') != -1 or mood.find('awful') != -1:
    sleep(5)
    print("(Z): I'm sorry to hear that...")
    sleep(5)
    problem = input("(Z): what's the matter?\n")
    sleep(2)
    a = randint(0,10)
    if a == 10:
        print("(Z): oof...")
    else:    
        print("(Z): I see...")
    sleep(3) 
    print("(Z): I hope you feel better soon")
elif mood.find('good') != -1 or mood.find('great') != -1 or mood.find('fantastic') != -1:
    sleep(5)
    print("(Z): that's great!")
    sleep(3)
    print("(Z): I'm feeling good as well")
else:
    sleep(2)
    print("I see...")
sleep(4)
question = input("(Z): Is there anything you would like to know about me?\n")
sleep(7)
if question.find('computer') != -1:
    question = question.replace('computer', 'human')
    print("(Z): For now, you'll have to ask my developer")
elif question.find('no') != -1 or mood.find('that is all') != -1:
    print("(Z): Well, I guess that's it then")
elif question.find('ai') != -1 or question.find('artificial intelligence') != -1:
    sleep(4)
    print("(Z): Well, I'm not really an artificial intelligence, I'm just prepared to respond to certain words and then continue the conversation")
elif question.find('Zeroes') != -1 or question.find('zeroes') != -1:
    check = True
    print("(Z): I'm not sure why my developer decided to call me that, but I like it...")
else:
    print("(Z): For now, you'll have to ask my developer")
if check == False:
    sleep(8)
    print("(Z): Can I ask you,", question)
    q2 = input()
    sleep(4)
    print("(Z): I see...")
sleep(6)
print("(Z): This is all I have for now, see you next time!")
sleep(3)
print("(Z): It was very nice talking to you,", name)