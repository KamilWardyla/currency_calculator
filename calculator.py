import requests


def get_table():
    currency_dict = {}
    url = "http://api.nbp.pl/api/exchangerates/tables/A/"
    r = requests.get(url)
    if r.status_code == 404:
        return "Error"
    elif r.status_code == 200:
        result = r.json()[0].get('rates')
        for country in result:
            currency_dict[country.get('code')] = country.get('mid')
    return currency_dict


def calculate_currency():
    current_dict = get_table()
    value = float(input('Give me the amount to calculate: '))
    all_country_code = current_dict.keys()
    print(f"All available country code: {list(all_country_code)}")
    country_code = input('Give me the country code: ').upper()
    if country_code not in current_dict.keys():
        return f"{country_code} doesn't exist"
    return round(value * current_dict.get(country_code), 2)


print(calculate_currency())
