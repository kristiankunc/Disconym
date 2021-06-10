import random
import mysql.connector as mysql

host = None
database = None
user = None
password = None

class Database:
    def connect():
        global host
        global database
        global user
        global password

        if host == None:
            with open("db_data.txt","r") as f:
                lines = f.readlines()
                host = lines[0]
                database = lines[1]
                user = lines[2]
                password = lines[3]

        global db_connection
        global cursor
        db_connection = mysql.connect(host=host, database=database, user=user, password=password)
        cursor = db_connection.cursor()

    def disconnect():
        db_connection.close()
        cursor.close()

    # PREFIX

    def add_prefix(guild_id, prefix):
        Database.connect()

        insert_query = "INSERT INTO prefixes (guild_id, prefix) VALUES (%s, %s);"
        cursor.execute(insert_query, (int(guild_id), str(prefix),))
        db_connection.commit()

        Database.disconnect()

    def remove_prefix(guild_id):
        Database.connect()

        delete_query = "DELETE FROM prefixes WHERE guild_id = %s;"
        cursor.execute(delete_query, (int(guild_id),))
        db_connection.commit()

        Database.disconnect()

    def replace_prefix(guild_id, prefix):
        Database.connect()

        replace_query = "UPDATE prefixes SET prefix = %s WHERE guild_id = %s;"
        cursor.execute(replace_query, (str(prefix), int(guild_id),))
        db_connection.commit()

        Database.disconnect()

    # BLACKLIST

    def add_blacklist(user_id, reason):
        Database.connect()

        insert_query = "INSERT INTO blacklist (user_id, reason) VALUES (%s, %s);"
        cursor.execute(insert_query, (int(user_id), str(reason),))
        db_connection.commit()

        Database.disconnect()

    def remove_blacklist(user_id):
        Database.connect()

        remove_query = "DELETE FROM blacklist WHERE user_id = '%s';"
        cursor.execute(remove_query, (int(user_id),))
        db_connection.commit()

        Database.disconnect()

    def find_prefix(guild_id):
        Database.connect()

        find_query = "SELECT prefix from prefixes where guild_id = %s;"
        cursor.execute(find_query, (int(guild_id),))
        data = cursor.fetchall()
        Database.disconnect()

        return data[0]

    def check_blacklist(user_id):
        Database.connect()

        check_query = "SELECT reason FROM blacklist WHERE user_id = %s;"
        cursor.execute(check_query, (int(user_id),))
        data = cursor.fetchall()

        try:
            d = data[0]

        except:
            return False


    # LOGGING

    def add_log(msg_link):
        Database.connect()

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
        Database.connect()

        remove_query = "DELETE FROM messages WHERE id = '%s';"
        cursor.execute(remove_query, (int(log_id),))
        db_connection.commit()

        Database.disconnect()

    
    def get_log(log_id):
        Database.connect()

        cursor.execute("SELECT msg_link from messages where id = '%s';", (int(log_id),))
        data = cursor.fetchall()

        Database.disconnect()

        return data[0]

    # API
    
    def get_total_messages():
        Database.connect()

        cursor.execute("SELECT * FROM messages")
        data = cursor.fetchall()

        Database.disconnect()

        return len(data)

    def clear_api_table():
        Database.connect()

        cursor.execute("DELETE FROM api")
        db_connection.commit()

        Database.disconnect()

    def update_api_data(guilds):
        Database.clear_api_table()
        total_msgs = int(Database.get_total_messages())

        Database.connect()

        insert_query = f"INSERT INTO api (msgs, guilds) VALUES ({total_msgs}, {guilds});"
        
        cursor.execute(insert_query)
        db_connection.commit()

        Database.disconnect()

    def read_api():
        Database.connect()

        cursor.execute("SELECT * FROM api")
        data = cursor.fetchone()

        return data