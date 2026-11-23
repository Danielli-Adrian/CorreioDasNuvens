import pygame
import random
from recursos.funcoes import inicializarBancoDeDados, limpar_tela, escreverDados, maior_pontuador
from recursos.trabalho import falar_boas_vindas


def jogar():
    fundoX = 0
    aviaoX = 95
    aviaoY = 325
    movimentoY = 0
    nuvemX = 1000
    nuvemY = random.randint(0, 621)
    velocidadeNuvem = 5
    passaroX = 1000
    passaroY = 160
    raioSol = 32
    crescimentoSol = 0.12
    pontos = 0
    pausado = False
    ventoSound.play()
    pygame.mixer.music.play(-1)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return None
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                return None
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                pausado = not pausado
                if pausado:
                    pygame.mixer.pause()
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.unpause()
                    pygame.mixer.music.unpause()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_UP:
                movimentoY = -7
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_DOWN:
                movimentoY = 7
            elif evento.type == pygame.KEYUP and evento.key == pygame.K_UP and movimentoY < 0:
                movimentoY = 0
            elif evento.type == pygame.KEYUP and evento.key == pygame.K_DOWN and movimentoY > 0:
                movimentoY = 0

        if not pausado:
            aviaoY = aviaoY + movimentoY
            if aviaoY < 0:
                aviaoY = 0
            elif aviaoY > 649:
                aviaoY = 649

            nuvemX = nuvemX - velocidadeNuvem
            if nuvemX < -135:
                nuvemX = 1000
                nuvemY = random.randint(0, 621)
                velocidadeNuvem = velocidadeNuvem + 1
                pontos = pontos + 1
                ventoSound.play()

            fundoX = fundoX - 1
            if fundoX <= -1000:
                fundoX = 0

            passaroX = passaroX - 2
            if passaroX < -40:
                passaroX = 1000
                passaroY = random.randint(90, 550)

            raioSol = raioSol + crescimentoSol
            if raioSol >= 40 or raioSol <= 26:
                crescimentoSol = -crescimentoSol

            pixelsAviaoX = set(range(aviaoX, aviaoX + 116))
            pixelsAviaoY = set(range(aviaoY, aviaoY + 51))
            pixelsNuvemX = set(range(nuvemX, nuvemX + 135))
            pixelsNuvemY = set(range(nuvemY, nuvemY + 79))
            if len(pixelsAviaoX.intersection(pixelsNuvemX)) > 20:
                if len(pixelsAviaoY.intersection(pixelsNuvemY)) > 20:
                    escreverDados(nome, pontos)
                    return pontos

        tela.blit(fundo, (fundoX, 0))
        tela.blit(fundo, (fundoX + 1000, 0))
        pygame.draw.circle(tela, amarelo, (910, 113), int(raioSol))
        tela.blit(passaro, (passaroX, passaroY))
        tela.blit(aviao, (aviaoX, aviaoY))
        tela.blit(nuvem, (nuvemX, nuvemY))

        pygame.draw.rect(tela, azul, (15, 12, 154, 39), border_radius=9)
        texto = fonteMenu.render("Pontos: " + str(pontos), True, branco)
        tela.blit(texto, (25, 20))
        texto = fontePequena.render("Press Space to Pause Game.", True, branco)
        tela.blit(texto, (25, 662))

        if pausado:
            pygame.draw.rect(tela, azul, (385, 302, 230, 96), border_radius=12)
            texto = fonteTitulo.render("PAUSE", True, branco)
            tela.blit(texto, (410, 319))

        pygame.display.update()
        relogio.tick(60)


