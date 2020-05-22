from requests.auth import HTTPBasicAuth  # or HTTPDigestAuth, or OAuth1, etc.
from requests import Session
from zeep import Client
from zeep.transports import Transport

session = Session()
session.auth = HTTPBasicAuth("LOGIN", "PASS")
client = Client('http://10.2.4.141/test1c5/ws/ws1.1cws?wsdl',
            transport=Transport(session=session))

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

answer = client.service.createRequest(
	clientName,
	phonePrimary,
	phoneSecondary,
	masterCallDate,
	taskDescription,
	address,
	deviceType,
	service,
	)
print(answer)
