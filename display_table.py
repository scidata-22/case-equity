import sqlite3
from prettytable import PrettyTable, HRuleStyle

# Connect to the SQLite database (sample.db)
conn = sqlite3.connect('sample.db')
cursor = conn.cursor()

# Step 1: Fetch the list of table names from the sqlite_master table
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Step 2: Loop through each table and display its contents
for table_name in tables:
    table_name = table_name[0]  # Extract table name from tuple
    # print(f"\nDisplaying contents of table: {table_name}")
    
    # Step 3: Fetch column names for the current table
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = cursor.fetchall()
    field_names = [col[1] for col in columns]  # Extract column names
    
    # Step 4: Fetch all rows from the table
    cursor.execute(f"SELECT * FROM {table_name};")
    rows = cursor.fetchall()
    
    # Step 5: Create a PrettyTable object
    table = PrettyTable()
    table.title = f"\033[31m{table_name}\033[0m"
    table.hrules = HRuleStyle.ALL

    # Apply yellow color to the field names using f-strings
    table.field_names = [f"\033[33m{field}\033[0m" for field in field_names]

    # Step 6: Add rows to the table
    for row in rows:
        table.add_row(row)

    # Step 7: Print the table
    print(table)

# Close the connection
conn.close()
