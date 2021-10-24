import discord 
from discord.ext import commands #modül

#komuta özel prefix isteyen silebilir
intents = discord.Intents().all()
Client= commands.Bot(command_prefix="$", intents=intents)

@Client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name='Rol İsmi') #burayı siz verilecek rolün ismini yazın
    await member.add_roles(role)

client.run('token')
