
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


# print(calibrationValue())  


numbers = {'zero':0 , 'one': 1 , 'two' : 2 , 'three' : 3 , 'four':4 , 'five': 5 , 'six' : 6 , 'seven': 7 , 'eight' : 8 , 'nine' : 9}
# print( numbers.)

# print( "sdoi".find("oi"))



def calibrationValuePart2():
    with open(R'C:\mine\dev\event of code\year 2023\day 1\example.txt', 'r') as file:
        totalCalibre = 0
        # print(("s".isdigit()))
        for line in file:
            calibre= ""
            
            minDigitalCalibre = {'pos':len(line) , 'value':""}
            maxDigitalCalibre = {'pos':-1 , 'value':""}


            for num in numbers:
                # print(num)
                if (line.find(num)!= -1 and line.find(num) < minDigitalCalibre['pos'] ):
                    minDigitalCalibre['pos']= line.find(num)
                    minDigitalCalibre['value'] = num
                    
                   
                if (line.find(num)!= -1 and line.find(num)> maxDigitalCalibre['pos'] ):
                    maxDigitalCalibre['pos']= line.find(num)
                    maxDigitalCalibre['value'] = num
                    # print(maxDigitalCalibre['value'])
            # print(minDigitalCalibre['value'] ,minDigitalCalibre['pos'] )        
            # print(maxDigitalCalibre['value'] ,maxDigitalCalibre['pos'] ) 
            if(minDigitalCalibre['value']!= ""):
                calibre = str(numbers[minDigitalCalibre['value']])     
            # print("----- end of line")
    

          
            for i in range (len(line)) : 
                if(line[i].isdigit() and i < minDigitalCalibre['pos'] ):
    #                 # print(char)
                    
                    calibre = line[i]
                    # print('calibre take first diget' , line[i])
                    break
            for i in range (len(line)-1 , -1 , -1) : 
                if(line[i].isdigit() and i > maxDigitalCalibre['pos']):
    #                 # print(char)
                    calibre += line[i]
                    # print('calibre take the secande degite' , calibre)
                    break
            if(len(calibre)==1 and maxDigitalCalibre['value']!= ""):
                calibre += str(numbers[maxDigitalCalibre['value']])
            totalCalibre += int(calibre)
    return totalCalibre

print(calibrationValuePart2())