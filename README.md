# flask-tox

Use virtualenv:

```bash
pip install -r requirements.txt
```
Or with pipenv:
```bash
pipenv shell
pipenv install
pipenv install -d
```

Run TestCase: 
```bash
python3 manage.py tests
```
Or run app with:
```bash
python3 manage.py runserver -l <host> -p <port>
```
Default values
1. Host default - ```0.0.0.0```
2. Port default - ```8000```

You can run with TOX using:

```bash
tox
```

For view couvered after run TOX using:
```bash
<your_browser> htmlcov/index.html
```
