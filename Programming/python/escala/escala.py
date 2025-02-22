# Importa as bibliotecas necessárias
import pdfplumber  # Para extrair texto de arquivos PDF
import pandas as pd  # Para manipulação de dados e criação de DataFrames
import re  # Para uso de expressões regulares
import os  # Para manipulação de caminhos e arquivos
import tkinter as tk  # Para criar a interface gráfica
from tkinterdnd2 import DND_FILES, TkinterDnD  # Para adicionar funcionalidade de "arrastar e soltar" arquivos
from tkinter import messagebox, filedialog  # Para exibir mensagens de erro ou sucesso e escolher arquivos
from collections import OrderedDict  # Para criar um dicionário ordenado

# Função para extrair dados do PDF
def extrair_dados_pdf(pdf_path):
    dados = OrderedDict()  # Cria um dicionário ordenado para armazenar os dados extraídos
    # Expressão regular para capturar as informações do formato esperado no PDF
    regex = re.compile(r"(\d{2}/\d{2}/\d{4} - \w+) (S\d .+?) - .+ - GAP GL")

    with pdfplumber.open(pdf_path) as pdf:  # Abre o PDF usando o pdfplumber
        for page in pdf.pages:  # Itera sobre todas as páginas do PDF
                texto = page.extract_text()  # Extrai o texto da página
                if texto:  # Verifica se o texto foi extraído com sucesso
                    for linha in texto.split("\n"):  # Separa o texto em linhas
                        match = regex.match(linha)  # Tenta encontrar uma correspondência com a expressão regular
                        if match:  # Se houver uma correspondência, extrai os dados
                            data_dia, nome = match.groups()  # Captura os dados de data e nome
                            if data_dia not in dados:  # Se a data ainda não está no dicionário, cria uma nova lista
                                dados[data_dia] = []
                            dados[data_dia].append(nome)  # Adiciona o nome à lista correspondente à data
    return dados  # Retorna os dados extraídos do PDF

# Função para salvar os dados extraídos em um arquivo Excel
def salvar_em_excel(dados, output_path):
    # Cria um DataFrame a partir dos dados extraídos, unindo os nomes por vírgula
    df = pd.DataFrame([
        [data_dia, ", ".join(nomes)]
        for data_dia, nomes in dados.items()
    ], columns=("Data e Dia", "Nomes"))

    # Cria um arquivo Excel e escreve o DataFrame nele
    with pd.ExcelWriter(output_path, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name='Escala')  # Escreve os dados no Excel

        # Obtenção do workbook e worksheet para formatação adicional
        workbook = writer.book
        worksheet = writer.sheets['Escala']

        # Define a formatação para centralizar o texto nas células
        cell_format = workbook.add_format({'align': 'center', 'valign': 'vcenter'})

        # Aplica a formatação centralizada nas colunas A e B
        worksheet.set_column('B:B', 70, cell_format)  # Coluna B: Nomes
        worksheet.set_column('A:A', 20, cell_format)  # Coluna A: Data e Dia

        writer.close()  # Fecha o escritor do arquivo Excel
    
    # Imprime uma mensagem informando o caminho do arquivo gerado
    print(f"Arquivo salvo em {output_path}")

# Função que será chamada quando o arquivo for arrastado ou solto na interface gráfica
def processar_arquivo(event):
    # Obtém o caminho do arquivo PDF
    pdf_path = event.data.strip().replace('{', '').replace('}', '')  # Remove chaves caso existam
    if not pdf_path.lower().endswith(".pdf"):  # Verifica se o arquivo é um PDF
        messagebox.showerror("Erro", "Por favor, solte um arquivo PDF válido.")  # Exibe um erro caso não seja PDF
        return
    
    # Cria o caminho do arquivo de saída (Excel)
    pasta, nome_pdf = os.path.split(pdf_path)  # Obtém a pasta e o nome do arquivo PDF
    nome_excel = os.path.splitext(nome_pdf)[0] + ".xlsx"  # Renomeia o arquivo para .xlsx
    output_path = os.path.join(pasta, nome_excel)  # Cria o caminho completo para o arquivo de saída

    try:
        dados = extrair_dados_pdf(pdf_path)  # Chama a função para extrair os dados do PDF
        salvar_em_excel(dados, output_path)  # Chama a função para salvar os dados no Excel
        # Exibe uma mensagem de sucesso
        messagebox.showinfo("Sucesso",f"Conversão concluida!\narquivo salvo em:\n{output_path}")
    except Exception as e:
        # Exibe uma mensagem de erro caso ocorra algum problema
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Função para permitir que o usuário selecione um arquivo PDF por meio de uma janela de diálogo
def selecionar_pdf():
    pdf_path = filedialog.askopenfilename(filetypes=[("Arquivos PDF", "*.pdf")])  # Abre a janela de seleção de arquivo
    if not pdf_path:  # Se nenhum arquivo for selecionado, retorna
        return
    
    # Cria o caminho do arquivo de saída (Excel)
    pasta, nome_pdf = os.path.split(pdf_path)  # Obtém a pasta e o nome do arquivo PDF
    nome_excel = os.path.splitext(nome_pdf)[0] + ".xlsx"  # Renomeia o arquivo para .xlsx
    output_path = os.path.join(pasta, nome_excel)  # Cria o caminho completo para o arquivo de saída

    try:
        dados = extrair_dados_pdf(pdf_path)  # Chama a função para extrair os dados do PDF
        salvar_em_excel(dados, output_path)  # Chama a função para salvar os dados no Excel
        # Exibe uma mensagem de sucesso
        messagebox.showinfo("Sucesso",f"Conversão concluida!\narquivo salvo em:\n{output_path}")
    except Exception as e:
        # Exibe uma mensagem de erro caso ocorra algum problema
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Configuração da interface gráfica
root = TkinterDnD.Tk()  # Cria a janela principal com suporte a "arrastar e soltar"
root.title("Conversor de Escala (PDF -> Excel)")  # Define o título da janela
root.geometry("400x200")  # Define o tamanho da janela
root.resizable(False,False)  # Impede o redimensionamento da janela

# Label explicativa
label = tk.Label(root, text="Selecione o arquivo PDF", font=("Arial", 14), fg="blue")  
label.pack(pady=10)

# Botão para selecionar o arquivo PDF
btn_selecionar = tk.Button(root, text="Selecionar PDF", font=("Arial", 14), command=selecionar_pdf)
btn_selecionar.pack(pady=10)

# Área de "arrastar e soltar" para o arquivo PDF
frame_drop = tk.Label(root, text="Solte o arquivo em PDF aqui.", bg="lightgreen", fg="black", font=("Arial", 12), relief="ridge", width=40, height=5)
frame_drop.pack(pady=20)

# Registra a área para receber o arquivo PDF arrastado
frame_drop.drop_target_register(DND_FILES)
frame_drop.dnd_bind("<<Drop>>", processar_arquivo)  # Define o que acontece quando um arquivo é solto

# Executa a interface gráfica
root.mainloop()
