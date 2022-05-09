import requests

try:
    with open("wordlist.txt", "r") as arquivo:
        words = arquivo.readlines()
except:
    print("arquivo não encontrado")

def brute(url, words):
	for word in words:
		try:
			url_diretorio = "{}/{}".format(url, word.strip())
			requisicao = requests.get(url_diretorio)
			resposta = requisicao.status_code
			if resposta != 404:
				print(f"FOUND - > {url_diretorio} - {resposta}")
			else:
				print(f"NOT FOUND -> {url_diretorio} - {resposta}")
		except Exception as error:
			print("erro", erro)

url = input("URL: ")
brute(url, words)
