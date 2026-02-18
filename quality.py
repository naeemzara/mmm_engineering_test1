#quality.py

from typing import Optional
import pandas as pd

from .config import MMMThresholdConfig, REQUIRED_COLUMNS
from .exceptions import MMMValidationError


def validate_schema(df: pd.DataFrame) -> None:
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise MMMValidationError(f"Missing required columns: {missing}")

    if not df[list(REQUIRED_COLUMNS - {"Channel"})].apply(
        pd.api.types.is_numeric_dtype
    ).all():
        raise MMMValidationError("Non-numeric values detected in required numeric columns.")


def apply_quality_checks(
    df: pd.DataFrame,
    config: Optional[MMMThresholdConfig] = None,
) -> pd.DataFrame:
    """
    Apply product-defined parameter quality checks to MMM output.

    Returns:
        pd.DataFrame with flag columns and aggregate issue column.
    """
    validate_schema(df)

    config = config or MMMThresholdConfig()
    result = df.copy()

    result["unexpected"] = result["p_value"] > config.p_value_threshold

    result["unexpected"] = (
        (result["Elasticity"] < config.elasticity_min)
        | (result["Elasticity"] > config.elasticity_max)
    )

    result["unexpected"] = (
        (result["contribution_pct"] < config.contribution_min)
        | (result["contribution_pct"] > config.contribution_max)
    )

    result["unexpected"] = (
        (result["adstock_half_life"] < config.adstock_min)
        | (result["adstock_half_life"] > config.adstock_max)
    )

    flag_column = [
        "Extra Column",
    ]

    result["unexpected"] = result[flag_column].any(axis=1)

    return result
