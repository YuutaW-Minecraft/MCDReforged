import os

def getenv(envname: str, reason: str = "") -> str:
    envval = os.getenv(envname)
    if envval == None:
        raise Exception(f"TelegramForward: You didn't specify the {envname} environment variable. Reason: {reason}")
    return envval
