import lexem

lexem_list = []

def read_f(name_f):
    with open(name_f) as f:
        while 1:
            oneSymbol = f.read(1)
            if not oneSymbol:
                break
            elif oneSymbol.isalpha():
                while oneSymbol.isalnum():
                    oneSymbol += f.read(1)
                    if oneSymbol =='END':
                        lexem_list.append(404)
                        break



                if oneSymbol[len(oneSymbol) - 1:].isalnum() == False and lexem.delimiter.get(oneSymbol[len(oneSymbol) - 1:]) is None and \
                        lexem.whitespace.get(oneSymbol[len(oneSymbol) - 1:]) is None:
                    return "ERROR: " + oneSymbol
                words(oneSymbol)
            elif oneSymbol.isdigit():
                while oneSymbol.isalnum():
                    oneSymbol += f.read(1)
                if not oneSymbol[0:-1].isdigit():
                    return "ERROR: " + oneSymbol
                if oneSymbol[len(oneSymbol) - 1:].isdigit() == False and lexem.delimiter.get(oneSymbol[len(oneSymbol) - 1:]) is None and \
                        lexem.whitespace.get(oneSymbol[len(oneSymbol) - 1:]) is None:
                    return "ERROR: " + oneSymbol
                constant(oneSymbol)

            elif oneSymbol == '(' and f.read(1) == '*':
                while oneSymbol != '*' or f.read(1) != ')':
                    oneSymbol = f.read(1)
                    if not oneSymbol:
                        return "ERROR with comment"

            elif lexem.delimiter.get(oneSymbol) is not None:
                lexem_list.append(lexem.delimiter.get(oneSymbol))
            elif lexem.whitespace.get(oneSymbol) is not None:
                continue
            else:
                return "ERROR: " + oneSymbol

    return lexem_list

def words(str):
    if not str[len(str) - 1].isalnum():
        strWithotLast = str[0:-1]
        strOfLast = str[len(str) - 1:]
        strWithotLast = strWithotLast.upper()
        if lexem.keywords.get(strWithotLast) is not None:
            lexem_list.append(lexem.keywords.get(strWithotLast))
        if lexem.keywords.get(strWithotLast) is None:
            if lexem.identifier.get(strWithotLast) is not None:
                lexem_list.append(lexem.identifier.get(strWithotLast))
            else:
                lexem.identifier[strWithotLast] = len(lexem.identifier.values()) + 1001
                lexem_list.append(lexem.identifier.get(strWithotLast))
        if lexem.whitespace.get(strOfLast) is not None:
            pass
        elif lexem.delimiter.get(strOfLast) is not None:
            lexem_list.append(lexem.delimiter.get(strOfLast))

def constant(str):
    strWithotLast = str[0:-1]
    strOfLast = str[len(str) - 1:]
    if lexem.constant.get(strWithotLast) is not None:
        lexem_list.append(lexem.constant.get(strWithotLast))
    else:
        lexem.constant[strWithotLast] = len(lexem.constant.values()) + 501
        lexem_list.append(lexem.constant.get(strWithotLast))
    if lexem.whitespace.get(strOfLast) is not None:
        pass
    elif lexem.delimiter.get(strOfLast) is not None:
        lexem_list.append(lexem.delimiter.get(strOfLast))








