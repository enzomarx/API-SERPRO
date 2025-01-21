import requests
import json

API_TOKEN = ""
API_URL = "https://api.serpro.gov.br/consulta-cnpj/v2"  

def consultar_cnpj(cnpj):
    url = f"{API_URL}/consultacnpj/{cnpj}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao consultar o CNPJ {cnpj}. Código de status: {response.status_code}")
        return None

def processar_quadro_societario(dados_cnpj):
    # Exemplo de como processar os dados do quadro societário
    if dados_cnpj and 'qSocio' in dados_cnpj:
        socios = dados_cnpj['qSocio']
        if socios:
            print(f"Quadro societário da empresa:")
            for socio in socios:
                nome = socio.get("nome", "Nome não disponível")
                cpf_cnpj = socio.get("cpf_cnpj", "CPF/CNPJ não disponível")
                cargo = socio.get("cargo", "Cargo não disponível")
                print(f"Nome: {nome}, CPF/CNPJ: {cpf_cnpj}, Cargo: {cargo}")
        else:
            print("Nenhum sócio encontrado para este CNPJ.")
    else:
        print("Não foi possível recuperar o quadro societário.")

cnpj = "12345678000195"  # Substitua pelo CNPJ real

dados_cnpj = consultar_cnpj(cnpj)

if dados_cnpj:
    processar_quadro_societario(dados_cnpj)



