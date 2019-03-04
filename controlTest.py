import time
import grovepi

p1 = 0
p2 = 2

butt = 4

grovepi.pinMode(p1, "INPUT")
grovepi.pinMode(p2, "INPUT")
grovepi.pinMode(butt, "INPUT")
time.sleep(1)

# values from example for maths stuff
adc_ref = 5
grove_vcc = 5
full_angle = 300

def processRotaryInput(rotary_input):
    if rotary_input <= 11.5:
        paddle_coord = 0
    elif rotary_input >= (1023-11.5):
        paddle_coord = 1000
    else:
         paddle_coord = rotary_input
    
    return int(paddle_coord / 10)


while True:
    try:
        p1_value = processRotaryInput(grovepi.analogRead(p1))
        p2_value = processRotaryInput(grovepi.analogRead(p2))
        butt_value = grovepi.digitalRead(butt)
        print(str(p1_value) + " " + str(p2_value) + " " + str(butt_value))
#       Rotary Sensors output number from 0 - 1023
    except IOError:
        print("Error")



