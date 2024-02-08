'''!
@file led.py
this file uses the PWM to control a LED

@author Abe Muldrow, Lucas Rambo, Peter Tomson
@date February 1st, 2024
'''

# imports
import micropython
import time
import cqueue

#
interrupt = pyb.Timer(1,freq = 1000)
#stores value for the pinC0 output pin
## Size of the queue for data storage
QUEUE_SIZE = 1000
## initializes the queue
int_queue = cqueue.IntQueue(QUEUE_SIZE)
first = 1
micropython.alloc_emergency_exception_buf(100)


def led_setup():
    pinPA0 = pyb.Pin (pyb.Pin.board.PA0, pyb.Pin.OUT_PP, value = 0)  # initializes the pin as an outport pin
    tim2 = pyb.Timer (2, freq=1000)	# sets up the correct timer 
    ch1 = tim2.channel (1, pyb.Timer.PWM_INVERTED, pin=pinPA0)	# set up correct channel for timer
    ch1.pulse_width_percent (100)
    return(ch1,pinPA0,tim2)
    

def led_brightness(perc,ch1):

    perc = 100 - perc
    ch1.pulse_width_percent (perc)
    

def led_interrupt():
    if first == 1:
        perc = 0
        up_flg = 1
        first = 0
    if up_flg == 1:
        perc = perc + (1/5000)
        led_brightness(perc,ch1)   
        if perc == 100:
            up_flg = 0
    else:
        perc = perc - (1/5000)
        led_brightness(perc,ch1)   
        if perc == 100:
            up_flg = 1


if __name__=="__main__":
    ret = led_setup()
    ch1 = ret[0]
    print(ret)
    perc = 0
    while True:
        try:
            for i in range(100):
                perc = perc + 1
                led_brightness(perc,ch1)  
                time.sleep(0.05)
            for i in range(100):
                perc = perc - 1
                led_brightness(perc,ch1)  
                time.sleep(0.05)
        except KeyboardInterrupt:
            break
        