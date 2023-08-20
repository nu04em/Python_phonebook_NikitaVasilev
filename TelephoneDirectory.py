# Кирилл Панфилов; 89094512531; Семинары GB
# Кирилл Панфилов; 89094512531; Семинары GB
# Кирилл Панфилов; 89094512531; Семинары GB
# Кирилл Панфилов; 89094512531; Семинары GB
# Кирилл Панфилов; 89094512531; Семинары GB
# Кирилл Панфилов; 89094512531; Семинары GB
# Кирилл Панфилов; 89094512531; Семинары GB
# Кирилл Панфилов; 89094512531; Семинары GB
# Кирилл Панфилов; 89094512531; Семинары GB
# Кирилл Панфилов; 89094512531; Семинары GB
# Кирилл Панфилов; 89094512531; Семинары GB
# Кирилл Панфилов; 89094512531; Семинары GB
# Кирилл Панфилов; 89094512531; Семинары GB
#
# выводить все контакты на экран
# добавить контакт
# удалить контакт
# изменить контакт
# найти контакт
# открыть или сохранить
# выход
#
# имя телефон комментарий
#
# phone.txt

def initial_notes():
    with open('phonebook.txt', 'a', encoding='UTF-8') as data:
        data.write('Иванов Иван Иванович 89011001010')
        data.write('Петров Петр Петрович 89011001011')
        data.write('Степанов Степан Степанович 89011001012')


def add_note():
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    phonenumber = input('Введите номер телефона: ')
    comment = input('Добавите комментарий: ')
    while not phonenumber.isdigit():
        phonenumber = input('Введите номер телефона: ')
    str = f'{surname} {name} {patronymic} {phonenumber} {comment}\n'
    with open('phonebook.txt', 'a', encoding='UTF-8') as data:
        data.write(str)

def find_note(str):
    with open('phonebook.txt', 'r', encoding='UTF-8') as data:
        for line in data:
            if str.lower() in line.lower().split():
                print(line, end='')

def delete_note(str):
    with open('phonebook.txt', 'r', encoding='UTF-8') as data:
        lst = data.readlines()
        for line in range(len(lst)):
            if str.lower() in lst[line].lower().split():
                lst[line] = ''
    with open('phonebook.txt', 'w', encoding='UTF-8') as data:
        for i in lst:
            data.write(i)

def edit_note(str):
    delete_note(str)
    add_note()

# action = ''
# while action != '6':
#     print(
#         '''
#     1. Добавить контакт
#     2. Удалить контакт
#     3. Изменить контакт
#     4. Найти контакт
#     5. Открыть и сохранить файл целиком
#     6. Выход из меню
#     '''
#     )
#     action = input('Введите порядковый номер действия: ')
#     if action == '1':



# initial notes()
while True:
    com = input('\nВыберите и введите необходимую команду: \nadd, all, '
                'find, ed, del, stop: ')
    if com.lower() == 'stop':
        break
    if com.lower() == 'add':
        add_note()
    if com.lower() == 'find':
        str = input('Что ищете?')
        find_note(str)
    if com.lower() == 'all':
        find_note('')
    if com.lower() == 'del':
        str = input('Какой контакт необходимо удалить?\n')
        delete_note(str)
    if com.lower() == 'ed':
        str = input('Какой контакт необходимо изменить?\n')
        delete_note(str)









