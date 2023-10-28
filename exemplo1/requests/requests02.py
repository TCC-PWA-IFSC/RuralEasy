import requests

url = "https://api.apilayer.com/exchangerates_data/latest"
headers= {
  "apikey": "sP6a67SbU3MTpjYzoapzO3zOCy0nn14W"
}

resposta = requests.request("GET", url, headers=headers)
#resposta = requests.get(url, headers=headers)

if resposta.status_code != 200:
    print("Erro ",resposta.status_code) 
else:
    print("Content-Type: ",resposta.headers['Content-Type'])
    print("**************Dados no formato JSON************ ")
    print(resposta.json())
    print("**************Dados no formato Texto************ ")
    print(resposta.text)