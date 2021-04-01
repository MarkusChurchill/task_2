#крч нихуя не разобрался с индексами списками и кортежах, начну читать всё заново.
#Прога ниже может проверить экспрешн на скобки ( в том числе вложенность скобок) но не более. 
def checkio(expression):
    list_brackets = []
    for i in expression:
        if i == "[" or i == "]" or i == "(" or i == ")" or i == "{" or i == "}":
            list_brackets.append(i) #создаю список нужных нам элементов
    if list_brackets.count("[") == list_brackets.count("]") and list_brackets.count("(") == list_brackets.count(")") and list_brackets.count("{") == list_brackets.count("}"):
      #если количество "(" равно количеству ")" и так далее...
        j = 0
        k = 0
        try:
            while j != range(len(list_brackets)): #попытка найти в списке соседние скобки
                if list_brackets[j] == "(" and list_brackets[j+1] == ")":
                    list_brackets.pop(j)
                    list_brackets.pop(j)
                    j = 0
                elif list_brackets[j] == "{" and list_brackets[j+1] == "}":
                    list_brackets.pop(j)
                    list_brackets.pop(j)
                    j = 0
                elif list_brackets[j] == "[" and list_brackets[j+1] == "]":
                    list_brackets.pop(j)
                    list_brackets.pop(j)
                    j = 0
                else:
                    j += 1

        except:
           if (len(list_brackets)) == 0:
               print(True,None,None)
           else:
                print(False)

    else:
            print(False)
checkio(input())
