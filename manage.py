import os
import argparse
from app import create_app
from unittest import TestLoader, runner


parser = argparse.ArgumentParser(prog='Managee', description='Managed Flask')

parser.add_argument('mode', type=str, help='Exec mode (runserver|tests)')
parser.add_argument('-p', '--port', action='store', default='8000')
parser.add_argument('-l', '--host', action='store', default='0.0.0.0')

args = parser.parse_args()

def runserver():
    port = int(args.port)
    host = str(args.host)
    app = create_app()
    app.run(host=host, port=port)

def tests():
    loader = TestLoader()
    tests = loader.discover('tests/')
    testRunner = runner.TextTestRunner()
    testRunner.run(tests) 

modes = {
    'runserver': runserver,
    'tests': tests
}[args.mode]()
        