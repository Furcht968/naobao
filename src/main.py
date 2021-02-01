import sys,re,os

def compileNb(file):
    nbfile = open(file,encoding="UTF-8")
    data = nbfile.read().replace("\n","")
    fb = ""
    for i in range(0, len(data), 3):
        now = data[i:i+3]
        if(re.match(r"[甲乙]{3}",now)):
            if(now=="甲甲甲"):
                fb+=">"
            elif(now=="甲甲乙"):
                fb+="<"
            elif(now=="甲乙甲"):
                fb+="+"
            elif(now=="甲乙乙"):
                fb+="-"
            elif(now=="乙甲甲"):
                fb+="."
            elif(now=="乙甲乙"):
                fb+=","
            elif(now=="乙乙甲"):
                fb+="["
            elif(now=="乙乙乙"):
                fb+="]"
        else:
            print("SyntaxError: Regulation error.")
            sys.exit(1)
    nbfile.close()
    return fb

def bfToNb(text):
    fixed = text.replace(">","甲甲甲").replace("<","甲甲乙").replace("+","甲乙甲").replace("-","甲乙乙").replace(".","乙甲甲").replace(",","乙甲乙").replace("[","乙乙甲").replace("]","乙乙乙")
    return fixed

def brainfucking(text):
    mem_size = 30000
    mem = [0 for i in range(mem_size)]
    ptr=0
    code = text.replace("\n","")
    head=0
    syntax = ["+","-",">","<","[","]",".",","]
    while head < len(code):
        if(code[head]=="+"):
            mem[ptr] += 1
        elif(code[head]=="-"):
            mem[ptr] -= 1
        elif(code[head]==">"):
            ptr += 1
            if(ptr > mem_size):
                print("MemoryError: OverFlowed!")
                sys.exit(1)
        elif(code[head]=="<"):
            if(ptr==0):
                print("MemoryError: Can't decryment anymore")
                sys.exit(1)
            ptr -= 1
        elif(code[head]=="["):
            if(mem[ptr]==0):
                count = 1
                while count != 0:
                    head += 1
                    if(head==len(code)):
                        print("SyntaxError: ] is missing.")
                        sys.exit(1)
                    if(code[head]=="["):
                        count += 1
                    elif(code[head]=="]"):
                        count -= 1
        elif(code[head]=="]"):
            if(mem[ptr]!=0):
                count = 1
                while count != 0:
                    head -= 1
                    if(head < 0):
                        print("SyntaxError: [ is missing.")
                        sys.exit(1)
                    if(code[head]=="]"):
                        count += 1
                    elif(code[head]=="["):
                        count -= 1
                         
        elif(code[head]=="."):
            print(chr(mem[ptr]),end="")
        elif(code[head]==","):
            mem[ptr] = ord(sys.stdin.buffer.read(1))
        else:
            print("SyntaxError: Regulation error.")
            sys.exit(1)
        head += 1

if __name__ == "__main__":
    if(len(sys.argv)==1):
        print("""
A programing language's Brainfuck of Chinese character 

Usage: naobao <Command|Nb/Bf Program> [<arguments>]

If Bf file select then interprete brainfuck.
If Nb file select then interprete naobao.

Available commands:
    compile   Compile to Brainfuck or naobao

""")
    if(len(sys.argv)>=2):
        if(sys.argv[1]=="compile"):
            if(len(sys.argv)!=3):
                print("Please select file.")
                sys.exit(1)
            else:
                bffile = sys.argv[2]
                
                if(os.path.exists(bffile)):
                    if(bffile.split(".")[-1]=="bf"):
                        data = open(sys.argv[2].split(".")[0]+".nb","w",encoding="UTF-8")
                        bfdata = open(bffile)
                        data.write(bfToNb(bfdata.read()))
                        data.close()
                        bfdata.close()
                        print("Compiled to brainfuck to naobao")
                    elif(bffile.split(".")[-1]=="nb"):
                        prg = compileNb(sys.argv[2])
                        data = open(sys.argv[2].split(".")[0]+".bf","w",encoding="UTF-8")
                        data.write(prg)
                        data.close()
                        print("Compiled to naobao to brainfuck")
                    else:
                        print("This file is not bf file.")
                        sys.exit(1)
                else:
                    print("File not found.")
                    sys.exit(1)


        elif(sys.argv[1].split(".")[-1]=="nb"):
            if(os.path.exists(sys.argv[1])):
                prg = compileNb(sys.argv[1])
                brainfucking(prg)
            else:
                print("File not found.")
        elif(sys.argv[1].split(".")[-1]=="bf"):
            if(os.path.exists(sys.argv[1])):
                brainfucking(open(sys.argv[1]).read())
            else:
                print("File not found.")
        else:
            print("Wasn't able to format specific.")
