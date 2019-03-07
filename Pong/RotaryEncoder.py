import grove

# ROTARY ENCODER STUFF BELOW 
potentiometer1 = 0
potentiometer2 = 0
grovepi.pinMode(potentiometer1,"INPUT")
grovepi.pinMode(potentiometer2,"INPUT")
adc_ref = 5
grove_vcc = 5
full_angle = 300
# Read sensor value from potentiometer
sensor_value = grovepi.analogRead(potentiometer)

# Calculate voltage
voltage = round((float)(sensor_value) * adc_ref / 1023, 2)

# Calculate rotation in degrees (0 to 300)
degrees = round((voltage * full_angle) / grove_vcc, 2)

screenposition = int(degrees/full_angle * 100) 




