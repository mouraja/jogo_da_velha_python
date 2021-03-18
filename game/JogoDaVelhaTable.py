
class JogoDaVelhaTable():

    def __init__(self, columns, title):
        self.__columns = columns
        self.__title = title

    def show(self, positions):
        right_margin = "          "  ## 10 spaces
        right_column_margin = "      %s   "
        header = right_margin + ' 1 + 2 + 3 '
        bar = right_column_margin + ' %s | %s | %s '
        trace = right_margin + '---+---+---'
        count = 0
        for i in range(5):
            print('')
        print(right_margin + self.__title)
        for i in range(3):
            print('')
        print(header)
        print('')
        for column in self.__columns:
            count += 1
            print(bar % (column, positions[column][0], positions[column][1], positions[column][2]))
            if count < 3:
                print(trace)
        for i in range(3):
            print('')
