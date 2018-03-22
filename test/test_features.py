import pytest
import pandas as pd
import numpy as np
import sys
#sys.path.append("../")
from data import feature_creation as fc
from data import load_data as ld


def test_pass_fail():
	data = np.array(['pass','fail'])
	testdata = pd.Series(data)
	assert  fc.pass_fail(testdata)[1] == 1
	
def test_fc():
	data = ld.load_data().iloc[1:2]
	assert len(fc.feature_creation(data).columns) == 17