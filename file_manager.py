import os
import shutil
from menu_functions import play_victory
from menu_functions import bank_account
import sys
from menu_functions import isdir
from menu_functions import isfile

while True:

    print('='*10)
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
    print('=' * 10)

    menu_choice = input('Выберите пункт меню: ')
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
        while True:
            save_dir = input('сохранить содержимое рабочей директории в файл? [да/нет] ')
            if save_dir == 'да':
                files = isfile()
                dirs = isdir()
                with open('listdir.txt', 'w') as f:
                    f.write(f'files: {files}\ndirs: {dirs}')
            elif save_dir == 'нет':
                break
            else:
                print('[да / нет]')

    elif menu_choice == '5':
        dirs = isdir()
        print(dirs)

    elif menu_choice == '6':
        files = isfile()
        print(files)

    elif menu_choice == '7':
        print('My OS is', sys.platform, '(', os.name, ')')

    elif menu_choice == '8':
        print('Информация о создателе:')
        print('Михаил, 32 годика')

    elif menu_choice == '9':
        play_victory()

    elif menu_choice == '10':
        bank_account()

    elif menu_choice == '11':
        break

    else:
        print('Неверный пункт меню')