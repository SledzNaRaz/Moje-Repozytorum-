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