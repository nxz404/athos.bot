import discord
from discord import ActivityType, Color, Interaction, activity, app_commands
from discord.ext import commands, tasks
from datetime import time
import random
import os
from dotenv import load_dotenv
import asyncio
from discord import SelectOption
from discord.ui import View, button, label, view

intents = discord.Intents.all()



class Bot_modificado(commands.Bot):

    def __init__(self):
        super().__init__(command_prefix='>', intents=discord.Intents.all())

    async def setup_hook(self):
        self.add_view(ultimo_passo())
        self.add_view(req())
        self.add_view(botaoRequisitos(msg_para_apagar=None, msg=None))
      
        


bot = Bot_modificado()


async def carregar_cogs():
    for arquivos in os.listdir('cogs'):
        if arquivos.endswith('.py'):
            await bot.load_extension(f'cogs.{arquivos[:-3]}')
            print(f'cogs.{arquivos[:-3]} carregada com sucesso!')

load_dotenv()
bot_token=os.getenv("DISCORD_TOKEN")


staff = 1427025826913849516
elite_staff = 1432055249102835712
geral = 1427014910134456421
divulgação = 1427036601799934072
ping_d = 1427403610425397338

#evento


import discord
from discord.ext import commands, tasks
import asyncio

# Certifique-se de que seu bot e intents estejam definidos corretamente fora deste snippet
# Exemplo: bot = commands.Bot(command_prefix='m!', intents=discord.Intents.default())

# --- Lista de Links para o Status ---
# Você pode gerenciar esta lista aqui
music_links = [
    "https://www.youtube.com/watch?v=xXQNdUpCQzw&list=RDxXQNdUpCQzw&start_radio=1",
    "https://www.youtube.com/watch?v=osPq9Yb8xm8&list=RDosPq9Yb8xm8&start_radio=1",
    "https://www.youtube.com/watch?v=56ZT2e2-VMA&list=RD56ZT2e2-VMA&start_radio=1",
    "https://www.youtube.com/watch?v=pcJnSmv4u4I&list=RDpcJnSmv4u4I&start_radio=1",
    "https://www.youtube.com/watch?v=qvSPt6a2wTQ&list=RDqvSPt6a2wTQ&start_radio=1",
    "https://www.youtube.com/watch?v=k3qsXGT5kjs&list=RDk3qsXGT5kjs&start_radio=1",
    "https://www.youtube.com/watch?v=nHn6bQE0vzE&list=RDnHn6bQE0vzE&start_radio=1",
    "https://www.youtube.com/watch?v=pjiKGrLbTE8&list=RDpjiKGrLbTE8&start_radio=1"
]

current_url_index = 0
@tasks.loop(minutes=5.0) 
async def change_status():
    global current_url_index
    url = music_links[current_url_index]
    activity = discord.Streaming(
        name="https://dcd.gg/neo-exe | /ajuda", 
        url=url
    )
    await bot.change_presence(activity=activity)
    
    current_url_index = (current_url_index + 1) % len(music_links)

@bot.event
async def on_ready():
    await carregar_cogs()
    sincs = await bot.tree.sync()
    
    if not change_status.is_running():
        change_status.start()
        
    
    print(f"{len(sincs)} comandos sincronizados com sucesso :D!")
    botc = len(bot.all_commands) + len(sincs)
    print(f"Há exatamente {botc} comandos no bot!")
    print("Liguei :D")



    

@bot.event
async def on_message(message):
    # Ignore messages from the bot itself to prevent infinite loops
    if message.author == bot.user:
        return

    # Check if the bot is mentioned in the message
    if message.content.lower() == "<@1429564793462984775>":
        await message.reply(f"<:athos_feliz_roxo:1458450205979447419> Eai {message.author.mention}, como vai?\nEu vou bem, sou **𝗮𝘁𝗵𝗼𝘀ᵇᵒᵗ**! Um bot de **moderação**, **roleplay** e **minigames**! Meus comandos são híbridos **(/ e >)**\n\n💫 Para ver **tudo** o que posso fazer **acesse** `/ajuda` <:athos_apaixonado_roxo:1458450208332583004>!")
          


    # Process commands after checking for mentions
    await bot.process_commands(message)
    
@bot.hybrid_command(name='ping', description='Mostra a latência do bot')
async def ping(inter):
    await inter.send(f"Pong! {round(bot.latency * 1000)}ms")


@bot.event
async def on_member_join(membro: discord.Member):
    guild = membro.guild
    canal = discord.utils.get(guild.channels, id=1427010608171188254)
    embed = discord.Embed(title=f'{membro.display_name} | Bem-vindo(a)!',
                          color=0xF3EAFB)
    embed.add_field(
        name='👋 Sabia que...',
        value=f'Temos aproximadamente {len(guild.members)} membros no servidor.'
    )
    embed.add_field(name='🛡️ Tag do Usuário',
                    value=f'`@{membro.name} `({membro.id})')
    embed.add_field(
        name=':name_badge: Prescisa de ajuda?',
        value='Consulte o <#1427011975992446990> e chame nossa equipe')
    embed.add_field(
        name=':police_officer: Evite punições!',
        value=
        'Leia as regras em <#1427010728505639144> para evitar ser punido no servidor!',
        inline=True)
    embed.set_image(url='https://i.imgur.com/TD3eucD.gif')
    embed.set_footer(text=f'{guild.name} • © Todos os direitos reservados')
    embed.set_thumbnail(url=membro.avatar)
    await canal.send(f'{membro.mention}')
    await canal.send(embed=embed)


