from configparser import ConfigParser
# config = ConfigParser()

# # load configuration file
# config.read("config.ini")

# # access the key "debug" in "DEFAULT" section
# config.get("DEFAULT", "debug")
# # Return "True"

# # Access the key "path" in "FILES" destion
# config.get("FILES", 'path')
# # Return "/path/to/file"


'''Creating configuration file programatically'''
# config = ConfigParser()
# config['settings'] = {'resolution':'320x240', 'color':'blue'}
# with open('example.ini', 'w') as configfile:
# 	config.write(configfile)

# with open('example.ini', 'r') as file:
# 	x = file.read()
# 	print(x)

# you can change any field by
# settings = config['settings']
# settings['color'] = red


config = ConfigParser()
config['settings'] = {}
config['Network connection'] = {"Wifi":'-', "Sim card": "-", "Hotspot": "-", "VPN": "-", "Private DNS": "-"}
config['Device connection'] = {}
config['Display'] = {}
config['Sound'] = {}
config['Apps & notifications'] = {}
config['Security & location'] = {}
config['Storage'] = {}

# secret = config['Network connection']
# secret['Wifi'] = {}
# secret['SIM cards and mobile network'] = {}
# secret['Hotspot & tethering'] = {}
# secret['VPN'] = {}
# secret['Private DNS'] = {}


with open('phone.ini', 'w') as configfile:
	config.write(configfile)


with open('phone.ini', 'r') as file:
	reader = file.read()
	print(reader)



