import os
import json

dic = {"Empty": True}
path = r"/Users/albert/Documents/IGCSE_Past_Papers"
code = "Empty"
files = ["Empty"]

help_doc = '''Help on module 'search_past_papers':
--- set
  > set (int)code
    Accepts a valid 4-digit integer subject code and loads corresponding json. 
    Returns a dictionary from the json file that can be later used in 'print'.
--- list
  > list *args
    Accepts multiple arguments that will be concatenated into a string.
    Returns all past papers that contain the string.
--- open
  > open (char)option
    Accepts a character indicating which file type to be opened.
    - q: question paper only
    - m: corresponding mark scheme only
    - b: both question paper and corresponding mark scheme
    Opens all files of the indicated type returned from the last 'list'. 
--- help
  > help
    Returns a help document. 
--- quit
  > quit
    Leaves the program properly and directly. '''


def subject(code): 
    dic = json.load(open(f"{code}.json"))
    return dic


def search(dic, string):
    flag = True
    files = []
    for year in dic.keys():
        for file in dic[year].keys():
            for page in dic[year][file].keys():
                if string in dic[year][file][page]:
                    print(file, f"[Page {page}]")
                    files.append(file)
                    flag = False
    if flag:
        print("Warning: no file found, unable to use 'open' later")
        files = ["Empty"]
    return files


try: 
    while True:
        action = input(">>> ")
        action_l = action.split()
        
        if len(action_l) <= 0:
            print("Invalid syntax: no command entered")
            
        elif action_l[0] == "set":
            if len(action_l) == 2:
                if len(action_l[1]) == 4: 
                    try:
                        code = action_l[1]
                        dic = subject(code)
                    except FileNotFoundError:
                        print("Execution failed: subject not supported, try a different code")
                else:
                    print(f"Execution failed: 'set' does not except argument '{action_l[1]}'")
            else:
                print(f"Execution failed: 'set' expects 1 argument, gets {len(action_l)-1}")
                
        elif action_l[0] == "list":
            if len(action_l) >= 2: 
                if "Empty" not in dic.keys():
                    files = search(dic, " ".join(action_l[1:]).lower())
                else: 
                    print("Execution failed: no subject selected, use 'set' first")
            else:
                print("Execution failed: 'list' expects at least 1 argument, gets 0")

        elif action_l[0] == "help":
            print(help_doc)

        elif action_l[0] == "quit":
            print("Process completed")
            break

        elif action_l[0] == "open":
            if len(action_l) == 2:
                if code != "Empty" and "Empty" not in files:
                    if action_l[1] == "m" or action_l[1] == "b":
                        for file in files: 
                            os.system(f"open {path}/{code}/20{file[6:8]}/{file[:9]}ms{file[11:]}")
                    if action_l[1] == "q" or action_l[1] == "b": 
                        for file in files: 
                            os.system(f"open {path}/{code}/20{file[6:8]}/{file}")
                    elif action_l[1] not in ["q", "m", "b"]:
                        print(f"Execution failed: 'open' does not except argument '{action_l[1]}'")
                elif code == "Empty":
                    print("Execution failed: no subject selected, use 'set' first")
                else: 
                    print("Execution failed: last 'list' finds no file")
            else:
                print(f"Execution failed: 'open' expects 1 argument, gets {len(action_l)-1}")
            
        else:
            print(f"Invalid syntax: command '{action_l[0]}' not found")

except KeyboardInterrupt:
    print("Process exited")
