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
