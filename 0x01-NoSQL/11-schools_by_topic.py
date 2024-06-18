#!/usr/bin/env python3
"""
Python will be topic searched
"""


def schools_by_topic(mongo_collection, topic):
    """
     returns the list of school having a specific topic

    :param mongo_collection
    :param topic
    """
    return mongo_collection.find({"topics": topic})
