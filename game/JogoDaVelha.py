import random
from os import system, name
from game.JogoDaVelhaPlay import JogoDaVelhaPlay
from game.JogoDaVelhaPlayer import JogoDaVelhaPlayer
from game.JogoDaVelhaTable import JogoDaVelhaTable


class JogoDaVelha:

    def __init__(self):
        blank_rows = [' ', ' ', ' ']
        self.__tag_x = "X"
        self.__tag_o = "O"
        self.__column_a = "A"
        self.__column_b = "B"
        self.__column_c = "C"
        self.__tags = [self.__tag_x, self.__tag_o]
        self.__columns = [self.__column_a, self.__column_b, self.__column_c]
        self.__positions = {self.__column_a: blank_rows[:], self.__column_b: blank_rows[:], self.__column_c: blank_rows[:]}
        self.__players = []
        self.__player = ""
        self.__game_name = "Game of Old Woman"
        self.__winner = ""
        self.__no_winner = "Empate!"
        self.__title = "Jogo da Velha v1.0.0"
        self.__table = JogoDaVelhaTable(self.__columns, self.__title)

    def __choose_players(self):
        players = []
        for tag in self.__tags:
            player_name = input("Quem irá jogar com " + tag + ": ")
            player = JogoDaVelhaPlayer(player_name, tag)
            players.append(player)
            print('\n')
        return players

    @staticmethod
    def __choose_begginer(players):
        player: object = random.choice(players)
        return player

    def start(self):
        print('Game %s\n' % self.__game_name)
        self.__players = self.__choose_players()
        self.__player = self.__choose_begginer(self.__players)
        self.clear()
        self.__plays(self.__player, self.__positions, self.__table)

    @staticmethod
    def __congratulations(player):
        print('')
        print('')
        print('>>>>>>     Youpy!  We have a champion!   <<<<<<<<')
        print('')
        print('')
        print('   ' + player.get_player_name() + 'wins !!!')
        print('')
        print('')
        print('      Enjoy your victory! We see soon !')
        print('')
        exit(0)

    def __plays(self, player, positions, table):
        who_play = player
        plays = positions
        play = JogoDaVelhaPlay()
        count_plays = 0
        table.show(plays)
        is_winner = False
        while not is_winner:
            is_winner, positions, way = play.play(who_play, plays)
            table.show(plays)
            if is_winner:
                self.__congratulations(player)
                exit(0)
            count_plays = count_plays + 1
            if count_plays == 9:
                return '', False, ''
            who_play = self.__next_player(who_play)

    @staticmethod
    def clear():
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

    def __next_player(self, player):
        if player == self.__players[0]:
            return self.__players[1]
        return self.__players[0]
