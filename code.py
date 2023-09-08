
# these lines import the necessary libraries to run this code
import time
import board
import digitalio
import pwmio

from adafruit_motor import motor #Imports a function from the adafruit_motor libraryf


left_motor_forward = board.GP12 #Initializes the variable left_motor_forward and attaches it to GP.12
left_motor_backward = board.GP13 #Initializes the variable left_motor_backward and attaches it to GP.12
right_motor_forward = board.GP14
right_motor_backward = board.GP15

pwm_La = pwmio.PWMOut(left_motor_forward, frequency=10000) # tells the hat the motor is an output
pwm_Lb = pwmio.PWMOut(left_motor_backward, frequency=10000)
pwm_Lc = pwmio.PWMOut(right_motor_forward , frequency=10000)
pwm_Ld = pwmio.PWMOut(right_motor_backward, frequency=10000)

Left_Motor = motor.DCMotor(pwm_La, pwm_Lb) # Configuration line(it's required)
Left_Motor_speed = 0 # intiates the variable for the left motor and it starts at 0
Right_Motor = motor.DCMotor(pwm_Lc, pwm_Ld)
Right_Motor_speed = 0




while True:

    Left_Motor_speed = 1 #Makes left motor roll foward
    Left_Motor.throttle = Left_Motor_speed
    time.sleep(1)
    Left_Motor_speed = 1
    Left_Motor.throttle = Left_Motor_speed
    time.sleep(1)
    Right_Motor_speed= 1
    Right_Motor.throttle = Right_Motor_speed
    time.sleep(1)
    Right_Motor_speed = 1
    Right_Motor.throttle = Right_Motor_speed
    time.sleep(1)







