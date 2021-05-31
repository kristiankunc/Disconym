# Disconym

Disconym is a Discord bot that allows you to send anonymous messages to other users

## Features

- Send feature: sends your input message to a selected user
- Report system: if a message is inappropriate, you can react to it and it will be sent to the moderation team who can blacklist the user
- Changeable prefix: you can change the bot's prefix
- Full support of slash commands

*more features soon*
 
## Official bot sites

- Bot invite - *Comming with full release*
- top.gg - *Comming with full release* 

## Running on local

1. clone the repo using `git clone`
```bash
$ git clone https://github.com/KristN1/Disconym.git
```
or download the code directly by clicking the green "Code" button and then "Download ZIP", then unzip the folder on your desktop

![How to download zip](https://github.com/KristN1/Disconym/blob/main/imgs/how-to-download.PNG?raw=true)



#### 2. Change to the directory
#### 3. create file called `token.txt` and paste there your [Discord Bot token](http://discord.com/developers)
#### 4. Create file called `db_data.txt` and paste data in the following format
```bash
mysql_server_ip
database_name
mysql_username
mysql_password
```

#### 4. Create all needed MySQL databse and tables

 - 4.1 create disconym database and switch to it
```bash
$ CREATE DATABASE disconym;
$ USE disconym;
```

 - 4.2 Create the blacklist table
```bash
$ CREATE TABLE blacklist(userid BIGINT, reason VARCHAR(256));
```
 - 4.3 Create the messages table
```bash
$ CREATE TABLE blacklist(id BIGINT, msg_link VARCHAR(148));
```
 - 4.4 create the prefixes table
```bash
$ CREATE TABLE blacklist(guild_id BIGINT, prefix STR);
```

#### 4. run main.py
```bash
$ python main.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.