import time 
import random

def getting_input ():
    input = random.randint (0,1)

    return input 

buttonPressed = False
ledOn = False
delayTimer = 0
ledMessage = False
totalNumberOfValidPresses = 0

def button_press_bounce ():
    global buttonPressed, ledOn, delayTimer, ledMessage, totalNumberOfValidPresses

    time.sleep (0.5)

    data = getting_input ()

    if data == 1 and ledOn:
        print ("The LED is on, please wait. DONT SPAM")
    elif data == 1 and not buttonPressed: 
        buttonPressed = True
    elif data == 0 and buttonPressed:
        buttonPressed = False
        ledOn = True 
        delayTimer = time.time()
        ledMessage = False
        totalNumberOfValidPresses += 1
        print ("The LED will now stay on for 3 seconds")
        

    if ledOn and not ledMessage: 
        print ("LED: ON")
        ledMessage = True

    if ledOn and (time.time() - delayTimer) > 3:
        ledOn = False
        ledMessage = False 
        print ("LED: OFF")
    
    


if __name__ == "__main__":
    while True: 
        try: 
            button_press_bounce()
        except KeyboardInterrupt:
            print ("\nThe program will now shut down")
            print (f"Total number of valid presses: {totalNumberOfValidPresses}")
            break 
