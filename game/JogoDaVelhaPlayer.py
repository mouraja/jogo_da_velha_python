
import time


class JogoDaVelhaPlayer():

    def __init__(self, player_name, tag):
        self.__player_name = player_name
        self.__tag = tag
        if tag == 'X':
            self.__color = "31"
        else:
            self.__color = "34"

    def get_tag(self):
        return (self.__tag)

    def get_color_tag(self):
        return ('\e[' + self.__color + 'm' + self.get_tag() + '\e[0m')

    def get_winner_tag(self):
        return ('\e[5;' + self.__color + 'm' + self.get_tag() + '\e[0m')

    def get_player_name(self):
        return self.__player_name

    def choose_play(self):
        print("Vez do jogador %s." % self.__player_name)
        play = input("Por favor, escolha uma jogada: ")
        if 'q' == play == 'Q':
            print("Que pena! Não quer mais jogar! ;-(")
            print("Volte outra vez pra jogar, se divertir com o Jogo da Velha.")
            time.sleep(3)
            exit(0)
        return play

