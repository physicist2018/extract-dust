from collections import namedtuple

Config = namedtuple(
    "Config",
    ["delta_d", "delta_nd"],
)


def get_default_config() -> Config:
    return Config(delta_d=0.31, delta_nd=0.05)
