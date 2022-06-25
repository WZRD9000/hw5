import random

actors = {'Харрисон Форд': '13.06.1942',
                  'Рутгер Хауэр': '23.01.1944',
                  'Шон Янг': '20.11.1959',
                  'Дэрил Ханна': '03.12.1960',
                  'Брайон Говард Джеймс': '20.02.1945',
                  'Райан Гослинг': '12.11.1980',
                  'Ана Де Армас': '30.04.1988',
                  'Джаред Лето': '26.12.1971',
                  'Дейв Батиста': '18.01.1969',
                  'Сильвия Хукс': '01.06.1983'
           }

months = {'01': 'января',
          '02': 'февраля',
          '03': 'марта',
          '04': 'апреля',
          '06': 'июня',
          '11': 'ноября',
          '12': 'декабря'
          }

days = {'01': 'первое',
        '03': 'третье',
        '12': 'двенадцатое',
        '13': 'тринадцатое',
        '18': 'восемнадцатое',
        '20': 'двадцатое',
        '23': 'двадцатьтретье',
        '26': 'двадцатьшестое',
        '30': 'тридцатое'
        }



def play_victory():
    play = True
    while play:
        rounds = None
        while rounds not in range(5, 11):
            rounds = int(input('Количество вопросов [от 5 до 10]: '))

        correct_count = 0
        incorrect_count= 0

        for i in range(rounds):
            name, date = random.choice(list(actors.items()))
            answer = input(f'Дата рождения {name}')
            if answer == date:
                print('Верно')
                correct_count += 1
            else:
                day, month, year = date.split('.')
                print(f'Неверно, {name} родился {days[day], months[month], year} года')
                incorrect_count += 1

        print('Правильных ответов: ', correct_count)
        print('Неправильных ответов: ', incorrect_count)
        print('Процент правильных ответов: ', correct_count * 100 / rounds)
        print('Процент неправильных ответов: ', incorrect_count * 100 / rounds)

        play_again = None
        while play_again not in ('да', 'нет'):
            play_again = input('Хотите сыграть еще раз? [да/нет]: ')

        play = play_again == 'да'


def bank_account():
    balance = 0
    purchase_history = []

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню')
        if choice == '1':
            refill = int(input('Введите сумму, которую хотите внести: '))
            balance += refill
            print(f'На Вашем счету {balance}')
        elif choice == '2':
            purchase_cost = int(input('Введите цену покупки: '))
            if purchase_cost > balance:
                print('Недостаточно средств')
            else:
                purchase_name = input('Введите наименование покупки: ')
                balance -= purchase_cost
                purchase_history.append((purchase_name, purchase_cost))
        elif choice == '3':
            print(purchase_history)
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')
