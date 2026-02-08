import discord
from discord.ext import commands
from discord import app_commands

class Roleplay(commands.Cog):
   def __init__(self, bot):
      self.bot = bot
      super().__init__()
   @app_commands.command(description="Dê um abraço em alguém")
   async def abraçar(self, inter: discord.Interaction, para: discord.Member):
      mbed = discord.Embed(title=f"{inter.user.display_name} abraçou {para.display_name}! <:athos_hug_roxo:1458449922671120414>",description='Um abraço com carinho e amizade!', color=0xBFE9EE)
      mbed.set_footer(text="Eles cresçem tão rápido...")
      mbed.set_image(url="https://i.imgur.com/tuH4gqZ.gif")
      await inter.response.send_message(embed=mbed)

   @app_commands.command(description="Dê um beijo em alguém")
   async def beijar(self, inter: discord.Interaction, para: discord.Member):
      mbed = discord.Embed(title=f"{inter.user.display_name} beijou {para.display_name}! <:athos_apaixonado_roxo:1458450208332583004>",description='Um beijo com muito carinho e amor!', color=0xBFE9EE)
      mbed.set_footer(text="Meu deus! Que atitude em...")
      mbed.set_image(url="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZWlpMnNyZDZ4aHM2dTIxc2pmcGRuMWxwMXBvejk1aXZkam9nb2RsYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/MQVpBqASxSlFu/giphy.gif")
      await inter.response.send_message(embed=mbed)

   @app_commands.command(description="Dê um soco em alguém")
   async def socar(self, inter: discord.Interaction, para: discord.Member):
      mbed = discord.Embed(title=f"{inter.user.display_name} socou {para.display_name}!",description='Um direto e depois um jab <:athos_com_medo:1458450213655023711>', color=0xBFE9EE)
      mbed.set_footer(text="SOCO SÉRIO, SUPER SÉRIO")
      mbed.set_image(url="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExdnF5Z3MyN2l2djZscWdydHRtajB0Ym1mOGRsdnYxZmFuYm0zN3dzOSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/oxbNORcXx76F2/giphy.gif")
      await inter.response.send_message(embed=mbed)

   @app_commands.command(description="Dê um tiro em alguém")
   async def atirar(self, inter: discord.Interaction, para: discord.Member):
      mbed = discord.Embed(title=f"{inter.user.display_name} atirou em {para.display_name}!",description='Um tiro na cabeça <:athos_com_medo:1458450213655023711>', color=0xBFE9EE)
      mbed.set_footer(text="BANG BANG 💥")
      mbed.set_image(url="https://i.imgur.com/1gN99rj.gif")
      await inter.response.send_message(embed=mbed)
      
async def setup(bot):
   await bot.add_cog(Roleplay(bot))