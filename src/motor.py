#Motor
import micropython
import time
import cqueue


def motor_setup():
    pinPA0 = pyb.Pin (pyb.Pin.board.PA0, pyb.Pin.OUT_PP, value = 0)  # initializes the pin as an outport pin
    pinPA1 = pyb.Pin (pyb.Pin.board.PA1, pyb.Pin.OUT_PP, value = 0)
    tim5 = pyb.Timer (5, freq=1000)	# sets up the correct timer
    t5ch1 = tim5.channel (1, pyb.Timer.PWM, pin=pinPA0)
    t5ch2 = tim5.channel (2, pyb.Timer.PWM, pin=pinPA1)	# set up correct channel for timer
#     ch1.pulse_width_percent (100)
    pinPC1 = pyb.Pin (pyb.Pin.board.PC1, pyb.Pin.OUT_PP, value = 0)
    return(t5ch2,pinPA0,pinPA1,pinPC1,tim5)
    


def motor_speed(perc,ch5):
    ch5.pulse_width_percent (perc)
    

    

if __name__=="__main__":
    ret = motor_setup()
    ch5 = ret[0]
    pinpc1 = ret[3]
    pinpc1.high()
    pina0 = ret[1]
    pina0.low()
    ch5.pulse_width_percent (50)
    while True:
        try:
            pass
        except KeyboardInterrupt:
            ch.pulse_width_percent (0)
            break
#     motor_speed(75,ch5)
#     ch5.pulse_width_percent (50)
#     time.sleep(4)
#     ch5.pulse_width_percent (50)
#         for i in range(100):
#     while True:
#         motor_speed(50,ch5)
#     except KeyboardInterrupt:
#             ch5.pulse_width_percent (0)