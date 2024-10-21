#!/usr/bin/env python3
"""" list all databases """


def list_all(mongo_collection):
    """ list all databases in MongoDB """
    return mongo_collection.list_database_names()
