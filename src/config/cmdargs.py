import argparse

from models.model import CmdArgs


def parse_cmd_args() -> CmdArgs:
    """
    Функция для парсинга аргументов командной строки и создания объекта CmdArgs.

    Возвращает:
        CmdArgs: инициализированный объект с параметрами из командной строки.
    """
    parser = argparse.ArgumentParser(
        description="Обработка входных параметров для конфигурации и входного файла."
    )

    # Добавляем обязательные аргументы
    parser.add_argument(
        "-c",
        "--cfg-file",
        type=str,
        required=True,
        help="Путь к конфигурационному файлу (обязательный параметр)",
    )

    parser.add_argument(
        "-d",
        "--dep-file",
        type=str,
        required=True,
        help="Путь к входному файлу с деполяризацией(обязательный параметр)",
    )

    parser.add_argument(
        "-f",
        "--fl-file",
        type=str,
        required=True,
        help="Путь к входному файлу с флуоресценцией(обязательный параметр)",
    )

    # Парсим аргументы
    args = parser.parse_args()

    # Создаём и возвращаем объект CmdArgs
    return CmdArgs(cfg_file=args.cfg_file, dep_file=args.dep_file, fl_file=args.fl_file)
