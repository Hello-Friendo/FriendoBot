# Creating a custom command

## Cogs

We seperate our commands into *Cogs* according to Pycord's guidelines. You can read more detail about Cogs on Pycord's [Guide](https://guide.pycord.dev/extensions/commands/cogs) and [Documentation](https://docs.pycord.dev/en/master/ext/commands/cogs.html).

# Creating a Cog

Create a new `.py` file in `/cogs` named after your command or functionality. A single cog file *can have* multiple commands. 

The file [cogs/hello.py](../cogs/hello.py) was created to be a boilerplate or template for creating your own custom commands. You can copy the file and rename it, or copy the contents and edit.

Cogs must contain the following code:

```python
from discord.ext import commands # Import Pycord commands

# Define a Class for our commands and functions
class Example(commands.Cog):
    def __init__(self, bot):
        pass 
    
    # Your code here

# Pycord's Cog loader calls the `setup(bot)` function when loaded
# This is to initalize a Cog and pass the bot object
# This must be OUTSIDE the class
def setup(bot):
    bot.add_cog(Example(bot))
```

# The Utility Classes

There are [utility classes](../utils/) that allow you to access the application config and logger in any Cog / sub-module. In order to use these classes they must be imported, then loaded in the `__init__` function.

### Example:

```python
import utils.log
import utils.config

class Example(commands.Cog):
    def __init__(self, bot):
        self.config = utils.config.load()
        self.log = utils.log.get()

    def do_something(self):
        self.config['secret_api_key']
        self.log.info('Oh, hi Mark!')
```

# Async / Await

Pycord is an ***asyncronous*** library. meaning that the system does not wait for an execution step to complete before moving on. In order to force Pycord to wait we create blockers using `await`, but `await` can only be called on *other asyncronous function*. 

Example:

```python
    async def log_hello(self, ctx):
        self.log.info(f"{ctx.author} said /hello!")

    # Create slash command for /hello
    @commands.slash_command(name="hello", description="Say Hello!")
    async def hello(self, ctx):        
        await self.log_hello(ctx)
        await ctx.respond(f"Hello {ctx.user.display_name}!")
```

In this example we are waiting to respond until the log file is written.

## Some reading on Async/Await | Blockers and Promises:

* [Discord.py - What is a coroutine](https://discordpy.readthedocs.io/en/async/faq.html#what-is-a-coroutine)
* [Real Python - Understanding Asynchronous Programming](https://realpython.com/python-async-features/#understanding-asynchronous-programming)
* [Discord.js - async-await.md](https://github.com/AnIdiotsGuide/discordjs-bot-guide/blob/master/other-guides/async-await.md)
* [Discord.js - Understanding async/await](https://discordjs.guide/additional-info/async-await.html#how-do-promises-work)
> The Discord.js concepts *do apply* to Pycord.py

# Performing REST Requests

Within Cogs you can perform REST requests using the [`AIOHTTP`](https://docs.aiohttp.org/en/stable/) library that comes with `pycord`.

Example:
```python
import aiohttp

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://python.org') as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html[:15], "...")
```

Prints:
```
Status: 200
Content-type: text/html; charset=utf-8
Body: <!doctype html> ...
```

You can see an example of this in [cogs/randomcat.py](../cogs/randomcat.py#L19)

For further details and examples view [AIOHTTP's](https://docs.aiohttp.org/en/stable/) documentation: https://docs.aiohttp.org/en/stable/

# Inspiration

> Scroll through and see if anything pops out at you, is so, **implement it!**
* ## [Github's list of public APIs](https://github.com/public-apis/public-apis)

> A good list of example commands already written
* ## [Pycord's Example Commands](https://github.com/Pycord-Development/pycord/tree/master/examples)

> Pycord's supported interactions
* ## [Pycord's Interactions Guide](https://guide.pycord.dev/interactions/)

> 42 Python Project Ideas for Beginners
* ## [Upgrad - Python Project Ideas](https://www.upgrad.com/blog/python-projects-ideas-topics-beginners/)

> Python Projects and Ideas
* ## [Hackr.io - Python Projects](https://hackr.io/blog/python-projects#beginner-level-python-project-ideas)