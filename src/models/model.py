"""
Модели данных приложения. Нарочно сделаны неизменяемыми
"""

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class CmdArgs:
    cfg_file: str
    dep_file: str
    fl_file: str


@dataclass(frozen=True)
class Table:
    row_labels: list[str]
    col_labels: list[str]
    data: np.ndarray


@dataclass(frozen=True)
class InputData:
    # beta: np.ndarray
    delta: Table
    gf: Table


@dataclass(frozen=True)
class OutputData:
    eta_d: Table
    delta_prime: Table
    delta_nd: Table
