# Example Game Functions Project, Ryan Kelley, v0.0 
import random 

def functionOne(): 
    pass

def functionTwo(param1):
    pass

def functionThree(param1 = "Default Value"):
    pass

def functionFour(param1, param2, param3):
    pass 

def catchBall(throwQuality, passCatchScore, weather): 
    if throwQuality > 5.0 and passCatchScore >= 99 and weather == 'Sunny':
        ballCaught = True
    elif throwQuality > 4.0 and passCatchScore >= 75 and weather == 'Windy':
        ballCaught = False 
    else:
        print('Oh, no, interception!\n')
        ballIntercepted = True 
        return ballIntercepted  
    return ballCaught