def dead(pontos):
    pygame.mixer.music.stop()
    trovaoSound.play()
    nomeMaior, maiorPontos, dataJogada, horaJogada = maior_pontuador()
    botaoJogar = pygame.Rect(60, 448, 220, 56)
    botaoSair = pygame.Rect(60, 521, 220, 56)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                return False
            elif evento.type == pygame.MOUSEBUTTONUP and evento.button == 1:
                if botaoJogar.collidepoint(evento.pos):
                    return True
                if botaoSair.collidepoint(evento.pos):
                    return False

        tela.blit(fundoDead, (0, 0))
        texto = fonteTitulo.render("Fim do voo", True, amarelo)
        tela.blit(texto, (60, 175))
        texto = fonteMenu.render(f"Seus pontos: {pontos}", True, branco)
        tela.blit(texto, (60, 260))
        texto = fonteMenu.render(f"Recorde: {nomeMaior} — {maiorPontos} ponto(s) em {dataJogada} às {horaJogada}", True, branco)
        tela.blit(texto, (60, 296))

        pygame.draw.rect(tela, azul, botaoJogar, border_radius=12)
        pygame.draw.rect(tela, amarelo, botaoJogar, 2, border_radius=12)
        texto = fonteMenu.render("Jogar de novo", True, branco)
        tela.blit(texto, (98, 463))
        pygame.draw.rect(tela, azul, botaoSair, border_radius=12)
        pygame.draw.rect(tela, amarelo, botaoSair, 2, border_radius=12)
        texto = fonteMenu.render("Sair do jogo", True, branco)
        tela.blit(texto, (108, 537))

        pygame.display.update()
        relogio.tick(60)


def start():
    nomeMaior, maiorPontos, dataJogada, horaJogada = maior_pontuador()
    recorde = "Recorde: nenhuma partida registrada"
    if nomeMaior is not None:
        recorde = f"Recorde: {nomeMaior} — {maiorPontos} ponto(s) em {dataJogada} às {horaJogada}"
    botaoJogar = pygame.Rect(60, 448, 220, 56)
    falou = False

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                return False
            elif evento.type == pygame.MOUSEBUTTONUP and evento.button == 1:
                if botaoJogar.collidepoint(evento.pos):
                    return True

        tela.blit(fundoStart, (0, 0))
        texto = fonteTitulo.render("Correio das Nuvens", True, amarelo)
        tela.blit(texto, (60, 175))
        texto = fonteMenu.render(f"Boas-vindas, {nome}!", True, branco)
        tela.blit(texto, (60, 260))
        texto = fonteMenu.render("Use as setas para subir ou descer e desviar da tempestade.", True, branco)
        tela.blit(texto, (60, 296))
        texto = fonteMenu.render("Cada nuvem evitada vale um ponto. Seu destino é o farol.", True, branco)
        tela.blit(texto, (60, 332))
        texto = fonteMenu.render(recorde, True, branco)
        tela.blit(texto, (60, 368))

        pygame.draw.rect(tela, azul, botaoJogar, border_radius=12)
        pygame.draw.rect(tela, amarelo, botaoJogar, 2, border_radius=12)
        texto = fonteMenu.render("Iniciar partida", True, branco)
        tela.blit(texto, (100, 463))

        pygame.display.update()
        if not falou:
            falar_boas_vindas(nome)
            falou = True
        relogio.tick(60)


if __name__ == "__main__":
    limpar_tela()
    inicializarBancoDeDados()
    while True:
        nome = input("Informe o nome do competidor: ").strip()
        if len(nome) > 0:
            break
        print("Nome inválido!")

    pygame.init()
    tamanho = (1000, 700)
    branco = (255, 249, 227)
    azul = (27, 58, 73)
    amarelo = (255, 217, 139)
    tela = pygame.display.set_mode(tamanho)
    pygame.display.set_caption("Correio das Nuvens")
    pygame.display.set_icon(pygame.image.load("bases/icone.png"))
    relogio = pygame.time.Clock()

    fundo = pygame.image.load("bases/background.png")
    fundoDead = pygame.image.load("bases/backgroundDead.png")
    fundoStart = pygame.image.load("bases/backgroundStart.png")
    aviao = pygame.image.load("bases/aviao.png")
    nuvem = pygame.image.load("bases/nuvem.png")
    passaro = pygame.image.load("bases/passaro.png")
    ventoSound = pygame.mixer.Sound("bases/nuvem.wav")
    trovaoSound = pygame.mixer.Sound("bases/fim.wav")
    pygame.mixer.music.load("bases/voo.wav")
    fonteMenu = pygame.font.Font(None, 29)
    fontePequena = pygame.font.Font(None, 22)
    fonteTitulo = pygame.font.Font(None, 68)

    continuar = start()
    while continuar:
        pontos = jogar()
        if pontos is None:
            break
        continuar = dead(pontos)

    pygame.quit()