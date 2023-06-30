from turtle import Turtle
import random

class Food(Turtle): # A classe Food herda as características da classe Turtle
# Então a comida é uma tartaruga praticamente
    def __init__(self): # Método construtor: 
        super().__init__() # Chama o método construtor de turtle
        self.shape("circle") # Configura a forma da comida para um círculo
        self.penup() # penup() faz com que a comida não deixe traços enquanto se move
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) # Configura o tamanho pela altura e largura
        self.color("blue") # Escolhe a cor azul para a comida
        self.speed("fastest") # Retira a animação da comida, para que ela possa reaparecer em outro lugar da tela assim que for comida
        self.refresh() # Posiciona comida

    def refresh(self): # Escolhe coordenadas aleatórias dentro interface para posicionar a comida
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
