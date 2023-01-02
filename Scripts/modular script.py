IC = pd.read_csv("G:\\My Drive\\Projects\\Projects\\Data\\temp\\ID.csv",encoding= 'unicode_escape')
df3 = pd.merge(df, IC, left_on='Ind', right_on='NHS5')
df3 = df3[['INDICATORS','Data','States']]
State