from ssh_client import run_command

def check_user(client): #Recibe el client SSH
    return run_command(client, "whoami")

def check_uptime(client): #Ejecuta el comando uptime
    return run_command(client, "uptime")

def check_disk(client): # Ejectua el comando df -h /
    return run_command(client, "df -h /")
