import csv
import random

lines = 0
lines30 = 0
flag = 0
result = open('result.txt', 'w')
pricols = open('20приколов.txt', 'w')
tegsTxT = open('tegs.txt', 'w')
tegsEnTxT = open('tegsEn.txt', 'w')

chooseSearch = input('Поиск по \n' + '1)Автору \n' + '2)Названию'+ '\n')

if chooseSearch == '1':
    writer = input('Введите имя автора ')
    SearchByWriter = open('SearchByWriter.txt', 'w')
    with open('books.csv', 'r') as csvfile:
        table = csv.reader(csvfile, delimiter=';')
        for row in table:
            lines = lines + 1
            writerList = row[3].lower()
            writer1 = writer.lower()
            indexWriter = int(writerList.find(writer1))
            if indexWriter != -1:
                flag = 1
                SearchByWriter.write(row[1] + ' ........ ' + row[3] + ' ....... Цена:' + row[7] + ' ....... ID:' + row[0] + '\n' + '\n')
        if flag == 0:
            print('Автор не найден')
            SearchByWriter.write('Автор не найден')
    SearchByWriter.close()

elif chooseSearch == '2':
    search = input('Что ищем? ')
    SearchByName = open('SearchByName.txt', 'w')
    with open('books.csv', 'r') as csvfile:
        table = csv.reader(csvfile, delimiter=';')
        for row in table:
            lines = lines + 1
            lower_case = row[1].lower()
            search1 = search.lower()
            index = lower_case.find(search1)
            if index != -1:
                flag = 1
                SearchByName.write(row[1] + ' ........ ' + row[3] + ' ....... Цена:' + row[7] + ' ....... ID:' + row[0] + '\n' + '\n')
        if flag == 0:
            print('Ничего нет')
            SearchByName.write('ничего нет')
    SearchByName.close()

else:
    with open('books.csv','r') as csvfile:
        table = csv.reader(csvfile, delimiter=';')
        for row in table:
            lines = lines + 1
    print('Ошибка')

# 20 случайных строк
randNumbers = [random.randint(1,lines) for i in range(20)]
numberOfAllLine = 0
numberOfLine = 1
tegsM = []

# Количество строк и список тегов
with open('books.csv') as csvfile:
    table = csv.reader(csvfile, delimiter=';')
    for row in table:

        if numberOfAllLine > 0:
            tegs = (row[12].rsplit('# '))
            for i in range(len(tegs)):
                if tegs[i] not in tegsM:
                    tegsM.append(tegs[i])

        if len(row[1]) >= 30:
            lines30 = lines30 + 1
        if numberOfAllLine in randNumbers:
            pricols.write(str(numberOfLine) + ')    (' + str(numberOfAllLine) + ') ' + row[3] + ' ........ ' + row[1] + ' .......' + row[6] + '\n' + '\n')
            numberOfLine = numberOfLine + 1
            numberOfAllLine = numberOfAllLine + 1
        else:
            numberOfAllLine = numberOfAllLine + 1

result.write('В файле ' + str(lines) + ' строк' + '\n' + 'В файле ' + str(lines30) + ' строчек, в которых больше 30 символов')
print('\n' + 'В файле ' + str(lines) + ' строк')
print('В файле ' + str(lines30) + ' строчек, в которых больше 30 символов' + '\n')

# Все теги для books.csv
print(tegsM)
for i in range(len(tegsM)):
   tegsTxT.write(tegsM[i] + '\n')
print('\nВсего ' + str(len(tegsM)) + ' тегов\n')

# Издатальства для books-en.csv
tegsEnM = []
numberOfLineEn = 0

with open('books-en.csv', 'r') as csvfile:
    table = csv.reader(csvfile, delimiter=';')
    for row in table:
        if numberOfLineEn > 0:
            tegsEn = (row[4])
            if tegsEn not in tegsEnM:
                tegsEnM.append(tegsEn)
        numberOfLineEn = numberOfLineEn + 1

print(tegsEnM)
for i in range(len(tegsEnM)):
    tegsEnTxT.write(tegsEnM[i] + '\n')
print('\nВсего ' + str(len(tegsEnM)) + ' издательств')
print(str(numberOfLineEn) + ' строк в books-en.csv\n')

