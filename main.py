import random


def display_board(board):
    blankBoard = """
___________________
|     |     |     |
|  7  |  8  |  9  |
|     |     |     |
|-----------------|
|     |     |     |
|  4  |  5  |  6  |
|     |     |     |
|-----------------|
|     |     |     |
|  1  |  2  |  3  |
|     |     |     |
|-----------------|
"""

    for i in range(1, 10):
        # элементы поля будут заменяться на board[i] после того как в цикле игрок выберет поле
        blankBoard = blankBoard.replace(str(i), board[i])

    print(blankBoard)


# заполнение поля (возвращается позиция на поле)
def place_marker(board, marker, position):
    board[position] = marker
    return board


# выигрышные комбинации
def win_check(board, mark):
    if board[1] == board[2] == board[3] == mark:
        return True
    if board[4] == board[5] == board[6] == mark:
        return True
    if board[7] == board[8] == board[9] == mark:
        return True
    if board[1] == board[4] == board[7] == mark:
        return True
    if board[2] == board[5] == board[8] == mark:
        return True
    if board[3] == board[6] == board[9] == mark:
        return True
    if board[1] == board[5] == board[9] == mark:
        return True
    if board[3] == board[5] == board[7] == mark:
        return True
    return False


if __name__ == "__main__":
    # формирую список чисел от 0 до 9
    nums = list(range(1, 10))
    i = 1
    # Разыгрывается маркер
    markers = ['X', 'O']
    # список для хранения выбора игрока (всего 10, так как 0 не может быть выбран игроком, а если сделать 9,
    # то выбор игрока будет всего от 1 до 8)
    board = [' '] * 10
    while True:
        # из списка nums (список возможных ходов) берется рандомная цифра и тут же удаляется,
        # чтобы другой игрок не мог взять такую же
        position = random.choice(nums)
        nums.remove(position)

        # очередность ходов игроков в зависимости от счетчика
        if i % 2 == 0:
            marker = markers[1]
        else:
            marker = markers[0]
        # Ход игрока (функция вернет в переменную board ход игрока, заменив пробел на цифру)
        place_marker(board, marker, int(position))
        # Вывод доски в терминал (изначально выводятся пробелы, далее, при замене пробелов на цифры выводятся цифры)
        display_board(board)
        # добавляем еденицу к счетчику для изменения игрока
        i += 1
        # проверяем победные комбинации
        if win_check(board, marker):
            print(f'выиграл игрок с маркером {marker}')
            break
        # если не выпала победная комбинация и закончились числа в nums - Ничья
        elif not win_check(board, marker) and not nums:
            print('Ничья')
            break
