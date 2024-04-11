import pygame
import random
from pygame.locals import *
from sys import exit

pygame.init()

largura = (600, 600)

janela = pygame.display.set_mode(largura)

Ponteiro = pygame.image.load("Ponteiro.png")
Ponteiro.set_colorkey((255, 0, 255))  # roxo transparente
PonteiroClick = pygame.image.load("PonteiroClick.png")
PonteiroClick.set_colorkey((255, 0, 255))  # roxo transparente
alvo = pygame.image.load("AlvoVariante.png")
alvo.set_colorkey((255, 0, 255))  # roxo transparente
cursor = Ponteiro
relogio = pygame.time.Clock()
clicou = False

# Lista para armazenar as posições dos alvos
alvos_pos = []

# Variável de pontuação inicial
pontuacao = 0

# Fonte para exibir a pontuação na tela
fonte = pygame.font.Font(None, 36)

# Fonte para as mensagens especiais
fonte_mensagem = pygame.font.Font(None, 48)

# Variáveis para controlar a exibição das mensagens especiais
exibir_mensagem_nice = False
exibir_mensagem_continue = False
exibir_mensagem_incansavel = False
mensagem_timer = 0

while True:
    relogio.tick(15)
    janela.fill((255, 255, 255))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            cursor = PonteiroClick
            clicou = True
        else:
            cursor = Ponteiro
            clicou = False

    mousex, mousey = pygame.mouse.get_pos()
    mouselocation = janela.blit(cursor, (mousex, mousey))

    # Se a lista de alvos estiver vazia ou um número aleatório for menor que 0.03, adiciona um novo alvo
    if not alvos_pos or random.random() < 0.03:
        # Adiciona um novo alvo com posição aleatória dentro da janela
        alvos_pos.append((random.randint(0, largura[0] - alvo.get_width()), random.randint(0, largura[1] - alvo.get_height())))

    # Desenha todos os alvos na tela
    for alvo_pos in alvos_pos:
        janela.blit(alvo, alvo_pos)

    # Verifica se o mouse colidiu com algum alvo e se o botão do mouse foi clicado
    for alvo_pos in alvos_pos:
        alvo_rect = pygame.Rect(alvo_pos, alvo.get_size())
        if alvo_rect.colliderect(mouselocation) and clicou:
            # Remove a posição do alvo da lista
            alvos_pos.remove(alvo_pos)
            # Incrementa a pontuação
            pontuacao += 1

    # Exibe a pontuação na tela
    texto_pontuacao = fonte.render(f'Pontuação: {pontuacao}', True, (0, 0, 0))
    janela.blit(texto_pontuacao, (10, 10))

    # Exibe as mensagens especiais
    if pontuacao == 10:
        exibir_mensagem_nice = True
        mensagem_timer = pygame.time.get_ticks()
    elif pontuacao == 20:
        exibir_mensagem_continue = True
        mensagem_timer = pygame.time.get_ticks()
    elif pontuacao == 30:
        exibir_mensagem_incansavel = True
        mensagem_timer = pygame.time.get_ticks()

    if exibir_mensagem_nice:
        texto_mensagem_nice = fonte_mensagem.render("NICE", True, (0, 255, 0))
        janela.blit(texto_mensagem_nice, (10, 60))
        if pygame.time.get_ticks() - mensagem_timer >= 4000:
            exibir_mensagem_nice = False

    if exibir_mensagem_continue:
        texto_mensagem_continue = fonte_mensagem.render("CONTINUE", True, (0, 255, 0))
        janela.blit(texto_mensagem_continue, (10, 60))
        if pygame.time.get_ticks() - mensagem_timer >= 4000:
            exibir_mensagem_continue = False

    if exibir_mensagem_incansavel:
        texto_mensagem_incansavel = fonte_mensagem.render("INCANSÁVEL", True, (0, 255, 0))
        janela.blit(texto_mensagem_incansavel, (10, 60))
        if pygame.time.get_ticks() - mensagem_timer >= 4000:
            exibir_mensagem_incansavel = False

    pygame.display.update()