@bot.event
async def on_member_remove(membro: discord.Member): # O nome aqui é 'membro'
    canal_saida = bot.get_channel(1427767372810424370)
    
    # Embed de saída padrão
    saida = discord.Embed(
        title='😭 #chateado!',
        description=f'⚰ {membro.display_name} saiu do servidor',
        color=0xF3EAFB)
    saida.set_image(url='https://i.imgur.com/h8yiU9r.gif')
    saida.set_footer(text=f'ID do usuário: {membro.id}')
    saida.set_thumbnail(url=membro.avatar)
    saida.set_author(name=f'{membro.display_name}',
                     icon_url=membro.display_avatar.url)
    
    if canal_saida:
        await canal_saida.send(embed=saida)

    # Lógica de remoção de parceria
    ID_CANAL_PARCERIAS = 1427015334912593920 
    canal_parcerias = bot.get_channel(ID_CANAL_PARCERIAS)
    
    if canal_parcerias:
        async for message in canal_parcerias.history(limit=100):
            # Alterado de 'member' para 'membro'
            if message.author == bot.user and str(membro.id) in message.content:
                try:
                    await message.delete()
                    
                    log_embed = discord.Embed(description=f"""
                    ## <:assustado:1465073211762016520> Parceria Encerrada!
                    Parceria com __**{membro.name}**__ foi encerrada porque ele(a) saiu do servidor!
                    """, color=0xEEE1EE)
                    log_embed.set_footer(text="neo.exe • © Todos os direitos reservados")
                    log_embed.set_image(url="https://i.imgur.com/h8yiU9r.gif")
                    
                    canal_log = bot.get_channel(1465075114335797451)
                    if canal_log:
                        await canal_log.send(embed=log_embed)
                except Exception as e:
                    print(f"Erro ao apagar mensagem ou enviar log: {e}")



@bot.command()
async def teste(ctx: commands.Context):
    await ctx.reply("🥺😳 Calma bebê, o bot está funcionando :D!")


@bot.tree.command(description='Escolha convites para divulgação')
@app_commands.describe(
    selecionar_convite="Escolha um dos assuntos para a divulgação")
