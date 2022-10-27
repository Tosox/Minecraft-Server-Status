import os
import subprocess
import sys
import socket

#
# Constants
#

command_template = 'Test-NetConnection -computername {} -port {}'

#
# Helper classes
#

class bcolors:
    """
    Helpers class to print colored text
    """
    
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
#
# Helper methods
#

def cmd_run(cmd: str) -> subprocess.CompletedProcess[bytes]:
    """
    Execute a powershell command

    Args:
        cmd (str): Command to run

    Returns:
        subprocess.CompletedProcess[bytes]: Command output
    """
    
    return subprocess.run(args = ['powershell', '-command', cmd], capture_output = True, timeout = 25)

def list_to_dict(input_list: list) -> dict[str, str]:
    """
    Convert a list into a dictionary

    Args:
        input_list (list): List to convert

    Returns:
        dict[str, str]: The converted list
    """
    
    dictionary = {}
    for i in range(len(input_list) - 1)[::2]:
        dictionary.update({ input_list[i]: input_list[i + 1] })
    return dictionary

def answer_to_dict(answer: str) -> dict[str, str]:
    """
    Clean up the answer and convert it into a dictionary

    Args:
        answer (str): Answer to convert

    Returns:
        dict[str, str]: Converted answer
    """
    
    # Clean up the answer
    formatted_answer = answer.replace(r'\n', '').replace(' ', '').replace('b\'', '').split(r'\r')
    formatted_answer = [elem for elem in formatted_answer if len(elem) > 1]
    formatted_answer = [elem.split(':') for elem in formatted_answer]
    formatted_answer = [elem for elems in formatted_answer for elem in elems]
    
    return list_to_dict(formatted_answer)

#
# Main methods
#

def print_status(ping_answer: str) -> None:
    """
    Print the server status

    Args:
        ping_answer (str): Command output
    """
    
    # Format the ping answer
    answer = answer_to_dict(ping_answer)
    
    # Check if the server is running
    did_tcp_succeed = answer.get('TcpTestSucceeded')
    if (did_tcp_succeed) and (did_tcp_succeed.lower() == 'true'):
        print(f'{bcolors.OKCYAN}The server is up and running{bcolors.ENDC}')
    else:
        print(f'{bcolors.WARNING}The server is offline or doesn\'t exist{bcolors.ENDC}')

def main(argv: list[str]) -> None:
    """
    Entry point

    Args:
        argv (list[str]): Program arguments
    """
    
    # Check if the syntax is valid
    argc = len(argv)
    if (argc != 3) and (argc != 5):
        print(f'{bcolors.FAIL}Error: please use the correct syntax: python {os.path.basename(argv[0])} -ip <address> [OPTIONAL: --port <port>]{bcolors.ENDC}')
        return
    
    # Check if the user is connected to the internet
    my_ip = socket.gethostbyname(socket.gethostname())
    if my_ip == '127.0.0.1':
        print(f'{bcolors.FAIL}Error: check your internet connection and try again{bcolors.ENDC}')
        return
    
    # Get the input address
    address_idx = argv.index('-ip') + 1
    address = argv[address_idx]
    
    # Get the optional input port
    try:
        port_idx = argv.index('--port') + 1
        port = argv[port_idx]
    except ValueError:
        port = 25565
    
    # Prepare the command
    command = command_template.format(address, port)
    
    # Run the command and check if it was successful
    try:
        ping = cmd_run(command)
    except subprocess.TimeoutExpired:
        print(f'{bcolors.WARNING}The connection timed out{bcolors.ENDC}')
        return
    if ping.returncode != 0:
        print(f'{bcolors.FAIL}Error: couldn\'t ping the server. Return code:{bcolors.ENDC}{bcolors.WARNING}{ping.returncode}{bcolors.ENDC}')
        return
    
    # Print the server status
    print_status(str(ping.stdout))

if __name__ == '__main__':
    main(sys.argv)
