from ssh_client import connect, run_command

def main():
    client = connect()

    try:
        output = run_command(client, "uptime")
        print(output)
    except Exception as e:
        print(f"Error en la pipeline: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    main()
