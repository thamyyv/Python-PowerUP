import pyautogui # No terminal: pip install pyautogui
import pandas # No terminal:  pip install pandas numpy openpyxl
import time
pyautogui.PAUSE = 0.3

# pyautogui.click -- clica ciom o mouse
# pyautogui.write -- escreve um texto
# pyautogui.press -- aperta 1 tecla
# pyautogui.hotkey -- atalho (combinação de teclas)

# PASSO A PASSO DO PROJETO

#------------------------------------------------------------------------------------   
# PASSO 1: ENTRAR NO SITE DA EMPRESA
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

# Abrir o Chrome
pyautogui.press("win")
pyautogui.write ("brave")
pyautogui.press ("enter")

time.sleep(3)

# Entrar no link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write (link)
pyautogui.press ("enter")

# Esperar o site carregar
time.sleep(3)

#------------------------------------------------------------------------------------
# PASSO 2: Fazer log In
pyautogui.click(x=213, y=368) #clicar no campo do email
pyautogui.write("123@gmail.com") #inserir seu email

pyautogui.press("tab") #passar para o campo da senha
pyautogui.write("123") #inserir sua senha
 
pyautogui.press("tab") #passar para o botão de log in
pyautogui.press("enter")
time.sleep(3)

#--------------------------------------------------------------------------------------
# PASSO 3: Importar a base de dados dos produtos
tabela = pandas.read_csv ("produtos.csv")
print(tabela)

for linha in tabela.index:
    #------------------------------------------------------------------------------------
    # PASSO 4: Cadastrar os produto
    pyautogui.click(x=206, y=262)

    codigo = tabela.loc[linha, "codigo"]

    # Preencher os ccampos
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):    
        pyautogui.write(str(tabela.loc[linha, "obs"]))

    # Apertar para enviar
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(999)