import random
import time

def choises():
    print('\n UPPRIFJUN \n')
    print('Hvað viltu keyra?: ')
    print('\n 0) : : Hætta : :')
    print('\n 1) : : Strengir : :')
    print('\n 2) : : Listar : :')

def choose():
    choise = input('\n VAL: ')
    return(int(choise))

def print_list(list):
    count = 0
    for i in list:
        if count == len(list)-1:
            print(i)
        else:
            print(i, end=' ')
            count = count+1


def Fjoldi_orda(strengur):
    count = 0
    newstring = strengur.split(' ')
    for i in newstring:
        if i != '':
            count = count+1
        else:
            deadvalue = ''
    return(count)


def Fyrstu_fimm(strengur):
    count2 = 0
    letter_list = []
    for i in strengur:
        if count2 < 5 and i !='':
            letter_list.append(i)
            count2 = count2 + 1
        elif count2 <5 and i == '':
            count2 = count2 + 1
        else:
            deadvalue = ''
    return(letter_list)


def sidustu_fjorir(strengur):
    return(strengur[-4:])


def midja(strengur):
    count3 = 0
    truelength = 0
    error = 'Það er ekki stafur í miðjunni'
    for i in strengur:
        if i != '' or i != ' ':
            truelength = truelength+1
    if truelength%2 == 0:
        return(error)
    elif truelength%2 != 0:
        for i in strengur:
            if count3 == ((truelength/2)-0.5) and i != '' and i != ' ':
                return(i)
            elif count3 == ((truelength/2)-0.5) and i == '':
                return(error)
            elif count3 == ((truelength/2)-0.5) and i == ' ':
                return(error)
            else:
                count3 = count3 + 1

def only_S(strengur):
    find_letter = 's'
    for i in strengur:
        if i == find_letter or i == find_letter.capitalize():
            deadvalue = ''
        else:
            strengur = strengur.replace(i, '$')
    return(strengur)


def create_random_list(low, High, numbs):
    random_list = []
    for i in range(numbs):
        random_list.append(random.randrange(low, High+1))
    return(random_list)

def sort(list,lowestlist):
    count = lowestlist
    list_sorted = []
    while count != len(list):
        for i in list:
            if count == i:
                list_sorted.append(i)
        count = count+1
    return(list_sorted)

def medaltal(listi):
    summa = 0
    for i in listi:
        summa = summa+i
    whole = summa/len(listi)
    return(float("%.2f" % whole))

def smaller_than_45000(listi):
    summa = 0
    for i in listi:
        summa = summa+i
    while summa > 45000:
        for i in listi:
            summa = summa+i
        listi = listi.pop(-1)
    return(listi)

def del_5(listi):
    count = 0
    for i in listi:
        if i%5 == 0:
            listi = listi.pop(count)
        count = count+1
    return(listi)


continuity = True

while continuity:
    choises()
    val = choose()
    if val == 0:
        print('\n Takk fyrir notkun Forritsins.')
        time.sleep(1.5)
        continuity = False
    elif val == 1:
        string = input('\n Sláðu inn setningu: ')
        time.sleep(1.5)
        fimm_listi = Fyrstu_fimm(string)

        print('\n \n Fjöldi orða: ',Fjoldi_orda(string))
        time.sleep(1.5)

        print('\n \nFyrstu fimm stafirnir: \n')

        print_list(fimm_listi)
        time.sleep(1.5)

        print('\n \nSíðustu Fjórir stafirnir:\n')

        print(sidustu_fjorir(string))
        time.sleep(1.5)

        print('\n \nMiðjustafurinn:\n')

        print(midja(string))
        time.sleep(1.5)

        print('\n \nÖll S: \n')

        print(only_S(string))
        time.sleep(1.5)
    if val == 2:
        lowestnumb = int(input('\n Sláðu inn læstu tölu random listans: '))
        highestnumb = int(input('\n Sláðu inn hæstu töluna í random listanum: '))
        howmany = int(input('\n Sláðu inn hversu margar tölur þú vilt í listanum: '))

        numb_list = create_random_list(lowestnumb, highestnumb, howmany)
        sortednumblist = sort(numb_list,lowestnumb)
        listi_undir_45000 = smaller_than_45000(sortednumblist)
        del_5_list = del_5(sortednumblist)

        time.sleep(1.5)

        print('\n Listi 34-68: \n')
        print_list(numb_list)
        time.sleep(1.5)

        print('\n Raðaður listi: \n')
        print_list(sortednumblist)
        time.sleep(1.5)

        print('\n Meðaltal listans: \n')
        print(medaltal(numb_list))
        time.sleep(1.5)

        print('\n Hæsta tala listans: \n')
        print(max(numb_list))
        time.sleep(1.5)

        print('\n Lægsta tala listans: \n')
        print(min(numb_list))
        time.sleep(1.5)

        print('\n Listi með summu undir 45000: \n')
        print('\n Summa listans: ', sum(numb_list),'\n')
        print_list(listi_undir_45000)
        print('\n Summa listans eftirbrytingu:', sum(listi_undir_45000),'\n')
        time.sleep(1.5)

        print('\n Engar tölur sem ganga upp í 5: \n')
        print_list(del_5_list)
        time.sleep(1.5)



