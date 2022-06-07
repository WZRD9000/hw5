import os
import shutil
import sys

while True:

    print('Выберите пункт меню: ')
    print('1 - создать папку')
    print('2 - удалить (файл/папку)')
    print('3 - копировать (файл/папку)')
    print('4 - просмотр содержимого рабочей директории;')
    print('5 - посмотреть только папки')
    print('6 - посмотреть только файлы')
    print('7 - просмотр информации об операционной системе')
    print('8 - создатель программы')
    print('9 - играть в викторину')
    print('10 - мой банковский счет')
    print('11 - выход')

    menu_choice = input('Выберите пункт меню')
    if menu_choice == '1':
        dir_name = input('введите название папки: ')
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)

    elif menu_choice == '2':
        remove_name = input('введите название папки/файла: ')
        if os.path.exists(remove_name):
            if os.path.isfile(remove_name):
                os.remove(remove_name)
            else:
                shutil.rmtree(remove_name)

    elif menu_choice == '3':
        copy_name = input('Введите название папки/файла')
        if os.path.exists(copy_name):
            if os.path.isfile(copy_name):
                shutil.copy(copy_name, f'copy_{copy_name}')
            else:
                shutil.copytree(copy_name, f'copy_{copy_name}')

    elif menu_choice == '4':
        print(os.listdir())

    elif menu_choice == '5':
        directories = []
        for i in os.listdir():
            if os.path.isdir(i):
                directories.append(i)
        print(directories)

    elif menu_choice == '6':
        files = []
        for i in os.listdir():
            if os.path.isfile(i):
                files.append(i)
        print(files)

    elif menu_choice == '7':
        print('My OS is', sys.platform, '(', os.name, ')')

    elif menu_choice == '8':
        print('Информация о создателе:')
        print('Михаил, 32 годика')

    elif menu_choice == '9':
        from menu_functions import play_victory
        play_victory()

    elif menu_choice == '10':
        from menu_functions import bank_account
        bank_account()

    elif menu_choice == '11':
        break

    else:
        print('Неверный пункт меню')