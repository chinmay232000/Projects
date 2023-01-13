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
	
	for filename in os.listdir(path):
		list1 = []
		list3 = []
		df = pd.DataFrame(m[['INDICATORS',name]])
		file ="G:\\My Drive\\Projects\\Projects\\Data\\temp\\"+ name + "\\"+ filename
		reader = PdfReader(file)
		if name == 'NHS3':
				
			n=reader.pages[0].extract_text()
			print(len(df[name]))
			for i in range(len(df[name])):
				b = df[name][i]
				
				if pd.isnull(b):
					c,d,e = np.nan, np.nan, np.nan
					templist = [c,d,e]
					list1.append(templist)
					continue 
				if filename == 'Bihar.pdf' and (b == "9. T, 9a. F") :
					b = "9a. F,9b. F"
				elif filename == 'Bihar.pdf' and (b == "9a. F, 9b. F"):
					b = "9b. F,Maternity care (for births in the last 3 years)"
				Start = n.find(b.split(',')[0])
				End = n.find(b.split(',')[1])		
				print(n)
				var = n[Start:End]
				print(b.split(',')[0])
				if End == 4601 or End == 4910:
					 var = var + 'na'	
				z = var.split()
				b = df[name][i]
				c,d,e = z[-1],z[-2],z[-9]
				list3 = [b]
				list2 = [c,d,e]
				
				for j in list2:
					
					if j.isnumeric():
						j = float(j)
						
					else:
						j = re.findall("\d+\.\d+",j)
						print(j)	
						if not j:
							j = np.nan
						else:
							j = float(j[0])
					
					list3.append(j)
					
				list1.append(list3)
				
			df2 = pd.DataFrame(list1)
			print(list3)
			print(df) 
			print(df2)
			df2.columns = ['IND','NHS1','NHS2','NHS3_x']
			df3 = pd.concat([df, df2], axis=1, join='inner')
			print(df3)
			df3.drop(['NHS3','IND'],axis = 1,inplace = True)
			print(df3)
			df = df3.reset_index(drop = True)
			print(df)
			
			file_name = os.path.basename(file)
			Name = os.path.splitext(file_name)[0]
			df3= pd.DataFrame([os.path.splitext(file_name)[0]])
			df3.columns = ['State']
			n,o= len(df), len(df3)
			df['States'] = np.tile(df3['State'], int(np.ceil(n / o)))[:n]
			df = pd.DataFrame(df)
			print(df)
			df.columns = ['INDICATORS','NHS1','NHS2','NHS3','States']

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
			Name = np.array([Name])
			df3 = pd.DataFrame(Name)
			df3.columns = ['State']
			m, n, o  =   len(df), len(df2), len(df3)
			df['Total'] = np.tile(df2['Total'], int(np.ceil(m / n)))[:m]
			df['States'] = np.tile(df3['State'], int(np.ceil(m / o)))[:m]
			df = pd.DataFrame(df)
			df.drop(name,axis = 1)
			
			print(df)
			df.to_csv(("G:\\My Drive\\Projects\\Projects\\Data\\Modified data\\"+name+"\\"+ Name + ".csv"), index = False)

Survey('NHS3')