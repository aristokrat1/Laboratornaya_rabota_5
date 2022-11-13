import random
def get_random_password(a = None) -> str:
    if a == None :
        a = 8
    numbers_letters = "abcdefghigjklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    password = random.sample(numbers_letters, a)
    return password

print(get_random_password())
