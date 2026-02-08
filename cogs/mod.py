import discord
from discord import app_commands
from discord.ext import commands
import asyncio

canal_logs = 1434533394838192240

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # --- SUPER MODERADOR ---

    @commands.has_role(1432055249102835712)
    @commands.hybrid_command(name='kick', description='Expulsa um membro do servidor')
    @commands.has_permissions(kick_members=True) # Corrigido para a permissão correta
    async def kick(self, ctx, membro: discord.Member, *, reason: str):
        # Simplificado: membro.kick é mais direto
        await membro.kick(reason=reason)
        
        kick_channel = self.bot.get_channel(canal_logs)
        kickmb = discord.Embed(
            title="🛡 EXPULSÃO",
            description=f"O membro(a) {membro.mention} foi expulso(a) do servidor, pois: {reason}\n\n**Não quebre as regras seu(a) boboca.**",
            color=0xBFE9EE)
        kickmb.set_footer(text=f"Expulso por: {ctx.author.name}")
        kickmb.set_thumbnail(url="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExczRnaHk0ZTgxaTI4YWJjYmloYjN1cGNib2Foamh5bDd1eTZuOHk2ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ILgS7Zl0Tnc7PY9Fb5/giphy.gif")
        kickmb.set_author(name=f'{membro.display_name}', icon_url=membro.display_avatar.url)

        await ctx.reply(f"{membro.mention} foi expulso com sucesso!", ephemeral=True)
        if kick_channel:
            await kick_channel.send(embed=kickmb)

    @commands.has_role(1432055249102835712)
    @commands.hybrid_command(name='banir', description='Bane um membro e apaga mensagens')
    @commands.has_permissions(ban_members=True)
    async def banir(self, ctx, membro: discord.Member, *, reason: str = "Não informado"):
        # SOLUÇÃO AQUI: delete_message_seconds limpa as mensagens (604800 = 7 dias)
        await membro.ban(reason=reason, delete_message_seconds=604800)
        
        banc = self.bot.get_channel(canal_logs)
        banmb = discord.Embed(
            title="🛡 BANIMENTO",
            description=f"O membro(a) {membro.mention} foi banido(a) do servidor, pois: {reason}\n\n**Não quebre as regras seu(a) boboca.**",
            color=0xBFE9EE)
        banmb.set_footer(text=f"Banido por: {ctx.author.name}")
        banmb.set_thumbnail(url="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExczRnaHk0ZTgxaTI4YWJjYmloYjN1cGNib2Foamh5bDd1eTZuOHk2ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ILgS7Zl0Tnc7PY9Fb5/giphy.gif")
        banmb.set_author(name=f'{membro.display_name}', icon_url=membro.display_avatar.url)

        await ctx.reply(f"{membro.mention} foi banido com sucesso e mensagens limpas!", ephemeral=True)
        if banc:
            await banc.send(embed=banmb)

    @commands.has_role(1432055249102835712)
    @commands.hybrid_command(name='desbanir', description='Desbane um membro do servidor')
    @commands.has_permissions(ban_members=True)
    async def desbanir(self, ctx, user: discord.User):
        try:
            await ctx.guild.unban(user)
            await ctx.reply(f"O {user.mention} foi desbanido(a) com sucesso!", ephemeral=True)
        except discord.NotFound:
            await ctx.reply(f"O usuário {user.name} não está na lista de banidos.", ephemeral=True)

    # --- MODERAÇÃO (SILENCIAR) ---

    @commands.has_permissions(moderate_members=True)
    @commands.hybrid_command(name="silenciar", description="Silencia um membro")
    async def silenciar(self, ctx, membro: discord.Member, tempo: int, *, reason: str = "Não informado"):
        # DICA: Use o timeout_into nativo do Discord se quiser algo mais moderno,
        # mas mantive sua lógica de cargo para respeitar seu design.
        
        guild = ctx.guild
        muted_role = discord.utils.get(guild.roles, name="Silenciado")
        
        if not muted_role:
            muted_role = await guild.create_role(name="Silenciado")
            for channel in guild.channels:
                await channel.set_permissions(muted_role, send_messages=False, speak=False)

        await membro.add_roles(muted_role, reason=reason)
        
        silenciarmb = discord.Embed(
            title="🛡 SILENCIAMENTO",
            description=f'O membro(a) {membro.mention} silenciado(a) por {tempo} minuto(s).\n**Motivo:** {reason}',
            color=0xBFE9EE)
        silenciarmb.set_footer(text=f"Silenciado por: {ctx.author.name}")
        silenciarmb.set_thumbnail(url='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExM2ZtMWVtc3Rmd3BvaHlmOHB5eGx6azlzb3ZycnF5eWFwYmdvM3hwYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/RzifPnDTZArCPdnX7M/giphy.gif')
        
        log_channel = self.bot.get_channel(canal_logs)
        if log_channel:
            await log_channel.send(embed=silenciarmb)
            
        await ctx.reply(f"{membro.mention} silenciado(a)!", ephemeral=True)

        await asyncio.sleep(tempo * 60)
        
        if muted_role in membro.roles:
            await membro.remove_roles(muted_role)
            # Embed de dessilenciamento aqui se desejar...

    # --- AVALIAÇÃO ---

    @app_commands.command(name="avaliar_staff", description="Utilize para avaliar um staff")
    @app_commands.describe(staff="Staff avaliado", avaliação="Nota de 1 a 5", motivo="Motivo", cargo="Cargo do staff")
    @app_commands.choices(avaliação=[
        app_commands.Choice(name="⭐⭐⭐⭐⭐", value=5),
        app_commands.Choice(name="⭐⭐⭐⭐", value=4),
        app_commands.Choice(name="⭐⭐⭐", value=3),
        app_commands.Choice(name="⭐⭐", value=2),
        app_commands.Choice(name="⭐", value=1)
    ])
    async def avaliar_staff(self, inter: discord.Interaction, staff: discord.Member, avaliação: int, motivo: str, cargo: discord.Role):
        canal_aval = self.bot.get_channel(1427676622567247983)
        embed = discord.Embed(
            title=f"Avaliação do staff {staff.display_name}",
            description=f"**Avaliação:** {avaliação} ⭐\n**Cargo:** {cargo.mention}\n**Motivo:** {motivo}\n`Avaliador: {inter.user.name}`",
            color=0xBFE9EE)
        await inter.response.send_message("Avaliação enviada!", ephemeral=True)
        if canal_aval:
            await canal_aval.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Mod(bot))