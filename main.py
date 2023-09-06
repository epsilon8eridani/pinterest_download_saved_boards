from dotenv import load_dotenv
from ColoredLogger import configure_logging
import logging
import os

def read_env() -> (tuple[bool, str, str, str]) :
    email=os.getenv('EMAIL')
    password=os.getenv('PASSWORD')
    username=os.getenv('UNAME')

    if email != None and password != None and username != None:
        return (True, email, password, username)
    else:
        return (False)


def main():
    configure_logging()
    logging.info('reading .env file...')
    load_dotenv()
    env = read_env()
    if env != (False):
        logging.info('data read out!')
    else:
        logging.fatal('enter the authorization data in the .env file')

if __name__ == "__main__":
    main()
