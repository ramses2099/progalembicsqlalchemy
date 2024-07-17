# progalembicsqlalchemy
Alembic Introduction - Migrations and Auto-Generating Revisions from SQLAlchemy Models

# Create virtual enviroment
1. python -m venv venv
1. ./venv/Scripts/activate
1. pip install alembic
1. create database in postgres create database alembic_db
1. install modules pip install alembic psycopg2
1. init project alembic init [project name]
1. create migration 
- alembic revision -m "Create Employee table" 
1. run migration with command
- alembic upgrade head or version id
1. add new column to the table
- alembic revision -m "add job_title column"
1. for see all changes apply to the database 
- alembic history
1. downgrade db remove all changes
- alembic downgrade base or revision id = 'acf1509bc2af'
1. remove all changes and file
1. create file models.py
1. using autogenerate
- alembic revision --autogenerate -m "message"
- alembic revision head