from bs4 import BeautifulSoup
import requests
import os

url="https://idle-champions.fandom.com/wiki/Combinations"

html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "lxml")
table = soup.find("table", attrs={"class": "article-table article-table-selected", "style": "background:transparent; width: 100%;"})
table_data = table.find_all("tr")
td = soup.select_one("td:nth-of-type(2)")


w = table_data[1].text.splitlines()
x = table_data[2].text.splitlines()
y = table_data[3].text.splitlines()
z = table_data[4].text.splitlines()
a = table_data[5].text.splitlines()
b = table_data[6].text.splitlines()
c = table_data[7].text.splitlines()
d = table_data[8].text.splitlines()
e = table_data[9].text.splitlines()
F = table_data[10].text.splitlines()
g = table_data[11].text.splitlines()
h = table_data[12].text.splitlines()
i = table_data[13].text.splitlines()
j = table_data[14].text.splitlines()
k = table_data[15].text.splitlines()
l = table_data[16].text.splitlines()
m = table_data[17].text.splitlines()
n = table_data[18].text.splitlines()
o = table_data[19].text.splitlines()
p = table_data[20].text.splitlines()
q = table_data[21].text.splitlines()
r = table_data[22].text.splitlines()
s = table_data[23].text.splitlines()
t = table_data[24].text.splitlines()
u = table_data[25].text.splitlines()
v = table_data[26].text.splitlines()
def codeupdate():
   if os.path.exists("Chests.txt") == True:
        f = open("Chests.txt","w+")
        f.write(w[2] + "\n")
        f.write(x[2] + "\n")
        f.write(y[2] + "\n")
        f.write(z[2] + "\n")
        f.write(a[2] + "\n")
        f.write(b[2] + "\n")
        f.write(c[2] + "\n")
        f.write(d[2] + "\n")
        f.write(e[2] + "\n")
        f.write(F[2] + "\n")
        f.write(g[2] + "\n")
        f.write(h[2] + "\n")
        f.write(i[2] + "\n")
        f.write(j[2] + "\n")
        f.write(k[2] + "\n")
        f.write(l[2] + "\n")
        f.write(m[2] + "\n")
        f.write(n[2] + "\n")
        f.write(o[2] + "\n")
        f.write(p[2] + "\n")
        f.write(q[2] + "\n")
        f.write(r[2] + "\n")
        f.write(s[2] + "\n")
        f.write(t[2] + "\n")
        f.write(u[2] + "\n")
        f.write(v[2] + "\n")
        f.close()
   else:
        with open('Chests.txt', 'w+') as fp:
            pass
        fp.close()
        codeupdate()

def POS():
    global line
    if os.path.exists("Chests.txt") == True:
        f = open('Chests.txt','r')
        line = f.readline().strip()
        checker()
    else:
        with open('Chests.txt', 'w+') as fp:
            pass
        fp.close()
        checker()
   
def checker():
    if w[2] == line:
        print('Duplicates')
        print("Null?")
    else:
        print('New Codes') 
        codeupdate()

POS()      

#https://stackoverflow.com/questions/28665941/python-click-by-coordinate-inside-a-window
