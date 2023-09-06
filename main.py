from py3pin.Pinterest import Pinterest
from dotenv import load_dotenv
from ColoredLogger import configure_logging
from progress.bar import Bar
import logging
import os
import requests


def read_env() -> (tuple[str, str, str]) | None:
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')
    username = os.getenv('UNAME')

    if email is not None and password is not None and username is not None:
        return email, password, username
    else:
        return None


def get_pins_on_board(board_id: str, pinterest: Pinterest) -> []:
    board_pins = []
    pin_batch = pinterest.board_feed(board_id=board_id)
    while len(pin_batch) > 0:
        board_pins += pin_batch
        pin_batch = pinterest.board_feed(board_id=board_id)
    return board_pins


def download_image(url: str, path: str):
    req = requests.get(url=url, stream=True)
    if req.status_code == 200:
        with open(path, 'wb') as f:
            for chunk in req.iter_content(chunk_size=8192):
                f.write(chunk)
    else:
        print(f"image can't save")


def download_boards(boards: [], pinterest: Pinterest):
    for board in boards:
        board_id = board['id']
        board_name = board['name']

        pins_on_board = get_pins_on_board(board_id, pinterest)
        pins_length = len(pins_on_board)
        if pins_length > 0:
            board_path = os.path.join('images', board_name)
            if not os.path.exists(board_path):
                os.makedirs(board_path)
            with Bar(f'Processing {board_name}', max=pins_length) as bar:
                for pin in pins_on_board:
                    if 'images' in pin:
                        pin_id = pin['id']
                        img_url = pin['images']['orig']['url']
                        ind = str(img_url).rfind('.')
                        extension = str(img_url)[ind:]
                        file_path = f"images/{board_name}/{pin_id}{extension}"
                        if not os.path.exists(file_path):
                            download_image(img_url, file_path)
                    bar.next()
        else:
            logging.error('error loading images or the board is empty')


def main():
    configure_logging()

    logging.info('reading .env file...')
    load_dotenv()
    env = read_env()
    if env is not None:
        pinterest = Pinterest(
            email=os.getenv('EMAIL'),
            password=os.getenv('PASSWORD'),
            username=os.getenv('UNAME'))
        boards = pinterest.boards_all()
        boards_count = len(boards)
        if boards_count > 0:
            logging.info(f'{boards_count} boards found')
            download_boards(boards, pinterest)
            logging.info('all boards downloaded')
        else:
            logging.fatal('authorization error or you have no boards')
    else:
        logging.fatal('enter the authorization data in the .env file')


if __name__ == "__main__":
    main()
