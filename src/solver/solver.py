import numpy as np

from config.readconfig import Config
from models.model import InputData, OutputData


def findEtaD(input_data: InputData, config: Config) -> OutputData:
    eta_d = (
        (input_data.delta - config.delta_nd)
        * (1.0 + config.delta_d)
        / ((config.delta_d - config.delta_nd) * (1 + input_data.delta))
    )
    dp_nd = config.delta_nd / (1.0 + config.delta_nd)
    dp_d = config.delta_d / (1.0 + config.delta_d)
    delta_prime = input_data.delta / (1.0 + input_data.delta)
    print(dp_d, dp_nd, np.max(delta_prime), np.min(delta_prime))
    delta_prime = np.where(delta_prime < dp_nd, dp_nd, delta_prime - eta_d * dp_d)
    delta_prime = np.where(delta_prime < 0, 0.01, delta_prime)
    delta_nd = delta_prime / (1 - delta_prime)
    delta_nd = np.where(delta_nd > 1, 1, delta_nd)

    return OutputData(eta_d, delta_prime, delta_nd)
