import re
from PyPDF2 import PdfReader
import pandas as pd
import os
import numpy as np
import tabula


def Survey(name):
	Base = "G:\\My Drive\\Projects\\Projects\\Data\\temp\\ID.csv"
	m = pd.read_csv(Base,header = 0, encoding = 'unicode escape')
	path ="G:\\My Drive\\Projects\\Projects\\Data\\temp\\"+ name
	df = pd.DataFrame(m[['INDICATORS',name]])
	for filename in os.listdir(path):
		list1 = []
		file ="G:\\My Drive\\Projects\\Projects\\Data\\temp\\"+ name + "\\"+ filename
		reader = PdfReader(file)
		if name = 'NHS3':
			df1 = tabula.read_pdf(file, pages = "all")
			for item in df1:
				for info in item.values:
					list1.append(info)
			df1 = pd.DataFrame(list1)
			df1.drop([2,3,4,5,6,7,9],axis = 1,inplace = True)
			df1.columns = ['IND','NHS3','NHS2','NHS1']
			df1.reset_index(drop = True)
			df3 = pd.merge(df, df1, left_on='IND', right_on='NHS3')
			df = df3.drop(['IND','NHS3_y'],axis = 1)
			df.columns = ['NHS3','NHS2','NHS1','INDICATORS']
			file_name = os.path.basename(file)
			Name = os.path.splitext(file_name)[0]
			df3 = pd.DataFrame([os.path.splitext(file_name)[0]])
			df3.columns = ['State']
			m, n = len(df), len(df3)
			df['States'] = np.tile(df3['State'], int(np.ceil(m / n)))[:m]
			df = pd.DataFrame(df)
			df.to_csv(("G:\\My Drive\\Projects\\Projects\\Data\\Modified data\\"+name+"\\"+ Name + ".csv"), index = False)
			
			
		else:
		
			s=reader.pages[2].extract_text()
			t=reader.pages[3].extract_text()
			u=reader.pages[4].extract_text()
			v=reader.pages[5].extract_text()
			n = s+t+u+v
			check = "\n.*\n1."
			a = list(re.findall(check,n))		
			z = a[0].split()
			count = z.count("Total")

			for i in range(len(df[name])):
				print(i)
				print(count)	
				b = df[name][i]
				print(b)
				if pd.isnull(b):
					c = np.nan
					list1.append(c)
					continue 
				var = list(re.findall(b,n))
				print(var)
				z = var[0].split()
			
			
				if count == 2:
					if b[-1].isnumeric():
						c = z[-3]
					else:
						c = z[-2]
				else:
					if b[-1].isnumeric():
						c = z[-2]
					else:
						c = z[-1]
						
				c = c.replace(",","")
				if c.isnumeric():
					c = float(c)	
				else:
					
					print(z)
					print(c)
					c = re.findall("\d+\.\d+",c)
					print(c)	
					if not c:
						c = None
					else:
						c = float(c[0])
				
					print(c)
				list1.append(c)
				print(list1)
				print(list1)
			df2 = pd.DataFrame(list1)
			df2.columns = ['Total']
			file_name = os.path.basename(file)
			Name = os.path.splitext(file_name)[0]
			df3 = pd.DataFrame([os.path.splitext(file_name)[0]])
			df3.columns = ['State']
			m, n, o  =   len(df), len(df2), len(df3)
			df['Total'] = np.tile(df2['Total'], int(np.ceil(m / n)))[:m]
			df['States'] = np.tile(df3['State'], int(np.ceil(m / o)))[:m]
			df = pd.DataFrame(df)
			df.drop(name,axis = 1)
			print(df)
			df.to_csv(("G:\\My Drive\\Projects\\Projects\\Data\\Modified data\\"+name+"\\"+ Name + ".csv"), index = False)

Survey('NHS5')