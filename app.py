from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)


# Функция для получения курсов валют со стороннего сайта.
def get_exchange_rates():
    try:
        response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
        data = response.json()
        # print(data)
        return data["Valute"]
    except Exception as e:
        print("Ошибка при получении курсов валют:", str(e))
        return {}


# Пример запроса - /api/rates?from=USD&to=RUB&value=1
# Основная функция для конвертации валют.
@app.route('/api/rates', methods=['GET'])
def convert_currency():
    from_currency = request.args.get('from')
    to_currency = request.args.get('to')
    amount = float(request.args.get('value', 0))

    if not from_currency or not to_currency or amount <= 0:
        return jsonify({"error": "Неправильный запрос"}), 400

    exchange_rates = get_exchange_rates()

    # Ввиду особой структуры ответа от сайта приходится разбивать нашу обработку на 3 части.
    if from_currency == "RUB":
        if to_currency in exchange_rates:
            rate = exchange_rates[to_currency]["Value"]
            result = amount / rate
        else:
            return jsonify({"error": f"Курс для валюты '{to_currency}' не найден"}), 404
    elif to_currency == "RUB":
        if from_currency in exchange_rates:
            rate = exchange_rates[from_currency]["Value"]
            result = amount * rate
        else:
            return jsonify({"error": f"Курс для валюты '{from_currency}' не найден"}), 404
    else:
        if from_currency in exchange_rates and to_currency in exchange_rates:
            from_rate = exchange_rates[from_currency]["Value"]
            to_rate = exchange_rates[to_currency]["Value"]
            result = (amount * from_rate) / to_rate
        else:
            return jsonify({"error": "Курс для одной или обеих валют не найден"}), 404

    return jsonify({"result": round(result, 2)})


@app.route('/', methods=['GET'])
def main_page():
    exchange_rates = get_exchange_rates()
    # print(exchange_rates)

    currencies = {}
    for currency in exchange_rates:
        currencies[currency] = exchange_rates[currency]["Name"]
    # print(currencies)
    return render_template("index.html", currencies=currencies)


if __name__ == '__main__':
    app.run(debug=True)