@app_commands.choices(selecionar_convite=[
    app_commands.Choice(name="neo.exe #200", value=1),
    app_commands.Choice(name="💯 neo.exe bateu a meta!", value=2),
    app_commands.Choice(name="Comunidade + Brawl Stars", value=3),
    app_commands.Choice(name="Comunidade", value=4),
    app_commands.Choice(name="Brawl Stars", value=5)
])
async def invite(inter: discord.Interaction, selecionar_convite: int):
    if selecionar_convite == 1:
      content = """
# :computer: *n̷e̷o̷.̷e̷x̷e̷ | #200*

Esquece servidor triste. Superamos os **100 membros** porque aqui a ideia é outra. 
Se não tá na **neo.exe**, tá jogando tempo fora.

## **POR QUE AQUI É** [**__ELITE?__**](https://cdn.discordapp.com/attachments/1426990937137086556/1457460882157338786/13.png?ex=695c15b8&is=695ac438&hm=7f1ae550baa3176b3afee7984f043af8fd3114d63c54f3a26eb7ee8439252fa9&)

> :fire: **Resenha Pura:** Chat que não dorme. Zero panelinha.
> :joystick: **Gameplays:** Roblox, Minecraft e outros jogos.
> :robot: **Sistema de Bots:** Athos.exe, Mudae, Gartic, Akinator e Loritta.
> :shield: **Staff Ativa:** Sem ADM de enfeite. A gente joga e resolve.
> :handshake: **Parcerias:** Portas abertas para crescer.

**100 membros foi o teste. O próximo nível é agora.**

:point_right: [__**Vem pra família:**__](https://discord.gg/bD3dND9FKv)  
[*Feito por players para players - **neo.exe***](https://cdn.discordapp.com/attachments/1427009152160632872/1464338014540005506/10c08da8876a9cc509e3ea2394a7256e-Picsart-BackgroundRemover-ezgif.com-effects_1.gif?ex=69751a8c&is=6973c90c&hm=6735c9a72c8a908582e36db51650eeeb505f5df95acdaa6afa0e9e14ad6b7992)
      """
      await inter.response.send_message(content=content)
      await inter.followup.send(
          'Para copiar o texto, clique com o botão direito e selecione copiar texto(ou pressione a mensagem). Como na imagem abaixo: [exemplo](https://media.discordapp.net/attachments/1429516787694702614/1439047112146026586/image.png?ex=6919188f&is=6917c70f&hm=017903536de07151a22248ca72f26960abd887b1588826ef1bd5773d6816f9e8&=&format=webp&quality=lossless&width=448&height=43)',
          ephemeral=True)
      return
  
    elif selecionar_convite == 1:
        content = "💻 Neo.exe — **100 membros**. Zero tédio.\n\nNão é mais promessa, é realidade.\nBatemos **100 membros** e seguimos crescendo com gente ativa,\nresenha boa e gameplay todo dia 🚀\n\nAqui não tem servidor morto nem panelinha estranha.\nÉ **comunidade de verdade**.\n\n🎮 **O que rola por aqui:**\n> 🔥 Galera ativa\n> 🕹️ Roblox • Minecraft • Brawl Stars (**clube próprio**)\n> 🤖 **athosᵇᵒᵗ** + Gartic, Mudae, Akinator, Lord e Lorrita\n> 🛠️ Staff presente\n> 💬 Chat pra trocar ideia, rir e jogar\n> 🤝 Parcerias abertas\n\n💯 **100 membros** foi só o começo.\nO próximo nível é agora.\n\n👉 [Entra e vem fazer parte da família:](https://discord.gg/bD3dND9FKv)\n[banner](https://cdn.discordapp.com/attachments/1426990937137086556/1457460882157338786/13.png?ex=695c15b8&is=695ac438&hm=7f1ae550baa3176b3afee7984f043af8fd3114d63c54f3a26eb7ee8439252fa9&)"
        await inter.response.send_message(content=content)
        await inter.followup.send(
            'Para copiar o texto, clique com o botão direito e selecione copiar texto(ou pressione a mensagem). Como na imagem abaixo: [exemplo](https://media.discordapp.net/attachments/1429516787694702614/1439047112146026586/image.png?ex=6919188f&is=6917c70f&hm=017903536de07151a22248ca72f26960abd887b1588826ef1bd5773d6816f9e8&=&format=webp&quality=lossless&width=448&height=43)',
            ephemeral=True)
        return
    elif selecionar_convite == 2:

        content = "**💻 Neo.exe — Conecte-se. Jogue. Divirta-se!**\n   \nProcurando um servidor pra relaxar, fazer amigos e jogar? 👀\nA Neo.exe é o lugar certo! Aqui o clima é leve, o papo é solto e a diversão nunca para 😄\n   \n🎮 **O que te espera por aqui:**\n✨ Comunidade ativa e acolhedora\n🕹️ Jogos como **Roblox**, **Minecraft** e **Brawl Stars** (com **clube próprio**!)\n🤖 Nosso bot oficial, **𝗮𝘁𝗵𝗼𝘀ᵇᵒᵗ**, além de outros bots incríveis como **Gartic**, **Mudae**, **Akinator**, **Lord** e **Lorrita**\n🛠️ Staff **presente** e sempre pronta pra ajudar\n💬 Espaços pra conversar, brincar e conhecer gente nova\n🤝 Parceria **ON!**\n   \n🚀 O servidor tá crescendo e precisa de pessoas como você pra deixar tudo ainda mais animado!\n   \n👉 Entra aí e vem fazer parte da família **Neo.exe**!\n🔗 [clique e vem fazer parte](https://discord.gg/bD3dND9FKv)\n[banner](https://cdn.discordapp.com/attachments/1426990937137086556/1457460882157338786/13.png?ex=695c15b8&is=695ac438&hm=7f1ae550baa3176b3afee7984f043af8fd3114d63c54f3a26eb7ee8439252fa9&)"
        await inter.response.send_message(content=content)
        await inter.followup.send(
            'Para copiar o texto, clique com o botão direito e selecione copiar texto(ou pressione a mensagem). Como na imagem abaixo: [exemplo](https://media.discordapp.net/attachments/1429516787694702614/1439047112146026586/image.png?ex=6919188f&is=6917c70f&hm=017903536de07151a22248ca72f26960abd887b1588826ef1bd5773d6816f9e8&=&format=webp&quality=lossless&width=448&height=43)',
            ephemeral=True)
        return
    elif selecionar_convite == 3:
        content = "**💫 Um lugar pra jogar, rir e fazer parte de algo real**\nㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ\nNem todo servidor é igual — e o nosso prova isso. Aqui, a gente valoriza o clima de comunidade, as amizades que nascem no chat e as partidas que viram história. O clube é um ponto de encontro pra quem curte games, conversas e boas energias.\nㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ\n🎮 O que rola por aqui:\n• Jogos de todos os estilos — do competitivo ao casual\n• Gente divertida, respeitosa e ativa\n• Eventos, squads e muito papo bom\n• Uma comunidade que cresce junta, todo dia\nㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ\n🌟 Se você tá cansado de servidores vazios e frios, vem pra um lugar onde você realmente faz parte da equipe.\nㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ\n**🚀 Vem fazer parte da família:**\n👉 https://discord.gg/bD3dND9FKv"
        await inter.response.send_message(content=content)
        await inter.followup.send(
            'Para copiar o texto, clique com o botão direito e selecione copiar texto(ou pressione a mensagem). Como na imagem abaixo: [exemplo](https://media.discordapp.net/attachments/1429516787694702614/1439047112146026586/image.png?ex=6919188f&is=6917c70f&hm=017903536de07151a22248ca72f26960abd887b1588826ef1bd5773d6816f9e8&=&format=webp&quality=lossless&width=448&height=43)',
            ephemeral=True)
        return
    elif selecionar_convite == 4:
        content = "**💻 ⚡ NEO.EXE — O FUTURO DO BRAWL STARS COMEÇOU! ⚡!**\nㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ\n👾 Bem-vindo à Neo.exe, o clube de Brawl Stars mais estiloso e caótico do Discord!\nAqui a gente não só joga — a gente evolui o sistema.\nㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ\n🚀 O que te espera dentro da Neo.exe:\nㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ\n💥 Times organizados pra empurrar troféus e dominar partidas\nㅤㅤㅤㅤㅤㅤㅤㅤㅤ\n🧠 Estratégias insanas pra cada modo e personagem\nㅤㅤㅤㅤㅤㅤㅤㅤㅤ\n🏆 Eventos e mini-torneios com destaque pra quem joga bem\nㅤㅤㅤㅤㅤㅤㅤㅤㅤ\n🎧 Chats, memes, bots e música pra manter o flow ligado\nㅤㅤㅤㅤㅤㅤㅤㅤㅤ\n💬 Uma comunidade ativa e unida, onde todo mundo tem espaço\nㅤㅤㅤㅤㅤㅤㅤㅤㅤ\n**⚡ Está pronto pra entrar no código?**\n**Conecte-se agora à Neo.exe.**\n👉 https://discord.gg/bD3dND9FKv"
        await inter.response.send_message(content=content)
        await inter.followup.send(
            'Para copiar o texto, clique com o botão direito e selecione copiar texto(ou pressione a mensagem). Como na imagem abaixo: [exemplo](https://media.discordapp.net/attachments/1429516787694702614/1439047112146026586/image.png?ex=6919188f&is=6917c70f&hm=017903536de07151a22248ca72f26960abd887b1588826ef1bd5773d6816f9e8&=&format=webp&quality=lossless&width=448&height=43)',
            ephemeral=True)
        return


