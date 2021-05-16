import os
import pycurl
import csv
import csv as cv
import json
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from datetime import datetime

##-----INPUT DATA 00-----#
tanggal = (datetime.today() + timedelta(days=0)).strftime("%d")
bulan = (datetime.today() + timedelta(days=0)).strftime("%m") 	
tahun = (datetime.today() + timedelta(days=0)).strftime("%Y")
tanggal_now = (datetime.today() + timedelta(days=0)).strftime("%d")
bulan_now = (datetime.today() + timedelta(days=0)).strftime("%m") 	
tahun_now = (datetime.today() + timedelta(days=0)).strftime("%Y")	

#======================================================= PONTIANAK WIOO ====================================================
with open('visibility_wioo.txt', 'wb') as f:
    c = pycurl.Curl()
    c.setopt(c.URL, 'http://aviation.bmkg.go.id/latest/metar.php?m=5&y=2021&i=wioo')
    c.setopt(c.WRITEDATA, f)
    c.perform()
    c.close()
print('FINISH, VIS WIOO PONTIANAK.txt')

df = pd.read_csv("F:visibility_wioo.txt",delimiter=' ',header =None,names=["Tanggal", "Waktu", "SAID31", "ICAO", "UTC", "SANDI", "STATION", "Angin", "Visibility", "Cuaca", "CLOUD1", "CLOUD12", "SUHU", "TEKANAN", "NOSIG/TEMPO", "FM/TL", "VIS", "WW", "CLD1", "CLD2"])
##df.drop(df.head(1).index,inplace=True)

df.drop(["SAID31","STATION", "UTC", "SANDI", "CLOUD1", "CLOUD12", "SUHU", "TEKANAN", "NOSIG/TEMPO", "FM/TL", "VIS", "WW", "CLD1", "CLD2"], axis=1, inplace=True)
df.to_csv("F:/spartan_fdrs/data/visibility_wioo.csv", index=False)
print(df.drop)

df = pd.read_csv("F:/spartan_fdrs/data/visibility_wioo.csv") 
# displying  dataframe - Output 1 
df.head() 
  
# inserting column with static value in data frame 
df.insert(2, "Lat", "-0.14888888888888888")
df.insert(3, "Long", "109.40277777777779")
  
# displaying data frame again - Output 2 
df.head() 

df.to_csv("F:/spartan_fdrs/data/visibility_wioo.csv", index=False)


#Input the last Data
top = pd.read_csv("F:/spartan_fdrs/data/visibility_wioo.csv", nrows=1)
headers = top.columns.values

with open("F:/spartan_fdrs/data/visibility_wioo.csv", "r") as f, open("F:/spartan_fdrs/data/visibility/vis_last_wioo.csv","w") as g:
    last_line = f.readlines()[-1].strip().split(",")
    c = csv.writer(g)
    c.writerow(headers)
    c.writerow(last_line)

bottom = pd.read_csv("F:/spartan_fdrs/data/visibility/vis_last_wioo.csv")
concatenated = pd.concat([bottom])
concatenated.reset_index(inplace=True, drop=True)
print (concatenated)

#Change to the Date
df = pd.read_csv("F:/spartan_fdrs/data/visibility/vis_last_wioo.csv")
date = []
for d in df["Tanggal"]:
    d = d.replace('/', '-')
    date.append(d)
df["Tanggal"] = date
print (date)
df.to_csv("F:/spartan_fdrs/data/visibility/vis_last_wioo.csv", index=False)

#Change to the ICAO
df = pd.read_csv("F:/spartan_fdrs/data/visibility/vis_last_wioo.csv")
station = []
for d in df["ICAO"]:
    d = d.replace('WIOO', 'Stamet I Supadio - Pontianak (WIOO)')
    station.append(d)
df["ICAO"] = station
print (station)
df.to_csv("F:/spartan_fdrs/data/visibility/vis_last_wioo.csv", index=False)


print("FINISH_PONTIANAK")

#======================================================= PALANGKARAYA WAGG ====================================================
with open('visibility_wagg.txt', 'wb') as f:
    c = pycurl.Curl()
    c.setopt(c.URL, 'http://aviation.bmkg.go.id/latest/metar.php?m=5&y=2021&i=wagg')
    c.setopt(c.WRITEDATA, f)
    c.perform()
    c.close()
print('FINISH, VIS WAGG PALANGKARAYA.txt')

