import pytest
import pandas as pd
import numpy as np
import sys
sys.path.append("../")
from data import feature_creation as fc
from data import load_data as ld


def test_pass_fail():
	data = np.array(['Pass','Fail'])
	testdata = pd.Series(data)
	assert  fc.pass_fail(testdata)[1] == 0
	
def test_fc():
	data = ld.load_data()
	tdata = fc.feature_creation(data)
	assert len(tdata.columns) == 74