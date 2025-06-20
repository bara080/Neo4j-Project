from neo4j import GraphDatabase
import os

URI = "neo4j+s://your-db-id.databases.neo4j.io"
USERNAME = "neo4j"
PASSWORD = os.environ.get("NEO4J_PASSWORD")  # Correct way in Python

driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))

def test_connection():
    with driver.session() as session:
        greeting = session.run("RETURN 'Hello from Neo4j!' AS message")
        print(greeting.single()["message"])

test_connection()
