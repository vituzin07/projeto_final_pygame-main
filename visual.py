import pygame

JANELA_LARGURA = 800
JANELA_ALTURA = 800

# Questão 1
ESTRADA_LARGURA = JANELA_LARGURA * 0.60 
MARCAS_ESTRADA_LARGURA = JANELA_LARGURA * 0.01 
FAIXA_DIREITA =  JANELA_LARGURA //2 + ESTRADA_LARGURA //4
FAIXA_ESQUERDA = JANELA_LARGURA //2 - ESTRADA_LARGURA // 4

def inicializar_jogo():
  pygame.init()
  pygame.display.set_caption('Corrida de carros')

  janela = pygame.display.set_mode((JANELA_LARGURA, JANELA_ALTURA))
  janela.fill((60, 220, 0))

  pygame.display.update()
  return janela

def inicializar_musica():
  pygame.mixer.init()
  pygame.mixer.music.load('assets/song.mp3')
  pygame.mixer.music.play()

def inicializar_carro(tipo):
  if tipo == 'jogador':
    return pygame.image.load('assets/car.png')
  elif tipo == 'oponente':
    return pygame.image.load('assets/otherCar.png')

def posicionar_carro(carro, horizontal, vertical):
  carro_posicao = carro.get_rect()
  carro_posicao.center = (horizontal, vertical)
  return carro_posicao

def desenhar_estrada(janela):
  # pista
    pygame.draw.rect(
        janela,
        (50, 50, 50),
        (JANELA_LARGURA/2-ESTRADA_LARGURA/2, 0, ESTRADA_LARGURA, JANELA_ALTURA))
    
    # linha central
    pygame.draw.rect(
        janela,
        (255, 240, 60),
        (JANELA_LARGURA/2 - MARCAS_ESTRADA_LARGURA/2, 0, MARCAS_ESTRADA_LARGURA, JANELA_ALTURA))
    
    # linha da esquerda
    pygame.draw.rect(
        janela,
        (255, 255, 255),
        (JANELA_LARGURA/2 - ESTRADA_LARGURA/2 + MARCAS_ESTRADA_LARGURA*2, 0, MARCAS_ESTRADA_LARGURA, JANELA_ALTURA))
    
    # linha da direita
    pygame.draw.rect(
        janela,
        (255, 255, 255),
        (JANELA_LARGURA/2 + ESTRADA_LARGURA/2 - MARCAS_ESTRADA_LARGURA*3, 0, MARCAS_ESTRADA_LARGURA, JANELA_ALTURA))

def desenhar_carros(janela, carros=None):
  for item in carros:
    janela.blit(item[0], item[1])
    

def atualizar_tela():
  pygame.display.update()

def encerrar_jogo():
  pygame.quit()