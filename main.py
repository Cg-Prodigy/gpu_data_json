import csv
import json
from pprint import pprint

def readGPUFile(file_path:str,output_path:str):
    gpu_dict={}
    with open(file_path,"r") as file:
        csv_file=list(csv.reader(file))
        col_headers=["Memory size","Memory type"]
        for row in csv_file[1:]:
            key=row[0].upper()
            if key not in gpu_dict.keys():
                gpu_dict[key]={}
            i_key=row[3]+" GB" if row[3] else "Not specified"
            gpu_spec_list={k:v for k,v in zip(col_headers,[i_key,f"{row[-2]}"])}   
            gpu_dict[key][row[1]]=gpu_spec_list
    with open(output_path,"w") as file:
        json.dump(gpu_dict,file)
readGPUFile("gpu_specs_v6.csv","gpu_specs.json")