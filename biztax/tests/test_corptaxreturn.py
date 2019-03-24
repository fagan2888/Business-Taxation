"""
Test CorpTaxReturn class.
"""
# CODING-STYLE CHECKS:
# pycodestyle test_corptaxreturn.py
# pylint --disable=locally-disabled test_corptaxreturn.py

import numpy as np
import pytest
# pylint: disable=import-error
from biztax import CorpTaxReturn, Data, Asset, Debt


def test_instantiation_and_update_methods(default_btax_params):
    """
    Test (in)correct CorpTaxReturn instantiation and update_* methods
    """
    good_btax_params = default_btax_params
    bad_btax_params = list()
    good_earnings = np.ones(14)
    bad1_earnings = np.ones(13)
    bad2_earnings = dict()
    good_data = Data()
    good_assets = Asset(default_btax_params)
    good_assets.calc_all()
    bad_assets = dict()
    good_debts = Debt(default_btax_params, np.ones(14))
    good_debts.calc_all()
    bad_debts = dict()
    # test (in)correct instantiation
    with pytest.raises(ValueError):
        CorpTaxReturn(bad_btax_params, good_earnings)
    with pytest.raises(AssertionError):
        CorpTaxReturn(good_btax_params, bad1_earnings)
    with pytest.raises(AssertionError):
        CorpTaxReturn(good_btax_params, bad2_earnings)
    CorpTaxReturn(good_btax_params, good_earnings, data=Data())
    CorpTaxReturn(good_btax_params, good_earnings, assets=good_assets)
    with pytest.raises(ValueError):
        CorpTaxReturn(good_btax_params, good_earnings, assets=bad_assets)
    CorpTaxReturn(good_btax_params, good_earnings, debts=good_debts)
    with pytest.raises(ValueError):
        CorpTaxReturn(good_btax_params, good_earnings, debts=bad_debts)
    # test update_* methods
    ctr = CorpTaxReturn(good_btax_params, good_earnings)
    assert isinstance(ctr, CorpTaxReturn)
    ctr.update_assets(good_assets)
    with pytest.raises(ValueError):
        ctr.update_assets(bad_assets)
    ctr.update_debts(good_debts)
    with pytest.raises(ValueError):
        ctr.update_debts(bad_debts)
    ctr.update_earnings(good_earnings)        