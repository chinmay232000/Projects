import pandas as pd
import os
import numpy as np



States = pd.read_csv("G:\\My Drive\\Projects\\Projects\\Data\\temp\\States.csv",header = 0,encoding= 'unicode_escape')
def Modular(name):
	path ="G:\\My Drive\\Projects\\Projects\\Data\\Modified Data\\"+ name

	for filename in os.listdir(path):
		file ="G:\\My Drive\\Projects\\Projects\\Data\\Modified Data\\"+ name + "\\"+ filename
		df = pd.DataFrame(States[['States',name]])
		df1 = pd.DataFrame(file)
		var = df1['States'][0]
		var2 = df.index[df['States']==var]
		df3 = pd.DataFrame(df['States'][var2])
		m,n = len(df1),len(df)
		df.drop(['States'],axis = 1)
		df1['States'] = np.tile(df['State'], int(np.ceil(m/n)))[:m]
		df = pd.DataFrame(df1)
		df.to_csv("G:\\My Drive\\Projects\\Projects\\Data\\Modular_Data\\" + name +"\\" + var +".csv",index = False)

def Unify():

	path ="G:\\My Drive\\Projects\\Projects\\Data\\Modular_Data\\"
	data = pd.DataFrame(States['States'])
	list1 = ['NHS5','NHS4','NHS3']
	for i in States['States']:
		for item in list1:
			file = path + item +"\\" + i + ".csv"
			if os.path.exists(file):
				df = pd.DataFrame(file)
				df4 = pd.merge(df4,df, how='inner', left_on = 'INDICATORS', right_on = 'INDICATORS')
		df4.drop(['States_x'],['States_y'],axis=1)
		df.to_csv("G:\\My Drive\\Projects\\Projects\\Data\\Merged_by_State_Final\\"+ i + ".csv")


Modular('NHS3')
Modular('NHS4')
Modular('NHS5')
Unify()





