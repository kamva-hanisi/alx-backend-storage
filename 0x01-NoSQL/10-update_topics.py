#!/usr/bin/env python3
""" Python using pymongo, change school """


def update_topics(mongo_collection, name, topics):
    """ Changes all topics of a school
    """

    shilde_name = {"name": name}
    new_values = {"$set": {"topics": topics}}

    mongo_collection.update_many(shilde_name, new_values)
