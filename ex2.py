import requests
def function():
    with open(r'E:\FIAP\PROGRAMAÇÃO\google clone\.py\Nova pasta\subdomains-top1million-5000.txt', 'r') as arquivo:
        subdominios = arquivo.readlines()[:20]
    return subdominios

subdominios = function()

for subdominio in subdominios:
    subdominio = subdominio.strip()
    url = f'http://{subdominio}.exemplo.com'
    try:
        req = requests.get(url)
        print(f'{url} - Status Code: {req.status_code}')
    except requests.exceptions.RequestException:
        print(f'Erro ao tentar acessar {url}')
