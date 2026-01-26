import json
from collections import namedtuple

Config = namedtuple(
    "Config",
    ["delta_d", "delta_nd"],
)


def get_default_config() -> Config:
    """Return the default configuration."""
    return Config(delta_d=0.31, delta_nd=0.05)


def read_config_from_json(filepath: str) -> Config:
    """Read configuration from a JSON file."""
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    return Config(delta_d=data["delta_d"], delta_nd=data["delta_nd"])
