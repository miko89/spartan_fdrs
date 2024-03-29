import os
import csv
import json
import pandas as pd
from datetime import datetime, timedelta
from datetime import datetime
##import shutil
##from PIL import Image
cwd = os.getcwd()
path = os.path.join(cwd, "HOTSPOT_JSON_INDO.py")


#-----INPUT DATA 00-----#
##tanggal_00 = "03"
##bulan_00 = "08"	 	
##tahun_00 = "2020"


##-----INPUT DATA 00-----#
tanggal_00 = (datetime.today() + timedelta(days=0)).strftime("%d")
bulan_00 = (datetime.today() + timedelta(days=0)).strftime("%m") 	
tahun_00 = (datetime.today() + timedelta(days=0)).strftime("%Y")
tanggal_now = (datetime.today() + timedelta(days=0)).strftime("%d")
bulan_now = (datetime.today() + timedelta(days=0)).strftime("%m") 	
tahun_now = (datetime.today() + timedelta(days=0)).strftime("%Y")	



df = pd.read_csv("F:/project_web/spartan_fdrs/data/titik_hotspot/"+tahun_00+""+bulan_00+""+tanggal_00+"/indonesia/hotspot_"+tahun_00+""+bulan_00+""+tanggal_00+"_indonesia.txt",delimiter='\t',header = None,names=["Bujur", "Lintang", "Kepercayaan", "Region", "Provinsi", "Kabupaten", "Kecamatan", "Satelit", "Tanggal", "Waktu", "Radius", "Type"])
df.drop(df.head(1).index,inplace=True)
df.to_csv("F:/project_web/spartan_fdrs/data/htsp.csv", index=False)
print(df.head)



file = 'F:/project_web/spartan_fdrs/data/htsp.csv'
json_file = 'F:/project_web/spartan_fdrs/data/htsp.json'
fieldnames = ("Bujur", "Lintang", "Kepercayaan", "Region", "Provinsi", "Kabupaten", "Kecamatan", "Satelit", "Tanggal", "Waktu", "Radius", "Type")

        
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
        f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': '))) 
print("FINISH Convert CSV to JSon File")


read_CSV(file,json_file)
