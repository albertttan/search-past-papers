import json

subject_code = input("Subject code: ")
dic = json.load(open(f"{subject_code}.json"))
search_str = input("Word or words to be searched: ").lower()
flag = True
print("\nThe following are files that contain such string: ")

for year in dic.keys():
    for file in dic[year].keys():
        for page in dic[year][file].keys():
            if search_str in dic[year][file][page]:
                print(file, f"[Page {page}]")
                flag = False

if flag:
    print("No file found")
