import os
import shutil
from menu_functions import play_victory
from menu_functions import bank_account
import sys
from menu_functions import isdir
from menu_functions import isfile
from menu_functions import main_menu_list


while True:

    main_menu_list()

    menu_choice = input('Выберите пункт меню: ')
    if menu_choice == '1':
        dir_name = input('введите название папки: ')
        try:
            os.mkdir(dir_name)
        except:
            print('папка с таким именем уже существует')

    elif menu_choice == '2':
        remove_name = input('введите название папки/файла: ')
        try:
            os.remove(remove_name) if os.path.isfile(remove_name) else shutil.rmtree(remove_name)
        except:
            print('папки/файла с таким именем не найдено')

    elif menu_choice == '3':
        copy_name = input('Введите название папки/файла')
        try:
            shutil.copy(copy_name, f'copy_{copy_name}') if os.path.isfile(copy_name) else shutil.copytree(copy_name, f'copy_{copy_name}')
        except:
            print('папки/файла с таким именем не найдено')

    elif menu_choice == '4':
        print(os.listdir())
        while True:
            save_dir = input('сохранить содержимое рабочей директории в файл? [да/нет] ')
            if save_dir == 'да':
                files = isfile()
                dirs = isdir()
                with open('listdir.txt', 'w') as f:
                    f.write(f'files: {files}\ndirs: {dirs}')
                break
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