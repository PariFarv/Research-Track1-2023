Assignment23 (Parisa Farvardin, S6101141)
================================

The goal of this project is to control the Robot to catch the golden boxes which are called `Token` in the code.

Running the simulator
----------------------

The project requires the Python2 installation, after cloning the project and its simulator from the GitHub link, it would be accessible to run the project:
```bash
$ python2 run.py assignment.py
```

Code Description
---------

This code is basically designed to run the Robot in a direct direction and turn to the right and left with defined speed and given time with a feature called `paddle`, and also the Robot will catch 6 golden boxes and then carry to almost the middle of the space and put them. In other words, this Robot has an aim to go for the boxes to move them in the Arena area. 

To do so, it is needed to define functions in order to not repeat a long piece of code. As mentioned before, one of the most important functions is the one which drives the Robot. The Robot includes two motors that should have a velocity to start moving. By assigning the same velocity to the motors of the Robot, it will move.
 
The other function is the one that helps the Robot turn. The fact is that when a velocity with the same value and opposite direction is assigned to the motors of the Robot, it will turn.

One of the vital functions of this code is the one that makes the Robot find the golden boxes. It is called `find_tokens` and its output is, as its name, to find the tokens. There are lots of strategies that could be determined, however, one of the most straightforward ones is to use a list. It is necessary to define the distance and the rotation of the boxes and then sort them with respect to the closest distance. Therefore, by calling this function, the Robot is going to find all tokens information (distance and rotation) and check if there are not any boxes, will return -1.

The last and probably foremost function is called `Load_Unload` which helps the Robot move through the given space, grab the boxes, and then release them in a controlled place. In this function, three arguments, called `paddle`, are defined so that with these paddles the Robot gains the capability of catching all boxes. The code is written in a way that first checks the distance of the boxes and the Robot with a threshold and if it is so close will grab it and go for releasing it in the center of the space. If not, the angle of the robot and the boxes is going to be checked with a threshold and then the Robot will make a decision to go forward, turn right, or turn left to grab the box and keep doing it to finally catch it. This function also exits the program if the Robot cannot find any box. 



Pseudocode
---------

Call the Robot class

Define a function to `Drive` the Robot in a straight way

Define a function to `Turn` the Robot 

Define a function to `Find the Token`:

Use the information in the robot class to have the Robot distance and 
rotation.

Store all distance and rotation for each Token in a list.

Sort them with respect to distances.

If there are any Token

       Have the distance and rotation data.

Else

       Return -1

Define a function to `Load and Unload` the Tokens:

	While 1:

		If there are no Tokens

			Print `I don't see any token!! ` and exit the code.

		Else if the Robot is near a Token

			Grab the Token and print `Found ONE TOKEN! `.

			Then move to the center, release it, and print `Done`.

			Then turn and go for other Tokens.

		Else if the Token is not so close

			Drive to it.

		Else if the Token is located on the left side of the Robot

			Turn left

		Else if the Token is located on the right side of the Robot
			Turn right

Repeat this function for all 6 Tokens.	

Results
---------

As a result, the final frame of the game is 6 boxes in the center of the space which is shown in the below picture:

<img src="./showimg/init.png" width="39%"/> <img src="./showimg/final.png" width="39%"/><br>






