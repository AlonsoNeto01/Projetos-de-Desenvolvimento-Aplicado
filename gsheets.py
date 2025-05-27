import gspread
import os
import json
from google.oauth2.service_account import Credentials

def get_client():
    creds_json = os.getenv("GOOGLE_SHEETS_CREDENTIALS_JSON")
    if not creds_json:
        raise ValueError("⚠️ Erro: Credenciais não encontradas! Verifique os secrets no Streamlit.")

    creds_dict = json.loads(creds_json)

    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = Credentials.from_service_account_info(creds_dict, scopes=scopes)
    client = gspread.authorize(creds)
    return client

def get_sheet():
    client = get_client()
    sheet = client.open("Contatos").sheet1  # Nome da planilha precisa ser exatamente igual
    return sheet

def listar_contatos():
    sheet = get_sheet()
    dados = sheet.get_all_records()
    return dados

