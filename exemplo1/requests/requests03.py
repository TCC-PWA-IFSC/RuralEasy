import requests

url = "https://api.apilayer.com/exchangerates_data/convert"

headers= {
  "apikey": "sP6a67SbU3MTpjYzoapzO3zOCy0nn14W"
}

params = {
    "to": "USD",
    "from": "BRL",
    "amount": "1000"
}

resposta = requests.request("GET", url, headers=headers, params=params)

if resposta.status_code != 200:
    print("Erro ",resposta.status_code) 
else:
    print(resposta.json())