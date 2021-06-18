"""
[DEFAULT]
debug = false

[web_server]
host = 127.0.0.1
port = 80
"""


import configparser

config = configparser.ConfigParser()
# config['DEFAULT'] = {
#     'debug' :  True
# }
# config['web_server'] = {
#     'host': '127.0.0.1',
#     'port': 80
# }
#
# with open('config.ini','w') as configFile:
#     config.write(configFile)
config.read('config.ini')
print(config['web_server'])
print(config['web_server']['host'])
