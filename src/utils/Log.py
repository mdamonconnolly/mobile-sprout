from colorama import init, Fore

def init_log():
    init(autoreset=True)

def log(message, level = "STANDARD"):
    
    if level == "STANDARD":
        print(message)
    elif level == "DEBUG":
        print(Fore.BLUE + message)
    elif level == "WARNING":
        pass #print in yellow
    elif level == "ERROR":
        pass #print in red
    elif level == "SUCCESS":
        pass #print in green
