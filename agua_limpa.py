from microbit import *
import speech  # biblioteca para usar o alto falante

on = False  # controla se a led está ligada ou nao
stir = 1  # controle da colher ???

while True:
    sensor = pin2.read_analog()  # lê um valor (analog indica q 
    # nao apenas 0 e 1) recebido pelo sensor de luz
    print(sensor)  # aparece na tela o valor lido


# para usar o print:
#   clicar em plotter e dps repl para ver a leitura em tempo real
#   usamos para calibrar quais valores sao pouca ou muita luz

    sleep(20)  # evitar bugs durante a leitura

# configurar diferentes leituras:
#   quando nada estiver presente (sem o copo) sensor < 230 (ou não, devemos 
#   calibrar com a luz do ambiente)

# acender as leds:
#   write: manda um valor;
#   digital: 0 ou 1;
#   1 = aceso

    if sensor > 230:

        pin13.write_digital(1)  # led azul
        pin8.write_digital(1)  # led verde
        pin12.write_digital(1)  # led verde?

        # mostrar a palavra 'esperando'
        display.scroll("ESPERANDO")

# configurações da fala do alto falante:
#   pitch: configura se a voz será fina ou grossa (do 0 -fina- ao 255 -grossa-)
#   speed: velocidade da voz (0 -rapido- ao 255 -devagar-)
#   mouth: voz bem articulada ou nao (0 -fantoche- ao 255 -super articulada-)
#   throat: voz relaxada ou tensa (0 -super tensa- ao 255 
# -totalmente relaxada-)

        speech.say("esperando para testar", speed=120, pitch=0, 
                   throat=100, mouth=0)

        stir = 1  # controla quando a colher deve ser mexida

    # caso a agua esteja limpa:
    elif sensor > 100 and sensor <= 230:
        if stir == 1:
            # se stir estiver ligada (???), ligamos o motor:
            pin15.write_digital(1)
            sleep(2000)  # motor funciona por 2s
            stir = 2  # motor para de girar
            if sensor > 100 and sensor <= 230:
                # desligar o motor:
                pin15.write_digital(0)  # desligar o motor
                pin13.write_digital(1)  # acender led azul para indicar q a 
                # agua está límpida
                pin8.write_digital(0)  # desligar led verde
                pin12.write_digital(0)  # apagar led vermelho
                display.show("LIMPA")
                speech.say("limpa!", speed=120, pitch=0, throat=100, mouth=0)

    # caso a agua esteja turva:
    elif sensor > 80 and sensor <= 100:
            pin13.write_digital(0)
            pin8.write_digital(1)  # ligar apenas o led verde
            pin12.write_digital(0)
            display.show("TURVA")
            speech.say("turva!", speed=120, pitch=0, 
                       throat=100, mouth=0)
            stir = 1  
            # caso o sensor leia novamente um valor referente a agua limpa, 
            # aciona a colher

    # caso a agua esteja suja:
    elif sensor > 60 and sensor <= 80:
        # acender os leds dos pinos 12 e 13 para obter a cor roxa
        pin13.write_digital(1)
        pin8.write_digital(0)
        pin12.write_digital(1)
        display.scroll("SUJA")
        speech.say("suja!", speed=120, pitch=0, throat=100, mouth=0)
        stir = 1

    # agua imbebível
    elif sensor > 0 and sensor <= 60:
        # acender apenas a led vermelha
        pin13.write_digital(1)
        pin8.write_digital(0)
        pin12.write_digital(1)
        display.scroll("IMBEBIVEL")
        speech.say("imbebível!", speed=120, pitch=0, throat=100, mouth=0)
        stir = 1

# quando apertamos o botão A:
#   se a led estiver acesa (on = True) ela apagará (on = False)
#   e vice-versa

    if button_a.was_pressed():
        # se a led está acesa:
        if on is True:
            on = False
        elif on is False:
            on = True

    if on is True:
        pin14.write_digital(1)
    elif on is False:
        pin14.write_digital(0)     
