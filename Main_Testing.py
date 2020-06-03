one = ['', 'Team Puma Knie Podcast', 'VELD-TEAL-LOAM', '1 Gold Chest', '29 Apr 2020', '']
two = ['', 'D&D Beyond Twitch', 'DORP-RUTH-LOTI', '1 Gold Chest', '28 Apr 2020', '05 May 2020']
three = ['', 'CNE', 'IRIS-BEHO-LDER', '2 Silver Chests', '28 Apr 2020', '01 Jan 2021']
four = ['', 'CNE', 'SUPP-LYFO-RYOU', '1 Gold Supply Chest', '28 Apr 2020', '05 May 2020']
import os

def codeupdate():
   if os.path.exists("chests.txt") == True:
        f= open("chests.txt","w+")
        f.write(one[2] + "\n")
        f.write(two[2] + "\n")
        f.write(three[2] + "\n")
        f.write(four[2] + "\n")
        f.close()
   else:
        f= open("chests.txt","w+")
        f.write(one[2] + "\n")
        f.write(two[2] + "\n")
        f.write(three[2] + "\n")
        f.write(four[2] + "\n")
        f.close()

def POS():
    global line
    f = open('chests.txt','r')
    line = f.readline().strip()
    checker()
   
def checker():
    if one[2] == line:
        print('Duplicates')
        print("Null?")
    else:
        print('New Codes') 
        codeupdate()
                
POS()