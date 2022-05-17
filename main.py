from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *


# Classe para criação dos principais elementos gráficos.
class MainDesign:
    def __init__(self, screenHeight, screenWidth):
        # Tamanho de tela em que o programa será exibido.
        self.screenHeight = screenHeight
        self.screenWidth = screenWidth

    def createAppScreen(self):
        # Função que define as caracteristicas da tela principal.
        root.title("Editor De Texto Python")
        root.minsize(width=self.screenWidth, height=self.screenHeight)
        root.maxsize(width=self.screenWidth, height=self.screenHeight)
        root.tk_setPalette(background='dimgrey', activeBackground='white', activeForeground='black',
                           foreground='snow', insertBackground='black', selectBackground='black', )

    def createAppNavbar(self):
        # Função que criar a barra de navegação superior do programa(novo arquivo e etc).
        navbar = Menu(root)
        menuNavbar = Menu(navbar, tearoff=0)
        menuNavbar.add_command(label="Novo Arquivo", command=FileAdm().createFile, font=("Arial", 10))
        menuNavbar.add_command(label="Abrir Arquivo", command=FileAdm().openFile, font=("Arial", 10))
        menuNavbar.add_command(label="Salvar", command=FileAdm().saveFile, font=("Arial", 10))
        menuNavbar.add_command(label="Sair", command=ErrorAdm("Fechar Programa ?", "Seu Progresso Não Será Salvo !").msgShowCloseProgram,
                               font=("Arial", 10))
        navbar.add_cascade(label="Arquivos", menu=menuNavbar)
        root.config(menu=navbar)


# Classe para gerenciamento de arquivos.
class FileAdm:
    def __init__(self):
        pass

    def createFile(self):
        # Função que cria um novo arquivo.
        msgCreate = askquestion(title="Criar Novo Arquivo", message="Deseja Criar Novo Arquivo ?")
        if msgCreate == 'yes':
            try:
                mainText.delete(0.0, END)
            except:
                ErrorAdm("Erro ao Criar Arquivo", "Impossível Criar Novo Arquivo !!!").msgShowError()

    def saveFile(self):
        # Função que salva um arquivo.
        file = asksaveasfile(mode='w', defaultextension='.txt')
        text = mainText.get(0.0, END)
        try:
            file.write(text)
        except:
            ErrorAdm("Erro ao Salvar", "Impossível Salvar o Arquivo !!!").msgShowError()

    def openFile(self):
        # Função que abre um arquivo para edição.
        try:
            file = askopenfile(mode='r')
            text = file.read()
            mainText.delete(0.0, END)
            mainText.insert(0.0, text)
        except:
            ErrorAdm("Erro ao Abrir Arquivo", "Impossível Abrir o Arquivo !!!").msgShowError()


# Classe para gerenciamento de erros.
class ErrorAdm:
    def __init__(self, title, text):
        # Titulo e Conteúdo da mensagem de erro.
        self.title = title
        self.text = text

    def msgShowError(self):
        # Função que mostra um erro ao usuário utilizando o messagebox.
        showerror(title=self.title, message=self.text)

    def msgShowCloseProgram(self):
        # Função que pergunta se o usuário deseja fechar o programa.
        msgClose = askquestion(title=self.title, message=self.text)
        if msgClose == 'yes':
            root.quit()


if __name__ == "__main__":
    # Criação da Tela Principal.
    root = Tk()
    textEditor = MainDesign(500, 500)
    textEditor.createAppScreen()

    # Criação da caixa de texto.
    mainText = Text(root, width=500, height=500, font=("Arial", 20))
    mainText.pack()

    # Criação da barra de navegação.
    textEditor.createAppNavbar()

    # Exibe a tela.
    root.mainloop()
