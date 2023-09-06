# Script to download all your boards from pinterest.com
Gently download and organize all your pictures into folders

# How to use
Create a variable environment with the command
```
python -m venv venv
```
Activate variable environment
```
. venv/scripts/activate
```
And set up dependencies
```
pip install -r requirements.txt
```

Put your credentials in .env file: `EMAIL`, `PASSWORD` and `USERNAME`
and run `main.py`
```
python main.py
```
Ignore the error `No credentials stored [Errno 2] No such file or directory`

If the authorization data is correct, the 'images' folder will be created, which will contain subfolders with all your boards and images.

**enjoy**✌️

# Used libraries:
* [py3-pinterest](https://github.com/bstoilov/py3-pinterest)
* [progress](https://github.com/verigak/progress)