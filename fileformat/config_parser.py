import configparser

cfgParser = configparser.ConfigParser()
cfgParser.read('config.ini')
saInterval = cfgParser['DEFAULT']['ServerAliveInterval']
print(saInterval)

print(cfgParser.getint('DEFAULT', 'CompressionLevel'))
print(cfgParser.get('bitbucket.org', 'User'))