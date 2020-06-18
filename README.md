# Flask App
Created flask application which will read content of given file.

Route created is as follow:

```http://127.0.0.1:5000/file/<filename>```
with optional query parameters as 'start' and 'end'

Filenames should be any of file1, file2, file3 or file4.

Note: I have hard coded path of file to read in app.py. Please change it according to your path.

## Clone the repo:
```
git clone https://github.com/rohitbs113/flask-test
cd flask-test
```

## Create virtualenv:
```python
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run the server:
python app.py

## The Endpoints:
```
http://127.0.0.1:5000/file/file3
http://127.0.0.1:5000/file/file3?start=1&end=10
```
