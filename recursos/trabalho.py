import pyttsx3


def falar_boas_vindas(nome):
    try:
        voz = pyttsx3.init()
        voz.say("Torre de controle chamando. Boa viagem, piloto " + nome + "!")
        voz.runAndWait()
    except Exception:
        print("A voz do Windows está indisponível.")