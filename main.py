def checker(text):
    if text == 'exit':
        quit()
    return text


def registration():
    while True:
        username = checker(input('Введите имя пользователя: '))
        if username == '':
            print('Строка логина не может быть пустой')
            continue
        if not username.isalpha():
            print('Логин может состоять только из букв')
            continue
        if len(username) <= 4:
            print('длина не может быть меньше четырех символов')
            continue
        password = input('Введите пароль: ')
        while password == '':
            print('Строка пароля не может быть пустой')
            password = input('Введите пароль: ')
        checker(password)
        while not password.isdigit():
            print('Пароль должен состоять только из цифр!')
            password = checker(input('Введите пароль: '))
        while len(password) <= 5:
            print('Длина пароля не может быть меньше пяти символов')
            password = checker(input('Введите пароль: '))

        age = input('Введите возраст: ')
        while age == '':
            print('Строка с возрастом не может быть пустой')
            age = input('Введите возраст: ')
        checker(age)
        while not age.isdigit():
            print('Возраст должен состоять только из цифр!')
            age = checker(input('Введите возраст: '))
        while len(age) > 2:
            print('Возраст не может быть больше двух символов')
            age = checker(input('Введите возраст: '))

        print('Добро пожаловать, ' + username + ' !')
        with open(username + '.txt', 'w') as TXT_FILE:
            TXT_FILE.write('Age  ' + age + '\n' + 'Password ' + password + '\n')
        break


def password_checker(text_file):
    for line in text_file:
        if 'Password' in line:
            string_with_password = line
    for i in range(3):
        password = input('Введите пароль: ')
        if password in string_with_password:
            print('авторизация успешна!')
        if password not in string_with_password and i != 2:
            print('Пароль неверен, Введите другой пароль или пройдите регистрацию, осталось попыток: ' + str(2-i))
        if password not in string_with_password and i == 2:
            print('Введите "y" для регистрации или введите "n" для выхода из программы')
            # Здесь остановились!!!
        # registration()


def main():
    print('Авторизация пользователя')
    username = checker(input('Введите имя пользователя: '))
    try:
        text_file = open(username + '.txt', 'r')
        password_checker(text_file)
    except FileNotFoundError:
        print('Ваш логин не найден, пройдите регистрацию')
        registration()


main()


# Сделать так чтоб везде можно было выйти с программы через команду 'еxit'
# В случае если найдёт логин но введено неправильно три раза пароль - переход на регистрацию,
# Сделать проверку на пароль, чтоб два раза было введено, а если неправильно то ещё раз надо повторить первый пароль, если опять неправильно то циклировать



