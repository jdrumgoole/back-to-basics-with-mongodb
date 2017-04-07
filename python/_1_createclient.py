'''
Created on 3 Jan 2017

Before running this program download mongodb from

https://www.mongodb.com/download-center#community

run the mongod deemon to start a database server.
This will start a server on port 27017.
This client connects to that port by default.

See also

http://api.mongodb.com/python/current/api/pymongo/mongo_client.html

@author: jdrumgoole
'''

import pprint
import pymongo


if __name__ == '__main__':

    client = pymongo.MongoClient()

    database = client["test"]

    response = database.command("ismaster")

    pprint.pprint(response)

'''
Example Output

JD10Gen:python jdrumgoole$ python createclient.py 
{u'ismaster': True,
 u'localTime': datetime.datetime(2017, 1, 3, 16, 54, 26, 650000),
 u'maxBsonObjectSize': 16777216,
 u'maxMessageSizeBytes': 48000000,
 u'maxWireVersion': 4,
 u'maxWriteBatchSize': 1000,
 u'minWireVersion': 0,
 u'ok': 1.0}
JD10Gen:python jdrumgoole$ 

What you will see if there is no server running (after a delay because the 
connection has to timeout)

JD10Gen:python jdrumgoole$ python createclient.py 
Traceback (most recent call last):
  File "createclient.py", line 23, in <module>
    response = database.command( "ismaster" )
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/pymongo/database.py", line 478, in command
    with client._socket_for_reads(read_preference) as (sock_info, slave_ok):
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/contextlib.py", line 17, in __enter__
    return self.gen.next()
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/pymongo/mongo_client.py", line 752, in _socket_for_reads
    with self._get_socket(read_preference) as sock_info:
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/contextlib.py", line 17, in __enter__
    return self.gen.next()
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/pymongo/mongo_client.py", line 716, in _get_socket
    server = self._get_topology().select_server(selector)
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/pymongo/topology.py", line 142, in select_server
    address))
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/pymongo/topology.py", line 118, in select_servers
    self._error_message(selector))
pymongo.errors.ServerSelectionTimeoutError: localhost:27017: [Errno 61] Connection refused
JD10Gen:python jdrumgoole$

'''
