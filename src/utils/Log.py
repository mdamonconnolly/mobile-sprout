from colorama import init, Fore

def init_log():
    init(autoreset=True)

def log(message, level = "STANDARD"):
    
    if level == "STANDARD":
        print(message)
    elif level == "DEBUG":
        print(Fore.BLUE + message)
    elif level == "WARNING":
        print(Fore.YELLOW + message) 
    elif level == "ERROR":
        print(Fore.RED + message)
    elif level == "SUCCESS":
        print(Fore.GREEN + message)
