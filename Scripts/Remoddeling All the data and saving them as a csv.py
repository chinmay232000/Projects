import tabula
import pandas as pd
import os
import numpy as np

def Survey(name):
	survey = name
	path ="G:\\My Drive\\Projects\\Projects\\Data\\temp\\"+ name
	for filename in os.listdir(path):
		list1 = []
		file ="G:\\My Drive\\Projects\\Projects\\Data\\temp\\"+ name + "\\"+ filename
		df = tabula.read_pdf(file, pages = "all")

		for item in df:
			for info in item.values:
				list1.append(info)
		df = pd.DataFrame(list1)
		if name == 'NHS5':

			df.columns = ['Ind', 'W', 'Total', 'NHS4']
			print(df)
			if df.loc[51,'Total'] == '':
				temp = df.iloc[48:101]
				cols = np.arange(df.W.str.split(expand = True).shape[1])
				temp[cols] = temp.W.str.split(expand = True)
				temp = temp.drop([0,1], axis=1)
				temp = temp.drop(['W', 'NHS4','Total'], axis=1)
				temp.columns = ['Ind','Total']
				df = df.drop(['W', 'NHS4'], axis=1)
				df.drop(df.loc[48:101].index, inplace=True)
				df = pd.concat([df, temp], axis=0)
				df.reset_index(drop = True)

			else:
				df = df.drop(['W', 'NHS4'], axis=1)
				df.reset_index(drop = True)
			df.drop([0,1],axis = 0,inplace = True)
		elif name == 'NHS4':
			if len(df.columns) == 3:
				df.drop([2],axis = 1,inplace = True)
			
			df.columns = ['Ind','W']
			
			cols = np.arange(df.W.str.split(expand = True).shape[1])
			df[cols] = df.W.str.split(expand = True)
			if len(df.columns == 5):
				df = df.drop(['W',0,1],axis = 1,inplace = True)
			else:
				df = df.drop(['W',0],axis = 1,inplace = True)
			df.columns = ['Ind','Total']
			df.drop([0],axis = 0,inplace = True)
			df.reset_index(drop = True)

		 
		print(df)
		# extracting file name
		file_name = os.path.basename(file)
		Name = os.path.splitext(file_name)[0]
		df2 = pd.DataFrame([os.path.splitext(file_name)[0]])
		df2.columns = ['State']
		m, n = len(df), len(df2)
		df['States'] = np.tile(df2['State'], int(np.ceil(m / n)))[:m]
		df.to_csv(("G:\\My Drive\\Projects\\Projects\\Data\\Modified data\\"+survey+"\\"+ Name + ".csv"), index = False)


Survey('NHS4')
Survey('NHS5')