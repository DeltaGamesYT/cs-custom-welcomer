import discord
from discord.ext import commands

# Variables de entorno y configuracion
# Environment and configuration variables
bot_token = "YOUR_TOKEN_GOES_HERE" # string
# Welcome messages channel's ID / ID del canal para mensajes Welcome
welcome_id = 0 # integer
# Leave messages channel's ID / ID del canal de mensajes Leave
leave_id = 0 # integer
# Message Type / Tipo de Mensaje
mtype = "text" # string; <text:embed>
# Messages / Mensajes
# Welcome
welcome_msg = "Hola [member.mention], bienvenido a **[guild.name]**!"
# Leave
leave_msg = "**[member.name]** salio de **[guild.name]**"
# Embed configuration / Configuracion de embed
# Only modify if you are using embed mode / Solo modificar si estas usando el modo embed
# Embed Title / Titulo del Embed
embed_title = "[guild.name]"
# Embed Colour / Color del Embed
embed_color = "#4488ee" # String: Format #RRGGBB <HEX>


# BOT CODE        CODIGO DEL BOT
# DON'T MODIFY    NO MODIFICAR
intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True
intents.typing = True
intents.presences = True

if mtype.lower() == "embed":
    if len(embed_color) == 7:
        for char in embed_color:
            if char == "#":
                continue
            if not char.lower() in "0123456789abcdef":
                print("\n\nERROR: Invalid embed color: " + str(embed_color) + ". Use #rrggbb format.")
                exit()
    else:
        print("\n\nERROR: Invalid embed color: " + str(embed_color) + ". Use #rrggbb format.")
        exit()

bot = commands.Bot(command_prefix='cscw!', intents=intents)

@bot.event
async def on_ready():
    print("CSCustomWelcomer v1.2.0\n\nReleased: 20/05/2024\n\nSource on https://github.com/deltagamesyt/cs-custom-welcomer")
    print(f"Cliente conectado: {bot.user.name}")
    print(f"Connected client: {bot.user.name}")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='member joins'))
@bot.event
async def on_member_join(member):
    server_name = member.guild.name
    if welcome_id and mtype.lower() == "text":
        welcomer_channel = member.guild.get_channel(welcome_id)
        message = welcome_msg.replace("[member.mention]", member.mention)
        message = message.replace("[guild.name]", server_name)
        await welcomer_channel.send(message)
    elif welcome_id and mtype.lower() == "embed":
        welcomer_channel = member.guild.get_channel(welcome_id)
        message = welcome_msg.replace("[member.mention]", member.mention)
        message = message.replace("[guild.name]", server_name)
        title = embed_title.replace("[guild.name]", server_name)
        embed = discord.Embed(title=title, color=discord.Colour.from_str(embed_color), description=message)
        await welcomer_channel.send(embed=embed)
@bot.event
async def on_member_remove(member):
    server_name = member.guild.name
    if leave_id and mtype.lower() == "text":
        leave_channel = member.guild.get_channel(leave_id)
        message = leave_msg.replace("[member.name]", member.name)
        message = message.replace("[guild.name]", server_name)
        await leave_channel.send(message)
    elif welcome_id and mtype.lower() == "embed":
        leave_channel = member.guild.get_channel(welcome_id)
        message = leave_msg.replace("[member.name]", member.name)
        message = message.replace("[guild.name]", server_name)
        title = embed_title.replace("[guild.name]", server_name)
        embed = discord.Embed(title=title, color=discord.Colour.from_str(embed_color), description=message)
        await leave_channel.send(embed=embed)
@bot.command()
async def test(ctx):
    await ctx.send("I'm Working!\n¡Estoy funcionando!")
bot.run(bot_token)
