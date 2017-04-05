'''
Created on 5 Apr 2017

@author: jdrumgoole
'''
import requests
import pymongo
import json

if __name__ == '__main__':
    print( '''
For this next set of examples we are going to use a public data set.
Lets download the zips.json file. A collection of ZIP codes for the US
in json format.

This data is hosted on github at :

https://github.com/jdrumgoole/back-to-basics-with-mongodb/tree/master/data
    ''')
    
    print( "Downloading zips")
    r = requests.get( "https://raw.githubusercontent.com/jdrumgoole/back-to-basics-with-mongodb/master/data/zips.json", stream=True)
    with open("zips.json", 'wb') as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chunk)
    print( "Created zips.json")
    
    print( "Importing zips.json in mongodb")
    client = pymongo.MongoClient()
    b2b_database = client[ "b2b" ]
    zips_collection = b2b_database[ "zips"]
    
    b2b_database.drop_collection( "zips" )
    
    count = 0
    with open( "zips.json", "r") as fd:
        for line in fd :
            line = line[:-1] #clip \n
            print( line )
            doc = json.loads( line ) #convert to a dict object
            zips_collection.insert_one( doc )
            count = count + 1 
            
    print( "Inserted %i documents" % count )
            
            
            