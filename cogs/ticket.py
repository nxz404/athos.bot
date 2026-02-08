import asyncio
import discord
from discord import app_commands
from discord.ext import commands
import random

intents = discord.Intents.all()


class Bot_modificado(commands.Bot):

    def __init__(self):
        super().__init__(command_prefix='>', intents=discord.Intents.all())
      
        


bot = Bot_modificado()

class Ticket(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        super().__init__()
    @app_commands.command(name="ticket_setup", description="Envia o setup do ticket")
    async def setup(self, interaction: discord.Interaction, canal: discord.TextChannel):
        enviocanal = discord.utils.get(interaction.guild.channels, id=canal.id)
        embed = discord.Embed(title="<a:ticket:1458455043240890613> **neo.exe** | Sistema de Tickets", 
        description="""**Bem-vindo(a)!** Aqui você pode **enviar reclamações, relatar problemas, fazer denúncias, solicitar parcerias** ou **falar com o suporte.**\n<:Designsemnome17:1458500175181123647> **Precisa de ajuda?**\nㅤ<:triangulozinho:1458491845939040482> Selecione abaixo o tipo de **atendimento que você precisa.**\nㅤ<:bolinha:1458491844395663402> Nossa equipe responde o **mais rápido possível!**""", 
        color=0x9F69E6)
        embed.set_image(url="https://i.imgur.com/w6pD765.png")
        embed.add_field(name="", value="`` ‣  Desenvolvedores: nxz.zx & hiroshiiiiikkk``")
        embed.set_footer(text="neo.exe • tickets online 24/7")
        await enviocanal.send(embed=embed, view=TicketSelection(self.bot))
        await interaction.response.send_message(f"Setup do ticket enviado com sucesso em {canal.mention}!", ephemeral = True)
#Sistema De Tickets
#criar ticket        
class TicketSelection(discord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.motivo = None
        self.bot = bot
    @discord.ui.select(
        custom_id="menu_atendimento",
        placeholder = "Selecione a opção que mais se adeque...",
        min_values=1,
        max_values=1,
        options = [
            discord.SelectOption(label="Atendimento simples (Dúvidas ou Suporte Geral)", description="Abra um ticket de suporte", emoji="<:simples:1458517790775578697>"),
            discord.SelectOption(label="Denúncia de membros", description="Denuncie comportamentos inadequados de membros.", emoji="<:denuncia:1458517782931964102>"),
            discord.SelectOption(label="Solicitação de Parcerias", description="Solicite parcerias, eventos e outras coisas.", emoji="<:parceria:1458517788753920133>"),
            discord.SelectOption(label="Quero fazer parte da neo.exe (STAFF)", description="Inicie seu recrutamento para se tornar um staff", emoji="<:staff:1458517792528662742>"),
            discord.SelectOption(label="Sugestões ou Feedbacks", description="Envie ideias para o servidor ou feedbacks.", emoji="<:sugestoes:1458517794210447463>"),
            discord.SelectOption(label="Relato de bugs ou mal funcionamento", description="Compartilhe informações sobre bugs em bots.", emoji="<:mal:1458517786623082689>"),
            discord.SelectOption(label="Reclamações sobre os serviços da Neo", description="Relate problemas ou insatisfações feitas por nós.", emoji="<:erro:1458517785037770903>")
        ]
    )
       
    async def select_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        await interaction.response.defer(ephemeral=True)
        categoria = discord.utils.get(interaction.guild.categories, id=1427625779063291997)
        self.motivo = select.values[0]
        categoria_ticket = discord.utils.get(interaction.guild.categories, id=1427625779063291997)
        ticket_channel = await interaction.guild.create_text_channel(
            name=f"ticket-{interaction.user.name}",
            category=categoria,
            topic=f"{interaction.user.id}"
        )

        overwrites = {
            interaction.guild.default_role: discord.PermissionOverwrite(view_channel=False),
            interaction.user: discord.PermissionOverwrite(view_channel=True, send_messages=True, read_message_history=True),
            interaction.guild.get_role(1427025826913849516): discord.PermissionOverwrite(view_channel=True, send_messages=True),
            interaction.guild.get_role(1469345464066375849): discord.PermissionOverwrite(view_channel=True, send_messages=True)
        }
        await ticket_channel.edit(overwrites=overwrites)
        
        await interaction.followup.send(f"Seu ticket foi criado em {ticket_channel.mention}", ephemeral=True)
        
        painel_ticket = self.bot.get_channel(1426990460127281162)
        embedpainel = discord.Embed(title=None, description=None, color=discord.Color.green())
        embedpainel.set_author(name=interaction.user.name, icon_url=interaction.user.avatar.url)
        embedpainel.add_field(name="**Informações**", value=f"Ticket: {ticket_channel.name}\nAção: **Abrir**", inline=True)
        embedpainel.add_field(name="Motivo", value=f"{self.motivo}", inline=True)
        
        if painel_ticket:
            await painel_ticket.send(embed=embedpainel)


        embed = discord.Embed(description=f"Seu atendimento começará em breve.\n<:bolinha:1458491844395663402>Por favor tenha paciência e seja respeitoso.\n<:bolinha:1458491844395663402>A Staff da neo.exe agradeçe :3\n\n<a:fechamento:1458455060706099244> **Motivo:**\n``{self.motivo}``", color=0x9F69E6)
        embed.set_image(url="https://media.discordapp.net/attachments/1426990937137086556/1457460882157338786/13.png?ex=695e0ff8&is=695cbe78&hm=024a7e442664a63cc3af819ec3f7808c0a841001c3a49f6407fca68b1a630c08&=&format=webp&quality=lossless&width=510&height=180")
        
        proxima_view = TicketFunction(bot=self.bot, motivo=self.motivo)
        await ticket_channel.send(f"{interaction.user.mention} Seja bem vindo(a)! <@&1427025826913849516><@&1469345464066375849>", embed=embed, view=proxima_view)
        
        await interaction.edit_original_response(view=self)
      
#Fechar/Assumir
class TicketFunction(discord.ui.View):
    def __init__(self, bot, motivo=None):
        super().__init__(timeout=None)
        self.motivo = motivo
        self.bot = bot
        
    @discord.ui.button(label="Fechar", style=discord.ButtonStyle.grey, custom_id="fechar", emoji="<a:fechamento:1458455060706099244>")
    async def fechar(self, interaction: discord.Interaction, button: discord.ui.Button):
        CARGO_AUTORIZADO = 1427025826913849516
        if not any(role.id == CARGO_AUTORIZADO for role in interaction.user.roles):
            return await interaction.response.send_message(
                "<a:erradinho:1458455049889124548> Você não tem permissão para fechar este ticket.",
                ephemeral=True
            )
        CARGO_AUTORIZADO2 = 1469345464066375849
        if not any(role.id == CARGO_AUTORIZADO for role in interaction.user.roles):
            return await interaction.response.send_message(
                "<a:erradinho:1458455049889124548> Você não tem permissão para fechar este ticket.",
                ephemeral=True
            )
        proxima_view = ConfirmarTicket(bot=self.bot, motivo=self.motivo)
        await interaction.response.send_message("**Você deseja realmente fechar este ticket?**", view=proxima_view, ephemeral=True)
    @discord.ui.button(label="Atender", style=discord.ButtonStyle.grey, emoji= "<a:atender:1458455058655088755>", custom_id="atender")
    async def atender(self, interaction: discord.Interaction, button: discord.ui.Button):
        CARGO_AUTORIZADO = 1427025826913849516
        if not any(role.id == CARGO_AUTORIZADO for role in interaction.user.roles):
            return await interaction.response.send_message(
                "<a:erradinho:1458455049889124548> Você não tem permissão para atender este ticket.",
                ephemeral=True
            )
        if not any(role.id == CARGO_AUTORIZADO for role in interaction.user.roles):
            return await interaction.response.send_message(
                "<a:erradinho:1458455049889124548> Você não tem permissão para fechar este ticket.",
                ephemeral=True
            )
        atenderEmbed = discord.Embed(
            description=f"""
                {interaction.user.mention} **assumiu** seu atendimento.\n
                **O que isso quer dizer?**
                <:bolinha:1458491844395663402> Problemas ou denúncias serão direcionados a ele(a).
                <:bolinha:1458491844395663402> Avalie ao final com **/avaliar_staff** em <#1427676622567247983>.""",
            color = 0x9F69E6
            
        )
        ticket_channel = interaction.channel
        ticket_id = discord.utils.get(interaction.guild.channels, id=ticket_channel.id)

        atenderEmbed.set_author(name=f"@{interaction.user.name}")
        atenderEmbed.set_thumbnail(url=interaction.user.avatar.url)
        await ticket_id.send(embed=atenderEmbed)
        await interaction.response.send_message("<a:certinho:1458455054251196472> Atendimento iniciado com sucesso!", ephemeral=True)

#confirmar/recusar
class ConfirmarTicket(discord.ui.View):
    def __init__(self, bot, motivo=None):
        super().__init__(timeout=None)
        self.motivo = motivo
        self.bot = bot
    @discord.ui.button(label="Confirmar", style=discord.ButtonStyle.red, custom_id="confirmar")
    async def confirmar(self, interaction: discord.Interaction, button: discord.ui.Button):
        ticket_channel = interaction.channel
        ticket_name = interaction.user
        ticket_id = discord.utils.get(interaction.guild.channels, id=ticket_channel.id)
        painel_ticket = self.bot.get_channel(1426990460127281162)

        try:
          dono_id = int(interaction.channel.topic)
          dono = interaction.guild.get_member(dono_id)
          if dono:
            await interaction.channel.set_permissions(dono, send_messages=False, view_channel=True)
        except:
          pass

        embedFechar = discord.Embed(title=None, description=None, color=discord.Color.yellow())
        embedFechar.set_author(name=interaction.user.name, icon_url=interaction.user.avatar.url)
        embedFechar.add_field(name="**Informações**", value=f"Ticket: {ticket_channel.name}\nAção: **Fechar**", inline=True)
        embedFechar.add_field(name="Motivo", value=f"{self.motivo}", inline=True)
        await painel_ticket.send(embed=embedFechar)
        fecharEmbed = discord.Embed(description=f"<a:fechamento:1458455060706099244> | {ticket_channel.mention} fechado por {interaction.user.mention}", color=discord.Color.yellow())
        await ticket_id.send(embed=fecharEmbed)
        proxima_view = Painel_CallCenter(bot=self.bot, motivo=self.motivo)
        callcenterEmbed = discord.Embed(description="``Painel de Atendimento de Ticket da Neo.exe``", color=0xffffff)
        await interaction.response.send_message(embed=callcenterEmbed, view=proxima_view, ephemeral = True)
    @discord.ui.button(label="Cancelar", style=discord.ButtonStyle.grey, custom_id="cancelar")
    async def cancelar(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("<a:erradinho:1458455049889124548> Fechamento cancelado.", ephemeral=True)

#Painel de Atendimento
class Painel_CallCenter(discord.ui.View):
    def __init__(self, bot, motivo=None):
        super().__init__(timeout=None)
        self.motivo = motivo
        self.bot = bot
    @discord.ui.button(label="Reabrir", style=discord.ButtonStyle.grey, custom_id="reabrir", emoji="<a:reabrir:1458455052057575488>")
    async def reabrir(self, interaction: discord.Interaction, button: discord.ui.Button):
        ticket_channel = interaction.channel
        ticket_name = interaction.user
        ticket_id = discord.utils.get(interaction.guild.channels, id=ticket_channel.id)
        painel_ticket = self.bot.get_channel(1426990460127281162)
        try:
          dono_id = int(interaction.channel.topic)
          dono = interaction.guild.get_member(dono_id)
          if dono:
            await interaction.channel.set_permissions(dono, send_messages=True, view_channel=True)
        except:
          pass
        reabrirEmbed = discord.Embed(color=discord.Color.blue())
        reabrirEmbed.set_author(name=interaction.user.name, icon_url=interaction.user.avatar.url)
        reabrirEmbed.add_field(name="**Informações**", value=f"Ticket: {ticket_channel.name}\nAção: **Reabrir**", inline=True)
        reabrirEmbed.add_field(name="Motivo", value=f"{self.motivo}", inline=True)
        await painel_ticket.send(embed=reabrirEmbed)
        await interaction.response.send_message("<a:certinho:1458455054251196472> Ticket reaberto com sucesso!", ephemeral=True)
        embedUsuarioReabrir = discord.Embed(description=f"<a:reabrir:1458455052057575488> | {ticket_channel.mention} reaberto por {interaction.user.mention}", color=discord.Color.blurple())
        await ticket_id.send(embed=embedUsuarioReabrir)
    @discord.ui.button(label="Excluir", style=discord.ButtonStyle.grey, custom_id="excluir", emoji = "<a:lixeira:1458455056113471703>")
    async def excluir(self, interaction: discord.Interaction, button: discord.ui.Button):
        ticket_channel = interaction.channel
        ticket_name = interaction.user
        ticket_id = discord.utils.get(interaction.guild.channels, id=ticket_channel.id)
        painel_ticket = self.bot.get_channel(1426990460127281162)
        excluirEmbed = discord.Embed(color=discord.Color.red())
        excluirEmbed.set_author(name=interaction.user.name, icon_url=interaction.user.avatar.url)
        excluirEmbed.add_field(name="**Informações**", value=f"Ticket: {ticket_channel.name}\nAção: **Excluir**", inline=True)
        excluirEmbed.add_field(name="Motivo", value=f"{self.motivo}", inline=True)
        await painel_ticket.send(embed=excluirEmbed)
        await interaction.response.send_message("<a:certinho:1458455054251196472> Exclusão de ticket autorizada.", ephemeral=True)
        tempoexcluir = discord.Embed(description=f"<a:lixeira:1458455056113471703> | O {ticket_channel.mention} será excluído em 5 segundos por {interaction.user.mention}",color=discord.Color.red())
        await ticket_id.send(embed=tempoexcluir)
        await asyncio.sleep(5)
        await ticket_channel.delete()
async def setup(bot):
  bot.add_view(TicketSelection(bot=bot))
  bot.add_view(TicketFunction(bot=bot))
  bot.add_view(ConfirmarTicket(bot=bot))
  bot.add_view(Painel_CallCenter(bot=bot))
  await bot.add_cog(Ticket(bot))