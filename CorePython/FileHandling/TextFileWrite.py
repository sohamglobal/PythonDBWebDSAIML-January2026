file=open("myinfo.txt","a")
line=input('Enter a line to store in file : ')
file.write(f"{line}\n")
file.close()