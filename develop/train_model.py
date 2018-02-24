from sklearn import linear_model
from sklearn import model_selection
from sklearn.model_selection import cross_val_predict
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn.model_selection import cross_val_score
import pickle

def train_model(df_f):
	"""Train our logistic classifier model on data frame, create pickle of model
	
	Args: 
	df (DataFrame): DataFrame output from feature_creation.py [or from DB]
	
	Returns:
	Print statement acknowledging completed training
	
	"""
	
	#Prepare data frame for scikit-learn
	Y = df_f['Pass_Fail']
	Y=Y.astype('int')
	X = df_f.drop(['address','city','inspection_id','dba_name','Pass_Fail','inspection_id'],axis=1)

	print(X.columns)
	
	#Generate model object
	clf = linear_model.LogisticRegression()
	m_fit = clf.fit(X, Y)
	
	#Pickle output
	pickling_on = open("Model.pickle","wb")
	pickle.dump(m_fit, pickling_on)
	pickling_on.close()

	print("Model has been trained and pickled.")