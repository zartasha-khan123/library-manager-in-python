import mysql.connector

try:
    conn = mysql.connector.connect(
        host="182.190.217.151",  # Public IP
        user="remote_user",
        password="mysons2830",
        database="library_db",
        port="3306"
    )
    print("✅ Remote MySQL Access Successful!")
except mysql.connector.Error as err:
    print(f"❌ Connection Failed: {err}")
