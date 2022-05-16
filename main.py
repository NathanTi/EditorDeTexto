from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *


class ProgramaPrincipal:
    def __init__(self, telaVertical, telaHorizontal):
        self.tamanhoTelaVertical = telaVertical
        self.tamanhoTelaHorizontal = telaHorizontal

    def criarTela(self):
        # Função que define as caracteristicas da tela principal.
        root.title("Editor De Texto Python")
        root.minsize(width=self.tamanhoTelaHorizontal, height=self.tamanhoTelaVertical)
        root.maxsize(width=self.tamanhoTelaHorizontal, height=self.tamanhoTelaVertical)
        root.tk_setPalette(background='dimgrey', activeBackground='white', activeForeground='black',
                           foreground='snow', insertBackground='black', selectBackground='black', )

    def criarNavbar(self):
        navbar = Menu(root)
        menuNavbar = Menu(navbar, tearoff=0)
        menuNavbar.add_command(label="Novo Arquivo", command=AdmArquivos().criarArquivo, font=("Arial", 10))
        menuNavbar.add_command(label="Abrir Arquivo", command=AdmArquivos().abrirArquivo, font=("Arial", 10))
        menuNavbar.add_command(label="Salvar", command=AdmArquivos().salvarArquivo, font=("Arial", 10))
        menuNavbar.add_command(label="Sair", command=AdmErros("Fechar Programa ?", "Seu Progresso Não Será Salvo !").msgFecharPrograma,
                               font=("Arial", 10))
        navbar.add_cascade(label="Arquivos", menu=menuNavbar)
        root.config(menu=navbar)


class AdmArquivos:
    def __init__(self):
        self.nomeArquivo = "Novo Arquivo"

    def criarArquivo(self):
        # Função que cria um novo arquivo.
        try:
            textoPrincipal.delete(0.0, END)
        except:
            AdmErros("Erro ao Criar Arquivo", "Impossível Criar Novo Arquivo !!!").msgMostrarErro()

    def salvarArquivo(self):
        # Função que salva um arquivo.
        arquivo = asksaveasfile(mode='w', defaultextension='.txt')
        texto = textoPrincipal.get(0.0, END)
        try:
            arquivo.write(texto)
        except:
            AdmErros("Erro ao Salvar", "Impossível Salvar o Arquivo !!!").msgMostrarErro()

    def abrirArquivo(self):
        # Função que abre um arquivo para edição.
        try:
            arquivo = askopenfile(mode='r')
            texto = arquivo.read()
            textoPrincipal.delete(0.0, END)
            textoPrincipal.insert(0.0, texto)
        except:
            AdmErros("Erro ao Abrir Arquivo", "Impossível Abrir o Arquivo !!!").msgMostrarErro()


class AdmErros:
    def __init__(self, titulo, texto):
        self.titulo = titulo
        self.texto = texto

    def msgMostrarErro(self):
        # Função que mostra um erro ao usuário utilizando o messagebox.
        showerror(title=self.titulo, message=self.texto)

    def msgFecharPrograma(self):
        # Funcionando
        sair = askquestion(title=self.titulo, message=self.texto)
        if (sair == 'yes'):
            root.quit()


# Criação da Tela Principal.
root = Tk()
programa = ProgramaPrincipal(500, 500)
programa.criarTela()

# Criação da caixa de texto.
textoPrincipal = Text(root, width=programa.tamanhoTelaHorizontal, height=programa.tamanhoTelaVertical, font=("Arial", 20))
textoPrincipal.pack()

# Criação da barra de navegação.
programa.criarNavbar()

# Exibe a tela.
root.mainloop()