df = pd.read_csv("F:visibility_wagg.txt",delimiter=' ',header =None,names=["Tanggal", "Waktu", "SAID31", "ICAO", "UTC", "SANDI", "STATION", "Angin", "Visibility", "Cuaca", "CLOUD1", "CLOUD12", "SUHU", "TEKANAN", "NOSIG/TEMPO", "FM/TL", "VIS", "WW", "CLD1", "CLD2"])
##df.drop(df.head(1).index,inplace=True)

df.drop(["SAID31","STATION", "UTC", "SANDI", "CLOUD1", "CLOUD12", "SUHU", "TEKANAN", "NOSIG/TEMPO", "FM/TL", "VIS", "WW", "CLD1", "CLD2"], axis=1, inplace=True)
df.to_csv("F:/spartan_fdrs/data/visibility_wagg.csv", index=False)
print(df.drop)

df = pd.read_csv("F:/spartan_fdrs/data/visibility_wagg.csv") 
# displying  dataframe - Output 1 
df.head() 
  
# inserting column with static value in data frame 
df.insert(2, "Lat", "-2.2266666666666666")
df.insert(3, "Long", "113.94388888888889")
  
# displaying data frame again - Output 2 
df.head() 

df.to_csv("F:/spartan_fdrs/data/visibility_wagg.csv", index=False)

top = pd.read_csv("F:/spartan_fdrs/data/visibility_wagg.csv", nrows=1)
headers = top.columns.values

with open("F:/spartan_fdrs/data/visibility_wagg.csv", "r") as f, open("F:/spartan_fdrs/data/visibility/vis_last_wagg.csv","w") as g:
    last_line = f.readlines()[-1].strip().split(",")
    c = csv.writer(g)
    c.writerow(headers)
    c.writerow(last_line)

bottom = pd.read_csv("F:/spartan_fdrs/data/visibility/vis_last_wagg.csv")
concatenated = pd.concat([bottom])
concatenated.reset_index(inplace=True, drop=True)

print (concatenated)


#Change to the Date
df = pd.read_csv("F:/spartan_fdrs/data/visibility/vis_last_wagg.csv")
date = []
for d in df["Tanggal"]:
    d = d.replace('/', '-')
    date.append(d)
df["Tanggal"] = date
print (date)
df.to_csv("F:/spartan_fdrs/data/visibility/vis_last_wagg.csv", index=False)


#Change to the ICAO
df = pd.read_csv("F:/spartan_fdrs/data/visibility/vis_last_wagg.csv")
station = []
for d in df["ICAO"]:
    d = d.replace('WAGG', 'Stamet Tjilik Riwut - Palangkaraya (WAGG)')
    station.append(d)
df["ICAO"] = station
print (station)
df.to_csv("F:/spartan_fdrs/data/visibility/vis_last_wagg.csv", index=False)


print("FINISH_PALANGKARAYA")


#======================================================= JAMBI WIJJ ====================================================
with open('visibility_wijj.txt', 'wb') as f:
    c = pycurl.Curl()
    c.setopt(c.URL, 'http://aviation.bmkg.go.id/latest/metar.php?m=5&y=2021&i=wijj')
    c.setopt(c.WRITEDATA, f)
    c.perform()
    c.close()
print('FINISH, VIS WIJJ JAMBI.txt')

df = pd.read_csv("F:visibility_wijj.txt",delimiter=' ',header =None,names=["Tanggal", "Waktu", "SAID31", "ICAO", "UTC", "SANDI", "STATION", "Angin", "Visibility", "Cuaca", "CLOUD1", "CLOUD12", "SUHU", "TEKANAN", "NOSIG/TEMPO", "FM/TL", "VIS", "WW", "CLD1", "CLD2"])
##df.drop(df.head(1).index,inplace=True)

df.drop(["SAID31","STATION", "UTC", "SANDI", "CLOUD1", "CLOUD12", "SUHU", "TEKANAN", "NOSIG/TEMPO", "FM/TL", "VIS", "WW", "CLD1", "CLD2"], axis=1, inplace=True)
df.to_csv("F:/spartan_fdrs/data/visibility_wijj.csv", index=False)
print(df.drop)

df = pd.read_csv("F:/spartan_fdrs/data/visibility_wijj.csv") 
# displying  dataframe - Output 1 
df.head() 
  
# inserting column with static value in data frame 
df.insert(2, "Lat", "-1.630466")
df.insert(3, "Long", "103.642847")
  
