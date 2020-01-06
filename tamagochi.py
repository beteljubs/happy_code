from microbit import *  # importa TODA a biblioteca do microbit
import random  # uso de numeros escolhidos aleatoriamente

interval = 5000  # tempo de espera até o tamagochi fazer algo

# variáveis de imagens

right = Image(
    "90900:"
    "00000:"
    "00000:"
    "90009:"
    "09990")

left = Image(
    "00909:"
    "00000:"
    "00000:"
    "90009:"
    "09990")

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

sono = Image(
    "99099:"
    "00000:"
    "00000:"
    "09990:"
    "00000")

'''
CRIAÇÃO DE CLASSE!!!!!!!! COISA NOVA
 o que é? grupo de métodos (funções) ou atributos (variáveis) em comum
 def __init__ ?
 self?
'''

class Jogo():  # declarando a classe de nome Jogo
    def __init__(self):  # self vai representar objetos da mesma classe
        self.last = None  # comparar o vetor do movimento do bichinho
        self.x_pos = 0  # x inicial do bichinho
        self.y_pos = 0  # y inicial do bichinho
        display.scroll("Pegue a bola")  # aparece quando A + B for pressionado
        self.draw()  # chamando função draw que vamos logo definir

'''
set_pixel(x, y, valor): escolhe a posição de um pixel
    x: pos em x
    y: pos em y
    valor: intensidade do brilho do pixel
'''

    def draw(self):
        imagem_bola = Image(  # imagem inicial: a bola c brilho 5 no meio do display
            "00000:"
            "00000:"
            "00500:"
            "00000:"
            "00000")
        imagem_bola.set_pixel(self.x_pos, self.y_pos, 9)  # add na imagem posição inicial do bichinho ????
        display.show(imagem)  # mostra a imagem inicial do jogo

'''
para sair de um loop podemos usar o comando 'break'
revisar while True
revisar estruturas condicionais
'''

    def start(self):  # função do inicio do jogo - roda em loop
        while True:  # loop
            # funções de controle que declararemos em seguida:
            self.check_win()  # controla se o bichinho pegou a bola
            self.check_dir()  # controla a posição do bichinho
            if button_a.is_pressed():  # se o botão for pressionado...
                break   # ...sairemos do loop
            if button_b.is_pressed():
                break

'''
uso da bib random: random.randrange(num): gera numero aleatório no intervalo (range) definido por num
para randrange(5) vai ser um numero aleatorio entre 0 e 4
'''

# função para definir lugares aleatorios para o bichinho surgir
    def novo_lugar(self):
        self.x_pos = random.randrange(5)  # novo valor para a posição em x
        self.y_pos = random.randrange(5)
        # checar se a posição nao é a mesma que a da bola (2,2)
        if self.x_pos == 2 and self.y_pos == 2:
            self.x_pos = 4  '''PODEMOS COLOCAR PARA ALEATORIZAR ENQUANTO FOR (2,2)'''
            self.y_pos = 4

    # checar se o bichinho pegou a bola (posição da bola = posição do bichinho)
    def check_win(self):
        if self.x_pos == 2 and self.y_pos == 2:
            display.show(Image.HEART)
            sleep(2000)
            self.novo_lugar()
            self.draw()

'''
comando return: sai da função? - condição segundo as trilhas
comparação com o break, que sai de um loop
'''

    # função para cuidar a posição do bichinho
    def check_dir(self):
        inc = acceleromoter.current_gesture()  # valor lido pelo acelerometro (indica a inclinação do micro:bit)
            if inc == self.last:  '''Q Q É ESSE LAST'''
                return

            if inc == "up":  # se o micro:bit estiver inclinado para cima...
                if self.y_pos < 4:  # ... e y < 4
                    self.y_pos += 1  # atualiza o valor da posição em y (ele desce)
            elif inc == "down":  # se estiver inclinado para baixo...
                if self.y_pos > 0:  # e a posição y for maior que 0 (ele nao esta na primeira linha)
                    self.y_pos -= 1  # ele sobe
            elif inc == "left":
                if self.x_pos > 0:  # se n estiver na primeira coluna
                    self.x_pos -= 1  # vai para a esquerda
            elif inc == "right":
                if self.x_pos < 4:  # se nao estiver na ultima coluna
                    self.x_pos += 1  # vai p direita
            else:  # para evitar erros na detecção de outros movimentos:
                return
            self.last = inc  '''explicação?'''
            self.draw()  # chama a função da imagem inicial do jogo

