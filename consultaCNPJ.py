import requests

headers = {
    "Accept": "application/json",
    "Authorization": "...Bearer code aqui..."
}

cnpj = "..."

url = f"https://gateway.apiserpro.serpro.gov.br/consulta-cnpj-df-trial/v2/basica/{cnpj}"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Erro ao acessar a API: {response.status_code}")
    print(response.text)
