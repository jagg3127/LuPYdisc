import os

def run_file():
    from LuPYdisc.Class.LuPYClient import _client
    try:
        if _client.PATH != None:
            path=_client.PATH.strip()
            if _client.DIRECTORY!=None: os.chdir(_client.DIRECTORY)
            with open(path.strip(), "r") as file:
                file=list(file)
                file_length=len(file)-1
                if file[file_length].strip() != "**": file.append("**")
                num=0
                while num < len(file):
                    run_str=[]
                    while True:
                        line=file[num].strip()
                        num+=1
                        if line == "**": break
                        if line != "":   
                            run_str.append(line)
    

                    _client.FILE_LIST_OF_LINES.append("\n ".join(run_str)+"\n")




    except AttributeError:
        return "ATTRIBUTE ERROR"