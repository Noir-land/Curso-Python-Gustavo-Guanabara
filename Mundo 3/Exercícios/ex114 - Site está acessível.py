'''
Crie um código em Python que teste se o site Pudim 
está acessivel pelo computador usado.
'''


import requests


def verificar_site(url):
    try:
        resposta = requests.get(url, timeout=5)
        if resposta.status_code == 200:
            print(f"O site {url} está ONLINE!")
        else:
            print(
                f"O site respondeu, mas retornou o status: {resposta.status_code}")

    except requests.ConnectionError:
        print(f"O site {url} está OFFLINE ou inacessível.")
    except requests.Timeout:
        print(f"O site {url} demorou muito para responder (Timeout).")
    except requests.RequestException as e:
        print(f"Ocorreu um erro: {e}")


verificar_site("https://pudim.com.br")
