import random
import time

"""
What you can get from this file 
fullValueList - List of the most current values (time can be changed)
averageList - List of the most current average values (time can be changed)

"""
valueList = []
fullValueList = []
averageList = []
fullValueListValuesOnly = []
averageListValuesOnly = []

def get_average_list (CutOffTime): 
    global averageList, fullValueList, fullValueListValuesOnly, averageListValuesOnly
    
    while True:
        time.sleep (1) # Get input every 1 second

        randomNumberGenerator = (random.randint (0,100)) #Generate a random input 
        currentTime = time.time()
        average = get_average(randomNumberGenerator) #Uses the get_average function to get the average
        fullValueList.append ((currentTime, randomNumberGenerator)) #Appends the inputted value from the rng into a list 
        print (f"The Input Value: {randomNumberGenerator}") #Shows the value that was inputted 
        

        if average is not None:
            averageList.append ((currentTime, average))

        #filter out values older than 5 seconds(Change the numbers here if you want to change the filter)(Maintenence param!)
        cutOffTimeForFullValueList = time.time() - CutOffTime
        #filter out values older than 3 minutes (Change the numbers here if you want to change the filter)(Maintenence param!)
        cutOffTimeForAverageList = time.time() - CutOffTime
        
        fullValueList = [value for value in fullValueList if value[0] >= cutOffTimeForFullValueList]
        averageList = [value for value in averageList if value[0] >= cutOffTimeForAverageList]

        fullValueListValuesOnly = [value[1] for value in fullValueList if value[0] >= cutOffTimeForFullValueList]
        averageListValuesOnly = [value[1] for value in averageList if value[0] >= cutOffTimeForAverageList]
        
    
        return averageList
    

def get_average (randomInt):
    global valueList #Declare that we are using the global value list 
    valueList.append(randomInt)
    print (f"checking current list: {valueList}") #Just for me to check if  the current list have reseted. Can safely delete or comment

    if len(valueList) == 5: # change to time 
        sum_values = 0 
        
        for i in valueList:
            sum_values += i
        
        #sum_values = sum(valueList), a quicker way to do it

        print (f"The sum is {sum_values}") #Just for me to check. Can safely delete or comment 
        average = sum_values / 5 
        print (f"The average is {average}") #Just for me to check. Can safely delete or comment 
        valueList = [] #reset it
        return average
    



if __name__ == "__main__":
    try:
        while True: 
            get_average_list(5)
    except KeyboardInterrupt:
        # print (f"The list of averages: \n\t {averageList}")
        # for timestamp, value in averageList:
        #     print(f"\tTimestamp: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))}, Value: {value}")

        # print (f"The full List of inputs gotten:\n\t{fullValueList}")
        # for timestamp, value in fullValueList:
        #     print(f"\tTimestamp: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))}, Value: {value}")

        print (f"Values only in Full Value List: {fullValueListValuesOnly}")
        print (f"Values only in Average List: {averageListValuesOnly}")
    # un-comment/comment line 63,64 and 67,68 above ^^, if you want the timestamps for each value printed out

    
    