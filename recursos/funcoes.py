import json
import os
from datetime import datetime


def limpar_tela():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def inicializarBancoDeDados():
    banco = open("log.dat", "a", encoding="utf-8")
    banco.close()


def escreverDados(nome, pontos):
    agora = datetime.now()
    partida = {
        "nome": nome,
        "pontos": pontos,
        "data": agora.strftime("%d/%m/%Y"),
        "hora": agora.strftime("%H:%M:%S")
    }
    banco = open("log.dat", "a", encoding="utf-8")
    banco.write(json.dumps(partida, ensure_ascii=False) + "\n")
    banco.close()


def maior_pontuador():
    nomeMaior = None
    maiorPontos = -1
    dataJogada = None
    horaJogada = None

    banco = open("log.dat", "r", encoding="utf-8")
    for linha in banco:
        if linha.strip():
            partida = json.loads(linha)
            if partida["pontos"] > maiorPontos:
                nomeMaior = partida["nome"]
                maiorPontos = partida["pontos"]
                dataJogada = partida["data"]
                horaJogada = partida["hora"]
    banco.close()
    return nomeMaior, maiorPontos, dataJogada, horaJogada