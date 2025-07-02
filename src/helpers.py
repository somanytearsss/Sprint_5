import random

class Helpers:

    def get_random_email():
        email_name = 'Artem_Elizarov_24_'
        domain = '@yandex.ru'
        rad = random.randint(100,999)
        random_email = email_name + str(rad) + domain
        return random_email

    def get_random_password():
        random_password = random.randint(100000, 999999)
        return random_password