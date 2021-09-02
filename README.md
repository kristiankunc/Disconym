<p align="center">
  <img width="400" height="400" src="https://github.com/KristN1/Disconym/blob/main/imgs/logo-circle.png?raw=true" alt="Disconym Logo Circle" />
</p>

<p align="center">
  <strong>Disconym - Discord bot for sending anonymous messages</strong>
</p>

<p align="center">
  <a href="https://discord.gg/123456">
    <img src="https://img.shields.io/website-up-down-green-red/http/cv.lbesson.qc.to.svg" alt="discord - users online" />
  </a>
  <img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg">
  <img src="https://img.shields.io/discord/849290134809608212.svg?color=7289da&label=Discord%20server&logo=discord&style=flat-square)](https://discord.gg/6YYF68zzPK)">
</p>

<h3 align="center">
  <a href="https://discord.gg/6YYF68zzPK">Discord server</a>
  <span> · </span>
  <a href="https://discord.gg/123456">Bot invite - <i>soon</i></a>
  <span> · </span>
  <a href="https://kristn.tech">Website - <i>soon</i></a>
</h3>

---

# Disconym

## Repo archived as discord.py is discontinued

## Features

- Send feature: sends your input message to a selected user
- Report system: if a message is inappropriate, you can react to it and it will be sent to the moderation team who can blacklist the user
- Changeable prefix: you can change the bot's prefix
- Full support of slash commands

*more features soon*

## Running on local

1. clone the repo using `git clone`
```bash
$ git clone https://github.com/KristN1/Disconym.git
```
or download the code directly by clicking the green "Code" button and then "Download ZIP", then unzip the folder on your desktop

![How to download zip](https://github.com/KristN1/Disconym/blob/main/imgs/how-to-download.PNG?raw=true)



#### 2. Change to the directory
#### 3. Rename `congif.json.example` to `config.json` and edit it with your credentials 
![Config example](https://raw.githubusercontent.com/KristN1/Disconym/main/imgs/config.json-example.png)

#### 4. Create all needed MySQL databse and tables
```bash
$ python init_database.py
```

#### 5. Run main.py
```bash
$ python main.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.