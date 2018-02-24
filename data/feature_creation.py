import pandas as pd
import re
from sqlalchemy import create_engine

#Function for bucketing Pass/Fail Outcomes
def pass_fail(raw):
    output = []
    i=0
    stop = (len(raw))
    while i < stop:
        if raw[i] == 'Pass':
            output.append(1)
        elif raw[i] == 'Fail':
            output.append(0)
        else:
            output.append('NA')
        i=i+1
    return output


def feature_creation(df):
	""" Take the raw dataframe from import, generate features for analysis
	
	Args: 
	df (DataFrame): DataFrame output from LoadData()
	
	Returns:
	df_f (DataFrame): DataFrame that includes feature generation
	
	"""
	#Define local variables
	i=0 #Counter
	infractions=[] #List of infractions to add to df
	crt = [] #List of critical infractions
	ser = [] #List of serious infractions
	mnr = [] #List of minor infractions
	

	#Isolate infraction Numbers and their bucket
	while i < len(df):
		s = df['violations'][i]
		infracs = re.findall("\d+",str(re.findall("\|\s\d+",s)))
		infrac_count = len([int(i) for i in infracs])
		m_count = len([int(i) for i in infracs if int(i) > 29 and int(i) <71])
		s_count = len([int(i) for i in infracs if int(i) > 14 and int(i) <30])
		c_count = len([int(i) for i in infracs if int(i) > 0 and int(i) <16])
    
		
		infractions.append(infrac_count)
		crt.append(m_count)
		ser.append(s_count)
		mnr.append(m_count)
		i=i+1
	
	#Add infractions to DataFrame
	df['infracs_total']=infractions
	df['infracs_minor']=mnr
	df['infracs_serious']=ser
	df['infracs_critical']=crt
	
	#Remove unnecessary columns
	cols = range(5,len(df.columns)) 
	df_f = df.iloc[:,cols]
	df_f['Pass_Fail'] = pass_fail(df_f['results']) #Bucket Pass/Fail outcomes
	df_f = df_f.drop(['aka_name','location','violations','results','latitude','longitude','state'], axis =1)
	
	#Remove unnecessary rows
	df_f = df_f[df_f.Pass_Fail != 'NA']
	df_f = df_f[df_f.facility_type == 'Restaurant']
	
	#Convert and bucket categorical to dummies
	risks = pd.get_dummies(df_f.risk)
	itype = pd.get_dummies(df_f.inspection_type)
	df_f = df_f.join(risks).join(itype)
	df_f['itype_re'] = round((df_f['Canvass Re-Inspection']+df_f['Complaint Re-Inspection']+df_f['License Re-Inspection']+.6)/3)
	df_f['itype_complaint'] = round((df_f['Short Form Complaint']+df_f['Complaint']+.1)/2)
	df_f.itype_re = df_f.itype_re.astype(int)
	df_f.itype_complaint = df_f.itype_complaint.astype(int)
	
	#Drop bucketed variables
	df_f = df_f.drop(['inspection_type','facility_type','inspection_date','license_','Canvass Re-Inspection','Complaint','Complaint Re-Inspection','License Re-Inspection','Short Form Complaint','risk'], axis=1)
	
	
	print(df_f.columns)
	return df_f

if __name__ == "__main__":
    feature_creation()
    
    

    