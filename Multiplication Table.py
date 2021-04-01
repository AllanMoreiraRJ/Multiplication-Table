import time

def select_multiplication_table():
    global times
    global number
    number = int(input('What table you need? '))
    times = int(input('How many times? '))

def calculator():
    for x in range(times + 1):
        print(f'{number} x {x} = {number * x}')
        time.sleep(0.2)


print('-' * 24)

select_multiplication_table()

print('=-' * 12,
      '\ncalculating...')
print('=-' * 12)

time.sleep(2)
calculator()