@commands.has_role(staff)
@bot.tree.command(
    description="Faça um anúncio em diferentes canais rapidamente.")
async def anunciar(inter: discord.Interaction, texto: str, *, canal: discord.TextChannel, pings:discord.Role, pings2:discord.Role, pings3:discord.Role):
    canal = bot.get_channel(canal.id)
    await canal.send(f"**ANÚNCIO** \n{texto}\n \n`Anúncio feito por: {inter.user.name}`\nPings: {pings.mention}{pings2.mention}{pings3.mention}")
    await inter.response.send_message(
        f"Anúncio feito com sucesso, no canal {canal.mention}!",
        ephemeral=True)


@bot.tree.command(name="limpar", description="Deleta mensagens do chat")
@app_commands.describe(
    amount="Número de mensagens para analisar",
    usuario="Usuário específico para apagar as mensagens"
)
@commands.has_permissions(manage_messages=True)
async def limpar(
    interaction: discord.Interaction,
    amount: app_commands.Range[int, 1, 1000], # Reduzi para 100 por segurança, mas pode manter 1000
    usuario: discord.Member = None # Parâmetro opcional
):
    await interaction.response.defer(ephemeral=True)

    # Função de verificação
    def check_mensagens(msg):
        if usuario:
            # Só retorna True se o autor da mensagem for o usuário escolhido
            return msg.author.id == usuario.id
        return True # Se não passar usuário, apaga tudo

    # O purge vai percorrer as mensagens e aplicar o filtro 'check'
    deleted = await interaction.channel.purge(limit=amount, check=check_mensagens)
    
    quantidade_deletada = len(deleted)
    
    if usuario:
        msg_final = f"Limpei {quantidade_deletada} mensagens de **{usuario.display_name}**."
    else:
        msg_final = f"Limpei {quantidade_deletada} mensagens do chat."

    await interaction.followup.send(msg_final, ephemeral=True)


@bot.tree.command(description="Crie embeds de forma fácil e prática")
async def criar_embed(inter: discord.Interaction, title: str, description: str,
                      link: str, cor: str, canal: discord.TextChannel):
    canal = bot.get_channel(canal.id)
    mbed = discord.Embed(title=f'{title}',
                         description=f'{description}',
                         color=discord.Colour.from_str(f'{cor}'))
    mbed.set_image(url=f'{link}')
    mbed.set_footer(text=f'{inter.user.name}',
                    icon_url=inter.user.display_avatar.url)
    await inter.response.send_message(
        f"Embed criada com sucesso no canal {canal.mention}!", ephemeral=True)
    await canal.send(embed=mbed)


@bot.hybrid_command(name='ajuda',
                    description='Mostra tudo o que o bot pode fazer <3')
