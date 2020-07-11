import os

os.environ['SECRET_KEY'] = '@-v+s@g^x!(hz@297cfqlerk(ij4z%sqn40tg@4tg$w5l_zj%7'

key = os.getenv('SECRET_KEY')

print(key)