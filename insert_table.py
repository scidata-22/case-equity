import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('sample.db')
cursor = conn.cursor()

# Insert data into ProductData Table
cursor.executemany('''
INSERT INTO ProductData (ProductID, ProductName, CurrentStage, LaunchDate) 
VALUES (?, ?, ?, ?)
''', [
    (101, 'Electric SUV Battery', 'Testing Phase', '2025-06-15'),
    (102, 'Hybrid Engine System', 'Final Approval', '2025-09-20'),
    (103, 'Autonomous Driving AI', 'Prototype Design', '2026-01-10'),
    (104, 'Electric Motor Controller', 'Design Phase', '2025-12-01'),
    (105, 'Battery Management System', 'Prototype Testing', '2026-04-10')
])

# Insert data into MilestoneData Table
cursor.executemany('''
INSERT INTO MilestoneData (MilestoneID, ProductID, MilestoneName, Status) 
VALUES (?, ?, ?, ?)
''', [
    (1, 101, 'Concept Approval', 'Completed'),
    (2, 101, 'Initial Prototype', 'Completed'),
    (3, 101, 'Testing', 'In Progress'),
    (4, 102, 'Supplier Agreement', 'Completed'),
    (5, 102, 'Crash Testing', 'Completed'),
    (6, 103, 'AI Training', 'In Progress'),
    (7, 104, 'Initial Design Review', 'Completed'),
    (8, 104, 'Prototype Fabrication', 'In Progress'),
    (9, 105, 'Initial Prototype', 'In Progress'),
    (10, 105, 'Testing Phase', 'Planned')
])

# Insert data into EngineeringData Table
cursor.executemany('''
INSERT INTO EngineeringData (EngineeringID, ProductID, ComplianceScore) 
VALUES (?, ?, ?)
''', [
    (1, 101, 85.5),
    (2, 102, 92.3),
    (3, 103, 78.0),
    (4, 104, 88.0),
    (5, 105, 91.5)
])

# Insert data into SupplyChainData Table
cursor.executemany('''
INSERT INTO SupplyChainData (SupplyID, ProductID, SupplierName, AvailabilityStatus) 
VALUES (?, ?, ?, ?)
''', [
    (1, 101, 'LG Batteries', 'Available'),
    (2, 101, 'Tesla Components', 'Available'),
    (3, 102, 'Bosch', 'Unavailable'),
    (4, 102, 'Continental', 'Available'),
    (5, 103, 'NVIDIA Chips', 'Unavailable'),
    (6, 104, 'Siemens', 'Available'),
    (7, 105, 'Panasonic', 'Available'),
    (8, 105, 'LG Chem', 'Unavailable')
])

# Commit changes and close connection
conn.commit()
conn.close()

print("Data inserted successfully.")
