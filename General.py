import main
import sintax
import lexem
import Generator
import types

name = 'lex2.txt'
lex = main.read_f(name)
print(lex)
for_lex = lex
print(' ')
print "DELIMITER: ", lexem.delimiter
print "KEYWORDS:  ", lexem.keywords
print "IDENTIFIER:", lexem.identifier
print "CONSTANT:  ", lexem.constant

tree1 = sintax.sintax()

f = open('text.txt', 'w')
for index in tree1:
    f.write(index)
i1 = ''
i2 = ' '
k = 0
ErrSint = ''
for i in tree1:
    if i.find('->')>0:
        i2=i2 + ' '
        k1 = ''
        while k<(len(i)):
            k1 = k1+''
            k = k+1
        j = k1 + i2
        print(j+i)
    elif i.find('SINTAX ERROR')>0 or i=="":
        ErrSint = tree1[1]
        break
    elif i.find('->')<0:
        k1 = ''
        while k<(len(i)):
            k1 = k1+' '
            k = k+1
        j = k1 + i2
        print('\t'+j+i)

print('--------------------------------------------------------------------------------------------------')

def lexm():
    fl = False
    t = type(for_lex)
    list_new = []
    str_new = ''
    if type(for_lex) == type(list_new):
        return
    if type(for_lex) == type(str_new):
        if for_lex.find('comment')>0:
            f = open(name)
            line = f.readlines()
            print('LEXICAL ERROR: error with comment'+'\n'+ line[0]+line[1]+line[2])
            fl = True
        else:
            f = open(name)
            line = f.readlines()
            print('LEXICAL ERROR:' + main.read_f(name) +'\n'+ line[0]+line[1]+line[2])
            fl = True
    return fl


def sint():
    fl = False
    if ErrSint!='':
        if ErrSint.find('procidentifier')>0:
            f = open(name)
            line = f.readlines()
            print(ErrSint + ' ' + 'in first line' +'\n'+line[0]+line[1]+line[2])
            fl = True

        elif ErrSint.find('403')>0:
            f = open(name)
            line = f.readlines()
            print(line[0]+line[1]+ ErrSint+' '+ 'in last line'+'\n'+line[2])
            fl = True

        elif ErrSint.find('404')>0:
            f = open(name)
            line = f.readlines()
            print(line[0]+line[1]+ ErrSint+' '+ 'in last line'+'\n'+line[2])
            fl = True

        elif ErrSint.find('labeldeclaration')>0:
            f = open(name)
            line = f.readlines()
            print(line[0]+ ErrSint+' '+ 'in second line'+'\n'+line[1]+line[2])
            fl = True
    return fl


def gen():
    fl = False
    f = open(name)
    line = f.readlines()
    liii = line[1]
    liii = liii.replace(';', ',')
    liii = liii.replace('LABEL ', ',')
    l = liii.split(',' or ' ' or ';')
    for i in l:
        kol = l.count(i)
        if kol>1:
            fl = True
            print(line[0]+ 'SEMANTIC ERROR: two identical numbers in the LABEL'+' '+ 'in second line'+'\n'+line[1]+line[2])

        if i.isdigit()==True:
            j = i
            j = int(j)
            if j>65536:
                fl = True
                print(line[0]+ 'SEMANTIC ERROR: too large a number'+' '+ 'in second line'+'\n'+line[1]+line[2])
    return fl



fl = lexm()
if fl!=True:
    fl = sint()
    if fl != True:
        fl = gen()
        if fl!=True:
            Generator.generator()




