# from decimal import Decimal,ROUND_HALF_EVEN


# n = Decimal("0.1")

# print( n + 2 )

# number = Decimal("0.444")
# number = number.quantize(Decimal("1.00"))
# print(number)       # 0.44
 
# number = Decimal("0.555678")
# print(number.quantize(Decimal("1.00")))       # 0.56
 
# number = Decimal("0.999")
# print(number.quantize(Decimal("1.00")))


# number = Decimal("10.025")      # 2 - ближайшее четное число
# print(number.quantize(Decimal("1.00"), ROUND_HALF_EVEN))       # 10.02
 
# number = Decimal("10.035")      # 4 - ближайшее четное число
# print(number.quantize(Decimal("1.00"), ROUND_HALF_EVEN))  

# from dataclasses import dataclass

# @dataclass
# class Book:
#     title: str
#     author: str


# book = Book(title=122, author="sdf")

# print(book)


# import psycopg2
# from datetime import date,timedelta

# conn = psycopg2.connect(
#                         dbname='lesson_4' ,
#                         user='ibrohim',
#                         host='localhost',
#                         password='postgres'
#                         )

# conn.autocommit = True
# cursor = conn.cursor()

# cursor.execute(""" CREATE TABLE IF NOT EXISTS books (
#                ID SERIAL PRIMARY KEY,
#                title text,
#                 author text,
#                reg_date date
# )""")


# def add_book(title, author):
#     today = date.today()
#     reg_date = str( today - timedelta(days=1) )
#     cursor.execute("""INSERT INTO books (title, author, reg_date)  
#                    VALUES (%s, %s, %s)""", (title, author, reg_date))

# add_book('Python', 'Ivan' )    





from decimal import Decimal, ROUND_HALF_EVEN,ROUND_HALF_DOWN,ROUND_HALF_UP

n = Decimal("0.1")
n2 = Decimal("0.2")
n3 = Decimal("0.3")

price = Decimal('12.45677433456')
print(price.quantize(Decimal("1.00") ,ROUND_HALF_UP ))

