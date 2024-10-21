#!/usr/bin/env python3
"""" list all documents in a collection of a database """


def list_all(mongo_collection: object) -> list:
    """ list all databases in MongoDB """
    return mongo_collection.find()
