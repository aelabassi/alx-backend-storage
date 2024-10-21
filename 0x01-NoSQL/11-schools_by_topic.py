#!/usr/bin/env python3
""" list of school having a specific topic """
import pymongo


def schools_by_topic(mongo_collection, topic):
    """ list of school having a specific topic
    Args:
        mongo_collection: pymongo collection object
        topic: (string) topic searched
    Returns:
        list of school having a specific topic
    """
    return mongo_collection.find({"topics": topic})
