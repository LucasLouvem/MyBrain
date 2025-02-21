import pdfplumber;
import pandas as pd;
import re;

def extrair_dados_pdf(pdf_path):
    dados = {}
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
                texto = page.extract_text()
                if texto:
                    linhas = texto.split("\n")
                    for linha in linhas:
                        match = re.match(r"(\d{2}/\d{2}/\d{4} - \w+) S\d (.+?) - .+ - GAP GL", linha)
                        if match:
                            data_dia, nome = match.groups()
                            if data_dia not in dados:
                                dados[data_dia] = []
                            dados[data_dia].append(nome)
    return dados

def salvar_em_excel(dados, output_path):
    linhas_formatadas = [[data_dia, ", ".join(nomes)] for data_dia, nomes in dados.items()]
    df = pd.DataFrame(linhas_formatadas, columns=["Data e Dia", "Nomes"])
    df.to_excel(output_path, index=False)
    print(f"Arquivo salvo em {output_path}")

pdf_path = "/home/lucas/Downloads/fevereiro.pdf"
output_path = "/home/lucas/Downloads/escala.xlsx"

dados = extrair_dados_pdf(pdf_path)
salvar_em_excel(dados, output_path)
