<!-- Template version 1.0
-->
<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/BrandonNNiles/Delta-Alpha-Kilo-Discord-Bot">
    <img src="media/images/dak.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">D.A.K. Discord Bot</h3>

  <p align="center">
    A management and analytical bot
    <br />
    <a href="https://github.com/BrandonNNiles/Delta-Alpha-Kilo-Discord-Bot"><strong>Project Repo</strong></a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#requirements">Requirements</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


The Delta Alpha Kilo Discord (D.A.K.) aims to provide a unique approach to the standard of logging and management-based bots on Discord. The D.A.K. bot provides functionality for SQL-based storage of messages and the ability to back up entire Discord servers channel by channel. Additionally, the bot includes useful tools for graphically analyzing the data, such as graphing. All of this can be done through the sleek user interface.

##### Noteable Features:
* User Interface
* Logging of real time events
* Chat commands
* Console-based host commands (ability to execute commands from a terminal)
    * Ability to add custom console-commands with little coding
* Full server back-up using SQLite
* Management operations
* Graphical analytics of server back-ups

This bot is still in development and subject to change.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

The following languages, tools, and frameworks were used to develop the project:

* SQLite3
* Discord.py

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

You can either: 
* a) [Add the bot to your server directly.](https://discord.com/api/oauth2/authorize?client_id=885352661493366824&permissions=8&scope=bot)

* b) Follow the following steps to get the bot up and running for yourself.

### Requirements

Install the following dependencies below:
* Discord.py
  ```sh
  pip install git+https://github.com/Rapptz/discord.py
  ```
* npm
  ```sh
  npm install npm@latest -g
  ```
* SQLite3
  ```sh
  npm install sqlite3
  ```

### Installation

1. Create a [Discord Bot Application](https://discord.com/developers/docs/)
    * a) Note your bot's token
    * b) Assign all privledge intents on the application's "Bot" page  
2. Clone the repo
   ```sh
   git clone https://github.com/BrandonNNiles/Delta-Alpha-Kilo-Discord-Bot.git
   ```
3. Install NPM packages (See above requirements)
4. Enter your token in `token.js`
   ```js
   {
        "bot_token": "YOUR_TOKEN_HERE"
    }
   ```
5. Execute the file `src/main.py`



<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
The main purpose of the bot is to extract useful information regarding statistics of a given server, this can be accomplished through a few different means.

### Chat Commands
Pending implementation.
### Console Commands
The following are a set of currently implemented commands that can be executed through the applications terminal. Due to the nature of the console, these would only be accessible through manual access of the bot's operation.
```
Command          Arguments                      Description
-------          ---------                      -----------
/channellist     [GuildID]                      Prints a list of all channels and their IDs.
/dbcount         [GuildID Phrase]               Counts how many times a given string occurs in the database.
/guildlist       [None]                         Prints a list of guilds and IDs that the bot is in.
/help            [None]                         Displays all commands available.
/say             [ChannelID Message]            Sends a message to a given channel.
/startchatting   [ChannelID]                    Enables constant chat mode.
```
####UI
Pending implementation.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Database message history
- [ ] User Interface
- [ ] Database analytics
    - [ ] Graphical Interpretations


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Brandon Niles - [LinkedIn](https://www.linkedin.com/in/brandonnniles/) - brandonniles00@gmail.com

<p align="right">(<a href="#readme-top">back to top</a>)</p>

