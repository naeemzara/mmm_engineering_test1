#config.py

from dataclasses import dataclass

@dataclass(frozen=True)
class MMMThresholdConfig:
    p_value_threshold: float = 0.1
    elasticity_min: float = 0.0
    elasticity_max: float = 3.0
    contribution_min: float = 1.0
    contribution_max: float = 60.0
    adstock_min: float = 1.0
    adstock_max: float = 150.0


REQUIRED_COLUMNS = {
    "Channel",
    "Coefficient",
    "p_value",
    "Elasticity",
    "contribution_pct",
    "adstock_half_life",
}