async def ajuda(ctx):
    botc = len(bot.all_commands) + len(await bot.tree.sync())
    comandos = discord.Embed(
        title="🌠 **Painel de comandos - 𝗮𝘁𝗵𝗼𝘀ᵇᵒᵗ**",
        description=
        f"<:athos_sla_roxo:1458450211679768691> Opa tudo bem? Eu sou o **𝗮𝘁𝗵𝗼𝘀ᵇᵒᵗ** seu bot de **jogos**,\n **rp** e **mod**!\n  \nSelecione uma das opções abaixo para descobrir tudo \nque posso fazer <:athos_feliz_roxo:1458450205979447419>\n     \n**📈 Todos os comandos: ``{botc}``**\n**📝 Criado por: <@1259110474142978058>**",
        color=0xBFE9EE)
    comandos.set_footer(text="neo.exe • © Todos os direitos reservados")
    comandos.set_thumbnail(url=bot.user.display_avatar)
    await ctx.send(embed=comandos, view=Dropdown())

class Dropdown(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    
        
    categorias = [
        SelectOption(label="Moderação", description="Comandos de moderação", emoji="🛡️", value="1"),
        SelectOption(label="Roleplay", description="Comandos de roleplay", emoji="💬", value="2"),
        SelectOption(label="Jogos", description="Comandos de jogos", emoji="🎮", value="3"),
        SelectOption(label="Outros", description="Comandos sem categoria", emoji="📌", value="4")
    ]
    @discord.ui.select(placeholder="Selecione uma categoria", options=categorias, custom_id="cat")
    async def cat(self, interaction: discord.Interaction, select: discord.ui.Select):
        if select.values[0] == "1":
            modbd = discord.Embed(title="🛡️ Moderação - Painel de comandos", description="*Comandos de* ***Moderação***\n``• /ban:`` **Bana membros do servidor**\n``• /desbanir:`` **Desbana membros do servidor**\n``• /silenciar:`` **Silencie membros do servidor**\n``• /kick:`` **Expulse membros do servidor**\n``• /avaliar_staff:`` **Avalie staff's após um atendimento**\n*Fique atento as próximas atualizações*", color=0xBFE9EE)
            modbd.set_footer(text="neo.exe • © Todos os direitos reservados")
            await interaction.response.edit_message(embed=modbd, view=DropdownView())
        elif select.values[0] == "2":
            roleplaybd = discord.Embed(title="💬 Roleplay - Painel de comandos", description="*Comandos de* ***Roleplay***\n``• /abraçar:`` **Abraçe um membro**\n``• /beijar:`` **Beije um membro**\n``• /socar:`` **Soque um membro**\n``• /atirar:`` **Atire em um membro**\n*Fique atento as próximas atualizações*", color=0xBFE9EE)
            roleplaybd.set_footer(text="neo.exe • © Todos os direitos reservados")
            await interaction.response.edit_message(embed=roleplaybd, view=DropdownView())

        elif select.values[0] == "3":
            jogosbd = discord.Embed(title="🎮 Jogos - Painel de comandos", description="*Comandos de* ***Jogos***\n``• /pedrapapeltesoura:`` **Jogue pedra papel e tesoura com o bot**\n``• /caraoucoroa:`` **Jogue cara ou coroa com o bot**\n``• /8ball:`` **Veja seu futuro por meio de uma pergunta**\n*Fique atento as próximas atualizações*", color=0xBFE9EE)
            jogosbd.set_footer(text="neo.exe • © Todos os direitos reservados")
            await interaction.response.edit_message(embed=jogosbd, view=DropdownView())
            

        if select.values[0] == "4":
            outrosbd = discord.Embed(title="📌 Outros - Painel de comandos", description="*Comandos sem* ***categoria***\n``• /invite:`` **Mostra convites para divulgação**\n``• /comandos_bot:`` **Mostra todos os comandos do bot**\n``• /anunciar:`` **Faça um anúncio em diferentes canais rapidamente**\n``• /limpar:`` **Deleta um número específico de mensagens**\n``• /criar_embed:`` **Crie embeds de forma fácil e prática**\n``• /ping:`` **Mostra o meu ping**\n``• /teste:`` **Me teste :D**\n``• /ajuda:`` **Mostra todos os comandos do bot**\n*Fique atento as próximas atualizações*", color=0xBFE9EE)
            outrosbd.set_footer(text="neo.exe • © Todos os direitos reservados")
            await interaction.response.edit_message(embed=outrosbd, view=DropdownView())

    @discord.ui.button(label="❌ Fechar", style=discord.ButtonStyle.red)
    async def button_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
            await interaction.response.edit_message(content="Painel fechado com sucesso!", view=None)
            await interaction.delete_original_response()

    

            

            

class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="❌ Fechar", style=discord.ButtonStyle.red, custom_id="fechar")
    async def fechar(self, interaction: discord.Interaction, button: discord.ui.Button):
        
        comando1s = "Painel de comandos fechado com sucesso!"
        
        await interaction.response.edit_message(content=comando1s, view=None)
        await interaction.delete_original_response()
    @discord.ui.button(label="🔄 Voltar", style=discord.ButtonStyle.blurple, custom_id="voltar")
    async def voltar(self, interaction: discord.Interaction, button: discord.ui.Button):
        comandos = discord.Embed(
        title="🌠 **Painel de comandos - 𝗮𝘁𝗵𝗼𝘀ᵇᵒᵗ**",
        description=
        f"<:athos_sla:1437243306839900180> Opa tudo bem? Eu sou o **𝗮𝘁𝗵𝗼𝘀ᵇᵒᵗ** seu bot de **jogos**,\n **rp** e **mod**!\n  \nSelecione uma das opções abaixo para descobrir tudo \nque posso fazer <:athos_happy:1437242575705604127>\n     \n**📈 Todos os comandos: ``{len(bot.all_commands)}``**\n**📝 Criado por: <@1259110474142978058>**",
        color=0xBFE9EE)
        comandos.set_footer(text="neo.exe • © Todos os direitos reservados")
        comandos.set_thumbnail(url=bot.user.display_avatar)
        await interaction.response.edit_message(embed=comandos, view=Dropdown())    

    


