import main
import lexem

def sintax():
    table = [
        {'numb':1,'adress':'start',               'kod':'signalprogram',       'AT':36,     'AF':False},#0
        {'numb':2,'adress':'signalprogram',       'kod':'program',             'AT':True,   'AF':False},#1
        {'numb':3,'adress':'program',             'kod': 'second',             'AT':True,   'AF':3},    #2
        {'numb':4,'adress':0,                     'kod': '402',                'AT':4,      'AF':False},#3
        {'numb':5,'adress':0,                     'kod':'procidentifier',      'AT':5,      'AF':False},#4
        {'numb':6,'adress':0,                     'kod':'parametrlist',        'AT':6,      'AF':False},#5
        {'numb':7,'adress':0,                     'kod': '59',                 'AT':7,      'AF':False},#6
        {'numb':8,'adress':0,                     'kod':'block',               'AT':8,      'AF':False},#7
        {'numb':9,'adress':0,                     'kod': '59',                 'AT':True,   'AF':False},#8
        {'numb':10,'adress':'second',              'kod': '401',                'AT':10,     'AF':False},#9
        {'numb':11,'adress':0,                     'kod':'procidentifier',      'AT':11,     'AF':False},#10
        {'numb':12,'adress':0,                     'kod': '59',                 'AT':12,     'AF':False},#11
        {'numb':13,'adress':0,                     'kod':'block',               'AT':13,     'AF':False},#12
        {'numb':14,'adress':0,                     'kod': '46',                 'AT':True,   'AF':False},#13
        {'numb':15,'adress':'block',               'kod':'declaration',         'AT':15,     'AF':False},#14
        {'numb':16,'adress':0,                     'kod': '403',                'AT':16,     'AF':False},#15
        {'numb':17,'adress':0,                     'kod':'statmentlist',        'AT':17,     'AF':False},#16
        {'numb':18,'adress':0,                     'kod': '404',                'AT':True,   'AF':False},#17
        {'numb':19,'adress':'declaration',         'kod':'labeldeclaration',    'AT':True,   'AF':False},#18
        {'numb':20,'adress':'labeldeclaration',    'kod': '405',                'AT':20,     'AF':23},   #19
        {'numb':21,'adress':0,                     'kod':'unsignedinteger',     'AT':21,     'AF':False},#20
        {'numb':22,'adress':0,                     'kod':'lablelist',           'AT':22,     'AF':False},#21
        {'numb':23,'adress':0,                     'kod': '59',                 'AT':True,   'AF':False},#22
        {'numb':24,'adress':0,                     'kod':'empty',               'AT':True,   'AF':True},#23
        {'numb':25,'adress':'lablelist',           'kod':'labelslistnew',       'AT':True,   'AF':25},    #24
        {'numb':26,'adress':0,                     'kod':'empty',               'AT':True,   'AF':True},#25
        {'numb':27,'adress':'labelslistnew',       'kod': '44',                 'AT':27,     'AF':False },#26
        {'numb':28,'adress':0,                     'kod':'unsignedinteger',     'AT':28,     'AF':False},#27
        {'numb':29,'adress':0,                     'kod':'lablelist',           'AT':True,   'AF':False},#28
        {'numb':30,'adress':'parametrlist',        'kod': '40',                 'AT':30,     'AF':32},#29
        {'numb':31,'adress':0,                     'kod':'declarationlist',     'AT':31,     'AF':False},#30
        {'numb':32,'adress':0,                     'kod': '41',                 'AT':True,   'AF':False},#31
        {'numb':33,'adress':0,                     'kod':'empty',               'AT':True,   'AF':True},#32
        {'numb':34,'adress':'declarationlist',     'kod':'empty',               'AT':True,   'AF':True},#33
        {'numb':35,'adress':'statmentlist',        'kod':'empty',               'AT':True,   'AF':True},#34
        {'numb':36,'adress':'procidentifier',      'kod':'identifier',          'AT':True,   'AF':False},#35
        {'numb':37,'adress':0,                     'kod':'#',                   'AT':True,   'AF':False}#36
        ]
    stack = []
    ind = 0
    lex = main.lexem_list
    lex.reverse()
    res = -1
    tree = []
    error = ''
    while 1:

        if res==True:
            if table[ind]['AT']==True:
                ind = stack.pop()
                res = True

                tree.append(table[ind]['adress'])
                tree.append(table[ind]['kod'])
                continue
            else:
                ind = table[ind]['AT']
                res = -1

                tree.append(table[ind]['kod'])
                tree.append(table[ind]['adress'])
                tree.append(a)
        elif res == False:
            if table[ind]['AF']==False:
                if len(stack)==0:
                    res = False
                    break
                else:
                    if table[ind]['adress']=='second' or table[ind]['adress']=='labelslistnew':
                        ind = stack.pop()
                        res = False
                        continue
                    else:
                        error = "SINTAX ERROR: in "+ str(table[ind]['kod'])
                        break



            elif table[ind]['AF']==True:

                tree.append(table[ind]['adress'])
                tree.append(table[ind]['kod'])
                if len(stack)==0:
                    error = "SINTAX ERROR: in "+ str(table[ind]['kod'])
                    break
                ind = stack.pop()
                res = True
                continue
            else:
                ind = table[ind]['AF']
                res = -1

        if table[ind]['kod'] == '#':
            if len(lex)==0:
                print('OK')
                break
            else:
                print('ERROR')
                break
        if len(lex)==0 and  len(stack)!=0:
            error = "SINTAX ERROR: in "+ str(table[ind]['kod'])
            res = False
            break
        if table[ind]['kod']=='identifier':
            new_l = lex.pop()
            if new_l in lexem.identifier.values():
                res = True
                tree.append(table[ind]['kod'])
                tree.append(new_l)
                ind = stack.pop()
                continue
            else:
                res = False
                ind = stack.pop()
                continue


        if table[ind]['kod'] == 'empty':
            res = False
            continue

        if table[ind]['kod'] == 'unsignedinteger':
            new_l = lex.pop()
            if new_l in lexem.constant.values():
                res = True
                continue
            else:
                res = False
                ind = stack.pop()
                continue

        if table[ind]['kod'].isalpha()== True:
            adr =  table[ind]['kod']
            stack.append(ind)
            for i in range(len(table)):
                if table[i]['adress'] == adr:
                    ind = i
                    break
            continue
        elif table[ind]['kod'].isdigit()== True:
            if table[ind]['kod'] == str(lex[len(lex)-1]):
                res = True
                a = lex.pop()
                continue

            else:
                res = False
                continue

    i = 0
    j = ''
    k = ''
    if res == False:
        print("ERROR")
        #print(error)
    else:
        print(tree)
        i1=[]
        while i < len(table)-1:
            if table[i]['adress']=='program' and table[i]['kod']=='second'  and 402 in tree:

                j = j + ' ' + 'program'
                j = j  + '->'+ '402'
                i = i+1
                k = 'program' + '->'+ '402'
                i1.append(k)

            elif table[i]['adress']!=0 and table[i]['adress'] in tree:
                j = j  + ' '+ table[i]['adress']
                j = j  + '->'+ table[i]['kod']
                k = table[i]['adress'] + '->'+ table[i]['kod']
                i1.append(k)


            elif table[i]['adress']!=0 and table[i]['adress'] not in tree and table[i]['adress']=='labeldeclaration':

                j = j + ' ' + 'labeldeclaration'
                j = j  + '->'
                k = 'labeldeclaration' + '->'
                i1.append(k)


            elif table[i]['adress']==0 and table[i]['kod'] in tree:
                j = j + ' ' + table[i]['kod']
                k =  table[i]['kod']
                i1.append(k)

            else:
                i = i+1
                while table[i]['adress'] == 0:
                    i = i+1
                    if table[i]['adress'] != 0:
                        i = i-1
                        break

            if table[i]['kod']=='identifier':
                if len(lexem.identifier)>0:
                    l1 = lexem.identifier.popitem()
                    l = str(l1[1])
                    j = j  + ' ' + table[i]['kod'] + '->' + l
                    k = table[i]['kod'] + '->' + l
                    i1.append(k)
                if len(lexem.identifier)>0:
                    l1 = lexem.identifier.popitem()
                    l = str(l1[1])
                    j = j  + ' ' + table[i]['kod'] + '->' + l
                    k = table[i]['kod'] + '->' + l
                    i1.append(k)
                if len(lexem.identifier)>0:
                    l1 = lexem.identifier.popitem()
                    l = str(l1[1])
                    j = j  + ' ' + table[i]['kod'] + '->' + l
                    k = table[i]['kod'] + '->' + l
                    i1.append(k)
                if len(lexem.identifier)>0:
                    l1 = lexem.identifier.popitem()
                    l = str(l1[1])
                    j = j  + ' ' + table[i]['kod'] + '->' + l
                    k = table[i]['kod'] + '->' + l
                    i1.append(k)
                if len(lexem.identifier)>0:
                    l1 = lexem.identifier.popitem()
                    l = str(l1[1])
                    j = j  + ' ' + table[i]['kod'] + '->' + l
                    k = table[i]['kod'] + '->' + l
                    i1.append(k)
            if table[i]['kod']=='unsignedinteger':
                if len(lexem.identifier)>0:
                    l1 = lexem.constant.popitem()
                    l = str(l1[1])
                    j = j  + ' ' + table[i]['kod'] + '->' + l
                    k = table[i]['kod'] + '->' + l
                    i1.append(k)

            i = i+1
    if res == False:
        return j,error
    else:
        return i1








