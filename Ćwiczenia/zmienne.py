from datetime import datetime
from itertools import count


i_liczba = 10.0 
i_liczba += 1 #dodawanie plus jeden do wyniku 
s_tekst1 = 'tekst1'
s_tekst2 = "tekst2"
print(s_tekst1 + " " + s_tekst2) #dodaweanie stringów ze spacją 
print(s_tekst1.find("t")) #numer miejsca w stringu 
print("t" in s_tekst1) #czy dana liczba jest w stringu 
print("Jest godzina " + str(str(i_liczba)))  #dodawanie liczby do stringa
print("Jest godzina {}".format(i_liczba,)) #dodawanie liczby do stringa inny sposób

l_arrary = [1, 2, "Str"]
l_arrary[2] = 20 #zamienianie w stringu wyrazu na inny 
l_arrary.append("3") #dodawanie do stringa 
l_arrary.sort() #sortowanie stringa 
print(l_arrary[:1]) #wyświetla od 0 do 1 miejsca string
l_arrary = [ for i in range(25) if i % 2 == 0 ] #uproszczona pętla z warunkiem wyświetla liczby od 0 do 25 ale tylko parzyste 

l_arrary = (1, 2, 3, 7) #krotka która jest niezmienialna 

s_slownik = {
    'title' : 'tytuł',
    'desctiption' : 'opis'
}
print(s_slownik["title"]) # wyświetla dany wyraz w słowniku 

s_slownik['year'] = 2022 #dodawanie do słownika 

del s_slownik['description'] #usuwanie ze słownika 

print(s_slownik.get("title")) #nawet jak nie będzie tego wyrazu program sie nie wywali tylko powie none zamiast błędu 

z_set1 = set( [1, 2, 3, 4, 5, 10, 7]) #zbiory 
z_set2 = set([ 10, 2, 3, 7])
print(z_set1.intersection(z_set2)) # część wspólna wzorów 
print(z_set1.union(z_set2)) #zwrot wszystkich liczb 
print(z_set1.difference(z_set2)) #wyświetla wyrazy które sie nie powtarzają 


name = input("Podaj swoje imie")
if len(name) <3: 
    print("Podaj minimum 3 znaki")   
else:
    print("Witaj", name)




a, b, c, d = 1, 1, 2, 2 #wylistowanie zmiennych 

if (a and b and c and d > 1):
    print("A")
else:
    print("B")


counter = 1 
while counter <= 10:
    print (counter)
    counter += 1 


while True:
    num = int(input("Podaj liczbe większą od 2 : "))
    if num > 2:
        print("Twoja liczba to ", num)
        break
    else:
        print("To zła liczba")



counter = 1 
while counter <= 20: #pętla sie kończy kiedy counter będzie większe niż 20 
    counter += 1 # dodaje sie jeden do counter 
    if counter % 2 == 0:
        continue  #pominięcie 
    print(counter)


counter = 1
while counter <= 10:
    print(counter)
    if counter == 5:
        exit() #wyjście z programu 
    print("Następny")


import time #wykorzystnie w przestrzeni backend sekundy od 1980 roku 

for v in range(2,6):
    print(v)
    time.sleep(3) #przy każdym przejściu pętli 3 sekunty przestoju 

a = time.gmtime() #data systemowa
a0 = time.gmtime()[0] #pobieramy wartość która nas interesuje za pomocą indeksu 

t1 = time.time()
# Tu sie robi pętla 
t2 = time.time() # to po pętli 
r = t2 - t1 #czas w jakim się pętla wykonała 


import time 
a = time.strftime("%Y", time.gmtime()) #czas za pomocą stringa 


a = datetime.datetime.now() #data systemowa 

today = datetime.date.today() # sam rok 

now = datetime.time(12, 3, 24 ,2222223323) #klasa czas i można sobie dać godzine jaką sie chce itp


import csv 

#odczyt
n_line  = 0
with open("testowy,csv", "r") as csvfile:
    reader = csv.reader(csvfile) #przypisanie pliku do zmiennej 
    for row in reader:
        if n_line == 0:
            print("s")
        n_line += 1 
    else:
        print("Nazwa user to :")
        n_line =+ 1 #autoinkrementacja 
    
    print("Ilość wierszy to : {n_line}" )
