#!/usr/bin/env python3
""" insert a document in collection based on kwargs """
import pymongo


def insert_school(mongo_collection: object, **kwargs):
    """ inserts a new document in a collection based on kwargs
    Args:
        mongo_collection: pymongo collection object
    Returns:
        the new _id
    """
    return mongo_collection.insert_one(kwargs).inserted_id
