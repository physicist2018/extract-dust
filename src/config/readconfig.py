import json
from pathlib import Path
from typing import Any, Dict, List

from models.config_models import Config


def read_config(file_path: str | Path) -> Config:
    """
    Читает конфигурацию из JSON‑файла и возвращает типизированный словарь.

    Args:
        file_path: путь к файлу конфигурации

    Returns:
        Словарь с конфигурацией, соответствующий типу Config

    Raises:
        FileNotFoundError: если файл не найден
        json.JSONDecodeError: если файл не является валидным JSON
        ValueError: если данные не соответствуют ожидаемой структуре
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Файл конфигурации не найден: {path}")

    with path.open("r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(
                f"Неверный JSON в файле {path}: {e}", e.doc, e.pos
            )

    # Валидация структуры
    validate_config(data)

    return data  # уже соответствует типу Config благодаря валидации


def validate_config(config: Dict) -> None:
    """
    Проверяет, что словарь соответствует ожидаемой структуре конфигурации.

    Args:
        config: словарь с конфигурацией

    Raises:
        ValueError: если структура или типы данных неверны
    """
    required_keys = ["delta_d", "delta_nd", "delta", "gf", "mc"]

    for key in required_keys:
        if key not in config:
            raise ValueError(f"Отсутствует обязательный ключ: {key}")

    # Проверка типов простых полей
    if not isinstance(config["delta_d"], (int, float)):
        raise ValueError("delta_d должен быть числом")
    if not isinstance(config["delta_nd"], (int, float)):
        raise ValueError("delta_nd должен быть числом")

    # Проверка delta
    if not isinstance(config["delta"], dict):
        raise ValueError("delta должен быть объектом")
    _validate_list_of_two_floats(config["delta"], "delta", ["u", "w", "s"])

    # Проверка gf
    if not isinstance(config["gf"], dict):
        raise ValueError("gf должен быть объектом")
    _validate_list_of_two_floats(config["gf"], "gf", ["u", "w", "s"])

    # Проверка mc
    if not isinstance(config["mc"], dict):
        raise ValueError("mc должен быть объектом")
    mc = config["mc"]
    if not isinstance(mc.get("niters"), int):
        raise ValueError("mc.niters должен быть целым числом")
    if not isinstance(mc.get("seed"), int):
        raise ValueError("mc.seed должен быть целым числом")
    if not isinstance(mc.get("nbest"), int):
        raise ValueError("mc.nbest должен быть целым числом")


def _validate_list_of_two_floats(obj: Dict, parent_key: str, keys: List[str]) -> None:
    """Проверяет, что указанные ключи содержат списки из двух чисел."""
    for key in keys:
        if key not in obj:
            raise ValueError(f"В {parent_key} отсутствует ключ: {key}")
        value = obj[key]
        if (
            not isinstance(value, list)
            or len(value) != 2
            or not all(isinstance(x, (int, float)) for x in value)
        ):
            raise ValueError(f"{parent_key}.{key} должен быть списком из двух чисел")


def display_config(
    config: Config, title: str = "Configuration", color: bool = True
) -> None:
    # ANSI‑цвета (сбрасываются автоматически)
    if color:
        COLORS = {
            "reset": "\033[0m",
            "key": "\033[1;34m",  # яркий синий (ключи)
            "number": "\033[0;32m",  # зелёный (числа)
            "list": "\033[0;33m",  # жёлтый (списки)
            "string": "\033[0;31m",  # красный (строки)
            "title": "\033[1;35m",  # пурпурный (заголовок)
        }
    else:
        COLORS = {
            key: "" for key in ["reset", "key", "number", "list", "string", "title"]
        }

    def format_value(v: Any) -> str:
        if isinstance(v, (int, float)):
            return f"{COLORS['number']}{v}{COLORS['reset']}"
        elif isinstance(v, list):
            items = ", ".join(format_value(item) for item in v)
            return f"{COLORS['list']}[{items}]{COLORS['reset']}"
        elif isinstance(v, str):
            return f"{COLORS['string']}'{v}'{COLORS['reset']}"
        else:
            return str(v)

    def print_item(key: str, value: Any, level: int = 0):
        indent = "  " * level
        key_str = f"{COLORS['key']}{key}{COLORS['reset']}"
        if isinstance(value, dict):
            print(f"{indent}{key_str}:")
            for k, v in value.items():
                print_item(k, v, level + 1)
        else:
            val_str = format_value(value)
            print(f"{indent}{key_str}: {val_str}")

    # Заголовок

    # Основное содержимое
    for key, value in config.items():
        print_item(key, value)
    print()  # пустая строка в конце
