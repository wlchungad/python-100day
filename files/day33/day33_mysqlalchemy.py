import sqlalchemy as db
from sqlalchemy import MetaData, Table, Column, Integer, String, Float, ForeignKey
from sqlalchemy_utils import database_exists, create_database
import pymysql

engine = db.create_engine('mysql+pymysql://root:Passw0rd@localhost:3306/test_db', echo=True)

try:
    conn = engine.connect() 
    print("Connection Successful")
except:
    if not database_exists(engine.url): 
        create_database(engine.url)
        print("Connection %s is created" % (engine.url))

# Create a MetaData object
metadata = MetaData()

# Define the employees table
employees = Table(
    "employees", metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(255), nullable=False),
    Column("department", String(255), nullable=False),
    Column("salary", Float, nullable=False)
)

departments = Table(
    "departments", metadata,
    Column("id", Integer, primary_key=True),
    Column("department_name", String(255), unique=True, nullable=False)
)

projects = Table(
    "projects", metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(255), unique=True, nullable=False),
    Column("budget", Integer, nullable=False)
)

tasks = Table(
    "tasks", metadata,
    Column("id", Integer, primary_key=Table),
    Column("project_id", Integer, ForeignKey("projects.id"), nullable=False),
    Column("task_name", String(255), nullable=False),
    Column("status", String(255), nullable=False)
)

metadata.create_all(engine)

print(metadata.tables.keys())