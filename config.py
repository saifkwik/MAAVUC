import sys

# Enter your API Key below:
api_key = '<Enter API Key here: '
if f'<' in api_key:
    print('INVALID API Key - Insert your Key in config.py file')
    sys.exit()
