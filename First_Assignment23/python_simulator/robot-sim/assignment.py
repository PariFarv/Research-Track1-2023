from __future__ import print_function

import time
from sr.robot import *

"""
Assignment23


"""

""" float: Threshold for the control of the orientation"""
a_th = 2.0

""" float: Threshold for the control of the linear distance"""
d_th = 0.4

""" instance of the class Robot"""
R = Robot()



"""
Function for setting a linear velocity
    
Args: speed (int): the speed of the wheels
      seconds (int): the time interval
"""
def drive(speed, seconds) :

    R.motors[0].m0.power = speed
    R.motors[0].m1.power = speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

    
"""
Function for setting an angular velocity
    
Args: speed (int): the speed of the wheels
      seconds (int): the time interval
"""
def turn(speed, seconds) :

    R.motors[0].m0.power = speed
    R.motors[0].m1.power = -speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0


"""
Defining a function that can search for closest token,
 using lists with the priority of distance
"""
def find_tokens():

    Tokens_placement = [] #Introducing a list to store data
    dist = 100
    
    for token in R.see(): #A loop for repeating data extraction of each Token
        dist = token.dist
        rot_y = token.rot_y
        Token_data = [dist, rot_y]  #A list to hold information for every Tokens
        Tokens_placement.append(Token_data) #To add new elements to the list


    Square_tokens = sorted(Tokens_placement, key=lambda x: x[0])  #To sort the list of Tokens_data by distance to find the closest token first
    if Square_tokens[0][0] < 100:  #A loop for making sure there exist any Token
        return Square_tokens
    else:
        return -1 


"""
1) This function will first check if any token exists: 
2) If not, the program will stop at the moment. 
3) If yes, however, continue analyzing the situation;
4) The first condition that should be checked is distance. It will compare with the threshold and if the Robot is close enough, will grab it. 
   Now it's time to carry it to the center and release it there. And finally turn around to grab the next Token.
5) If it is not that close the Robot should find a way to the Token. This time the angular velocity threshold will be compared with the rotation. 
   In case the Robot cannot directly drive to the Token, it will turn to the right or left.
6) Arguments of this function are named to "paddle" mainly because they remind of a game paddle to control the Robot. 
   They are actually three parameters to set the time of drive() and turn() functions that made the Robot controllable. 
"""
def Load_Unload(paddle1,paddle2,paddle3) :
	while 1:
        	Square_tokens = find_tokens()
        	if Square_tokens == -1: #In case no Token is detected, the program will no longer run
    			print("I don't see any TOKEN!")
    			exit()
        	elif Square_tokens[0][0] < d_th: #If the Robot is close enough to the Token, first it will grab it, then carry it to the center, release it and then turn back to another one
    			R.grab()
    			print("Found ONE TOKEN!")
    			turn(-5, paddle1)
    			drive(30, paddle2)
    			R.release()
    			print("Done!")
    			drive(-10, 2)
    			turn(5, paddle3)
    			break
        	elif Square_tokens[0][1] <= a_th: #This monitor the distance between the Robot and each Token and then drive to it
    			drive(20, 0.5)
    			print("Ah, On the way Grabbing!")
        	elif Square_tokens[0][1] < -a_th: #If the Token was on the left of the robot (in comparison with the defined threshold) it will turn to the left
    			turn(-2, 0.5)
    			print("Left a bit...")
        	elif Square_tokens[0][1] > a_th: #If the Token was on the right of the robot (in comparison with the defined threshold) it will turn to the right
    			turn(2, 0.5)
    			print("Right a bit...")


"""
The main function is to call the Load_Unload function six times that the Robot be able to find, grab and release all six tokens.
"""
    
def main() : 


	Load_Unload(2,5,5)
	print("ONE Token has been carried!")
	Load_Unload(9,3,4)
	print("The second one has been carried as well!")
	Load_Unload(9,3.5,4)
	print("Half of Tokens have been moved!")
	Load_Unload(9,4,4.5)
	print("Wait for others to be loaded!")
	Load_Unload(10,3,4)
	print("Just One has left!")
	Load_Unload(8.5,3.5,1)
	print ("Mission Completed!")


main()

