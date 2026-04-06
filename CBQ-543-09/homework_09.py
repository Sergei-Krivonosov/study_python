#Task1


class RegistrationError(Exception):
    pass

def registration(username, password):

    if type(username) != str:
        raise RegistrationError()
    if len(username) < 4:
        raise RegistrationError()
    if len(username) > 15:
        raise RegistrationError()
    if not str.isalpha(username):
        raise RegistrationError()

    if type(password) != str:
        raise RegistrationError()
    if len(password) < 8:
        raise RegistrationError()
    if len(password) > 45:
        raise RegistrationError()
    if not str.isalnum(password):
        raise RegistrationError()

    return True

print(registration('Alexa', 'qwerty123'))


#Task2


while True:
    user_login = input('Введите логин: ')
    user_password = input('Введите пароль: ')

    try:
        registration(user_login, user_password)
        print('Успешно!')
        break
    except RegistrationError:
        print('Ошибка регистрации!')



