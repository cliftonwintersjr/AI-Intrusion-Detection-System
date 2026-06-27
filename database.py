import mysql.connector

# -----------------------------
# Database Connection
# -----------------------------
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="CyberC85!",
        database="ai"
    )

# -----------------------------
# Insert Alert Function
# -----------------------------
def insert_alert(alert_data):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO alerts (
        timestamp,
        attack_type,
        severity,
        description,
        packet_size,
        packets_per_second,
        connection_duration,
        failed_connections,
        data_transfer_rate,
        connection_attempts
    )
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    values = (
        alert_data["timestamp"],
        alert_data["attack_type"],
        alert_data["severity"],
        alert_data["description"],
        alert_data["packet_size"],
        alert_data["packets_per_second"],
        alert_data["connection_duration"],
        alert_data["failed_connections"],
        alert_data["data_transfer_rate"],
        alert_data["connection_attempts"]
    )

    cursor.execute(sql, values)
    conn.commit()

    cursor.close()
    conn.close()

    print("🗄️ Alert stored in database")

def get_alerts():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(""" 
        SELECT *
        FROM alerts
        ORDER BY timestamp DESC
    """)

    alerts = cursor.fetchall()

    cursor.close()
    conn.close()


    return alerts