# displaying data frame again - Output 2 
df.head() 

df.to_csv("F:/spartan_fdrs/data/visibility_wijj.csv", index=False)

top = pd.read_csv("F:/spartan_fdrs/data/visibility_wijj.csv", nrows=1)
headers = top.columns.values

with open("F:/spartan_fdrs/data/visibility_wijj.csv", "r") as f, open("F:/spartan_fdrs/data/visibility/vis_last_wijj.csv","w") as g:
    last_line = f.readlines()[-1].strip().split(",")
    c = csv.writer(g)
    c.writerow(headers)
    c.writerow(last_line)

bottom = pd.read_csv("F:/spartan_fdrs/data/visibility/vis_last_wijj.csv")
concatenated = pd.concat([bottom])
concatenated.reset_index(inplace=True, drop=True)

print (concatenated)

#Change to the Date
df = pd.read_csv("F:/spartan_fdrs/data/visibility/vis_last_wijj.csv")
date = []
for d in df["Tanggal"]:
    d = d.replace('/', '-')
    date.append(d)
df["Tanggal"] = date
print (date)
df.to_csv("F:/spartan_fdrs/data/visibility/vis_last_wijj.csv", index=False)


#Change to the ICAO
df = pd.read_csv("F:/spartan_fdrs/data/visibility/vis_last_wijj.csv")
station = []
for d in df["ICAO"]:
    d = d.replace('WIJJ', 'Stamet I Sultan Thaha - Jambi (WIJJ)')
    station.append(d)
df["ICAO"] = station
print (station)
df.to_csv("F:/spartan_fdrs/data/visibility/vis_last_wijj.csv", index=False)





print("FINISH_JAMBI")


#======================================================= PEKANBARU WIBB ====================================================
with open('visibility_wibb.txt', 'wb') as f:
    c = pycurl.Curl()
    c.setopt(c.URL, 'http://aviation.bmkg.go.id/latest/metar.php?m=5&y=2021&i=wibb')
    c.setopt(c.WRITEDATA, f)
    c.perform()
    c.close()
print('FINISH, VIS WIBB PEKANBARU.txt')

df = pd.read_csv("F:visibility_wibb.txt",delimiter=' ',header =None,names=["Tanggal", "Waktu", "SAID31", "ICAO", "UTC", "SANDI", "STATION", "Angin", "Visibility", "Cuaca", "CLOUD1", "CLOUD12", "SUHU", "TEKANAN", "NOSIG/TEMPO", "FM/TL", "VIS", "WW", "CLD1", "CLD2"])
##df.drop(df.head(1).index,inplace=True)

df.drop(["SAID31","STATION", "UTC", "SANDI", "CLOUD1", "CLOUD12", "SUHU", "TEKANAN", "NOSIG/TEMPO", "FM/TL", "VIS", "WW", "CLD1", "CLD2"], axis=1, inplace=True)
df.to_csv("F:/spartan_fdrs/data/visibility_wibb.csv", index=False)
print(df.drop)

df = pd.read_csv("F:/spartan_fdrs/data/visibility_wibb.csv") 
# displying  dataframe - Output 1 
df.head() 
  
# inserting column with static value in data frame 
df.insert(2, "Lat", "0.46")
df.insert(3, "Long", "101.44388888888889")
  
# displaying data frame again - Output 2 
df.head() 

df.to_csv("F:/spartan_fdrs/data/visibility_wibb.csv", index=False)

top = pd.read_csv("F:/spartan_fdrs/data/visibility_wibb.csv", nrows=1)
headers = top.columns.values

with open("F:/spartan_fdrs/data/visibility_wibb.csv", "r") as f, open("F:/spartan_fdrs/data/visibility/vis_last_wibb.csv","w") as g:
    last_line = f.readlines()[-1].strip().split(",")
    c = csv.writer(g)
    c.writerow(headers)
    c.writerow(last_line)

bottom = pd.read_csv("F:/spartan_fdrs/data/visibility/vis_last_wibb.csv")
concatenated = pd.concat([bottom])
concatenated.reset_index(inplace=True, drop=True)

print (concatenated)


#Change to the Date
df = pd.read_csv("F:/spartan_fdrs/data/visibility/vis_last_wibb.csv")
date = []
for d in df["Tanggal"]:
    d = d.replace('/', '-')
    date.append(d)
