#!/usr/bin/env python3
"""insert into db"""

import pymongo


def insert_school(mongo_collection, **kwargs):
    """insert into db"""
    return mongo_collection.insert_one(kwargs).inserted_id