from microbit import *  # importa TODA a biblioteca do microbit
import random  # uso de numeros escolhidos aleatoriamente

interval = 5000  # tempo de espera até o tamagochi fazer algo

# variáveis de imagens:

# imagens olhando para os lados
right = Image(
    "00000:"
    "90900:"
    "00000:"
    "90009:"
    "09990")

left = Image(
    "00000:"
    "00909:"
    "00000:"
    "90009:"
    "09990")

# imagens comendo
abre_boca = Image(
    "09090:"
    "00000:"
    "09990:"
    "90009:"
    "09990")

fecha_boca = Image(
    "09090:"
    "00000:"
    "00000:"
    "09990:"
    "00000")

# é usada?
sono = Image(
    "99099:"
    "00000:"
    "00000:"
    "09990:"
    "00000")

# declaração da classe do joguinho q criaremos
class Jogo():
    def __init__(self):  # self (?)
        self.last = None  # comparar o vetor do movimento do bichinho (?)
        self.x_pos = 0  # x inicial do bichinho
        self.y_pos = 0  # y inicial do bichinho
        display.scroll("Pegue a bola")  # aparece quando A + B for pressionado
        self.draw()  # chamando função draw que vamos logo definir

    # define a imagem que aparece no display durante o jogo
    def draw(self):
        # bola c brilho 5 no meio do display
        imagem_bola = Image(
            "00000:"
            "00000:"
            "00500:"
            "00000:"
            "00000")

        # add na imagem posição inicial do bichinho:
        imagem_bola.set_pixel(self.x_pos, self.y_pos, 9)
        display.show(imagem_bola)  # mostra a imagem inicial do jogo

    # função do inicio do jogo - roda em loop
    def start(self):
        while True:  # loop
            # funções de controle que declararemos em seguida:
            self.check_win()  # controla se o bichinho pegou a bola
            self.check_dir()  # controla a posição do bichinho

            # se apertamos em algum botão, sai do jogo:
            if button_a.is_pressed():
                break
            if button_b.is_pressed():
                break

    # função que irá aleatorizar uma nova posição para o bichinho
    def novo_lugar(self):
        self.x_pos = random.randrange(5)  # novo valor para a posição em x
        self.y_pos = random.randrange(5)  # novo valor para a posição em y

        # checar se a posição nao é a mesma que a da bola (2,2)
        if self.x_pos == 2 and self.y_pos == 2:
            # se for a mesma, ir para (4,4)
            self.x_pos = 4
            '''PODEMOS COLOCAR PARA ALEATORIZAR ENQUANTO FOR (2,2)'''
            self.y_pos = 4

    # checar se o bichinho pegou a bola (bola e bichinho na mesma pos)
    def check_win(self):
        if self.x_pos == 2 and self.y_pos == 2:
            display.show(Image.HEART)
            sleep(2000)
            # chama funções para reiniciar o joguinho:
            self.novo_lugar()
            self.draw()

    # função para cuidar a posição do bichinho
    def check_dir(self):
        inc = accelerometer.current_gesture()  # inclinação do m:b

        if inc == self.last: (?)
            return

        # se o m:b estiver inclinado para cima:
        if inc == "up":
            # se ele não estiver na última linha:
            if self.y_pos < 4:
                self.y_pos += 1  # ele desce

        # se o m:b estiver inclinado para baixo:
        elif inc == "down":
            # se ele não estiver na primeira linha:
            if self.y_pos > 0:
                self.y_pos -= 1  # ele sobe

        # se o m:b estiver inclinado para a esquerda:
        elif inc == "left":
            # se ele não estiver na primeira coluna:
            if self.x_pos > 0:
                self.x_pos -= 1  # vai para a esquerda

        # se o m:b estiver inclinado para a direita:
        elif inc == "right":
            # se ele não estiver na última coluna:
            if self.x_pos < 4:
                self.x_pos += 1  # vai p direita

        # para evitar erros na detecção de outros movimentos:
        else:
            return

        self.last = inc  # o que isso ta fazendo?

        self.draw()  # mantém a imagem aparecendo (?)

