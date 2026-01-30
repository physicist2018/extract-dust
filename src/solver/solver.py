import numpy as np

from config.readconfig import Config
from models.model import InputData, OutputData, Table


def findEtaD(input_data: InputData, config: Config) -> OutputData:
    """
    Функция для доли пылевого аэрозоля в смеси eta_d.

    Args:
        input_data (InputData): Входные данные для расчета.
        config (Config): Конфигурационные параметры.

    Returns:
        OutputData: Выходные данные, содержащие коэффициент деполяризации
        для не пыли, ее долю eta_d.
    """

    eta_d = (
        (input_data.delta.data - config["delta_nd"])
        * (1.0 + config["delta_d"])
        / ((config["delta_d"] - config["delta_nd"]) * (1 + input_data.delta.data))
    )
    # вычисляем потенциалы констант деполяризации для пыли и не пыли
    dp_nd = config["delta_nd"] / (1.0 + config["delta_nd"])
    dp_d = config["delta_d"] / (1.0 + config["delta_d"])
    # Вычисляем потенциал деполяризации для данных
    delta_prime = input_data.delta.data / (1.0 + input_data.delta.data)

    # dp=dp_nd, if dp<dp_nd, else dp=dp-eta_d*dp_d (вот здесь косяк был)
    delta_prime = np.where(delta_prime < dp_nd, dp_nd, delta_prime - eta_d * dp_d)
    # dp = 0.01 if dp<0
    delta_prime = np.where(delta_prime < 0, 0.01, delta_prime)

    # пересчет в деполяризацию
    delta_nd = delta_prime / (1 - delta_prime)
    delta_nd = np.where(delta_nd > 1, 1, delta_nd)

    return OutputData(
        Table(
            row_labels=input_data.delta.row_labels,
            col_labels=input_data.delta.col_labels,
            data=eta_d,
        ),
        Table(
            row_labels=input_data.delta.row_labels,
            col_labels=input_data.delta.col_labels,
            data=delta_prime,
        ),
        Table(
            row_labels=input_data.delta.row_labels,
            col_labels=input_data.delta.col_labels,
            data=delta_nd,
        ),
    )


def prepareData(input: InputData, config: Config) -> InputData:
    """
    Предобработка входных матриц, исключатся вклад пыли из обеих матриц
    delta и Gf

    Input parametes:
        input: InputData - входные данные
        config: Config - конфигурация

    Output:
        InputData - обработанные входные данные
    """

    result = findEtaD(input, config)
    gf = Table(
        row_labels=input.gf.row_labels,
        col_labels=input.gf.col_labels,
        data=input.gf.data - input.gf.data * result.eta_d.data,
    )

    return InputData(result.delta_nd, gf)
