#!/bin/sh
# 
# use the mongodbimport tool (a standard commandline tool that comes with every MongoDB
# installation) to import data from the zips.json collection.
#
# We import into the "b2b' database.
# The data is stored in the "zips" collection.
# We drop the collection "zips" if it exists before loading the new collection.
# we read from file zips.json.
#
# We expect a default "mongod" deamon to be running on port 
# 20717. (Just start a mongod for this to happen).
#

echo "Importing zips.json into mongod on port 27017"

mongoimport --db b2b --collection restaurants --drop --file nyc_restaurants.json 
