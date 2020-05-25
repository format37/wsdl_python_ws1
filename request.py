from requests.auth import HTTPBasicAuth  # or HTTPDigestAuth, or OAuth1, etc.
from requests import Session
from zeep import Client
from zeep.transports import Transport

session = Session()
with open('auth.login','r') as file:
	login=file.read().replace('\n', '')
	file.close()
with open('auth.pass','r') as file:
	password=file.read().replace('\n', '')
	file.close()

print(login,password)
session.auth = HTTPBasicAuth(login, password)
client = Client('http://10.2.4.141/test1c5/ws/ws1.1cws?wsdl',transport=Transport(session=session))

def createRequest():
	
	print('call createRequest')
	
	clientName		= "name"
	phonePrimary		= "123"
	phoneSecondary		= "456"
	masterCallDate		= '2020-05-21-16:02'
	taskDescription	= 'do something'
	deviceType		= 'tv'
	service		= 'repair'

	address		= {
		'guid':'0',
		'city':'a',
		'street':'b',
		'dom':'1',
		'str':'2',
		'kor':'3',
		'pod':'4',
		'floor':'5',
		'apartment':'6',
		}

	request = client.service.createRequest(
		clientName,
		phonePrimary,
		phoneSecondary,
		masterCallDate,
		taskDescription,
		address,
		deviceType,
		service,
		)
		
	code		= request.result.code
	message		= request.result.message
	
	print('code',code)
	print('message',message)

def serviceList():
	
	print('call serviceList')
	
	request = client.service.serviceList()
	
	code		= request.result.code
	message		= request.result.message
	services	= request.services
	
	print('code',code)
	print('message',message)
	print('services (',len(services),'):')
	for service in services:
		print(service)
	
#createRequest()
serviceList()