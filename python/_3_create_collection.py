'''
Created on 13 Jan 2017

@author: jdrumgoole
'''

import pymongo
import pprint
from datetime import datetime

if __name__ == '__main__':
    
    client = pymongo.MongoClient( host="mongodb://localhost:27017" )
    
    #
    # Create a database called test_database
    #
    print( 
'''
Make A Database
===============
database = client.get_database( "test_database" )
will create a database if it doesn't exist otherwise it will provide a
connection to an existing database called "test_database"
'''      )
    
    database = client.get_database( "test_database" )
    pprint.pprint( database )
    
    #
    # Allow us to run this program multiple times (don't do this in production :-))
    database.drop_collection( "new_collection")
    database.drop_collection( "new_collecton_2")
    
    print( '''
Make A Collection
==================
collection = database.create_collection( "new_collection" )
    
Each database can store many collections.
Collections are analogous to tables in the relational world.
However a collection stores JSON docs so each "row" of a collection
is a JSON document which may be hierarchical in nature.
    ''' )
    collection = database.create_collection( "new_collection" )
    pprint.pprint( collection )  
    
    print( '''
Single Insertion:
=================
collection.insert_one( { "Hello" :"World"})  
doc = collection.find_one( {"Hello" :"World"})
pprint.pprint( doc )

We insert a single simple JSON document (what else but  "Hello World"?)

We then look for that document using the same field as we inserted.

When we print our the object we will see that another field
has been added, the "_id" field. This field is added by the client
and is unique for every document in the collection.

''' 
    )
    collection.insert_one( { "Hello" :"World"})
    doc = collection.find_one( {"Hello" :"World"})    
    pprint.pprint( doc )
    
    print( '''
Second Insertion:
==================

collection.insert_one( {"Hello" : "World" })
cursor = collection.find( {"Hello" : "World"})
for doc in cursor:
    pprint.pprint( doc )

Look what happens if we insert the same document again. We get
another document inserted but it has a different _id field.
This allows us to distinguish duplicates.
Lets print out both documents using find(). find_one only returns the 
first document that matches a query find() returns a cursor that we
can iterate over to find all documents that match the query.
The cursor returned complies with the python iterator protocol.
    ''')
    

    collection.insert_one( {"Hello" : "World" })
    cursor = collection.find( {"Hello" : "World"})
    for doc in cursor:
        pprint.pprint( doc )
        
    print( '''
Inserting an Integer Type
=========================

collection.insert_one( { "year of birth" : 1975 })
doc = collection.find_one( { "year of birth" : 1975 })
pprint.pprint( doc )
print( type( doc[ "year of birth"]))

The mongodb python driver understands how to convert python dicts
to JSON so we can used all the power of python. Here we insert an integer.
Note how pprint correctly prints out an integer (there are no quotes).
        ''' )
    collection.insert_one( { "year of birth" : 1975 })
    doc = collection.find_one( { "year of birth" : 1975 })
    pprint.pprint( doc )
    print( "type of field 'year of birth' is: %s" % type( doc[ "year of birth"]))
    
    print( '''
Inserting a Floating point type
================================
collection.insert_one( { "weight" : 70.76 })
doc = collection.find_one( { "weight" : 70.76 })
pprint.pprint( doc )
print( "type of field 'weight' is: %s" %type( doc[ 'weight']))

Here we insert a floating point type.
    ''')
    collection.insert_one( { "weight" : 70.76 })
    doc = collection.find_one( { "weight" : 70.76 })
    pprint.pprint( doc )
    print( "type of field 'weight' is: %s" %type( doc[ 'weight']))
    
    print( '''
Inserting a datetime  object
==============================
now = datetime.utcnow()
collection.insert_one( { "timestamp" : now })
doc = collection.find_one( { "timestamp" : now })
pprint.pprint( doc )
print( "type of field 'timestamp' is: %s" %type( doc[ 'timestamp']))

The driver knows about datetime objects as well. 
    ''')
    
    now = datetime.utcnow()
    collection.insert_one( { "timestamp" : now })
    doc = collection.find_one( { "timestamp" : now })
    pprint.pprint( doc )
    print( "type of field 'timestamp' is: %s" %type( doc[ 'timestamp']))
    
    print( '''
Inserting a list
===================
a = [ 1, 2, 3, 4, 5 ]
collection.insert_one( { "values" : a })
doc = collection.find_one( { "values" : a })
pprint.pprint( doc )
print( "type of field 'values' is: %s" %type( doc[ 'values']))

The driver understands nested types. So we can insert a list type
as a value a document.
    ''')
    a = [ 1, 2, 3, 4, 5 ]
    collection.insert_one( { "values" : a })
    doc = collection.find_one( { "values" : a })
    pprint.pprint( doc )
    print( "type of field 'values' is: %s" %type( doc[ 'values']))
    
    print( '''
Inserting a sub-document (a dict inside a dict)
===============================================

d = { "nested" : "value" }
collection.insert_one( { "topvalue" : d })
doc = collection.find_one( { "topvalue" : d })
pprint.pprint( doc )
print( "type of field 'topvalue' is: %s" %type( doc[ 'topvalue']))

We can inserted nested documents so we can model hierarchy very easily.
    ''' )
    
    d = { "nested" : "value" }
    collection.insert_one( { "topvalue" : d })
    doc = collection.find_one( { "topvalue" : d })
    pprint.pprint( doc )
    print( "type of field 'topvalue' is: %s" %type( doc[ 'topvalue']))
    
    print( '''
Lets see all the content
========================
Now note how all these different structures were written to the same collection
    ''')

    for i in collection.find() :
        pprint.pprint( i )