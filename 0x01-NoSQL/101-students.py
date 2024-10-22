#!/usr/bin/env python3
""" aggregate and sort """
import pymongo


def top_students(mongo_collection):
    """ list all students sorted by average score
    Args:
        mongo_collection: pymongo collection object
    Returns:
        list of students sorted by average score
    """
    return mongo_collection.aggregate([
        {"$project": {
            "name": "$name",
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ])
