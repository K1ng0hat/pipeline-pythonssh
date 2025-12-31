from ssh_client import connect
from tasks.healthcheck import check_user, check_uptime, check_disk

def main():
    client = connect()

    try:
        print("=== HEALTHCHECK ===")

        print("User:", check_user(client).strip())
        print("Uptime:", check_uptime(client).strip())
        print("Disk:")
        print(check_disk(client))

        print("Healthcheck finalizado correctamente")

    except Exception as e:
        print(f"Pipeline falló: {e}")

    finally:
        client.close()

if __name__ == "__main__":
    main()
