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
    
    client = pymongo.MongoClient(host="mongodb://localhost:27017")
    
    database = client["test"]
    
    response = database.command("ismaster")
    
    pprint.pprint(response)