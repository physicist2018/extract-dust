import numpy as np

from models.model import Table


def read_matrix_file(filename) -> Table:
    """
    Читает файл с матрицей и возвращает:
    - numpy-матрицу числовых значений
    - список заголовков столбцов (первая строка)
    - список заголовков строк (первый элемент каждой строки данных)


    Формат файла:
    "A" "B" "C" "D"
    "1" 1  2  3  4
    "2" 3  4  5  6

    Возвращает:
    matrix = np.array([[1, 2, 3, 4], [3, 4, 5, 6]])
    collabels = ["A", "B", "C", "D"]
    rowlabels = ["1", "2"]
    """
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Удаляем переносы строк и разбиваем на элементы
    lines = [line.strip().split() for line in lines]

    # Первая строка — заголовки столбцов (без кавычек)
    collabels = [item.strip('"') for item in lines[0]]

    # Остальные строки — данные матрицы
    rowlabels = []
    data = []

    for line in lines[1:]:
        # Первый элемент строки — заголовок строки (без кавычек)
        rowlabel = line[0].strip('"')
        rowlabels.append(rowlabel)

        # Остальные элементы — числовые данные
        row_data = [float(item) for item in line[1:]]
        data.append(row_data)

    # Создаём numpy-матрицу
    matrix = np.array(data)

    return Table(row_labels=rowlabels, col_labels=collabels, data=matrix)
