import os
import signal
import time

def stop_forward():
    # Read the PID from the file
    with open("forward_pid.txt", "r") as f:
        pid = int(f.read())
    
    # Terminate the process using its PID
    os.kill(pid, signal.SIGTERM)

# Stop the forward.py process
stop_forward()
