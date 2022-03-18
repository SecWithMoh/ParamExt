import sys
import re
import subprocess
from logging import exception
import urllib.parse as lazy


def RunUfnurl(Fname):
    print("[+] I'm Working On Unfurl Section...")
    bashcmd="cat "+Fname.strip()+" | unfurl format %q > Query.txt"
    subprocess.run(['/bin/bash', '-c', bashcmd])




def ParamExt():
    Result_File = open("output.txt", "a")
    Trash_File = open("trash.txt", "a")
    FileName= "Query.txt"
    print("[+] I'm Working on Extract Param Section...")
    regex = re.compile('[@!#-$%^*()<>?/\|;.}{~:]')
    try:
        with open(FileName) as infile:
            try:
                for line in infile:

                    Xrawurl=lazy.parse_qsl(line)

                    for i in range(len(Xrawurl)):
                        tmp=lazy.unquote(Xrawurl[i][0])
                        tmp=tmp.replace("amp;",'')
                        if (regex.search(tmp.strip()) == None):
                            Result_File.write(tmp.strip()+"\n")
                        else:
                            Trash_File.write(tmp+"\n")

            except Exception as Inex:
                print("[-]Error Inside main Process Section:> "+Inex)
        Result_File.close()
        Trash_File.close()
    except Exception as Oex:
        print("[-]main ParamExt Func Error:> "+Oex)



def UniqueParam(Ufname):
    print("[+] I'm Working On Unique Param Section...")
    bashcmd="cat output.txt | sort -u >"+Ufname.strip()+""
    subprocess.run(['/bin/bash', '-c', bashcmd])
    

if __name__ == "__main__":
    print("  ____                                _____        _                    ")
    print(" |  _ \  __ _  _ __  __ _  _ __ ___  | ____|__  __| |_     _ __   _   _ ")
    print(" | |_) |/ _` || '__|/ _` || '_ ` _ \ |  _|  \ \/ /| __|   | '_ \ | | | |")
    print(" |  __/| (_| || |  | (_| || | | | | || |___  >  < | |_  _ | |_) || |_| |")
    print(" |_|    \__,_||_|   \__,_||_| |_| |_||_____|/_/\_\ \__|(_)| .__/  \__, |")
    print("                                                          |_|     |___/ ")
    print("         Offline Query String Parameter Extractor From URL")
    print("                 https://github.com/BbhunterOne")
    print("")
    print("")
    print("----------------------------------------------------------------------")

    try:
        if len(sys.argv) > 2:
            RunUfnurl(sys.argv[1])
            ParamExt()
            UniqueParam(sys.argv[2])
            print("[+] All Tasks Well Done.")
        else:
            print("[-]Please provide Input and Output FileName. (python3 ParamExt.py urls.txt params.txt)")
            sys.exit(0)  
    except Exception as err:
        print("[*]Main error:"+err)
