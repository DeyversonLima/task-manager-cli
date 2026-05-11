import requests
API_URL = "https://economia.awesomeapi.com.br/json/last/USD-BRL"


def get_dollar_exchange_rate():
    try:
        response = requests.get(API_URL, timeout=5)
        if response.status_code == 200:
            data = response.json()
            rate = data["USDBRL"]["bid"]
            return f"\n💵 Dólar hoje: R$ {rate}"
        return "Cotação indisponível."
    except requests.RequestException:
        return "Erro ao buscar cotação."
