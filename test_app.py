import pytest

def f(x):
	return x+1
	
def test_answer():
	assert f(3) == 4

def read_file(filename):
	f = open(filename, 'r')

def test_ioerror():
	with pytest.raises(IOError):
		read_file('abbscd')


# raise SystemExit("the file you are trying to read does not exist")