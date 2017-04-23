'''
Created on 6 Apr 2017

@author: jdrumgoole
'''

import utils

if __name__ == '__main__':
    
    collection = utils.open_collection( "zips" )

    print( "Opened collection zips")
    
    print(
'''
Here is the set of all zip codes whose population is 1000 or greater.

    cursor = collection.find( { "pop" : { "$gte" : 1000 }})
''')
    
    cursor = collection.find( { "pop" : { "$gte" : 1000 }})
    
    utils.cursor_print( cursor )
    print(
'''
Here is a boolean "and" query. "$and" is implied
by including the additional clauses. Here we find all zipcodes in DC and that
have a pop greater than or equal to 1000.

    cursor = collection.find( { "state" : "DC",
                                "pop" : { "$gte" : 1000 }})
''')

    cursor = collection.find( { "state" : "DC",
                                "pop" : { "$gte" : 1000 }})
    
    utils.cursor_print( cursor )
    
    print(
'''
Here is a boolean "$or" operator. Lets find all the zip codes in DC and MA that
have a population greater than or equal 1000.

    cursor = collection.find( { "$or"  : [ { "state" : "DC" } , { "state" : "MA" } ],
                                "pop" : { "$gte" : 1000 }})
'''        
)
    
    cursor = collection.find( { "$or"  : [ { "state" : "DC" } , { "state" : "MA" } ],
                                "pop" : { "$gte" : 1000 }})
    
    utils.cursor_print( cursor )


    print( 
'''
An easier way to do this is with $in

    cursor = collection.find( { "state" : { "$in" : [ "DC", "MA" ] },
                                "pop" : { "$gte" : 1000 }})
''' )
    
    cursor = collection.find( { "state" : { "$in" : [ "DC", "MA" ] },
                                "pop" : { "$gte" : 1000 }})
    
    utils.cursor_print( cursor )
    
    print(
'''
Here is a boolean "$not" operator. Lets find all the zip codes $not in DC and MA that
have a population greater than or equal 1000.

    cursor = collection.find( { "state" : { "$not" : { "$in" : [ "DC", "MA" ] }},
                                "pop" : { "$gte" : 1000 }})
'''        
)
    
    cursor = collection.find( { "state" : { "$not" : { "$in" : [ "DC", "MA" ] }},
                                "pop" : { "$gte" : 1000 }})
    
    utils.cursor_print( cursor)
    

    