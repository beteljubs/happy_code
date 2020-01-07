from microbit import *
import music

# variável responsável por descer e subir o elevador
up = False

'''
revisar funções
seguranca(): função para controlar a segurança do elevador; não fecha se tiver gente na porta
'''

# se for ativada, desliga os motores
def seguranca():
    pin12.write_digital(0)
    pin16.write_digital(0)

    # som para avisar que foi detectado alguem na porta
    music.play(music.FUNERAL)

'''
para um botão: var = pin.read_digital()
a var receberá ou 1 ou 0 (unicos posíveis no read_digital)
    1: botão sendo pressionado
    0: botão não pressionado
obs: cor1 = cor do botão escolhido para o pino 1
'''

while True:
    button_cor1 = pin1.read_digital()
    # sensor que detectará algum passageiro
    sensor = pin2.read_analog()  '''colocar alguma explicação sobre isso'''

    # se o botão for pressionado, checaremos se há alguem na porta
    if button_cor1 is (1) and up is True:

        if sensor > 300:
            # elevador sobe:
            pin12.write_digital(1)
            pin16.write_digital(0)
            # tempo para chegar no topo:
            sleep(9000)
            # desligar os dois pinos do motor:
            pin12.write_digital(0)
            pin16.write_digital(0)
            # acender led para avisar que os passageiros podem sair
            pin8.write_digital(1)
            sleep(2000)
            pin8.write_digital(0)
            up = False  # indica que já está no topo

        else:  # caso tenha alguém na porta
            seguranca()  # chamar a função

    elif button_cor1 is (1) and up is False:
        if sensor > 300:
            # agora será ao contrário o pino que ta ligado, pois trocamos o sentido do motor
            pin12.write_digital(0)
            pin16.write_digital(1)
            sleep(9000)
            pin12.write_digital(0)  # para os motores
            pin16.write_digital(0)
            pin8.write_digital(1)  # acende a led
            music.play(music.POWER_DOWN)
            sleep(2000)
            up = True  # indica que está no térreo
        else:
            seguranca()
            
