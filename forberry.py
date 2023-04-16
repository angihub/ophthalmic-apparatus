import utime
from machine import Pin

def sbros(a, b, c, d, e, f, g, h):
    a.low()
    b.low()
    c.low()
    d.low()
    e.low()
    f.low()
    g.low()
    h.low()
 
def start():
    start_time = utime.ticks_ms()
    return start_time


button = Pin(5, Pin.IN)

led1 = Pin(9, Pin.OUT)
led2 = Pin(8, Pin.OUT)
led3 = Pin(7, Pin.OUT)
led4 = Pin(6, Pin.OUT)
led5 = Pin(10, Pin.OUT)
led6 = Pin(11, Pin.OUT)
led7 = Pin(12, Pin.OUT)
led8 = Pin(13, Pin.OUT)


start_time = start()


i = 0
state_on = False
need_time = 0

sbros(led1, led2, led3, led4, led5, led6, led7, led8)

while 1:
    current_time = utime.ticks_ms()
    
    if (button.value() == 1):
        state_on = not state_on
        print("BTN: ", state_on)
        i = 0
        utime.sleep(0.500)
    
    if (state_on):
        if (current_time >= need_time and (current_time - start_time)<= 300000):
            if((current_time - start_time) > 300000):
                state_on = False
            elif (i == 0):
                led1.high()
                need_time = current_time + 1500
                i = 1
            elif (i == 1):
                led1.low()
                led2.high()
                need_time = current_time + 1000
                i = 2
            elif (i == 2):
                led2.low()
                led3.high()
                need_time = current_time + 1000
                i = 3
            elif (i == 3):
                led3.low()
                led4.high()
                need_time = current_time + 1000
                i = 4
            elif (i == 4):
                led4.low()
                led5.high()
                need_time = current_time + 1000
                i = 5
            elif (i == 5):
                led5.low()
                led6.high()
                need_time = current_time + 1000
                i = 6
            elif (i == 6):
                led6.low()
                led7.high()
                need_time = current_time + 1000
                i = 7
            elif (i == 7):
                led7.low()
                led8.high()
                need_time = current_time + 1500
                i = 8
            elif (i == 8):
                led8.low()
                led7.high()
                need_time = current_time + 1000
                i = 9
            elif (i == 9):
                led7.low()
                led6.high()
                need_time = current_time + 1000
                i = 10
            elif (i == 10):
                led6.low()
                led5.high()
                need_time = current_time + 1000
                i = 11
            elif (i == 11):
                led5.low()
                led4.high()
                need_time = current_time + 1000
                i = 12
            elif (i == 12):
                led4.low()
                led3.high()
                need_time = current_time + 1000
                i = 13
            elif (i == 13):
                led3.low()
                led2.high()
                need_time = current_time + 1000
                i = 14
            elif (i == 14):
                led2.low()
                i = 0
            print(current_time - start_time)
            
                
    else:
        sbros(led1, led2, led3, led4, led5, led6, led7, led8)
        start_time = start()
            
   
    
    #print(current_time - start_time)
    
    utime.sleep(0.01)

