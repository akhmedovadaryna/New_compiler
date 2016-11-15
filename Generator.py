import main
import sintax
import lexem


def generator():
    tree = main.read_f('lex2.txt')
    s = []
    tree_new = []
    for i in tree:
        s.append(i)
        if i==59:
            tree_new.append(s)
            s = []
        elif i==46:
            tree_new.append(s)
            s = []
    print(';ASM')
    print('.data')
    s = []
    s1 = []
    for i in tree:
        s = []
        if i==405:
            j = lexem.constant.keys()
            for j1 in j:
                j1 = int(j1)
                if j1>0 and j1<=10:
                    print('A'+str(j1)+' db ?')
                elif j1>10 and j1<=20:
                    print('B'+str(j1-10)+' dd ?')
                elif j1>20 and j1<=30:
                    print('D'+str(j1-20)+' dw ?')



    print('.code')
    for i in tree_new:
        if i[0]==401:
            a = lexem.identifier.keys()
            for j in a:
                1
            print('@'+ j+':')
            print('nop')
            print('end'+' '+j)
        elif i[0]==402:
            a = lexem.identifier.keys()
            for j in a:
                1
            print('@'+ j+':')
            print('nop')
            print('ret')