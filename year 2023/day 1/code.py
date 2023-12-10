
def calibrationValue():
    with open(R'C:\mine\dev\event of code\year 2023\day 1\input.txt', 'r') as file:
        totalCalibre = 0
        # print(("s".isdigit()))
        for line in file:
            calibre= ""
            # Process each line
            # print(len(line.strip()))
            for char in (line) : 
                if(char.isdigit()):
                    # print(char)  
                    calibre += char
                    break
            for char in (line[::-1]) : 
                if(char.isdigit()):
                    # print(char)
                    calibre += char
                    break
            totalCalibre += int(calibre)
    return totalCalibre                 


print(calibrationValue())  