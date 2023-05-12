import argparse

import requests


def main():
    args = parse_args()
    result = calculate(args.amount, args.currency)
    print(result)


def calculate(amount: float, currency: str):
    exchange_rate = get_exchange_rate(currency)
    return round(amount * exchange_rate, 2)

def get_exchange_rate(currency: str):
    url = f'http://api.nbp.pl/api/exchangerates/rates/A/{currency}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['rates'][0]['mid']
    raise ValueError(f'Invalid currency {currency}')

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('amount', type=float, help='Amount to convert')
    parser.add_argument('currency', help='Currency code to convert to')
    return parser.parse_args()


if __name__ == '__main__':
    main()