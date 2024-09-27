import tarfile
import os
import sys


dirname = ""
factpath = 'emulator'
with tarfile.open('emulator.tar', 'a') as tar:
    while True:
        command = input('~' + dirname + '# ')

        
        if command == 'ls':
            if factpath == 'emulator':
                for name in tar.getnames():
                    if "/" in name:
                        pass
                    else:
                        print(name)
            else:
                if dirname in tar.getnames():
                    for member in tar.getmembers():
                        if member.name.startswith(dirname + "/"):
                            print("  " + member.name[len(dirname) + 1:])

                            
        elif command == "exit":
            exit(0)


        elif command.startswith('tail'):
            try:
                file_name = command.split(" ")[1]
                with open(file_name, 'r') as file:
                    lines = file.readlines()
                    for line in lines[-1:-11:-1]:
                        print(line, end='')
            except:
                print("no file")

                
        elif command == "clear":
            print("\n" * 45)

            
        elif command.startswith('cd'):
            if len(command) == 2:
                dirname = ""
                factpath = 'emulator'
            else:
                ndir = command.split(" ")[1]
                if ndir in tar.getnames():
                    dirname = ndir
                    factpath = 'emulator' + '/' + ndir
                else:
                    print("sh: cd: can't cd to " + ndir + ": No such file or directory")

                    
        
        else:
            print("Неизвестная команда")
