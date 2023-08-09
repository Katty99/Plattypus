import requests


def get_exchange_rates(target_currencies=None):
    url = "https://v6.exchangerate-api.com/v6/838b5cbc404e4e339adaf79c/latest/USD"
    if target_currencies is None:
        target_currencies = ['EUR', 'GBP', 'AUD', 'USD', 'BGN']

    params = {
            'symbols': ','.join(target_currencies),
        }

    response = requests.get(url, params=params)
    data = response.json()
    return data