# Последнее дополнительное задание
print('Сортировка по каким критериям?' + '\n' + '1)До 150 рублей' + '\n' + '2)До 2016 года')
print('3)Только 2014, 2016 и 2017 года' + '\n' + '4)До 200 рублей' + '\n' + '5)Нет критериев')
print('6)От 150 рублей' + '\n' + '7)От 2016 до 2018 года' + '\n' + '8)Только 2015 и 2018 года')
print('9)От 200 рублей' + '\n' + '10)От 2018 года')
b = input()
print()
best20 = []
best20i = []
best20txt = open('best20.txt', 'w')
UgeZapisano = []
pipipupu = 0

with open('books.csv', 'r') as csvfile:
    table = csv.reader(csvfile, delimiter=';')
    if b == '1':
        for row in table:
            try:
                pop = row[7].replace(',', '.')
                pop1 = float(pop)
            except:
                pop1 = 1000
            if pop1 < 150.0:
                best20.append(int(row[8]))
                best20i.append(row[10])

    elif b == '2':
        for row in table:
            try:
                c = int(row[6][0:4])
            except:
                c =10000
            if int(c) < 2016:
                best20.append(int(row[8]))
                best20i.append(row[10])

    elif b == '3':
        for row in table:
            try:
                c = int(row[6][0:4])
            except:
                c =10000
            if int(c) == 2016 or int(c) == 2014 or int(c) == 2017:
                best20.append(int(row[8]))
                best20i.append(row[10])

    elif b == '4':
        for row in table:
            try:
                pop = row[7].replace(',', '.')
                pop1 = float(pop)
            except:
                pop1 = 1000
            if pop1 < 200.0:
                best20.append(int(row[8]))
                best20i.append(row[10])

    elif b =='5':
        for row in table:
            try:
                best20.append(int(row[8]))
                best20i.append(row[10])
            except:
                a = 1

    if b == '6':
        for row in table:
            try:
                pop = row[7].replace(',', '.')
                pop1 = float(pop)
            except:
                pop1 = 100
            if pop1 > 150.0:
                best20.append(int(row[8]))
                best20i.append(row[10])

    elif b == '7':
        for row in table:
            try:
                c = int(row[6][0:4])
            except:
                c =10000
            if int(c) >= 2016 and int(c) < 2018:
                best20.append(int(row[8]))
                best20i.append(row[10])

    elif b == '8':
        for row in table:
            try:
                c = int(row[6][0:4])
            except:
                c =10000
            if int(c) == 2015 or int(c) == 2018:
                best20.append(int(row[8]))
                best20i.append(row[10])

    elif b == '9':
        for row in table:
            try:
                pop = row[7].replace(',', '.')
                pop1 = float(pop)
            except:
                pop1 = 100
            if pop1 > 200.0:
                best20.append(int(row[8]))
                best20i.append(row[10])

    elif b == '10':
        for row in table:
            try:
                c = int(row[6][0:4])
            except:
                c =100
            if int(c) >= 2018:
                best20.append(int(row[8]))
                best20i.append(row[10])

with open('books.csv', 'r') as csvfile:
    table = csv.reader(csvfile, delimiter=';')
    best20.sort(reverse=True)
    del best20[20:-1]
    del best20[-1]
    o = 1

    for row in table:
        if o <= 20:
            for u in range(len(best20)):
                if row[8] == str(best20[u]) and row[10] in best20i and row[10] not in UgeZapisano:
                    best20txt.write(str(o) + ') ' + row[1] + ' ........ ' + row[3] + ' ........ ' + row[6] + ' ....... Популярность: ' + row[8] + ' ....... Цена:' + row[7] + ' ....... ID:' + row[0] + '\n')
                    UgeZapisano.append(row[10])
                    o = o + 1


# 20приколов.txt - 20 случайных записей
# best20.txt - Файл из последнего дополнительного задания(20 самых популярных по критериям)
# result.txt - Информация о books.csv
# SearchByName.txt - Результат поиска по названию
# SearchByWriter.txt - Поиск по писателю
# tegs.txt - Теги из books.csv
# tegsEn.txt - Издальства из books-en.csv

best20txt.close()
result.close()
pricols.close()
tegsTxT.close()
tegsEnTxT.close()