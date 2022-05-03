from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *

'''Declaração das variáveis globais e/ou constantes'''
TAMANHO_TELA_VERTICAL = 500
TAMANHO_TELA_HORIZONTAL = 500

'''Funções de uso Geral'''
def mostrarErro(titulo, texto):
    # Função que mostra um erro ao usuário utilizando o messagebox.
    showerror(title=titulo, message=texto)

def criarTela():
    # Função que define as caracteristicas da tela principal.
    root.title("Editor de Texto")
    root.minsize(width=TAMANHO_TELA_HORIZONTAL, height=TAMANHO_TELA_VERTICAL)
    root.maxsize(width=TAMANHO_TELA_HORIZONTAL, height=TAMANHO_TELA_VERTICAL)
    root.tk_setPalette(background='dimgrey', activeBackground='white', activeForeground='black',
                       foreground='snow', insertBackground='black', selectBackground='black',)

def criarNavbar():
    navbar = Menu(root)
    menuNavbar = Menu(navbar, tearoff=0)
    menuNavbar.add_command(label="Novo Arquivo", command=criarArquivo, font=("Arial", 10))
    menuNavbar.add_command(label="Abrir Arquivo", command=abrirArquivo, font=("Arial", 10))
    menuNavbar.add_command(label="Salvar", command=salvarArquivo, font=("Arial", 10))
    menuNavbar.add_command(label="Sair", command=fecharPrograma, font=("Arial", 10))
    navbar.add_cascade(label="Arquivos", menu=menuNavbar)
    root.config(menu=navbar)

def fecharPrograma():
    titulo = "Fechar Programa ?"
    msg = "Se Você Fechar o Programa Agora Seu Progresso Não Será Salvo !"
    sair = askquestion(title=titulo, message=msg)
    if (sair == 'yes'):
        root.quit()

'''Funções de manipulação de arquivos'''
def criarArquivo():
    # Função que cria um novo arquivo.
    global nomeArquivo
    try:
        nomeArquivo = "Novo Arquivo"
        textoPrincipal.delete(0.0, END)
    except:
        mostrarErro("Erro ao Criar Arquivo", "Impossível Criar Novo Arquivo !!!")

def salvarArquivo():
    # Função que salva um arquivo.
    arquivo = asksaveasfile(mode='w', defaultextension='.txt')
    texto = textoPrincipal.get(0.0, END)
    try:
        arquivo.write(texto)
    except:
        mostrarErro("Erro ao Salvar", "Impossível Salvar o Arquivo !!!")

def abrirArquivo():
    # Função que abre um arquivo para edição.
    try:
        arquivo = askopenfile(mode='r')
        texto = arquivo.read()
        textoPrincipal.delete(0.0, END)
        textoPrincipal.insert(0.0, texto)
    except:
        mostrarErro("Erro ao Abrir Arquivo", "Impossível Abrir o Arquivo !!!")

'''Código Principal'''
# Criação da Tela Principal.
root = Tk()
criarTela()

# Criação da caixa de texto.
textoPrincipal = Text(root, width=TAMANHO_TELA_HORIZONTAL, height=TAMANHO_TELA_VERTICAL, font=("Arial", 20))
textoPrincipal.pack()

# Criação da barra de navegação.
criarNavbar()

# Exibe a tela.
root.mainloop()
