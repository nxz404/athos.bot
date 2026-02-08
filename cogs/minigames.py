import asyncio
import discord
from discord import app_commands
from discord.ext import commands
import random



class Minigames(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @app_commands.command(description='Deve ser cara ou coroa?')
    async def cara_coroa(self, int:discord.Interaction):
       
        await int.response.defer()
        await asyncio.sleep(4)
        await int.followup.send('Deve ser...')
        await asyncio.sleep(2)
        random.random()
        cara_coroa = ['Cara 🤡', 'Coroa 👑']
        get = random.choice(cara_coroa)
        await int.followup.send(f'{get}')
        
    @app_commands.command(name='8ball', description='Faça uma pergunta para o bot')
    async def _8ball(self, int:discord.Interaction, *, pergunta:str):
        resposta = ['Sim', 'Não', 'Talvez', 'Provavelmente', 'Claro que sim', 'Claro que não', 'Não sei', 'Não tenho certeza', 'Provavelmente não', 'Provavelmente sim', 'Não sei, mas acho que sim', 'Não sei, mas acho que não', 'Não sei, mas acho que talvez', 'Não sei, mas acho que provavelmente', 'Não sei, mas acho que provavelmente não', 'Não sei, mas acho que provavelmente sim']
        get = random.choice(resposta)
        await int.response.defer()
        await asyncio.sleep(4)
        await int.followup.send('🔮 Consultando os deuses...')
        await asyncio.sleep(2)
        await int.delete_original_response()
        await int.followup.send(f'**{int.user.display_name}** perguntou: **"{pergunta}"**\n🔮 E os deuses responderam: **{get}**')

    @app_commands.command(name='pedra_papel_tesoura', description='Jogue pedra, papel ou tesoura com o bot')
    @app_commands.choices(escolha=[app_commands.Choice(name='Pedra', value='pedra'), app_commands.Choice(name='Papel', value='papel'), app_commands.Choice(name='Tesoura', value='tesoura')])
    async def pedra_papel_tesoura(self, int:discord.Interaction, escolha:str):
        jogadas = ['pedra', 'papel', 'tesoura']
        get = random.choice(jogadas)
        await int.response.send_message("🤖 Pedra, papel ou tesoura?")
        
        if escolha == 'pedra' and get == 'tesoura':
            await int.followup.send('Você: **Pedra** x Bot: **Tesoura**')
            await asyncio.sleep(2)
            await int.followup.send('Você ganhou! 🎉')
        elif escolha == 'pedra' and get == 'papel':
            await int.followup.send('Você: **Pedra** x Bot: **Papel**')
            await asyncio.sleep(2)
            await int.followup.send('Você perdeu! 😢')
        elif escolha == 'pedra' and get == 'pedra':
            await int.followup.send('Você: **Pedra** x Bot: **Pedra**')
            await asyncio.sleep(2)
            await int.followup.send('Empate! 🤝')
        elif escolha == 'papel' and get == 'pedra':
            await int.followup.send('Você: **Papel** x Bot: **Pedra**')
            await asyncio.sleep(2)
            await int.followup.send('Você ganhou! 🎉')
        elif escolha == 'papel' and get == 'tesoura':
            await int.followup.send('Você: **Papel** x Bot: **Tesoura**')
            await asyncio.sleep(2)
            await int.followup.send('Você perdeu! 😢')
        elif escolha == 'papel' and get == 'papel':
            await int.followup.send('Você: **Papel** x Bot: **Papel**')
            await asyncio.sleep(2)
            await int.followup.send('Empate! 🤝')
        elif escolha == 'tesoura' and get == 'papel':
            await int.followup.send('Você: **Tesoura** x Bot: **Papel**')
            await asyncio.sleep(2)
            await int.followup.send('Você ganhou! 🎉')
        elif escolha == 'tesoura' and get == 'pedra':
            await int.followup.send('Você: **Tesoura** x Bot: **Pedra**')
            await asyncio.sleep(2)
            await int.followup.send('Você perdeu! 😢')
        elif escolha == 'tesoura' and get == 'tesoura':
            await int.followup.send('Você: **Tesoura** x Bot: **Tesoura**')
            await asyncio.sleep(2)
            await int.followup.send('Empate! 🤝')

        await int.delete_original_response()

async def setup(bot):
    await bot.add_cog(Minigames(bot))