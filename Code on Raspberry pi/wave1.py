import time
from adafruit_pca9685 import PCA9685
import board

# Initialize the PCA9685 controller
i2c_bus = board.I2C()
pca = PCA9685(i2c_bus)
pca.frequency = 50  # Set PWM frequency to 50 Hz

# Define min and max pulse lengths for SG90 servo (in microseconds)
SERVO_MIN = 500
SERVO_MAX = 2400


def s(channel, angle):
    if(channel%2!=0):
        pulse = SERVO_MIN + (angle / 180) * (SERVO_MAX - SERVO_MIN)
    else:
        pulse = SERVO_MIN + ((180-angle) / 180) * (SERVO_MAX - SERVO_MIN)

    pca.channels[(channel-1)].duty_cycle = int(pulse * 65536 / 20000)

def ud(i,j,s,a):
    j=j+(2*a);
    i=i+(4*a);
    a=a*10;
    while(i<=84 and i>=20):
        set_servo_angle(4, i)
        set_servo_angle1(5, i)
        i=i+a;
        while(j<=42 and j>=20):
            
            set_servo_angle(0, j)
            set_servo_angle1(1, j)
            j=j+a;
        time.sleep(s);

# Function to set servo angle
def set_servo_angle(channel, angle):
    pulse1 = SERVO_MIN + (angle / 180) * (SERVO_MAX - SERVO_MIN)
    pulse2 = SERVO_MIN + ((180-angle) / 180) * (SERVO_MAX - SERVO_MIN)
    pca.channels[channel].duty_cycle = int(pulse1 * 65536 / 20000)  # Convert pulse width to PCA9685 duty cycle
    pca.channels[channel+3].duty_cycle = int(pulse2 * 65536 / 20000)

def set_servo_angle1(channel, angle):
    pulse1 = SERVO_MIN + (angle / 180) * (SERVO_MAX - SERVO_MIN)
    pulse2 = SERVO_MIN + ((180-angle) / 180) * (SERVO_MAX - SERVO_MIN)
    pca.channels[channel].duty_cycle = int(pulse2 * 65536 / 20000)  # Convert pulse width to PCA9685 duty cycle
    pca.channels[channel+1].duty_cycle = int(pulse1 * 65536 / 20000)

def sit():
    ud(84,42,0.2,1)
    s(3,20)
    s(4,20)
    s(7,40)
    s(8,40)

def wave():
    sit()
    i=0
    while (i<=3):
        s(2,180)
        time.sleep(0.2)
        s(2,135)
        time.sleep(0.2)
        i=i+1
    s(2,42)

def main():
    s=0.2;
    wave()


if __name__ == "__main__":
    main()