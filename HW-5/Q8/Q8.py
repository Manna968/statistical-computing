import subprocess
import sys

def install(package):
    #if pip doesn't work, try pip3 in the following statement
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


import psycopg2

#tweak the database parameters to match your specific postgres database.
conn = psycopg2.connect(host="localhost", 
                        port="5432", 
                        user="postgres", 
                        password="Zxm199819", 
                        database="postgres"
                        #You may add the following line if you have schemaa
                        #,options="-c search_path=nfl"
                       )
cur = conn.cursor()

display = '''select * from employee limit 10 '''
cur.execute(display)
rows = cur.fetchall()
for row in rows:
    print(row)

print("First 10 records were shown successfully.")
conn.commit()

cur.close()
conn.close()