from turtle import Turtle
import time
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)] # Posições de início dos três segmentos iniciais da cobra
MOVE_DISTANCE = 20 # Distância percorrida pela cobra numa iteração do loop while no módulo main
UP = 90 # As constantes UP, DOWN, LEFT e RIGHT definem para os ângulos para que uma tartaruga aponte para cima, baixo, esquerda e direita respectivamente
DOWN = 270
LEFT = 180
RIGHT = 0

# Uma cobra é composta por tartarugas brancas em formato de quadrado, seus segmentos, que juntas formam a cobra
class Snake:

    def __init__(self): 
        self.segments = [] # Lista que conterá os segmentos da cobra
        self.create_snake() # Cria a cobra

    # Cria uma cobra de tamanho de três segmentos na posição inicial (centro da tela)
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
        self.head = self.segments[0] # Define que o segmento na 1ª posição da lista será a cabeça da cobra

    # Adiciona um novo segmento à cobra
    def add_segment(self, position): 
        new_segment = Turtle("square") # Cria um novo segmento com o formato de quadrado
        new_segment.color("white") # Define a cor do segmento como branca
        new_segment.penup() # penup() faz com que o segmento não deixe um rastro quando se mover
        new_segment.goto(position) # Coloca o novo segmento em sua posição na cobra
        self.segments.append(new_segment) # Adiciona o novo segmento na lista de segmentos
    
    # Deleta a cobra atual e cria uma nova no centro da tela
    def reset(self): 
        time.sleep(0.5) # Delay de 500ms
        for seg in self.segments:
            seg.hideturtle() # Torna todos os segmentos da cobra invisíveis
        self.segments.clear() # Esvazia a lista de segmentos
        self.create_snake() # Cria uma nova cobra

    # Aumenta o comprimento da cobra adcionando um segmento ao fim dela
    def extend(self):
        self.add_segment(self.segments[-1].position())

    # Move a cobra para frente
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1): # Para cada segmento da cobra:
            new_x = self.segments[seg_num - 1].xcor() # Obtém as coordenadas do segmento anterior
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y) # Move o segmento para a posição do segmento anterior
        self.head.forward(MOVE_DISTANCE) # Move a cabeça da cobra para frente

    # Faz com que a cobra se direcione para cima
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    # Faz com que a cobra se direcione para baixo
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    # Faz com que a cobra se direcione para a esquerda
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    # Faz com que a cobra se direcione para a direita
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
