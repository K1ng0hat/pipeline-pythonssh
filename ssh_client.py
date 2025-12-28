import paramiko

def connect():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    client.connect(
        hostname="IP_DEL_SERVIDOR",
        username="USUARIO",
        key_filename="C:/ruta/a/tu/llave.pem"
    )

    return client


def run_command(client, command):
    stdin, stdout, stderr = client.exec_command(command)
    exit_status = stdout.channel.recv_exit_status()

    if exit_status != 0:
        raise Exception(stderr.read().decode())

    return stdout.read().decode()