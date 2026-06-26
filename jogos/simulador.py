# importar o módulo pgzrun para rodar o jogo
#centralizar a tela
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

import pgzrun

# criar um "ator"
quad = Actor('quadrado.png')
# definir posição do ator (x, y)
quad.pos = 300, 50

quad2 = Actor('quadrado.png')
quad2.pos = 500, 100

# criar uma "base"
base = Actor('base2.png')
# definir a posição da base
base.pos = 400, 560

# definir largura e altura da janela
WIDTH = 800
HEIGHT = 600
TITLE = "Quadrado Caindo"

# método que vai desenhar os atores na tela
def draw():
    # limpar a tela
    screen.fill("black")
    # desenhar os atores
    quad.draw()
    quad2.draw()
    base.draw()

# método que vai atualizar a posição dos atores
def update():
    # se o ator NÃO colidiu com a base...
    if not quad.colliderect(base):
        # o ator continua "caindo"
        quad.top += 5        
    
    if not quad2.colliderect(base):
        quad2.top += 8

# executar o jogo
pgzrun.go()

''' EXERCÍCIOS:

a) aumentar a velocidade de queda do quadrado ok
b) mudar a posição inicial do quadrado (colocar o quadrado mais alto) ok
c) mudar a posição da base (colocar a base mais para baixo) ok
d) mudar as figuras da base e do quadrado ok
e) colocar 2 quadrados caindo ao mesmo tempo ok

Para fazer as atividades a seguir, você deverá buscar na Internet/IA
como realizá-las no pygame zero:

f) alterar a cor de fundo da janela
===> "como alterar a cor de fundo da janela no pygame zero"
g) centralizar a janela na tela
===> "como centralizar a janela no pygame zero"
h) colocar um título na janela
===> "como colocar um título na janela no pygame zero"

'''