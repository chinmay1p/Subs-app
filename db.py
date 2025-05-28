import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
cli=MongoClient(os.getenv("MONGO_URI"))
db=cli.subsys
pln=db.plans
sub=db.subs 