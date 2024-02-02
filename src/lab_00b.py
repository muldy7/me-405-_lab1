'''!
@file lab_01.py
This file contains code which computes the answer to lab0 week 1. This code sets up a timer interrupt to generate a step reponse
from the physical circuit we created. This same code is used in the main.py file stored on the microcontroller for our lab0 week2 code. 

@author Abe Muldrow, Lucas Rambo, Peter Tomson
@date January 28th, 2024
'''

# imports
import micropython
import time
import cqueue

## interrupt value
# to set up the timer channel and frequency
interrupt = pyb.Timer(1,freq = 1000)
## stores value for the pinC0 output pin
pinC0 = pyb.Pin (pyb.Pin.board.PC0, pyb.Pin.OUT_PP, value = 0)  # initializes the pin as an outport pin
## store value for the pinB0 input pin
pinB0 = pyb.Pin (pyb.Pin.board.PB0, pyb.Pin.IN, value = 0) # initializes the input pin
## adcpin
# to store the pinB0 for the timer interrupt
adcpin = pyb.ADC(pinB0)
## Size of the queue for data storage
QUEUE_SIZE = 1000
## initializes the queue
int_queue = cqueue.IntQueue(QUEUE_SIZE)
## List for outputted values
output_array=[]  # array where the outputted values will go before printing
## variable for the step size
step = 0.001
## list of time values for the final data
time = list(range(QUEUE_SIZE)) # list of times to print alongside output_array


def main():
    """!
    This function initializes the program and runs the step reponse function
    """
    micropython.alloc_emergency_exception_buf(100) # alocates buffer for emergency exception handling, used when memory is a constraint
    
    interrupt.counter()	# gets the timer value
    step_response()
    

#def timer_int(tim_num):
def timer_int(tim_num):
    """!
    This function is for the timer interrupt. It runs interrupt on the previously set frequency store in the interrupt variable. 
    
    @param tim_num is the timer channel number set earlier by pyb.Timer. In this case tim_num = 1
    """
    # COLLECT ADC
    int_queue.put(adcpin.read())  #read and put into queue. inside the put() is the value that will be read from the pin. this has not been set up in the code yet
    int_queue.full()
    if int_queue.full() == True:
            interrupt.callback(None)          #If queue is full, disable Callback 
    else:
        pass
    pass 
      


def step_response():# run this function when requeste dby user or through GUI
    """!
    This function creates the step response and reads the queue to print the data.
    When the queue is full after reading the data from the input pin it adds the queue to our array list for data storage.
    The final array is then printed line by line so it can be read by our computer code. 
    """
    # Function code here
    
    interrupt.callback(timer_int)  			# configure and enable the calllback. example : timmy.callback(timer_cb)
    pinC0.high()                   			# set the trigger pin to high pin.high   (pinC0.value(1)
    while not int_queue.full():             # wait for a full queue ( while not my_que.full()
            pass							# pass
                                   
    pinC0.low()	 # Set pin back to low
    
    while int_queue.any():	# iterate through the queue to and add to the array output_array
        output=int_queue.get()
        output_array.append(output)
    output_array_f = [(3.3/4096)*x for x in output_array]
    pairs = list(zip(time, output_array_f))
    for line in pairs:
        print(line)
    

if __name__ == "__main__":
    main()