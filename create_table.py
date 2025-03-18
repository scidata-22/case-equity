import sqlite3

# Connect to SQLite database (creates the database if it doesn't exist)
conn = sqlite3.connect('sample.db')
cursor = conn.cursor()

# Create ProductData Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS ProductData (
    ProductID INTEGER PRIMARY KEY,
    ProductName TEXT NOT NULL,
    CurrentStage TEXT NOT NULL,
    LaunchDate DATE NOT NULL
)
''')

# Create MilestoneData Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS MilestoneData (
    MilestoneID INTEGER PRIMARY KEY,
    ProductID INTEGER,
    MilestoneName TEXT NOT NULL,
    Status TEXT NOT NULL,
    FOREIGN KEY (ProductID) REFERENCES ProductData (ProductID)
)
''')

# Create EngineeringData Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS EngineeringData (
    EngineeringID INTEGER PRIMARY KEY,
    ProductID INTEGER,
    ComplianceScore REAL NOT NULL,
    FOREIGN KEY (ProductID) REFERENCES ProductData (ProductID)
)
''')

# Create SupplyChainData Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS SupplyChainData (
    SupplyID INTEGER PRIMARY KEY,
    ProductID INTEGER,
    SupplierName TEXT NOT NULL,
    AvailabilityStatus TEXT NOT NULL,
    FOREIGN KEY (ProductID) REFERENCES ProductData (ProductID)
)
''')

# Commit changes and close connection
conn.commit()
conn.close()

print("Tables created successfully.")
