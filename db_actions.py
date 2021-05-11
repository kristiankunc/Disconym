import random
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

    # PREFIX

    def add_prefix(guild_id, prefix):
        Database.connect(Database())

        insert_query = "INSERT INTO prefixes (guild_id, prefix) VALUES (%s, %s);"
        cursor.execute(insert_query, (int(guild_id), str(prefix),))
        db_connection.commit()

        Database.disconnect()

    def remove_prefix(guild_id):
        Database.connect(Database())

        delete_query = "DELETE FROM prefixes WHERE guild_id = %s;"
        cursor.execute(delete_query, (int(guild_id),))
        db_connection.commit()

        Database.disconnect()

    def replace_prefix(guild_id, prefix):
        Database.connect(Database())

        replace_query = "UPDATE prefixes SET prefix = %s WHERE guild_id = %s;"
        cursor.execute(replace_query, (str(prefix), int(guild_id),))
        db_connection.commit()

        Database.disconnect()

    # BLACKLIST

    def add_blacklist(user_id, reason):
        Database.connect(Database())

        insert_query = "INSERT INTO blacklist (user_id, reason) VALUES (%s, %s);"
        cursor.execute(insert_query, ( int(user_id), str(reason),))
        db_connection.commit()

        Database.disconnect()

    def remove_blacklist(user_id):
        Database.connect(Database())

        remove_query = "DELETE FROM blacklist WHERE user_id = '%s';"
        cursor.execute(remove_query, (int(user_id),))
        db_connection.commit()

        Database.disconnect()

    def find_prefix(guild_id):
        Database.connect(Database())

        find_query = "SELECT prefix from prefixes where guild_id = %s;"
        cursor.execute(find_query, (int(guild_id),))
        data = cursor.fetchall()
        
        return data[0]

        Database.disconnect()

    def check_blacklist(user_id):
        Database.connect(Database())

        check_query = "SELECT reason FROM blacklist WHERE user_id = %s;"
        cursor.execute(check_query, (int(user_id),))
        data = cursor.fetchall()

        try:
            d = data[0]

        except:
            return False


    # LOGGING

    def add_log(msg_link):
        Database.connect(Database())

        msg_id = random.randint(10000,99999)

        cursor.execute("SELECT msg_link FROM messages WHERE id = (%s);", (int(msg_id),))
        check_id_fetch = cursor.fetchone()

        if check_id_fetch != 0:

            insert_query = "INSERT INTO messages (id, msg_link) VALUES (%s, %s);"

            cursor.execute(insert_query, (int(msg_id), str(msg_link),))
            db_connection.commit()

        else:
            Database.add_log(msg_id)
        
        Database.disconnect()
        
        return msg_id


    def remove_log(log_id):
        Database.connect(Database())

        remove_query = "DELETE FROM messages WHERE id = '%s';"
        cursor.execute(remove_query, (int(log_id),))
        db_connection.commit()

        Database.disconnect()

    
    def get_log(log_id):
        Database.connect(Database())

        cursor.execute("SELECT msg_link from messages where id = '%s';", (int(log_id),))
        data = cursor.fetchall()
        
        return data[0]

        Database.disconnect()