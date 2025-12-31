# Este archivo se utiliza para establecer una conexion SSH con un servidor remoto y ejecutar comandos en el mismo (infraestructura de red)

import paramiko
from config import SSH_HOST, SSH_USER, SSH_KEY_PATH, SSH_PORT #exporting from config.py the config variables
def connect():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    client.connect(
        hostname=SSH_HOST,
        username=SSH_USER,
        key_filename=SSH_KEY_PATH,
        port=SSH_PORT
    )
    return client # Retorna el cliente SSH conectado


def run_command(client, command):
    stdin, stdout, stderr = client.exec_command(command)
    exit_status = stdout.channel.recv_exit_status()

    if exit_status != 0:
        raise Exception(stderr.read().decode())

    return stdout.read().decode()