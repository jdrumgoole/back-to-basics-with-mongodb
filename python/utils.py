'''
Created on 6 Apr 2017

@author: jdrumgoole
'''
import pymongo
import sys

def open_collection( collection_name, database_name="b2b", timeout=1000 ):
    '''
    Create a client. Create a database "database" and a collection
    "collection".
    
    return the collection object.
    
    We validate the connection by explicitly calling ismaster.
    
    We drop the serverSelectionTimeoutMS (default 30seconds)
    to 1 second as we are connecting locally to probably a single server.
    
    '''

    client = pymongo.MongoClient( serverSelectionTimeoutMS=timeout )
    database = client[ database_name ]
    collection = database[ collection_name ]
    #
    # Make sure we have a collection
    print( "Connecting to database server...")
    try:
    
        _ = database.command("ismaster")
        print( "connected" )
        print( "collection '%s.%s' has %i documents" % ( database_name, 
                                                         collection_name, 
                                                         collection.count()))
        return collection
    
    except pymongo.errors.ServerSelectionTimeoutError, e:
        print( "connection failed: %s" % e )
        print( "No mongod found on port 27017")
        sys.exit( 2 )
    
    
def cursor_print( cursor, verbose=False ):
    count = 0
    for i in cursor:
        count = count + 1
        if verbose:
            print( i )
    print( "%i records" % count )
    return count