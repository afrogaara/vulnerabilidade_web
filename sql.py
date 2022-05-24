from urllib import parse 

url = "http://www.bancocn.com/cat.php?id=2"
parse_url = parse.urlsplit(url) # split na url usando parse 
print(parse_url)
objeto_python = parse.parse_qs(parse_url.query) # pega o parse(objeto do parse_url, não d python)\n

#e transforma em objeto do python
#netloc = dominio #path #query #fragment 

for chave in objeto_python.keys():  
    for c in "\"'":
        objeto_python[chave] = c   
        chave_encode = parse.urlencode(objeto_python)
        url_final = parse_url._replace(query=chave_encode) #resultado é um objeto do python 
        print(url_final)
          