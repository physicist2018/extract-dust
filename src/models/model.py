from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class InputData:
    beta: np.ndarray
    delta: np.ndarray
    gf: np.ndarray


@dataclass(frozen=True)
class OutputData:
    eta_d: np.ndarray
    delta_prime: np.ndarray
    delta_nd: np.ndarray
