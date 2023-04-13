import os
import re
import json
import PyPDF2 as pdf

path = "/Users/albert/Desktop/YK Pao School/Y9/Others/IGCSE Past Papers"

for subject in sorted(os.listdir(path)):
    if "." not in subject: 
        print(f"Starting to read {subject} ...")
        subject_code = subject.split()[-1].replace("(", "").replace(")", "")
        dic = {}
        for year in sorted(os.listdir(path+"/"+subject)):
            if "." not in year: 
                dic[year] = {}
                for file in sorted(os.listdir(path+"/"+subject+"/"+year)):
                    if re.match("\d\d\d\d_\w\d\d_qp_\d\d?.pdf", file):
                        print(f"Reading ./{subject}/{year}/{file} ...")
                        dic[year][file] = {}
                        r = pdf.PdfReader(open(path+"/"+subject+"/"+year+"/"+file, "rb"))
                        for page in range(len(r.pages)): 
                            dic[year][file][str(int(page)+1)] = r.pages[page].extract_text().lower().replace("\n", " ").replace("....", "")
        print(f"Creating {subject_code}.json ...")
        with open(f"{subject_code}.json", "w") as f:
            json.dump(dic, f, indent=4)
        print(f"Created {subject_code}.json")
print("Process completed")
