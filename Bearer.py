# Neste codigo você tem a solicitação do Bearer Token conforme o segundo passo da documentação https://apicenter.estaleiro.serpro.gov.br/documentacao/consulta-cnpj/pt/quick_start/ 
# Basta substituir o CONSUMER_KEY e CONSUMER_SECRET por suas credenciais e executar este codigo.

import base64
import requests
from requests.auth import HTTPBasicAuth

CONSUMER_KEY = "..."
CONSUMER_SECRET = "..."

auth_string = f"{CONSUMER_KEY}:{CONSUMER_SECRET}"
auth_base64 = base64.b64encode(auth_string.encode('utf-8')).decode('utf-8')

url = "https://gateway.apiserpro.serpro.gov.br/token"

headers = {
    "Authorization": f"Basic {auth_base64}",
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "grant_type": "client_credentials"
}

response = requests.post(url, headers=headers, data=data)

if response.status_code == 200:
    token_data = response.json()  
    access_token = token_data.get('access_token')  
    print(f"Token de Acesso: {access_token}")
else:
    print(f"Erro ao obter o token: {response.status_code} - {response.text}")
