import random
characters='abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIHKLMNOPQRSTUVWXYZ_#@!&%$+-/*'
#print(len(characters))
def generatemypasscode(size_passcode):
    mypasscode=''
    char_length=len(characters)-1
    for i in range(size_passcode):       
        codeelement=random.randint(0,char_length)  # to generate random character 
        mypasscode=mypasscode + characters[codeelement] # to build the passcode 
    return mypasscode
print()
ans='Y'
while (ans=='Y'):
    size_passcode=int(input("Please enter the size of passcode character to generate: "))
    print(generatemypasscode(size_passcode))
    ans=input("Do you to generate more passcode...? (Y/N) ").upper()
print("Thank you ! You are DONE!")