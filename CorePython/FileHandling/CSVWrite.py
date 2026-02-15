file=open("players.csv","a")

nm=input('Enter name : ')
country=input('Enter country : ')
sport=input('Enter sport : ')

file.write(f"{nm},{country},{sport}\n")
file.close()