from urllib import parse 
import requests 
import sys 
import copy 

headers = dict()

def cabecalho(headers):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36', 
    'Cookies': 'PHPSESSID=l9ch345hadvt735qhaf4u5knd3; cf_clearance=OJB11jqCtZxOxA03jXRo9H9c7WkY_INbsxUTyd1dhFs-1653494635-0-150'}
    return headers


def parsing(url):
    try:
        parse_url = parse.urlsplit(url) # split na url usando parse 
    
        objeto_python = parse.parse_qs(parse_url.query) # pega o parse(objeto do parse_url, não d python)\n
        return objeto_python, parse_url
    except:
        print("erro ao fazer parsing")   
    
    
def injection(objeto_python, parse_url):
    for chave in objeto_python.keys():  
        query = copy.deepcopy(objeto_python)       
     
        for c in "'\"":
            query[chave][0] = c 
            params = parse.urlencode(query, doseq=True)
            url_final = parse_url._replace(query=params)
            URL = url_final.geturl()
            return URL

def requisicao(URL, headers):   
    try:
        req = requests.get(URL, headers=headers)
        html = req.text 
        return html 
    except:
        print("erro ao fazer requisição")


def vuln(html):
    if "Warning: mysql" in html:
        print("é vulneravel")




if __name__=="__main__":
    url = sys.argv[1]
    headers = cabecalho(headers)
    objeto_python, parse_url = parsing(url)  
    URL = injection(objeto_python, parse_url)
    html = requisicao(URL, headers)
    
    vuln(html)
    



