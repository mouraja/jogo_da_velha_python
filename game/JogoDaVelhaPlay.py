import re

class JogoDaVelhaPlay():

    def __check_win_vertical(self, player, positions):
        plays = positions
        for row in range(3):
            print("Check vencedor")
            if positions['A'][row] != ' ' and positions['A'][row] == positions['B'][row] == positions['C'][row]:
                print("Venceu na vertical")
                plays['A'][row] = plays['B'][row] = plays['C'][row] = player.get_winner_tag()
                return True, plays, 'vertical'
        return self.__check_win_horizontal(player, positions)

    def __check_win_horizontal(self, player, positions):
        plays = positions
        for column in ['A', 'B', 'C']:
            if positions[column][0] != ' ' and positions[column][0] == positions[column][1] == positions[column][2]:
                print("Venceu na horizontal")
                plays[column][0] = plays[column][1] = plays[column][2] = player.get_winner_tag()
                return True, plays, "horizontal"
        return self.__check_win_diagonal(player, positions)

    def __check_win_diagonal(self, player, positions):
        plays = positions
        if positions['B'][1] != ' ':
            if positions['A'][0] == positions['B'][1] == positions['C'][2]:
                print("Venceu na diagonal descendente")
                plays['A'][0] = plays['B'][1] = plays['C'][2] = player.get_winner_tag()
                return True, plays, 'diagonal descendent'
            elif positions['A'][2] == positions['B'][1] == positions['C'][0]:
                print("Venceu na diagonal ascendente")
                plays['A'][2] = plays['B'][1] = plays['C'][0] = player.get_winner_tag()
                return True, plays, 'diagonal ascendent'
        return False, positions, ''

    def __check_win(self, player, positions):
        return self.__check_win_vertical(player, positions)

    def __validate_position_free(self, play, plays):
        column = play.group(1).upper()
        row = int(play.group(2)) - 1
        if plays[column][row] == ' ':
            return True, column, row
        return False, '', ''

    def __validate_play(self, play, plays):
        valid_play = re.search(r"^([ABCabc])([123])$", play)
        if valid_play:
            is_position_free, column, row = self.__validate_position_free(valid_play, plays)
            if is_position_free:
                return is_position_free, column, row
            print("Jogada já foi feita!")
            print("Escolha uma posição livre. Por favor!")
        else:
            print("Jogada 'inválida! %s." % play)
            print("Escolha jogada válida! Por favor!")
        return False, '', ''

    def play(self, player, positions):
        plays = positions
        print("Tecle 'q' para encerrar o jogo.")
        while True:
            play = player.choose_play()
            valid, column, row = self.__validate_play(play, plays)
            if valid:
                #print(plays.get(column)[row])
                #print(player.get_tag())
                #lista = plays.get(column)
                #lista[row] = player.get_tag()
                plays.get(column)[row] = player.get_tag()
                #temp = {column: lista}
                #plays.update(temp)
                return self.__check_win(player, plays)
            print("Tente outra vez!")
            time.sleep(1)
        return False, plays, ''

