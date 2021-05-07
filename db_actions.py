import mysql.connector as mysql

class Database:
    def __init__(self):
        with open("db_data.txt","r") as f:
            lines = f.readlines()
            self.host = lines[0]
            self.database = lines[1]
            self.user = lines[2]
            self.password = lines[3]

    def connect(self):
        global db_connection
        global cursor
        db_connection = mysql.connect(host=self.host, database=self.database, user=self.user, password=self.password)
        cursor = db_connection.cursor()

    def disconnect():
        db_connection.close()
        cursor.close()

    def add_prefix(guild_id, prefix):
        Database.connect(Database())

        insert_query = f"INSERT INTO prefixes (guild_id, prefix) VALUES ({int(guild_id)}, '{str(prefix)}')"

        cursor.execute(insert_query)
        db_connection.commit()

        Database.disconnect()

    def remove_prefix(guild_id):
        Database.connect(Database())

        delete_query = f"DELETE FROM prefixes WHERE guild_id = '{int(guild_id)}'"

        cursor.execute(delete_query)
        db_connection.commit()

        Database.disconnect()

    def replace_prefix(guild_id, prefix):
        Database.connect(Database())

        replace_query = f"UPDATE prefixes SET prefix = '{prefix}' WHERE guild_id = '{guild_id}'"

        cursor.execute(replace_query)
        db_connection.commit()

        Database.disconnect()

    def find_prefix(guild_id):
        Database.connect(Database())

        cursor.execute("SELECT * from prefixes")
        data = cursor.fetchall()

        for row in data:
            if row[0] == guild_id:
                return str(row[1])

        Database.disconnect()