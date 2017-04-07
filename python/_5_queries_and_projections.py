'''
Created on 5 Apr 2017

See 

https://docs.mongodb.com/manual/reference/operator/query/

https://docs.mongodb.com/manual/reference/operator/query-comparison/


@author: jdrumgoole
'''
import pymongo
if __name__ == '__main__':
    
    client = pymongo.MongoClient()
    database = client[ "b2b" ]
    zips_collection = database[ "zips" ]
    
    print( 
    '''
A simple query for the first document in a collection
    first = zips_collection.find_one()
''')
    
    first = zips_collection.find_one()
    print( first )
    
    print( 
    '''
Now query that returns a cursor. We must iterate the cursor 
to return the documents. Note that the find does not send the query
to the server until we begin to read the documents. So the first round 
trip to the server happens on the first line of the for loop.

    count = 0 
    cursor = zips_collection.find()
    for i in cursor: #server gets query
        count = count + 1 
        print( i )
''')
    count = 0 
    cursor = zips_collection.find()
    for i in cursor:
        count = count + 1 
        print( i )
    print( "%i documents" % count )
    
    print(
'''
Now we want find a specific field by value. Lets find what city is at
zip code "01036".

    doc =  zips_collection.find_one( { "_id" : "01036" })
''' 
        )
    
    doc =  zips_collection.find_one( { "_id" : "01036" })
    print( doc )
    
    print(
'''
What happens if the result set will be more than one document?

    cursor = zips_collection.find( { "pop" : 426 })
    count = 0
    for i in cursor:
        count = count + 1 
        print( i )
        
If you call find_one the first document returned by the collection
query will be produced. If you call find() then a cursor will be returned 
that you can use to iterate over the complete result set.
'''
    )
    
    print( "Find one")
    doc = zips_collection.find_one( { "pop" : 426 })
    print( doc )
    
    print( "" )
    
    print( "Find many")
    cursor = zips_collection.find( { "pop" : 426 })
    count = 0
    for i in cursor:
        count = count + 1 
        print( i )
    print( "%i documents" % count )
    
    print(
'''
We can control the output with projections. Project tells the server to only 
return a subset of the fields in a document.
'''
    )
    
    print( "Suppress the _id field")
    cursor = zips_collection.find( { "pop" : 426 }, { "_id" : 0 })
    count = 0
    for i in cursor:
        count = count + 1 
        print( i )
    print( "%i documents" % count )
    
    print( "Suppress the _id and loc fields")
    cursor = zips_collection.find( { "pop" : 426 }, { "_id" : 0, "loc" : 0 })
    count = 0
    for i in cursor:
        count = count + 1 
        print( i )
    print( "%i documents" % count )
    
    print(
'''
Explicitly include a field. Note once you have a field with a value of '1'
then all other fields are excluded except other fields with a value of '1'.
Note in this scenario the _id field will always be included unless it is
explicitly excluded by setting it to _id : 0.
''' )

    print( "Just include the loc field")
    cursor = zips_collection.find( { "pop" : 426 }, {  "loc" : 1 })
    count = 0
    for i in cursor:
        count = count + 1 
        print( i )
    print( "%i documents" % count )
    
    print( "Just include the loc field and supress the _id field" )
    cursor = zips_collection.find( { "pop" : 426 }, {  "_id" : 0, "loc" : 1 })
    count = 0
    for i in cursor:
        count = count + 1 
        print( i )
    print( "%i documents" % count )