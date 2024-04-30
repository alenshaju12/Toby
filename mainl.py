import paramiko

# Function to run remote script on Raspberry Pi
def run_remote_script(ip, username, password, script_path):
    # Connect to the Raspberry Pi over SSH
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username=username, password=password)

    # Execute the Python script
    command = f'python {script_path}'
    stdin, stdout, stderr = ssh.exec_command(command)

    # Close the SSH connection
    ssh.close()

# Main function
def main():
    t = 1
    pi_ip = 'raspberrypi'
    pi_username = 'pi'
    pi_password = 'pi'
    while t == 1:
        text = input()
        if text:
            print("You said:", text)
            # Remove spaces from the text
            text = text.replace(' ', '')
            print("Processed text:", text)
            # Check for specific commands
            if text == "exit":
                t = 2
            if text in ['walk', 'sit', 'sitdown', 'standup', 'wave', 'stop']:
                # Path to the Python script on Raspberry Pi
                script_path = f'/home/pi/Desktop/{text}.py'
                # Run the remote script
                run_remote_script(pi_ip, pi_username, pi_password, script_path)

# Run the main function
if __name__ == "__main__":
    main()

