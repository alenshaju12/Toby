import os
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

def main():   
    s=0.2
    # Write the PID to a file
    with open("forward_pid.txt", "w") as f:
        f.write(str(os.getpid()))
    
    while True:
        time.sleep(s)
        set_servo_angle(0, 34)
        set_servo_angle(4, 68)
        time.sleep(s)
        set_servo_angle1(1, 42)
        set_servo_angle1(5, 84)
        time.sleep(s)
        set_servo_angle(0, 45)
        set_servo_angle(4, 70)
        time.sleep(s)
        set_servo_angle(0, 52)
        set_servo_angle(4, 82)
        time.sleep(s)
        set_servo_angle1(1, 34)
        set_servo_angle1(5, 68)
        time.sleep(s)
        set_servo_angle(0, 42)
        set_servo_angle(4, 84)
        time.sleep(s)
        set_servo_angle1(1, 45)
        set_servo_angle1(5, 70)
        time.sleep(s)
        set_servo_angle1(1, 52)
        set_servo_angle1(5, 82)

if __name__ == "__main__":
    main()