class ultimo_passo(discord.ui.View):

    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='Clica em mim!',
                       style=discord.ButtonStyle.primary,
                       custom_id='botao')
    async def botao(self, inter: discord.Interaction,
                    button: discord.ui.Button):
        cargo = inter.guild.get_role(1428364808616677427)
        cargo2 = inter.guild.get_role(1427020441981157456)
        await inter.user.remove_roles(cargo)
        await inter.user.add_roles(cargo2)
        await inter.response.send_message(
            'Você liberou o servidor com sucesso, e recebeu o cargo <@&1427020441981157456>!',
            ephemeral=True)


@commands.has_role(staff)
@bot.tree.command(description='Botão de registrar')
async def registro(inter: discord.Interaction, canal: discord.TextChannel):
    chat = bot.get_channel(canal.id)
    await chat.send('Clique no botão para liberar o servidor',
                    view=ultimo_passo())
    await inter.response.send_message('Botão enviado com sucesso!',
                                      ephemeral=True)


class botaoRequisitos(discord.ui.View):
    def __init__(self, msg_para_apagar, msg):
        super().__init__(timeout=None)
        self.msg_para_apagar = msg_para_apagar
        self.msg = msg
    try:
        @discord.ui.button(label="Ver requisitos", style=discord.ButtonStyle.gray, emoji="<:confuso:1465073216958759238>", custom_id="requisitos")
        async def requisitos(self, interaction: discord.Interaction, button: discord.ui.Button):
            req_embed = discord.Embed(
                title="""
                Requisitos da Parceria
                """,
                description=f"""
                __A parceria firmada com **{interaction.user.name}** atendeu aos seguintes requisitos:__

                • Ter no minímo **30 membros**
                • Ter uma staff **ativa**
                • Ter um servidor **ativo** e com regras **claras**
                • Ter um **representante no servidor** da neo.exe
                • **Ajudar** no engajamento do servidor
                """
            )
            req_embed.set_footer(text="neo.exe • © Todos os direitos reservados")
            req_embed.set_image(url="https://i.imgur.com/Y7Y3JUF.gif")
            await interaction.response.send_message(embed=req_embed, ephemeral=True)
        @discord.ui.button(label="Cancelar parceria", style=discord.ButtonStyle.gray, emoji="<:tchau:1465073213770825822>", custom_id="cancelar")
        async def cancelar(self, interaction: discord.Interaction, button: discord.ui.Button):
            try:
                await self.msg_para_apagar.delete()
                no_embed = discord.Embed(description=f"""
        ## <:assustado:1465007835174932490> Parceria Encerrada!
        Olá **{interaction.user.name}**! 
        Informamos que a parceria foi encerrada em comum acordo. Agradecemos pelo tempo de colaboração e desejamos sucesso nos próximos projetos.
        """, color=0xEEE1EE)
                no_embed.set_footer(text="neo.exe • © Todos os direitos reservados")
                no_embed.set_image(url="https://i.imgur.com/h8yiU9r.gif")
                await interaction.response.send_message(embed=no_embed, ephemeral=True)
                no_embed_global = discord.Embed(description=f"""
        ## <:assustado:1465007835174932490> Parceria Encerrada!
        Parceria com __**{interaction.user.name}**__ foi encerrada por escolha própia!
        """, color=0xEEE1EE)
                no_embed_global.set_footer(text="neo.exe • © Todos os direitos reservados")
                no_embed_global.set_image(url="https://i.imgur.com/h8yiU9r.gif")
                canal = bot.get_channel(1465075114335797451)
                await canal.send(embed=no_embed_global)
                
                
            except:
                await interaction.response.send_message("<:confuso:1465073216958759238> Vish... ao que parece, a parceria já foi terminada ou a mensagem não pode ser apagada!", ephemeral=True)
            
        @discord.ui.button(label="Visualizar Texto", style=discord.ButtonStyle.gray, emoji="<:animado:1465073228618793175>", custom_id="texto")
        async def texto(self, interaction: discord.Interaction, button: discord.ui.Button):
            if self.msg is None:
                await interaction.response.send_message("<:confuso:1465073216958759238> Vish... ao que parece, o texto é muito antigo ou foi apagado!",ephemeral = True)
                return
            selfmsgembed = discord.Embed(description=self.msg, color=0xEEE1EE)
            await interaction.response.send_message(embed=selfmsgembed, content = "-# Mensagem enviada no servidor", ephemeral=True)
    except:
        ctx.send("Um erro desconhecido ocorreu!")
            

