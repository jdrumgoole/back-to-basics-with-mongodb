'''
Created on 3 Jan 2017

@author: jdrumgoole
This is using an explicit MongoDB URI.
which follows the standard URI form of:

scheme:[//[user:password@]host[:port]][/]path[?query][#fragment]

The documentation for the format of a MongoDB URI is at:

https://docs.mongodb.com/manual/reference/connection-string/

The program is functionally equivalent to the previous (v1) createclient
program

'''
import pymongo
import pprint

if __name__ == '__main__':
    
    client = pymongo.MongoClient( host="mongodb://localhost:27017" )
    
    database = client["test"]
    
    # 'ismaster' is the official commnand to ping the server. Until 
    # ismaster is called the client has had not contact with the server
    # the database will not be created on the server until this command executes.
    #
    # A database is a container for a set of collections. Each database is guaranteed to
    # be stored in an independent collection of on disk files
    #
    response = database.command("ismaster")
    
    pprint.pprint(response)