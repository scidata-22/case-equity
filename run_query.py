import sqlite3
from prettytable import PrettyTable, HRuleStyle

# Connect to the SQLite database (sample.db)
conn = sqlite3.connect('sample.db')
cursor = conn.cursor()

# Step 1: Create Indexes for Faster Querying
cursor.execute('CREATE INDEX IF NOT EXISTS idx_product_id ON ProductData (ProductID);')
cursor.execute('CREATE INDEX IF NOT EXISTS idx_milestone_product ON MilestoneData (ProductID);')
cursor.execute('CREATE INDEX IF NOT EXISTS idx_engineering_product ON EngineeringData (ProductID);')
cursor.execute('CREATE INDEX IF NOT EXISTS idx_supply_product ON SupplyChainData (ProductID);')

# Step 2: Define the SQL Query with Common Table Expressions (CTEs)
query = '''
WITH MilestoneCompletion AS (
    SELECT 
        ProductID,
        COUNT(*) AS TotalMilestones,
        SUM(CASE WHEN Status = 'Completed' THEN 1 ELSE 0 END) AS CompletedMilestones,
        ROUND(100.0 * SUM(CASE WHEN Status = 'Completed' THEN 1 ELSE 0 END) / COUNT(*), 2) AS CompletionRate
    FROM MilestoneData
    GROUP BY ProductID
),
EngineeringCompliance AS (
    SELECT 
        ProductID,
        AVG(ComplianceScore) AS AvgComplianceScore
    FROM EngineeringData
    GROUP BY ProductID
),
SupplyChainReadiness AS (
    SELECT 
        ProductID,
        COUNT(CASE WHEN AvailabilityStatus = 'Available' THEN 1 END) * 100.0 / COUNT(*) AS ReadinessScore
    FROM SupplyChainData
    GROUP BY ProductID
)

-- Step 3: Final Query to Combine All Data
SELECT 
    p.ProductID, 
    p.ProductName, 
    p.CurrentStage, 
    m.CompletionRate AS MilestoneCompletion, 
    e.AvgComplianceScore AS EngineeringCompliance, 
    s.ReadinessScore AS SupplierReadiness
FROM ProductData p
LEFT JOIN MilestoneCompletion m ON p.ProductID = m.ProductID
LEFT JOIN EngineeringCompliance e ON p.ProductID = e.ProductID
LEFT JOIN SupplyChainReadiness s ON p.ProductID = s.ProductID
WHERE p.LaunchDate > DATE('now') -- Filter for upcoming product launches
ORDER BY MilestoneCompletion DESC, EngineeringCompliance DESC;
'''

# Step 3: Execute the query
cursor.execute(query)

# Fetch the results
rows = cursor.fetchall()

# Create a PrettyTable object
table = PrettyTable()

# Define column names for the table
table.field_names = [f"\033[33m{field}\033[0m" for field in ["ProductID", "ProductName", "CurrentStage", "MilestoneCompletion", "EngineeringCompliance", "SupplierReadiness"]]

# Add rows to the table
for row in rows:
    table.add_row(row)

# Set horizontal rule style (you can choose HRuleStyle.ALL, HRuleStyle.HEADER, etc.)
table.hrules = HRuleStyle.ALL  # Applies horizontal rules to all rows

# Print the table
print(table)

# Close the connection
conn.close()
