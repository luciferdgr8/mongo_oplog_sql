# still working on it
from pymongo import MongoClient


def create_connection(*args,**kwargs):
    client = MongoClient(**kwargs)
    return client

def get_database(*args,**kwargs):
    client= create_connection(*args, **kwargs)
    return client[kwargs.get('database')]

def get_collection(*args,**kwargs):
    db = get_database(*args,**kwargs)
    return db[kwargs.get('collection')]

def get_documents(*args,**kwargs):
    no_of_docs = kwargs.get('docs_count')
    last_doc = kwargs.get('last_doc_id')
    return collection.find({'_id':{'$gt':last_doc}}).limit(no_of_doc)

def serialize_docs(**args,**kwargs):
    schema_require = kwargs.get('required_schema')
        