class Parceria_Modal(discord.ui.Modal):
    def __init__(self):
        super().__init__(title='Painel de Divulgação')

    parceria = discord.ui.TextInput(
        label='Texto + link',
        placeholder='Digite o texto da divulgação com o link do servidor',
        style=discord.TextStyle.paragraph,
        required=True)
    representante = discord.ui.TextInput(
            label= 'Representante',
            placeholder='Nome de usuário do membro ou o ID de quem está realizando a parceria',
            style=discord.TextStyle.short,
            required=True)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        # 1. Pegar o canal
        canal = bot.get_channel(1427015334912593920)
        if not canal:
            await interaction.followup.send("Canal não encontrado!", ephemeral=True)
            return

        # 2. Buscar o membro
        input_rep = self.representante.value.strip()
        membro = None

        try:
            if input_rep.isdigit():
                # fetch_member busca na API do Discord, mais garantido que get_member
                membro = await interaction.guild.fetch_member(int(input_rep))
            else:
                membro = discord.utils.get(interaction.guild.members, name=input_rep)
        except discord.NotFound:
            membro = None

        # --- VALIDAÇÃO CRÍTICA ---
        if membro is None:
            return await interaction.followup.send(
                f"<:assustado:1465007835174932490> Não consegui encontrar o membro `{input_rep}`. Verifique o ID ou Nome e tente novamente.", 
                ephemeral=True
            )

        # 3. Dar o cargo
        divulgador = interaction.guild.get_role(1427036601799934072)
        if divulgador:
            try:
                await membro.add_roles(divulgador)
            except discord.Forbidden:
                await interaction.followup.send("Bot sem permissão para dar cargo.")
        conteudo_parceria = (
            f'{self.parceria.value}\n\n'
            f'> Representante: {membro.mention}\n'
            f'> <@&1427403610425397338>\n'
            f'> -# ``Divulgação feita por: {interaction.user.display_name}``'
        )
        ola_log_embed = discord.Embed(description=f"""
        ## <:oi:1465073219751903537> Nova Parceria!
        Parceria firmada com **{membro.name}**! 
        Ficamos muito felizes em firmar essa parceria e esperamos que ela traga crescimento, união e bons resultados para ambas as comunidades.
        """, color=0xEEE1EE)
        ola_log_embed_v2 = discord.Embed(description=f"""
        ## <:animado:1465073228618793175> Nova Parceria!
        Parceria firmada com **{membro.name}**!
        Ficamos muito felizes em firmar essa parceria e esperamos que ela traga crescimento, união e bons resultados para ambas as comunidades.
        """, color=0xEEE1EE)
        lista_log_msgs = [ola_log_embed, ola_log_embed_v2]
        msgs_log = random.choice(lista_log_msgs)
        canal_log = bot.get_channel(1465075114335797451)
        await canal_log.send(embed=msgs_log)
        try:
          proxima_msg = await canal.send(conteudo_parceria)
          ola_embed = discord.Embed(description=f"""
          ## <:oi:1465073219751903537> Nova Parceria!
          Olá **{membro.name}**! 
          Ficamos muito felizes em firmar essa parceria e esperamos que ela traga crescimento, união e bons resultados para ambas as comunidades.
          """, color=0xEEE1EE)
          ola_embed_v2 = discord.Embed(description=f"""
          ## <:animado:1465073228618793175> Nova Parceria!
          Olá **{membro.name}**! 
          Ficamos muito felizes em firmar essa parceria e esperamos que ela traga crescimento, união e bons resultados para ambas as comunidades.
          """, color=0xEEE1EE)
          lista_msgs = [ola_embed, ola_embed_v2]
          msgs = random.choice(lista_msgs)
          proxima_view = botaoRequisitos(msg_para_apagar=proxima_msg, msg=conteudo_parceria)
          await membro.send(embed=msgs, view=proxima_view)
          await interaction.followup.send("Divulgação enviada com sucesso e foi possível fazer o envio na DM!", ephemeral = True)
        except:
          await interaction.followup.send("Divulgação enviada com sucesso, porém não foi possível fazer o envio na DM!", ephemeral = True)


@bot.tree.command(name='divulgação', description='Enviar uma divulgação')
async def divulgar(inter: discord.Interaction):
    await inter.response.send_modal(Parceria_Modal())

