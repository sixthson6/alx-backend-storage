#!/usr/bin/env python3
"""Connecto to mongodb database
list all documents"""

import pymongo


def list_all(mongo_collection):
    """list all documents in mongod db"""
    return mongo_collection.find()
