#This file includes the configurations to run tests and the three test cases 

#conftest

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


#test_edge

def apply_quality_checks(valid_df):
    valid_df["Elasticity"] = 4
    result = apply_quality_checks(valid_df)
    assert result["unexpected"].iloc[0] is True

#test_invalid_input

import pandas as pd
import pytest
from quality import apply_quality_checks
from exceptions import MMMValidationError

def test_missing_columns():
    df = pd.DataFrame({"Channel": ["Search"]})
    with pytest.raises(MMMValidationError):
        apply_quality_checks(df)

#test_happy_path
from quality import apply_quality_checks
def test_happy_path(valid_df):
    result = apply_quality_checks(valid_df)
    assert result["unexpected"].iloc[0] is False
