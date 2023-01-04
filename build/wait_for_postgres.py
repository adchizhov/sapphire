import socket
import time
import os


def wait_for_postgres():
    """
    Wait until successfully ping postgis host
    """
    port = int(os.environ["POSTGRES_PORT"])
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            s.connect((os.environ['POSTGRES_HOST'], port))
            s.close()
            break
        except socket.error as ex:
            time.sleep(0.1)


if __name__ == '__main__':
    wait_for_postgres()
