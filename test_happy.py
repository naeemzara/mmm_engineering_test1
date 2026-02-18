#test_happy.py

from mmm_quality_checks.quality import apply_quality_checks

def test_happy_path(valid_df):
    result = apply_quality_checks(valid_df)
    assert result["has_any_issue"].iloc[0] is False
