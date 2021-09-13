import string
import random
import zipfile

PASSWORD_LENGTH = 4


def extract_archive(file_to_open, password):
    """
    Функция открывает архив с паролем.
    Возвращает результат операции (bool)
    """
    try:
        file_to_open.extractall(pwd=password.encode())
        return True
    except Exception as e:
        print(e)
        return False


def pw_gen(size=4, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def hack_archive(file_name):
    file_to_open = zipfile.ZipFile(file_name)
    wrong_passwords = []
    tries = 0
    while True:
        password = pw_gen()
        if password in wrong_passwords:
            continue
        if extract_archive(file_to_open, password) is True:
            break
        else:
            wrong_passwords.append(password)
            tries = tries + 1

    print(f'Archive {file_name} is hacked. Password - {password}')
    print(f'Password was found after {tries} tries')


filename = 'hack_me.zip'
hack_archive(filename)
