from turtle import Turtle
ALIGNMENT = "center" # Constante que define o alinhamento no centro
FONT = ("Courier", 24, "normal") # Constante que contém a tupla definindo a fonte, tamanho da fonte tamanho, e tipo da fonte

class Scoreboard(Turtle): # Scoreboard herda de Turtle

    def __init__(self): # Método construtor
        super().__init__()
        self.score = 0 # score é o atributo que é igual a pontuação da partida atual
        historic = open("Scoreboard.txt", "r") # Todas os high scores já alcançados são salvos em Scoreboard, para saber qual é o high score atual
        list_scores = historic.readlines() # Lê o arquivo e guarda todos os high scores na lista list_scores
        if len(list_scores) != 0: # Se a lista não estiver vazia: 
            self.high_score = int(list_scores[-1].rstrip()) # será definido como high score o maior número da lista, que será sempre o último
            print(self.high_score)
        else:
            self.high_score = 0 # Caso contrário, o high score é definido como 0
        historic.close()
        self.color("white") # Para se definir a cor da letra do placar como branca, pode-se usar o método color() da classe Turtle
        self.penup() # Faz com que a "tartaruga" não deixe traços quando se movimentar
        self.goto(0, 270) # Coloca o placar para o topo da janela na parte central
        self.hideturtle() # Esconde a "tartaruga"
        self.update_scoreboard() # Exibe o placar

    def update_scoreboard(self): # Atualiza o placar
        self.clear() # Deleta o placar anterior
        self.write(f"Score: {self.score}  High score: {self.high_score}", align=ALIGNMENT, font=FONT) # Reescreve o novo placar com os novos valores
    
    def reset(self): # Reseta o placar e salva a pontuação atual em Scoreboard.txt se ela for maior que o high score atual
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Scoreboard.txt", "a") as file:
                file.write(str(self.high_score) + "\n")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self): # Incrementa o placar em um ponto
        self.score += 1
        self.update_scoreboard()

