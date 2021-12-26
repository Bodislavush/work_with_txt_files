def registration():
    while True:
        def checker(text):
            if text == 'exit':
                quit()
        username = input('Введите имя пользователя: ')
        if username == '':
            print('Строка логина не может быть пустой')
            continue
        if not username.isalpha():
            print('Логин может состоять только из букв')
            continue
        if len(username) <= 4:
            print('длина не может быть меньше четырех символов')
            continue
        checker(username)
        password = input('Введите пароль: ')
        while password == '':
            print('Строка пароля не может быть пустой')
            password = input('Введите пароль: ')
        checker(password)
        while not password.isdigit():
            print('Пароль должен состоять только из цифр!')
            password = input('Введите пароль: ')
        while len(password) <= 5:
            print('Длина пароля не может быть меньше пяти символов')
            password = input('Введите пароль: ')

        age = input('Введите возраст: ')
        while age == '':
            print('Строка с возрастом не может быть пустой')
            age = input('Введите возраст: ')
        checker(age)
        while not age.isdigit():
            print('Возраст должен состоять только из цифр!')
            age = input('Введите возраст: ')
        while len(age) > 2:
            print('Возраст не может быть больше двух символов')
            age = input('Введите возраст: ')

        print('Добро пожаловать, ' + username + ' !')
        with open(username + '.txt', 'w') as TXT_FILE:
            TXT_FILE.write('Age  ' + age + '\n' + 'Password ' + password + '\n')
        break


def password_ckecker():
    password = input('Введите пароль: ')
    pass

print('Авторизация пользователя')
username = input('Введите имя пользователя: ')
try:
    open(username + '.txt', 'r')
    password_ckecker()
except FileNotFoundError:
    print('Ваш логин не найден, пройдите регистрацию')
    registration()










