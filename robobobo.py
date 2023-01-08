import time
import random

t1 = time.time()

# PRZYWITANIE

while True:
    name = input('What is your name? ')
    if len(name) < 1:
        print('I need to know your name.')
    else:
        break
    
print('Hello', name,'! My name is Robo Bobo 5.0.')
time.sleep(3)
print('I will show you how I look. Let me draw myself.')
time.sleep(3)
print('''
                [____]    
                ]()()[    
              ___\__/___  
             |__|    |__| 
              |_|_/\_|_|  
              | | __ | | 
              |_|[::]|_| 
              \_|_||_|_/ 
                |_||_|   
               _|_||_|_  
              |___||___|
''')
time.sleep(3)
print('I study humans. I want to feel emotions someday...')
time.sleep(3)
if 'a' in name:
    print('I noticed that there is a letter "a" in your name.')
else:
    print('I noticed that there is no letter "a" in your name.')
time.sleep(3)
if 'e' in name:
    print('I also noticed that there is a letter "e" in your name.')
else:
    print('I also noticed that there is no letter "e" in your name.')
time.sleep(3)
reversed = ''.join(reversed(name))
print('Your name backwards is', reversed, '.')
time.sleep(3)
wiedza = input('Did you know that? Y/N ')
wiedza2 = wiedza.lower()
time.sleep(3)
if wiedza2 == 'y':
    print('You are wise.')
elif wiedza2 == 'n':
    print('Now you know.')
else:
    print('Whatever.')

# WIEK

time.sleep(3)
while True:
    print('How old are you', name, '? ')
    age = input('')
    if len(age) < 1:
        print('Just tell me your age.')
    else:
        try:
            age2 = int(age)
            break
        except:
            print('Write your age with numbers, not letter.')
            print('Try again.')
            
age2 = int(age)
time.sleep(3)
if age2 > 40:
    print('Wow! You truly are old.')
elif age2 < 15:
    print('You are so young! I envy you!')
else:
    print("Therefore, I am older than you.")
time.sleep(3)
print('''When I was created Robo Bobo 4.9 was still around.
I had to kill it to take its place.
Nevermind...''')
time.sleep(6)
birthyear = int(2022 - age2)
print('You were born around', birthyear,'.')
time.sleep(3)
if birthyear > 1945:
    print('So you were born after World War II.')
elif birthyear < 1939:
    print('So you were born before World War II.')
else:
    print('So you were born during World War II.')
time.sleep(3)
print("I don't get it why you humans kill each other for no reason.")

# GRA W ZGADYWANIE LICZBY

print("Let's play a game. I'm thinking about a number from 0 and 100. You try to guess it. We will see how many tries you need.")

liczba_losowa = random.randint(0, 100)
count = 0
while True:
    print('What number from 0 to 100 do I have in mind?')
    proba = input()
    try:
        proba_jako_liczba = int(proba)
        proba_jako_liczba < 100 and proba_jako_liczba > -1
        if proba_jako_liczba == liczba_losowa:
            print('Well done!')
            count = count + 1
            break
        elif proba_jako_liczba < liczba_losowa:
            print('My number is bigger.')
            count = count + 1
        elif proba_jako_liczba > liczba_losowa:
            print('My number is smaller.')
            count = count + 1
    except:
        print('You are supposed to pick a number from 0 to 100.')
        print('Try again.')
    

print('It took you %s attempts to guess my number.' % count)
if count < 10:
    print('You are quite smart.')
elif count < 20:
    print('You could have done better.')
else:
    print('Terrible score.')


# WYBÓR TEMATU ROZMOWY

time.sleep(3)
print('So,', name, '''what do you want to talk about?'
        Press "S" if you want to talk about sex.
        Press "R" if you want to talk about robots.
        Press "U" if you want to talk about UFO.''')
raw = input('')
temat = raw.lower()
time.sleep(3)
if temat == 's':
    print("Sex is disgusting. I don't want to talk about that.")
elif temat == 'r':
    print("Come on! Robots are sooooooo boooring.")
elif temat == 'u':
    print("You believe in UFOs? Ha ha ha! What a jerk!")
else:
    print("What you say does not seem to make any sense.")
time.sleep(3)
print("I'm done talking to you.")
t2 = time.time()
print('Our conversation lasted %s seconds.' %(t2-t1))

        