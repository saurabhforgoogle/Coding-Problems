import mysql.connector
import mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="sksjr@2000",
  database="users_insta"
)

import pandas as pd   
df=pd.read_csv(r'C:\Users\saurabh\Documents\Desktop\Projects\SQLusingPython\login.txt',delimiter='|')
df=df.split()
#df.columns=['no','score','username','password']
print(df.columns)

