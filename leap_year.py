def leap_year(year):
    try:
        year = int(year)
    except:
        #print("error: input must be an integer")
        return "error: input must be an integer"
    if  year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                #print(year, "is a leap year\n")
                return "yes"
            else:
                #print(year, "is not a leap year\n")
                return "no"
        else:
            #print(year, "is a leap year\n")
            return "yes"
            
    else:
        #print(year, "is not a leap year\n")
        return "no"
        
#leap_year(400)