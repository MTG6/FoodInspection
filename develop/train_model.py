from sklearn import linear_model
from sklearn import model_selection
from sklearn.model_selection import cross_val_predict
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn.model_selection import cross_val_score
import pickle
import logging

#Create model specification object for pickling
class model_reqs:
    def __init__(self, model , specs):
        self.model = model
        self.specs = list(specs)

def train_model(df_f):
	"""Train our logistic classifier model on data frame, create pickle of model.
	
	Args: 
		df_f (DataFrame): DataFrame output from prepare_app.
	
	Returns:
		None
	
	"""
	
	#Prepare data frame for scikit-learn
	Y = df_f['Pass_Fail']
	Y=Y.astype('int')
	X = df_f.drop(['address','city','inspection_id','dba_name','Pass_Fail','inspection_id'],axis=1)
	
	#Generate model object
	clf = linear_model.LogisticRegression()
	m_fit = clf.fit(X, Y)
	
	#Store model and df schema requirements
	modelspecs = model_reqs(m_fit,X.columns)
	
	#Pickle output
	pickling_on = open("ModelSpec.pickle","wb")
	pickle.dump(modelspecs, pickling_on)
	pickling_on.close()

	logging.debug(' -- Model has been trained and pickled.')