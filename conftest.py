import pandas as pd
import pytest


@pytest.fixture
def valid_df():
    return pd.DataFrame({
        "Channel": ["Search"],
        "Coefficient": [0.5],
        "p_value": [0.05],
        "Elasticity": [1.5],
        "contribution_pct": [30],
        "adstock_half_life": [10],
    })