class req(discord.ui.View):
  def __init__(self):
    super().__init__(timeout=None)
  @discord.ui.button(label='✅ Aceitar',
                               style=discord.ButtonStyle.green, custom_id="aceitar")
  async def aceitar(self, inter:discord.Interaction, button:discord.ui.Button):
    await inter.response.send_message('Você aceitou os requisitos para fazer parceria, e recebeu o cargo de <@&1427036601799934072>! Agora utilize o comando **/divulgação** e coloque seu texto junto com o link do servidor.', ephemeral=True)
    await inter.followup.send("Agora para pegar nosso texto deverá utilizar o comando **/invite**, e selecionar a opção **que mais se adeque** ao seu servidor.\n[exemplo](https://i.imgur.com/NcqsqCO.png)", ephemeral=True)
    await inter.followup.send(f"{inter.user.display_name} aceitou os requisitos para fazer parceria.")
    cargo = inter.guild.get_role(1427036601799934072)
    await inter.user.add_roles(cargo)
  @discord.ui.button(label='❌ Recusar',
                               style=discord.ButtonStyle.red, custom_id="recusar")
  async def recusar(self, inter:discord.Interaction, button:discord.ui.Button):
    await inter.response.send_message(
            'Você recusou os requisitos para fazer parceria!, e perdeu o cargo <@&1427036601799934072>',
            ephemeral=True)
    await inter.followup.send(
            f"{inter.user.display_name} recusou os requisitos para fazer parceria."
        )
    cargo = inter.guild.get_role(1427036601799934072)
    await inter.user.remove_roles(cargo)

@bot.tree.command(name='req_parceria',
                  description='Mostra os requisitos para fazer parceria')
async def req_parceria(inter: discord.Interaction):
    requisitos = discord.Embed(
        title='Requisitos para fazer parceria',
        description=
        'Para fazer parceria com o servidor, você precisa ter:\n \n• No minímo **30 membros**\n• Ter uma staff **ativa**\n• Ter um servidor **ativo** e com regras **claras**\n• Ter um **representante no servidor** da neo.exe\n• Ajudar no **engajamento** do servidor\n \n``Caso você não cumpra os requisitos, e clicar em aceitar, você será banido do servidor.``'
    )
    requisitos.set_footer(text='neo.exe • © Todos os direitos reservados')
    requisitos.set_image(url='https://i.imgur.com/Y7Y3JUF.gif')
    await inter.response.send_message(embed=requisitos)


#loops
@tasks.loop(time=time(12, 40, 00))
async def acorda_meus_lindos():
    canal = bot.get_channel(geral)
    random.random()
    falas = [
        "<@&1427038331266400439>, bora acordar chat <3!",
        "<@&1427038331266400439>, como vocês estão chat?",
        "<@&1427038331266400439>, dormiram bem? Já vão pra aula?",
        "<@&1427038331266400439>, qual foi a notícia mais aleatória que vocês viram hoje? Me contem! 🤯",
        "<@&1427038331266400439>, o que vocês acham de um x1 no brawl stars?",
        "<@&1427038331266400439>, salve, salve! 🙌 Mandem o melhor GIF que vocês têm na manga! Mostrem a criatividade! 😂",
        "<@&1427038331266400439>, hora de dar uma pausa! ☕ O que estão ouvindo de bom ou jogando agora? 🎶",
        "<@&1427038331266400439>, o chat tá quieto demais... 🤫 Bora movimentar! Digitem a primeira coisa que vier à cabeça! 💬"
    ]
    get = random.choice(falas)
    await canal.send(get)


@tasks.loop(time=time(15, 30, 00))
async def almoça_meus_lindos():
    canal = bot.get_channel(geral)
    random.random()
    falas = [
        "<@&1427038331266400439>, quem aí conseguiu comer algo decente hoje? 🥗 Contem pra gente! 👇",
        "<@&1427038331266400439>, a pergunta que não quer calar: já almoçaram? Qual foi a boa de hoje? 🤤",
        "<@&1427038331266400439>, pausa para o *check-in*! Almoço feito? 🍲 Se sim, digitem 'FUI' no chat! ✅",
        "<@&1427038331266400439>, estamos no pico do almoço! Quem já bateu o prato? 🍽️ E quem ainda está esperando? 😫",
        "<@&1427038331266400439>, **STOP!** Já se alimentaram? 🛑 Não fiquem com fome, recarreguem! 🍎",
        "<@&1427038331266400439>, que fome 🤤! O que vocês comeram?",
        "<@&1427038331266400439>, A comida ta saindo por aqui... o que vocês comeram?"
    ]
    get = random.choice(falas)
    await canal.send(get)


@tasks.loop(time=time(00, 30, 00))
async def dormir_meus_lindos():
    canal = bot.get_channel(geral)
    random.random()
    falas = [
        "<@&1427038331266400439>, bora dormir chat <3!",
        "<@&1427038331266400439>, como vocês estão chat?",
        "<@&1427038331266400439>, como foi o dia de vocês?",
        "<@&1427038331266400439>, o que vocês acham de um x1 no brawl stars?",
        "<@&1427038331266400439>, salve, salve! O que comeram de bom no jantar?",
        "<@&1427038331266400439>, o que estão jogando?",
        "<@&1427038331266400439>, o que estão pensando agora me contem <3"
    ]
    get = random.choice(falas)
    await canal.send(get)


bot.run(bot_token)

#terminamos o bot :D