class Pet(object):
    def __init__(self):
        self.tempo = 0  # controla o tempo de vida do tamagochi
        self.feliz()  # criaremos a função abaixo
        self.acao = False # se False nao consideramos a movimentação do m:b
        e = 10  # valor inicial de glicemia no sangue

    # funções de possíveis emoções do bichinho

    def feliz(self):
        display.show(Image.HAPPY)
        self.acao = False  # movimento do m:b não levado em consideração

    def triste(self):
        display.show(Image.ANGRY)
        self.acao = False  # movimento do m:b não levado em consideração

    def dormindo(self):
        display.show(Image.ASLEEP)
        self.acao = False  # movimento do m:b não levado em consideração

    def surpreso(self):
        display.show(Image.SURPRISED)
        self.acao = True  # o movimento do m:b é levado em consideração

        # se tiver mais que um mínimo de glicemia:
        if self.glic > 4:
            self.glic -= 0.1  # glicemia cai

    # função que fará a glicemia cair com o tempo
    def glicemia(self):
        # a cada 2s cai 0.1 de glicemia
        if self.glic > 0:
            self.glic -= 0.1
        self.carinha()  # definirá que carinho o bichinho fará

    # função que determina a carinha do bichinho pelo nivel de glicemia
    def carinha(self):
        if self.glic < 4:  # glicemia baixa demais
            self.triste()
        if self.glic > 8:  # glicemia alta demais
            self.dormindo()
        else:  # glicemia normal
            self.feliz()

    # funcao para checar os movimentos do microbit
    def check_mov(self):
        inc = accelerometer.current_gesture()  # inclinação do m:b

        # se o m:b for sacudido:
        if inc == "shake":
            self.surpreso()
            sleep(1000)

        # se o m:b for virado para baixo:
        elif inc == "face down":
            display.show(Image.CONFUSED)
            self.acao = True

        # se o m:b for inclinado para a esquerda:
        elif inc == "left":
            display.show(left)
            self.acao = True

        # se o m:b for inclinado para a direita:
        elif inc == "right":
            display.show(right)
            self.acao = True

        # caso o m:b não esteja se movendo, carinha de acordo com a glicemia
        else:
            if self.acao:
                self.carinha()

    # definições do que acontece ao apertar os botões:
    def check_botao(self):
        # se os dois botões forem apertados, ele começa o jogo:
        if button_a.is_pressed() and button_b.is_pressed():
            self.jogar()  # definiremos depois

        # se o botão A for apertado, ele come e aumenta a glicemia:
        elif button_a.is_pressed():
            self.glic += 1
            display.show([abre_boca, fecha_boca,
                         abre_boca, fecha_boca], 300)
            self.carinha()

        # se o botão B for apertado, aparece o nível de glicemia:
        elif button_b.is_pressed():
            display.scroll("{0:0.1f}".format(self.glic))

    # função que checará a morte do bichinho, de acordo com o nivel de glicemia:
    def check_morte(self):
        # se a qtd de glicemia for muito baixa:
        if self.glic < 1:
            display.show(Image.SKULL)
            return True  # faz seguir no loop até q o m:b seja resetado (como?)

        # se a qtd de glicemia for muito alta
        elif self.glic > 25:
            display.show(Image.GHOST)
            return True  # faz seguir no loop até q o m:b seja resetado (como?)

        return False  # bichinho vivo e código ainda rodando

    # chamará outras funções enquanto nada acontece:
    def espera(self):
        while True:  # loop
            if self.check_morte():
                break  # sai do loop, para de chamar as funções pq ta morto

            self.check_mov()
            self.check_botao()

            controle do tempo:
            atual = running_time()  # tempo corrido do código
            delta = atual - self.tempo  # inicialmente delta = atual

             # se já passou 5 segundos desde a ultima vez q entrou nesse if
            if delta > interval:
                self.tempo = atual  # tempo = tempo corrido do código
                self.glicemia()  # começa a considerar o
                 valor de glicemia

    # função para ir para o jogo
    def jogar(self):
        jogo = Jogo()  # funcao do jogo atribuida a uma variável (pq?)
        jogo.start()  # começa o jogo (função start)

# o que isso faz?
if __name__ == '__main__':
    pet = Pet()  # (pq?)
    pet.espera()
