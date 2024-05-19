import discord
from discord.ext import commands

# Variables de entorno y configuracion
# Environment and configuration variables
bot_token = "YOUR_TOKEN_GOES_HERE" # string
# Welcome messages channel's ID / ID del canal para mensajes Welcome
welcome_id = 0 # integer
# Leave messages channel's ID / ID del canal de mensajes Leave
leave_id = 0 # integer
# Messages / Mensajes
# Welcome
welcome_msg = "Hola [member.mention], bienvenido a **[guild.name]**!"
# Leave
leave_msg = "**[member.name]** salio de **[guild.name]**"


# BOT CODE        CODIGO DEL BOT
# DON'T MODIFY    NO MODIFICAR
intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True
intents.typing = True
intents.presences = True
bot = commands.Bot(command_prefix='cscw!', intents=intents)

@bot.event
async def on_ready():
    print("CSCustomWelcomer v1.0.1\n\nReleased: 19/05/2024\n\nSource on https://github.com/deltagamesyt/cs-custom-welcomer")
    print(f"Cliente conectado: {bot.user.name}")
    print(f"Connected client: {bot.user.name}")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='member joins'))
@bot.event
async def on_member_join(member):
    server_name = member.guild.name
    if welcome_id:
        welcomer_channel = member.guild.get_channel(welcome_id)
        message = welcome_msg.replace("[member.mention]", member.mention)
        message = message.replace("[guild.name]", server_name)
        await welcomer_channel.send(message)
@bot.event
async def on_member_remove(member):
    server_name = member.guild.name
    if leave_id:
        leave_channel = member.guild.get_channel(leave_id)
        message = leave_msg.replace("[member.name]", member.name)
        message = message.replace("[guild.name]", server_name)
        await leave_channel.send(message)
@bot.command()
async def test(ctx):
    await ctx.send("I'm Working!\n¡Estoy funcionando!")
bot.run(bot_token)
