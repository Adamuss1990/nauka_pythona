#marka = ' polonez'
#ilosc_drzwi = 5
#print ("Nowa marka to " + marka + ' z ' +  str( ilosc_drzwi ) + '!')
#print(marka.upper())
#print(marka.lower())


#rachunek = 300


#print ("W styczniu rachunek za gaz wynosi" + str( rachunek) )
#print ("ile miesiecy)")
#print ("miesiecy bedzie kosztowac)" + str(rachunek* input([])))


#szkola = ['podstawowa','srednia']
#klasa = [1,3]

#len okresla nam dlugosc lini
#print(len(ilosc))


#for s in szkola:
#    print(s)
#for k in klasa:
#    print(k)

#aby wypisac obok siebie wartosci
#szkola = ['podstawowa', 'srednia']
#klasa = [1, 3]

#print(" dlugosc: {0}".format(len(szkola)))

#liczy nam jaka tablica jest duga range(len())
#for idx in range(len(szkola) ) :
#    print( " idx: " + str(idx) + ": " + szkola[idx])
#    print(szkola[idx] + " ilosc klas " + str(klasa[idx]))

#

#pracownik = {'imie': 'Adam',
#            'miasto': 'Bytom',
#            'numer': 50803}
#print(pracownik['imie'])
#for key, value in pracownik.iteritems():
#    print("{0}:{1}".format(key, value))

#identyczne zachwoanie jak powyszy przyklad

#for key in pracownik:
#    print("{0}:{1}".format(key, pracownik[key]))


#nastepne zadanie
#def - funkcja

def print_dict(d):
    for key, value in d.iteritems():
        print("{0}:{1}".format(key, value))

# dwie podogi __ sa to zmienne wewnetrzne
if __name__== "__main__":
    pracownik = {'imie': 'Adam',
            'miasto': 'Bytom',
            'numer': 50803}

    print_dict(pracownik)
    print_dict(pracownik)
