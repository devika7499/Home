import sqlite3

conn = sqlite3.connect("production.db")
cursor = conn.cursor()

# Create the table
cursor.execute("CREATE TABLE IF NOT EXISTS production (API_WELL_NUMBER TEXT, OIL INTEGER, GAS INTEGER, BRINE INTEGER)")

# Insert the annual data into the table
for _, row in annual_data .iterrows():
    cursor.execute("INSERT INTO production VALUES (?, ?, ?, ?)",
                   (row["API WELL NUMBER"], row["OIL"], row["GAS"], row["BRINE"]))

# Commit the changes and close the connection
conn.commit()
conn.close()
