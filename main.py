def startup():
    global year, drivers, races
    
    year = input("year (YYYY): ")
    races = input("races: ")
    drivers = input("drivers: ")


def create_opening():
    file = open(year +"_results.txt", "a")
    
    file.write("{{Drivers standings|title=Drivers Championship|rounds="+str(races)+"\n")
    file.write("|coltitle=Race"+"\n"+"|hideupcoming=false|width=850"+"\n")
    
    print("Enter the end date of each round and then the final end date (usually the last GP end date) \n")
    
    for i in range(int(races)):
        date = input("round "+str(i+1)+" date (MM-DD): ")
        file.write("|round"+str(i+1)+"edate="+str(year)+"-"+str(date)+" \n")

    enddate = input("season end "+str(i+1)+" date (MM-DD): ")
    file.write("|edate="+str(year)+"-"+str(enddate)+" \n")
    
    file.write(" \n")
    file.close()


def create_points():
    file = open(year +"_results.txt", "a")

    print("Add the points value for positions 1-10\n")
    for i in range(10):
        points = input("pos "+str(i+1)+" points: ")
        file.write("|pt"+str(i+1)+"="+str(points)+" ")

    file.write(" \n")
    file.close()


def create_races():
    file = open(year +"_results.txt", "a")

    print("Add the race name without 'Grand Prix', e.g. just 'Australian'\n")
    for i in range(int(races)):
        race = input("race "+ str(i+1) + " name: ") + " Grand Prix"
        flag = input("race "+ str(i+1) + " flag: ")

        num = str(i+1)
        
        file.write("|r"+num+"={{RaceFlag|flag="+flag+" |race="+race+" |racelink="+year+" "+race+"}} \n")

    file.write(" \n")
    file.close()

    
def create_drivers():
    file = open(year +"_results.txt", "a")

    print("Enter each drivers full name, flag, and team as well as standings, with standings seperated by a comma \n")
    
    for i in range(int(drivers)):
        driver = input("driver "+ str(i+1) + ": ")
        flag = input("flag "+ str(i+1) + ": ")
        team = input("team "+ str(i+1) + ": ")
        standings = input("stnds "+ str(i+1) + ": ")

        num = str(i+1)

        file.write("|player"+num+"=" + driver + " |flag"+num+"=" + flag + " |team"+num+"=" + team + " |standings"+num+"="+standings+"\n")
    
    file.write("\n }}")
    file.close()


print("F1 Liquidpedia Inputter V0.1\nBy: kitbinary\n")

#run functions
startup()
create_opening()
create_points()
create_races()
create_drivers()

#close file
print("Data written!")
