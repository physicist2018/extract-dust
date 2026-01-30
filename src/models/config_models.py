from typing import List, TypedDict


class DeltaConfig(TypedDict):
    u: List[float]
    w: List[float]
    s: List[float]


class GFConfig(TypedDict):
    u: List[float]
    w: List[float]
    s: List[float]


class MCConfig(TypedDict):
    niters: int
    seed: int
    nbest: int


class Config(TypedDict):
    delta_d: float
    delta_nd: float
    delta: DeltaConfig
    gf: GFConfig
    mc: MCConfig
