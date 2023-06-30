from turtle import Screen # Importa a classe Screen para criar a interface
from snake import Snake # Importa a classe Snake para criar a cobra
from food import Food # Importa a classe Food para criar a comida
from scoreboard import Scoreboard # Importa a classe Scoreboard para criar o placar
import time

screen = Screen() #Cria a interface do módulo turtle
screen.setup(width=600, height=600) #Configura o tamanho da tela para 600x600
screen.bgcolor("black") #Configura a cor de fundo para preto
screen.title("The Snake Game") #Coloca a string "The Snake Game" como título da interface
screen.tracer(0) #Desativa as atualizações automáticas da interface (desativa as animações)

snake = Snake() #Cria a cobra
food = Food() # Cria a comida
scoreboard = Scoreboard() #Cria o placar com a pontuação atual e a maior pontuação já atingida

screen.listen() # Permite que a interface "ouça" as teclas do teclado

#Os comandos abaixo tornam possível que a cobra seja controlada tanto pelas teclas: ⬆️, ⬅️, ⬇️ e ➡️ ou pelas teclas W, A, S, D 
screen.onkey(snake.up, "Up")
screen.onkey(snake.up, "w") #Os comandos foram realizados com caracteres minúsculos e maiúsculos para o jogo ser insensitive case
screen.onkey(snake.up, "W")

screen.onkey(snake.down, "Down")
screen.onkey(snake.down, "s")
screen.onkey(snake.down, "S")

screen.onkey(snake.left, "Left")
screen.onkey(snake.left, "a")
screen.onkey(snake.left, "A")

screen.onkey(snake.right, "Right")
screen.onkey(snake.right, "d")
screen.onkey(snake.right, "D")

game_is_on = True # Variável que assumirá valor True enquanto o jogo não tiver acabado
while game_is_on:
    screen.update() # Atualiza a tela
    time.sleep(0.1) # Pausa o programa por 100ms
    snake.move() # Move a cobra

    #Detecta colisão com a comida.
    if snake.head.distance(food) < 15:
        food.refresh() # Posiciona a comida em outro lugar aleatório
        snake.extend() # Aumenta o tamanho da cobra
        scoreboard.increase_score() # Incrementa a pontuação atual

    #Detecta colisão da cobra com as os limites da interface.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280: # Talvez seja necessário ajustar esses valores para o programa funcionar corretamente em seu computador
        scoreboard.reset() # Reseta o placar
        snake.reset() # Reseta a cobrinha

    #Detecta colisão com a cauda da cobra.
    for segment in snake.segments:
        if segment == snake.head: # Se o segmento da cobra for a cabeça 
            pass
        elif snake.head.distance(segment) < 10: # Se a distância da cabeça da cobra até um de seus segmentos for menor que 10
            scoreboard.reset() # Reseta o placar
            snake.reset() # Reseta a cobrinha

screen.exitonclick() # Mantém a janela aberta
