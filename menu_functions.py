

def play_victory():

    def victory():
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

        rounds = int(input('Количество вопросов: '))
        if rounds < 5:
            rounds = int(input('Количество вопросов [5-10]: '))
        elif rounds > 10:
            rounds = int(input('Количество вопросов [5-10]: '))

        correct_count = 0
        incorrect_count= 0

        import random
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

    victory()
    while True:
        play_again = input('Хотите сыграть еще раз? [да/нет]: ')

        if play_again == 'да':
            victory()
        else:
            break


def bank_account():

    ballance = 0
    purchase_history = []


    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню')
        if choice == '1':
            refill = int(input('Введите сумму, которую хотите внести: '))
            ballance += refill
            print(f'На Вашем счету {ballance}')
        elif choice == '2':
            purchase_cost = int(input('Введите цену покупки: '))
            if purchase_cost > ballance:
                print('Недостаточно средств')
            else:
                purchase_name = input('Введите наименование покупки: ')
                ballance -= purchase_cost
                purchase_history.append((purchase_name, purchase_cost))
        elif choice == '3':
            print(purchase_history)
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')
