'''
Created on 5 Apr 2017

@author: jdrumgoole
'''

import pymongo

if __name__ == '__main__':
    
    client = pymongo.MongoClient()
    database = client[ "b2b" ]
    zips_collection = database[ "zips" ]
    
    print(
'''
We can use query operators to produce more fine grained queries.
For instance to find zip codes with populations greater than 90,000 we use
the $gt operator.

    cursor = zips_collection.find( { "pop" : { "$gt" : 90000 }})
    count = 0
    for i in cursor:
        count = count + 1
        print( i )
    print( "%i records" % count )
    
''')
    
    cursor = zips_collection.find( { "pop" : { "$gt" : 90000 }})
    count = 0
    for i in cursor:
        count = count + 1
        print( i )
    print( "%i records" % count )
    
    print(
'''
We can do the inverse with $lt.
For instance to find zip codes with populations less than 1000 we use
the $lt operator.

    cursor = zips_collection.find( { "pop" : { "$lt" : 10 }})
    count = 0
    for i in cursor:
        count = count + 1
        print( i )
    print( "%i records" % count )
    
''') 
    
    cursor = zips_collection.find( { "pop" : { "$lt" : 10 }})
    count = 0
    for i in cursor:
        count = count + 1
        print( i )
    print( "%i records" % count ) 
    
    print(
'''
We can use the "in" operator to see if a value is a member of a set (aka an array).
Lets see the populations of the zip codes in three states. Rhode Island, District of 
Columbia and Delaware.

    cursor = zips_collection.find( { "state" : { "$in" : [ "DC", "RI", "DE"] }},
                                   { "pop" : 1, "state" : 1})
    count = 0
    for i in cursor:
        count = count + 1
        print( i )
    print( "%i records" % count ) 

''') 

    cursor = zips_collection.find( { "state" : { "$in" : [ "DC", "RI", "DE"] }},
                                   { "pop" : 1, "state" : 1})
    count = 0
    for i in cursor:
        count = count + 1
        print( i )
    print( "%i records" % count ) 
        