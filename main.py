import discord
import os
from discord.ext import commands
from webserver import keepalive

client = commands.Bot(description = "GD Bot", command_prefix = "!")
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='GDLauncher'))
    print("#################\n# Bot is online #\n#################")
    print("Running as: " + client.user.name)
    print("Discord.py: " + discord.__version__)
    print("Created by Cranky Supertoon#7376")

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

@client.command()
async def faq(ctx):
  await ctx.send('https://github.com/gorilla-devs/GDLauncher/wiki/FAQ-Frequently-Asked-Questions')

@client.command(aliases=['logs'])
async def log(ctx):
  await ctx.send('To View your Log click **>_** near the Top Left of the Launcher and then go to console. If you are further having issues feel free to upload the log to a paste site.\nHeres a list of some paste sites:\n      - <https://gist.github.com/>\n      - <https://pastebin.com/>\n      - <https://hastebin.com/>\n      - <https://paste.feed-the-beast.com/>\n      - <https://paste.dimdev.org/>')

@client.command()
async def java(ctx):
  await ctx.send('**GDLauncher Requires a 64-bit version of Java 8.**\n\n**Windows:**\n<https://adoptopenjdk.net> Grab the `x64 JRE` with a `.msi` extension.\n\n**MacOS**\n<https://adoptopenjdk.net> Grab the `x64` bit `.pkg`\n\n**Arch Linux / Manjaro**\n`sudo pacman -S jre8-openjdk`  **or**  `yay -S jdk8-openjdk`\n\n**Debian / Ubuntu**\n`sudo apt-get install openjdk-8-jre`\n\n**RHEL / Fedora**\n`sudo dnf install java-1.8.0-openjdk`\n\n\nFor more info type `!javainfo`')



@client.command()
async def javainfo(ctx):
  await ctx.send('- **Java Virtual Machine (JVM)** - The core part that turns java code into native code for your specific operation system (OS).\n- **Java Runtime Enviroment (JRE)** - The part of Java that allows java applications to work. In turn it bundles the **JVM**\n- **Java Development Kit (JDK)** - The part of java that allows developers like Mojang to make Java based applications. Also includes the **JRE** and **JVM**\n\n**Java SE** is a closed source piece of software by **Oracle** that is different from the open source **OpenJDK** project. Either version works for **Minecraft**')

@client.event
async def on_member_join(member):
  channel = client.get_channel(423619991007657995)
  await channel.send(f"Hello {member.mention}, welcome to GorillaDevs, the home of GDLauncher")

@client.event
async def on_member_remove(member):
  channel = client.get_channel(423619991007657995)
  await channel.send(f"{member.mention} was blown up by a Creeper")

@client.command("info")
async def s_info(ctx):
    server = ctx.guild
    try:
        icon = server.icon_url_as(size=256)
    except Exception as e:
        icon = ("\uFEFF")
    embed = discord.Embed(title=f"Server info for {server.name}", description=None, colour=0x98FB98)
    embed.set_thumbnail(url=icon)
    # Basic info -- Name, Region, ID, Owner (USER+descrim, ID), Creation date, member count
    embed.add_field(name="Name", value=server.name, inline=False)
    embed.add_field(name="Region", value=server.region, inline=True)
    embed.add_field(name="ID", value=server.id, inline=True)
    embed.add_field(name="Owner", value=f"{server.owner.name}**-**{server.owner.id}", inline=True)
    embed.add_field(name="Creation Date", value=f"{server.created_at}", inline=True)
    embed.add_field(name="Server Icon Url", value=server.icon_url, inline=False)
    embed.add_field(name="Member Count", value=server.member_count, inline=True)
    await ctx.send(content=None, embed=embed)

@client.command()
async def help(ctx):
  author = ctx.message.author
  
  embed = discord.Embed(
  color = discord.Color.orange()
  )

  embed.set_author(name="Commands:")
  embed.add_field(name="General", value="!help - Shows This Message\n!ping - Says Pong Back To You", inline=False)
  embed.add_field(name="Debug", value="!java - Shows Download Links to Java\n!javainfo - Explains The Different Java Versions\n!log - Shows how to find GDLauncher Logs")
  await ctx.send(author, embed=embed)

@client.event
async def on_message(message):
  if message.channel.id == 692021271071948834 or message.channel.id == 692020276644282418:
    await message.add_reaction('👍')
    await message.add_reaction('👎')
  await client.process_commands(message)

keepalive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run(TOKEN)
