import pymysql

def test_database_schema():
    conn = None
    cursor = None
    try:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            database='subscribers_db'
        )
        cursor = conn.cursor()

        # Test if 'subscribers' table exists
        cursor.execute("SHOW TABLES LIKE 'subscribers';")
        result = cursor.fetchone()
        assert result, "❌ Table 'subscribers' does not exist!"
        print("✅ Table 'subscribers' exists!")

        # Test if 'subscription_date' column exists
        cursor.execute("SHOW COLUMNS FROM subscribers LIKE 'subscription_date';")
        result = cursor.fetchone()
        assert result, "❌ Column 'subscription_date' does not exist!"
        print("✅ Column 'subscription_date' exists!")

        # Insert a test subscriber
        cursor.execute("INSERT INTO subscribers (email) VALUES ('test@example.com');")
        conn.commit()

        # Validate if subscription_date is auto-populated
        cursor.execute("SELECT subscription_date FROM subscribers WHERE email='test@example.com';")
        result = cursor.fetchone()
        assert result and result[0] is not None, "❌ subscription_date not auto-populated!"
        print("✅ subscription_date is auto-populated!")

    except Exception as e:
        print(f"❌ Test failed: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    test_database_schema()
