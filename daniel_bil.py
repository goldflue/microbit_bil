venstreSensor = 0
højreSensor = 0
højreMotor = 0
venstreMotor = 0
def kørLigeud(num: number):
    ContinuousServo.spin_one_way_with_speed(AnalogPin.P1, num * 1)
    ContinuousServo.spin_other_way_with_speed(AnalogPin.P0, num * 0.5)
def drejVenstre(num2: number):
    ContinuousServo.spin_one_way_with_speed(AnalogPin.P1, num2 * 1)
    ContinuousServo.turn_off_motor(DigitalPin.P0)
def drejHøjre(num3: number):
    ContinuousServo.turn_off_motor(DigitalPin.P1)
    ContinuousServo.spin_other_way_with_speed(AnalogPin.P0, num3 * 1)

def on_forever():
    global venstreSensor, højreSensor, højreMotor, venstreMotor
    venstreSensor = pins.digital_read_pin(DigitalPin.P8)
    højreSensor = pins.digital_read_pin(DigitalPin.P9)
    højreMotor = pins.digital_read_pin(DigitalPin.P1)
    venstreMotor = pins.digital_read_pin(DigitalPin.P0)
    if højreSensor == 0 and venstreSensor == 0:
        kørLigeud(2)
    elif højreSensor == 1 and venstreSensor == 0:
        drejHøjre(4)
    elif højreSensor == 0 and venstreSensor == 1:
        drejVenstre(4)
    else:
        ContinuousServo.turn_off_motor(DigitalPin.P0)
        ContinuousServo.turn_off_motor(DigitalPin.P1)
basic.forever(on_forever)