df["Tanggal"] = date
print (date)
df.to_csv("F:/spartan_fdrs/data/visibility/vis_last_wibb.csv", index=False)


#Change to the ICAO
df = pd.read_csv("F:/spartan_fdrs/data/visibility/vis_last_wibb.csv")
station = []
for d in df["ICAO"]:
    d = d.replace('WIBB', 'Stamet I Sultan Syarif Kasim II - Pekanbaru (WIBB)')
    station.append(d)
df["ICAO"] = station
print (station)
df.to_csv("F:/spartan_fdrs/data/visibility/vis_last_wibb.csv", index=False)


print("FINISH_PEKANBARU")


#======================================================= PALEMBANG WIPP ====================================================
with open('visibility_wipp.txt', 'wb') as f:
    c = pycurl.Curl()
    c.setopt(c.URL, 'http://aviation.bmkg.go.id/latest/metar.php?m=5&y=2021&i=wipp')
    c.setopt(c.WRITEDATA, f)
    c.perform()
    c.close()
print('FINISH, VIS WIPP PALEMBANG.txt')

df = pd.read_csv("F:visibility_wipp.txt",delimiter=' ',header =None,names=["Tanggal", "Waktu", "SAID31", "ICAO", "UTC", "SANDI", "STATION", "Angin", "Visibility", "Cuaca", "CLOUD1", "CLOUD12", "SUHU", "TEKANAN", "NOSIG/TEMPO", "FM/TL", "VIS", "WW", "CLD1", "CLD2"])
##df.drop(df.head(1).index,inplace=True)

df.drop(["SAID31","STATION", "UTC", "SANDI", "CLOUD1", "CLOUD12", "SUHU", "TEKANAN", "NOSIG/TEMPO", "FM/TL", "VIS", "WW", "CLD1", "CLD2"], axis=1, inplace=True)
df.to_csv("F:/spartan_fdrs/data/visibility_wipp.csv", index=False)
print(df.drop)

df = pd.read_csv("F:/spartan_fdrs/data/visibility_wipp.csv") 
# displying  dataframe - Output 1 
df.head() 
  
# inserting column with static value in data frame 
df.insert(2, "Lat", "-2.897777777777778")
df.insert(3, "Long", "104.70083333333334")
  
# displaying data frame again - Output 2 
df.head() 

df.to_csv("F:/spartan_fdrs/data/visibility_wipp.csv", index=False)

top = pd.read_csv("F:/spartan_fdrs/data/visibility_wipp.csv", nrows=1)
headers = top.columns.values

with open("F:/spartan_fdrs/data/visibility_wipp.csv", "r") as f, open("F:/spartan_fdrs/data/visibility/vis_last_wipp.csv","w") as g:
    last_line = f.readlines()[-1].strip().split(",")
    c = csv.writer(g)
    c.writerow(headers)
    c.writerow(last_line)

bottom = pd.read_csv("F:/spartan_fdrs/data/visibility/vis_last_wipp.csv")
concatenated = pd.concat([bottom])
concatenated.reset_index(inplace=True, drop=True)

print (concatenated)


#Change to the Date
df = pd.read_csv("F:/spartan_fdrs/data/visibility/vis_last_wipp.csv")
date = []
for d in df["Tanggal"]:
    d = d.replace('/', '-')
    date.append(d)
df["Tanggal"] = date
print (date)
df.to_csv("F:/spartan_fdrs/data/visibility/vis_last_wipp.csv", index=False)


#Change to the ICAO
df = pd.read_csv("F:/spartan_fdrs/data/visibility/vis_last_wipp.csv")
station = []
for d in df["ICAO"]:
    d = d.replace('WIPP', 'Sultan Mahmud Badaruddin II - Palembang (WIPP)')
    station.append(d)
df["ICAO"] = station
print (station)
df.to_csv("F:/spartan_fdrs/data/visibility/vis_last_wipp.csv", index=False)


print("FINISH_PALEMBANG")


# MERGE DATA VISIBILITY ALL STATION
import pandas as pd
import glob

path = r'F:/spartan_fdrs/data/visibility/' # use your path
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)
print (frame)
frame.to_csv('F:/spartan_fdrs/data/visibility.csv')

# convert CSV to JSON 
file = 'F:/spartan_fdrs/data/visibility.csv'
json_file = 'F:/spartan_fdrs/data/visibility.json'
fieldnames = ("Tanggal", "Waktu", "ICAO", "Angin", "Visibility", "Cuaca")

        
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
