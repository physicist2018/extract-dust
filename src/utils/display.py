import numpy as np
from matplotlib import pyplot as plt

from utils.readwrite import Table


def plot_table_heatmap(table: Table, cmap="viridis", figsize=(8, 6), title=None):
    """
    Отрисовывает тепловую карту (heatmap) для объекта Table.

    Параметры:
    - table: объект класса Table с полями data, row_labels, col_labels
    - cmap: цветовая палитра (по умолчанию 'viridis')
    - figsize: размер фигуры (по умолчанию (8, 6))
    - title: заголовок графика (опционально)
    """
    fig, ax = plt.subplots(figsize=figsize)

    # Создаем тепловую карту
    im = ax.imshow(table.data, cmap=cmap, aspect="auto", origin="lower")

    # Настраиваем подписи по осям
    ax.set_xticks(np.arange(len(table.col_labels)))
    ax.set_yticks(np.arange(len(table.row_labels)))

    ax.set_xticklabels(table.col_labels)
    ax.set_yticklabels(table.row_labels)

    ax.set_xlabel("Номер профиля")
    ax.set_ylabel("Высота")

    # Поворачиваем подписи по оси X для лучшей читаемости (если нужно)
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

    # Добавляем colorbar
    cbar = ax.figure.colorbar(im, ax=ax)
    cbar.ax.set_ylabel("Значение", rotation=-90, va="bottom")

    # Добавляем заголовок, если задан
    if title:
        ax.set_title(title)

    # Добавляем сетку для лучшей читаемости
    ax.grid(False)

    # Подстраиваем расположение элементов
    plt.tight_layout()

    return fig, ax
