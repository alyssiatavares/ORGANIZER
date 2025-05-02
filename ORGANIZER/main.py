import os
from tkinter.filedialog import askdirectory #importou so a funcao askdirectory

way = askdirectory(title="Select the folder to organize") #aqui ele abre a janela para selecionar a pasta
if not way:
    print("No folder was selected. Exiting the program.")
    exit() #se o usuario nao selecionar nada, ele encerra o programa
    
file_list = os.listdir(way) #aqui ele lista os arquivos da pasta selecionada

categories = {
    "Documents": [".doc", ".docx", ".pdf", ".txt", ".pptx", ".xlsx", ".csv"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".avi", ".mov"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"],
    "Others": [],
}

for file in file_list:
    file_path = os.path.join(way, file) #aqui ele junta o caminho da pasta com o nome do arquivo
    if os.path.isdir(file_path):
        continue #se o arquivo for uma pasta, ele ignora
    
    name, extension = os.path.splitext(file) #aqui ele separa o nome do arquivo da extensao (01. Arquivo.pdf -> 01. Arquivo, .pdf)
    moved = False #aqui ele marca que o arquivo nao foi movido
    for folder in categories:
        if extension.lower() in categories[folder]:
            folder_path = os.path.join(way, folder)
            if not os.path.exists(folder_path): #aqui ele verifica se a pasta ja existe
                os.mkdir(folder_path) #aqui ele cria a pasta se ela nao existir
            os.rename(file_path, os.path.join(folder_path, file)) #aqui ele move o arquivo para a pasta correspondente
            moved = True #aqui ele marca que o arquivo foi movido
            break
    if not moved: #se o arquivo nao foi movido, ele move para a pasta Others
        folder_path = os.path.join(way, "Others")
        if not os.path.exists(folder_path): #aqui ele verifica se a pasta ja existe
            os.mkdir(folder_path)
        os.rename(file_path, os.path.join(folder_path, file)) #aqui ele move o arquivo para a pasta Others
        