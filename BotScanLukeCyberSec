import subprocess

def display_ascii_name():
    ascii_art = '''
  ______   ____   __    __       _______. __    __       ___       __       ___      .__   __.  _______ 
 /      |  \   \ /  \  /  \     /       ||  |  |  |     /   \     |  |     /   \     |  \ |  | |   ____|
|  ,----'   \   Y   \/    \   |   (----`|  |__|  |    /  ^  \    |  |    /  ^  \    |   \|  | |  |__   
|  |         \     /  / \  \   \   \    |   __   |   /  /_\  \   |  |   /  /_\  \   |  . `  | |   __|  
|  `----.     |   /  ____  \ .----)   |  |  |  |  |  /  _____  \  |  |  /  _____  \  |  |\   | |  |____ 
 \______|     |___/__/    \__\|_______/|__|  |__| /__/     \__\ |__| /__/     \__\ |__| \__| |_______|
                                                                                                       
    '''
    print(ascii_art)

def execute_command_in_separate_terminal(command):
    subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', command])

def perform_scanning(target):
    print("[*] Performing vulnerability scanning on the target:", target)
    execute_command_in_separate_terminal(f"nmap {target}")
    execute_command_in_separate_terminal(f"seeker -t {target}")
    execute_command_in_separate_terminal(f"whois {target}")
    execute_command_in_separate_terminal(f"foremost -i {target}")
    execute_command_in_separate_terminal(f"hidra -s {target}")

def main():
    display_ascii_name()
    target = input("Enter the target for vulnerability scanning: ")
    perform_scanning(target)

if __name__ == "__main__":
    main()
