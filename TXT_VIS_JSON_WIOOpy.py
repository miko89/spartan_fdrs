import os
import pycurl
import csv
import csv as cv
import json
import pandas as pd
from datetime import datetime, timedelta
from datetime import datetime
##import shutil
##from PIL import Image
cwd = os.getcwd()
path = os.path.join(cwd, "TXT_TO_JSON_SATELITBMKG.py")


#-----INPUT DATA 00-----#
##tanggal_00 = "03"
##bulan_00 = "08"	 	
##tahun_00 = "2020"
	

##-----INPUT DATA 00-----#
tanggal = (datetime.today() + timedelta(days=0)).strftime("%d")
bulan = (datetime.today() + timedelta(days=0)).strftime("%m") 	
tahun = (datetime.today() + timedelta(days=0)).strftime("%Y")
tanggal_now = (datetime.today() + timedelta(days=0)).strftime("%d")
bulan_now = (datetime.today() + timedelta(days=0)).strftime("%m") 	
tahun_now = (datetime.today() + timedelta(days=0)).strftime("%Y")	




# As long as the file is opened in binary mode, both Python 2 and Python 3
# can write response body to it without decoding.
from io import BytesIO

buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, 'http://aviation.bmkg.go.id/latest/metar.php?m=bulan&y=tahun&i=wioo')
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

body = buffer.getvalue()
# Body is a byte string.
# We have to know the encoding in order to print it to a text file
# such as standard output.
print(body.decode('iso-8859-1'))


with open('visibility_wioo.txt', 'wb') as f:
    c = pycurl.Curl()
    c.setopt(c.URL, 'http://aviation.bmkg.go.id/latest/metar.php?m=8&y=2020&i=wioo')
    c.setopt(c.WRITEDATA, f)
    c.perform()
    c.close()
print('finish, save.txt')


df = pd.read_csv("F:visibility_wioo.txt",delimiter=' ',header =None,names=["DD/MM/YYYY", "TIME", "SAID31", "ICAO", "UTC", "SANDI", "STATION", "WIND", "VISIBILITY", "WEATHER", "CLOUD1", "CLOUD12", "SUHU", "TEKANAN", "NOSIG/TEMPO", "FM/TL", "VIS", "WW", "CLD1", "CLD2"])
##df.drop(df.head(1).index,inplace=True)

df.drop(["SAID31","STATION", "UTC", "SANDI", "CLOUD1", "CLOUD12", "SUHU", "TEKANAN", "NOSIG/TEMPO", "FM/TL", "VIS", "WW", "CLD1", "CLD2"], axis=1, inplace=True)
df.to_csv("F:/spartan_fdrs/data/visibility.csv", index=False)
print(df.drop)

data = pd.read_csv("F:/spartan_fdrs/data/visibility_wioo.csv") 
# displying  dataframe - Output 1 
df.head() 
  
# inserting column with static value in data frame 
df.insert(2, "LAT", "-0.14888888888888888")
df.insert(3, "LONG", "109.40277777777779")
  
# displaying data frame again - Output 2 
df.head() 

df.to_csv("F:/spartan_fdrs/data/visibility_wioo.csv", index=False)

top = pd.read_csv("F:/spartan_fdrs/data/visibility_wioo.csv", nrows=1)
headers = top.columns.values

with open("F:/spartan_fdrs/data/visibility_wioo.csv", "r") as f, open("F:/spartan_fdrs/data/visibility_lasttime.csv","w") as g:
    last_line = f.readlines()[-1].strip().split(",")
    c = csv.writer(g)
    c.writerow(headers)
    c.writerow(last_line)

bottom = pd.read_csv("F:/spartan_fdrs/data/visibility__wioo.csv")
concatenated = pd.concat([bottom])
concatenated.reset_index(inplace=True, drop=True)

print(concatenated)

file = 'F:/spartan_fdrs/data/visibility__wioo.csv'
json_file = 'F:/spartan_fdrs/data/visibility_wioo.json'
fieldnames = ("DD/MM/YYYY", "ICAO", "WIND", "VISIBILITY", "WEATHER")

        
##Read CSV File
def read_CSV(file, json_file):
    csv_rows = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        field = reader.fieldnames
        for row in reader:
            csv_rows.extend([{field[i]:row[field[i]] for i in range(len(field))}])
        convert_write_json(csv_rows, json_file)
print("Membaca File CSV")

##Convert csv data into json
def convert_write_json(data, json_file):
    with open(json_file, "w") as f:
        f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',',': ')))

read_CSV(file,json_file)
print("FINISH")

