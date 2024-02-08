#Motor
import micropython
import time
import pyb
# have to import pyb for it work on the board

class MotorDriver:
    """! 
    This class implements a motor driver for an ME405 kit. 
    """
    def __init__ (self, en_pin, in1pin, in2pin, timer):
        """! 
        Creates a motor driver by initializing GPIO
        pins and turning off the motor for safety. 
        @param en_pin (There will be several parameters)
        """
        en_pin = getattr(pyb.Pin.board, en_pin)
        in1pin = getattr(pyb.Pin.board, in1pin)
        in2pin = getattr(pyb.Pin.board, in2pin)
 
        self.ENx = pyb.Pin (en_pin, pyb.Pin.OUT_PP, value = 0)
        self.IN1x = pyb.Pin (in1pin, pyb.Pin.OUT_PP, value = 0)
        self.IN2x = pyb.Pin (in2pin, pyb.Pin.OUT_PP, value = 0)
        self.t = pyb.Timer(timer, freq=1000)
        self.tch1 = self.t.channel(1,pyb.Timer.PWM, pin=self.IN1x)
        self.tch2 = self.t.channel(2,pyb.Timer.PWM, pin=self.IN2x)
        self.ENx.high()
        print ("Creating a motor driver")

    def set_duty_cycle (self, level):
        """!
        This method sets the duty cycle to be sent
        to the motor to the given level. Positive values
        cause torque in one direction, negative values
        in the opposite direction.
        @param level A signed integer holding the duty
               cycle of the voltage sent to the motor 
        """
        
#         self.tch1.pulse_width_percent(0)
#         self.tch2.pulse_width_percent(100)
#         self.IN2x.high()
        if level >= 0:
            self.tch1.pulse_width_percent(0)
            self.tch2.pulse_width_percent(level)
        else:
            self.tch2.pulse_width_percent(0)
            self.tch1.pulse_width_percent(-1*level)
                
        print (f"Setting duty cycle to {level}")

# def motor_setup():
# #     pinPA0 = pyb.Pin (pyb.Pin.board.PA0, pyb.Pin.OUT_PP, value = 0)  # initializes the pin as an outport pin
# #     pinPA1 = pyb.Pin (pyb.Pin.board.PA1, pyb.Pin.OUT_PP, value = 0)
# #     tim5 = pyb.Timer (5, freq=1000)	# sets up the correct timer
# #     t5ch1 = tim5.channel (1, pyb.Timer.PWM, pin=pinPA0)
# #     t5ch2 = tim5.channel (2, pyb.Timer.PWM, pin=pinPA1)	# set up correct channel for timer
# # #     ch1.pulse_width_percent (100)
# #     pinPC1 = pyb.Pin (pyb.Pin.board.PC1, pyb.Pin.OUT_PP, value = 0)
# #     return(t5ch2,pinPA0,pinPA1,pinPC1,tim5)
        

if __name__ == "__main__":

    motor1 = MotorDriver ('PA10', 'PB4', 'PB5', 3)
    #motor1 = MotorDriver (pyb.Pin(pyb.Pin.board.PA10, pyb.Pin.OUT_PP, value = 0), PB4, PB5, 3)
    #motor2 = MotorDriver (PC1, PA0, PA1, 5)
    perc = -100
    
    while True:
        try:
            for i in range(200):
                    perc = perc + 1
                    motor1.set_duty_cycle(perc) 
                    time.sleep(0.05)
            for i in range(200):
                    perc = perc - 1
                    motor1.set_duty_cycle(perc)  
                    time.sleep(0.05)
        except KeyboardInterrupt:
            motor1.set_duty_cycle(0)
            break
        
#    motor1.set_duty_cycle(50)
#    time.sleep(5)
#    motor1.set_duty_cycle(-50)
#    time.sleep(5)
#     motor1.in1pin.low()
#     motor1.in2pin.high()
#     time.sleep(5)
#     while True:
#        #speed = int(input("Motor Speed: "))
# #        motor1.set_duty_cycle(speed)
# #        time.sleep(5)
#         motor1.in1pin.low()
#         time.sleep(2)
#         motor1.in2pin.high()
#         time.sleep(2)
#         print('running')
    
   

    
    
   
   
   
   
   
  
#     while True:
#         try:
#             pass
#         except KeyboardInterrupt:
#             ch.pulse_width_percent (0)
#             break
#     motor_speed(75,ch5)
#     ch5.pulse_width_percent (50)
#     time.sleep(4)
#     ch5.pulse_width_percent (50)
#         for i in range(100):
#     while True:
#         motor_speed(50,ch5)
#     except KeyboardInterrupt:
#             ch5.pulse_width_percent (0)