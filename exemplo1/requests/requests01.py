import requests

resposta = requests.get("http://www.google.com/")
#resposta = requests.get("http://www.google.com/pagina-inexistente")
print("Status code: ",resposta.status_code) 
print("Content-Type: ",resposta.headers['Content-Type']) 
print("**********Cabeçalho da resposta***********") 
print(resposta.headers)
print("**********Corpo da resposta***************") 
print(resposta.content)