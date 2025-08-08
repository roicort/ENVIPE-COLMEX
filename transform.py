import os
import glob
import pandas as pd
from dbfread import DBF

def dbf_to_csv(dbf_path, csv_path):

    # Leer DBF con codificación latin1 y guardar CSV en UTF-8
    table = DBF(dbf_path, load=True, encoding='latin1')
    df = pd.DataFrame(iter(table))
    df.to_csv(csv_path, index=False, encoding='utf-8')

def convert_all_dbf_in_folder(folder):
    dbf_files = glob.glob(os.path.join(folder, "*.dbf"))
    print(f"Found {len(dbf_files)} DBF files in folder: {folder}")
    for dbf_file in dbf_files:
        csv_file = os.path.splitext(dbf_file)[0] + ".csv"
        print(f"Converting {dbf_file} -> {csv_file}")
        dbf_to_csv(dbf_file, csv_file)


folder_2018 = os.path.dirname(os.path.abspath(__file__)) + "/data/2018"
print(f"Converting all DBF files in folder: {folder_2018}")
convert_all_dbf_in_folder(folder_2018)

folder_2019 = os.path.dirname(os.path.abspath(__file__)) + "/data/2019"
print(f"Converting all DBF files in folder: {folder_2019}")
convert_all_dbf_in_folder(folder_2019)

folder_2020 = os.path.dirname(os.path.abspath(__file__)) + "/data/2020"
print(f"Converting all DBF files in folder: {folder_2020}")
convert_all_dbf_in_folder(folder_2020)