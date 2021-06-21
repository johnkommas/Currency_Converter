# write your code here!
# print('Meet a conicoin!')

import sys
import requests
import json




def get_input(ask=''):
    try:
        console = float(input(ask))
    except ValueError:
        print('Value Error')
        return get_input(ask)
    except KeyboardInterrupt:
        print('Terminating Program')
        sys.exit(1)
    return console


def convert(rate, money, new_cur):
    convertion = round(rate * money, 2)
    print(f"You received {convertion} {new_cur.upper()}. ")


def get_data(code):
    results = requests.get(f'https://www.floatrates.com/daily/{code}.json').text
    return json.loads(results)



# Read the Currency you have
my_currency = input()
rates = get_data(my_currency)
cached_rate = {}
if 'eur' in rates:
    cached_rate['EUR'] = rates['eur']['rate']
else:
    cached_rate['EUR'] = 1
if 'usd' in rates:
    cached_rate['USD'] = rates['usd']['rate']
else:
    cached_rate['USD'] = 1
# Read the Currency you want
while True:
    new_currency = input()
    if new_currency == '':
        break
    money = float(input())
    print("Checking the cache...")
    if new_currency.upper() in cached_rate:
        print('Oh! It is in the cache!')
        convert(rates[new_currency.lower()]['rate'], money, new_currency)
    else:
        print('Sorry, but it is not in the cache!')
        cached_rate[new_currency.upper()] = rates[new_currency]['rate']
        convert(rates[new_currency.lower()]['rate'], money, new_currency)








