# Setting up the project

## Requirements

* [Git](https://git-scm.com/downloads)
* A GitHub account
* [Visual Studio Code](https://code.visualstudio.com/download)
    * [Live Share Extension for *class*](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare)
* Python 3.10 (Installable through the Microsoft Store on Windows)

## Creating the virtual environment

A virtual environment copies the installed Python system environment, but isolates the packages a project requires into a local installion. This keeps the system install clean by installing packages locally instead of globally to the system.

### **Creating the virtual environment**

```
python3 -m venv .bot-env
```

### **Activate the virtual environment**

**Windows:**

```
.bot-env\Scripts\activate.bat
```

**OSX / Linux:**

```
source .bot-env/Scripts/activate
```

## Installing the required libraries

```
pip install -r requirements.txt
```

## Get config.yaml
Ask Mark <@bearlikelion> for the latest config.yaml

## Run the bot

```
python bot.py
```