'''
revisar variavel booleana
'''

class Pet(objeto):
    def __init__(self):
        self.tempo = 0  # controlar o tempo pecorrido
        self.feliz()  # criaremos a função abaixo
        self.acao = False  # momentos que o movimento do micro:bit n deve ser considerado
        self.glic = 6.5  # atribui valor inicial de glicemia no sangue

    # função feliz:
    def feliz(self):
        display.show(Image.HAPPY)
        self.acao = False  # movimento do m:b não levado em consideração

    def triste(self):
        display.show(Image.ANGRY)
        self.acao = False

    def dormindo(self):
        display.show(Image.SLEEP)
        self.acao = False

    def surpreso(self):  # o nivel de glicemia cai
        display.show(Image.SURPRISED)
        self.acao = True  # o movimento do m:b é levado em consideração
        if self.glic > 4:  # checar o nivel de glicemia
            self.glic -= 0.1  # glicemia cai

# função que fara a glicemia cair com o tempo
    def glicemia(self):
        if self.glic > 0:
            self.glic -= 0.1
        self.carinha()  # ja programaremos

# função que determina a carinha do bichinho de acordo com o nivel de glicemia
    def carinha(self):
        if self.glic < 4:  # glicemia baixa demais
            self.sad()
        if self.glic > 8:  # glicemia alta demais
            self.dormindo()
        else:  # glicemia normal
            self.feliz()

    # funcao para checar os movimentos do microbit
    def check_mov(self):
        inc = accelerometer.current_gesture()
        if inc == "shake":  # se o m:b estiver sendo agitado
            self.surpreso()
            sleep(1000)
        elif inc == "face down":
            display.show(Image.CONFUSED)
            self.acao = True
        elif inc == "left":
            display.show(left)
            self.acao = True
        elif inc == "right":
            display.show(right)
            self.acao = True
        else:
            if self.acao:
                self.carinha()

'''
display.show([img1, img2, img3, img4], num):
    mostra as imagens da lista com num = delay entre cada imagem (em ms)

display.scroll("{0:0.xf}, {1:0.xf}".format(var1, var2))
    vai mostrar uma mensagem com as duas variaveis
    - o primeiro numero (0 e 1) dentro das {} indica qual variavel (na ordem de dentro do format)
    - e o :0.xf indica que é uma var tipo float (numero real) e queremos x casas decimais
'''

    # funcao que checa os botões
    def check_botao(self):
        if button_a.is_pressed() and button_b.is_pressed():
            self.jogar()  # definiremos depois
        elif button_a.is_pressed():
            self.glic += 1
            display.show([boca_aberta, boca_fechada, boca_aberta, boca_fechada], 300)
            self.carinha()
        elif button_b.is_pressed():
            display.scroll("{0:0.1f}".format(self.glic))  # mostrar o nivel de glicemia

    def check_morte(self):
        if self.glic < 1:
            display.show(Image.SKULL)
            return True '''???''' # faz seguir no loop até q o m:b seja resetado
        elif self.glic > 30:
            display.show(Image.GHOST)
            return True
        return False  # bichinho vivo e código ainda rodando

# chamará outras funções enquanto nada acontece
    def espera(self):
        while True:
            if self.check_morte():
                break
            self.check_mov()
            self.check_botao()
            atual = running_time()  # tempo corrido
            delta = atual - self.last_time
            if delta > INTERVAL: '''interval???'''
                self.last_time = atual
                self.glicemia()

    # função para ir para o jogo
    def jogar(self):
        jogo = Jogo()  # funcao do jogo atribuida a uma variável
        game.start()  # começa o jogo (função start)


'''
DAFUCKKKKKK??????
\/ \/ \/ \/ \/
'''

if __name__ -- '__main__':
    pet = Pet()
    pet.espera()