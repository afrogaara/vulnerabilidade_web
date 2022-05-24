from urllib import parse 
import requests 
import sys 
#lembrar de usar argumentos 
header = dict()

def cabecalho(header):
    header['User-Agent'] =  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
    header['Cookies'] = 'Cookies' 'cookie-banner-consent-accepted=false; glb_uid="uYlGaiZh1JyTJ65XSL9RtTQC_YkBMCnNpZfmP0EJqy0="; GLBEXP=Jerw+PyFhonvjyWSv6iFwBmVwl6AkI/D4Z23yTBqWfU=; kppid=6117059538656703488; hsid=5938eca4-26f3-4765-beaf-492e2cc8a958; nav13574=10c6b464a48cf0e1bf8f66a6b510|2_145; _pbjs_userid_consent_data=3524755945110770; _li_dcdm_c=.globo.com; _lc2_fpi=da5812f14a1e--01g3w1e7n92prpnzct59jr86r7; pbjs_sharedId=6f395a48-fcb0-4596-84fc-ef660c1ea15b; utag_main=v_id:0180f81717d40053a67f64f5457805073001506b00bd0$_sn:1$_se:2$_ss:0$_st:1653431903179$ses_id:1653429704662%3Bexp-session$_pn:2%3Bexp-session; _cb=CE_c1KDS4z2ICRqJIL; _chartbeat2=.1653430103893.1653430103893.1.aJAqpBuk8i4DASJ3BDa8ipaBfxVAB.1; _cb_svref=null; _gid=GA1.2.1418011252.1653430104; _gat_g1_portal=1; sophi.session=1.47515a4e-822c-47bd-b931-30e1a8e2ecce.1653430103947.1.1653430103947..32de796f-4a2a-4650-99e2-e1aaeeee1dce; __gads=ID=a7ec050f00ec6308:T=1653430103:S=ALNI_MYK7xjIgurN2DytG7-CagL3Jy2cIA; __gpi=UID=00000604dc1fca98:T=1653430103:RT=1653430103:S=ALNI_MZtKVURrrdtyZOlR8nKg5fLI8CJ3g; _fbp=fb.1.1653430104304.1301363585; _ga_4DF8YFDHV7=GS1.1.1653430104.1.0.1653430104.0; _ga=GA1.1.1993142322.1653430104; _gcl_au=1.1.448730340.1653430105; FCNEC=[["AKsRol8tkXjPE9OgPY6K4OVsJmApXQeX-65X5ndxbsbhMWgL4Be2m-hKLGP0EKHXwS0zdtxgZDOLaCyG9YOdZy1bzCCa-KF8Axh7iA1Fi_OudGRNCogznUmtFjZ45I59_N-Wt-yI_I60XGJLbptaokGVo_lL8Pnw9g=="],null,[]]; _lr_sampling_rate=100'
    return header


def requisicao(url, header):
    try:
        req = requests.get(url, headers=header)
        if req.status_code == 200:
            return req 
        else:
            print("Erro ao fazer requisição!")
    except Exception as erro:
        print(error)
    pass


def html(req):
    try:
        parse_url = parse.urlsplit(req) # split na url usando parse 
        objeto_python = parse.parse_qs(parse_url.query) # pega o parse(objeto do parse_url, não d python)\n
    except:
        print("erro ao fazer parsing")
    for chave in objeto_python.keys():  
        for c in "\"'":
            objeto_python[chave] = c   
            chave_encode = parse.urlencode(objeto_python)
            url_final = parse_url._replace(query=chave_encode) #resultado é um objeto do python 
            print(url_final)

if __name__=="__main__":
    if cabecalho(header):
        req = requisicao(url, header)
        html(req)
