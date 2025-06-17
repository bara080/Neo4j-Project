from neo4j import GraphDatabase

# Replace with your Neo4j Aura credentials
URI = "neo4j+s://your-db-id.databases.neo4j.io"
USERNAME = "neo4j"
PASSWORD = "your-password"

driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))

def test_connection():
    with driver.session() as session:
        greeting = session.run("RETURN 'Hello from Neo4j!' AS message")
        print(greeting.single()["message"])

test_connection()
