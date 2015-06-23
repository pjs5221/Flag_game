import time
import RPi.GPIO as GPIO
import random

GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.OUT)  #Blue Flag
GPIO.setup(18, GPIO.OUT)  #White Flag
GPIO.setup(5, GPIO.IN)
GPIO.setup(6, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(19, GPIO.IN)
GPIO.setup(26, GPIO.IN)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

motor1 = GPIO.PWM(15, 50)
motor2 = GPIO.PWM(18, 50)
GPIO.output(23, GPIO.LOW)	#Green
GPIO.output(24, GPIO.LOW)	#Red

def Easy_mode():
	easy_order = random.randint(1,4)
	if(easy_order == 1):
		print("Blue flag Up!\n")
		while(GPIO.input(5) == 0 and GPIO.input(6) == 0 and GPIO.input(13)
					== 0 and GPIO.input(19) == 0):
			time.sleep(0.001)
		if(GPIO.input(5) == 1):
			motor1.start(12.5)
			GPIO.output(23, GPIO.HIGH)
			print("\nYou Win^0^") 
		else:
			if(GPIO.input(6) == 1):
				motor1.start(2.5)
			elif(GPIO.input(13) == 1):
				motor2.start(12.5)
			elif(GPIO.input(19) == 1):
				motor2.start(2.5)
			GPIO.output(24, GPIO.HIGH)
			print("\nYou Lose-_-")
		time.sleep(3)
	elif(easy_order ==2):
		print("Blue flag Down!\n")	
		while(GPIO.input(5) == 0 and GPIO.input(6) == 0 and GPIO.input(13)
					== 0 and GPIO.input(19) == 0):
			time.sleep(0.001)
		if(GPIO.input(6) == 1):
			motor1.start(2.5)
			GPIO.output(23, GPIO.HIGH)
			print("\nYou Win^0^")
		else:		
			if(GPIO.input(5) == 1):
				motor1.start(12.5)
			elif(GPIO.input(13) == 1):
				motor2.start(12.5)
			elif(GPIO.input(19) == 1):
				motor2.start(2.5)
			GPIO.output(24, GPIO.HIGH)
			print("\nYou Lose-_-")
		time.sleep(3)
	elif(easy_order ==3):
		print("White flag Up!\n")	
		while(GPIO.input(5) == 0 and GPIO.input(6) == 0 and GPIO.input(13)
					== 0 and GPIO.input(19) == 0):
			time.sleep(0.001)
		if(GPIO.input(13) == 1):
			motor2.start(12.5)
			GPIO.output(23, GPIO.HIGH)
			print("\nYou Win^0^")
		else:	
			if(GPIO.input(5) == 1):
				motor1.start(12.5)
			elif(GPIO.input(6) == 1):
				motor1.start(2.5)
			elif(GPIO.input(19) == 1):
				motor2.start(2.5)
			GPIO.output(24, GPIO.HIGH)
			print("\nYou Lose-_-")
		time.sleep(3)
	else:
		print("White flag Down!\n")
		while(GPIO.input(5) == 0 and GPIO.input(6) == 0 and GPIO.input(13)
					== 0 and GPIO.input(19) == 0):
			time.sleep(0.001)
		if(GPIO.input(19) == 1):
			motor2.start(2.5)
			GPIO.output(23, GPIO.HIGH)
			print("\nYou Win^0^")
		else:
			if(GPIO.input(5) == 1):
				motor1.start(12.5)
			elif(GPIO.input(6) == 1):
				motor1.start(2.5)
			elif(GPIO.input(13) == 1):
				motor2.start(12.5)
			GPIO.output(24, GPIO.HIGH)
			print("\nYou Lose-_-")
		time.sleep(3)

	GPIO.output(23, GPIO.LOW)
	GPIO.output(24, GPIO.LOW)	
	motor1.start(7.5)
	motor2.start(7.5)
	time.sleep(0.5)

def Hard_mode():
	isReleased = True
	blue_flag = random.randint(1,2)
	white_flag = random.randint(1,2)
	if(blue_flag == 1 and white_flag == 1):
		print("Blue flag Up / White flag Up!")	
		while(GPIO.input(5) == 0 and GPIO.input(6) == 0 and GPIO.input(13)
					== 0 and GPIO.input(19) == 0):
			time.sleep(0.001)
		if(GPIO.input(5) == 1):
			motor1.start(12.5)
			visReleased = False
			time.sleep(1)		
			while(GPIO.input(5) == 0 and GPIO.input(6) == 0 and GPIO.input(13)== 0 and GPIO.input(19) == 0):
				isReleased = True
			if(GPIO.input(13) == 1 and isReleased == True):
				motor2.start(12.5)
				GPIO.output(23, GPIO.HIGH)
				print("\nYou Win^0^")
			else:
				GPIO.output(24, GPIO.HIGH)
				print("\nYou Lose-_-")

		else:
			GPIO.output(24, GPIO.HIGH)
			print("\nYou Lose-_-")
	
		time.sleep(3)


	elif(blue_flag == 1 and white_flag == 2):
		print("Blue flag Up / White flag Down!")	
		while(GPIO.input(5) == 0 and GPIO.input(6) == 0 and GPIO.input(13)
					== 0 and GPIO.input(19) == 0):
			time.sleep(0.001)
		if(GPIO.input(5) == 1):
			motor1.start(12.5)
			visReleased = False
			time.sleep(1)		
			while(GPIO.input(5) == 0 and GPIO.input(6) == 0 and GPIO.input(13)== 0 and GPIO.input(19) == 0):
				isReleased = True
			if(GPIO.input(19) == 1 and isReleased == True):
				motor2.start(2.5)
				GPIO.output(23, GPIO.HIGH)
				print("\nYou Win^0^")
			else:
				GPIO.output(24, GPIO.HIGH)
				print("\nYou Lose-_-")
		else:
			GPIO.output(24, GPIO.HIGH)
			print("\nYou Lose-_-")
		time.sleep(3)


	elif(blue_flag == 2 and white_flag == 1):
		print("Blue flag Down / White flag Up!")
		while(GPIO.input(5) == 0 and GPIO.input(6) == 0 and GPIO.input(13)
					== 0 and GPIO.input(19) == 0):
			time.sleep(0.001)
		if(GPIO.input(6) == 1):
			motor1.start(2.5)
			visReleased = False
			time.sleep(1)		
			while(GPIO.input(5) == 0 and GPIO.input(6) == 0 and GPIO.input(13)== 0 and GPIO.input(19) == 0):
				isReleased = True
			if(GPIO.input(13) == 1 and isReleased == True):
				motor2.start(12.5)
				GPIO.output(23, GPIO.HIGH)
				print("\nYou Win^0^")
			else:
				GPIO.output(24, GPIO.HIGH)
				print("\nYou Lose-_-")
		else:
			GPIO.output(24, GPIO.HIGH)
			print("\nYou Lose-_-")
		time.sleep(3)

	else:
		print("Blue flag Down / White flag Down!")	
		while(GPIO.input(5) == 0 and GPIO.input(6) == 0 and GPIO.input(13)
					== 0 and GPIO.input(19) == 0):
			time.sleep(0.001)
		if(GPIO.input(6) == 1):
			motor1.start(2.5)
			visReleased = False
			time.sleep(1)		
			while(GPIO.input(5) == 0 and GPIO.input(6) == 0 and GPIO.input(13)== 0 and GPIO.input(19) == 0):
				isReleased = True
			if(GPIO.input(19) == 1 and isReleased == True):
				motor2.start(2.5)
				GPIO.output(23, GPIO.HIGH)
				print("\nYou Win^0^")
			else:
				GPIO.output(24, GPIO.HIGH)
				print("\nYou Lose-_-")
		else:
			GPIO.output(24, GPIO.HIGH)
			print("\nYou Lose-_-")
		time.sleep(3)

	GPIO.output(23, GPIO.LOW)
	GPIO.output(24, GPIO.LOW)
	motor1.start(7.5)
	motor2.start(7.5)
	time.sleep(0.5)

while True:
	print("\n\n<Select Mode>")
	print("Easy : 1  Hard : 2")

	mode = raw_input()

	if(mode == "1"):
		Easy_mode()
	if(mode == "2"):
		Hard_mode()


