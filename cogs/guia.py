import asyncio
import discord
from discord import app_commands
from discord.ext import commands
import random

class Guia(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        super().__init__()
    @app_commands.command(name="guia_setup", description="Envia um guia do servidor")
    async def guia_setup(self, interaction: discord.Interaction, canal: discord.TextChannel):
      embedGuia = discord.Embed(title="\n**Seja muito bem vindo(a) à neo.exe**", description=f"**neo.exe** é um lugar para se divertir, jogar e resenhar. \n*{emoji_triangulo} Feito por players para players!*\n\n**Estatistícas**:\nNeste momento o servidor conta com {interaction.guild.member_count} membros, e também conta com 18 staffs preparados para ajudar você\n\n**Links importantes:**\n{emoji_bolinha}Convite: https://discord.gg/bD3dND9FKv\n{emoji_bolinha}Servidor **Aliado:** https://discord.gg/Mc3SkxBacf", color=0x9f69e6)
      imagemguia = discord.Embed(title=None, description=None, color=0x9f69e6)
      imagemguia.set_image(url=img_guia)
      embedGuia.set_image(url=linha_guia)
      canalGuia = self.bot.get_channel(canal.id)
      await canalGuia.send(embed=imagemguia)
      await canalGuia.send(embed=embedGuia, view=Botoes())
      await interaction.response.send_message(f"Mensagem guia enviada em {canal.mention}, com sucesso!", ephemeral=True)

BotaoRegras = "<:regras:1458457337328042085>"
BotaoCargos = "<:cargos:1458457333150519329>"
BotaoWare = "<:pasta_aberta:1458457347554017340>"
BotaoBots = "<:bots:1458457331707678884>"
emoji_bolinha = "<:bolinha:1458491844395663402>"
emoji_triangulo = "<:triangulozinho:1458491845939040482>"
img_guia = "https://media.discordapp.net/attachments/1426990937137086556/1457460882157338786/13.png?ex=695c15b8&is=695ac438&hm=7f1ae550baa3176b3afee7984f043af8fd3114d63c54f3a26eb7ee8439252fa9&=&format=webp&quality=lossless&width=510&height=180"
linha_guia = "https://cdn.discordapp.com/attachments/1426990937137086556/1457562594029338646/Design_sem_nome_12.png?ex=695c7472&is=695b22f2&hm=3044bb0e9afed956ca1b49bf72f568c860900535af71be36e13cbcbe74af3161"
img_regras = "https://cdn.discordapp.com/attachments/1460010000192639253/1460878653003927592/21_Sem_Titulo_20260114030709.png?ex=696d2204&is=696bd084&hm=2d17a2b24a15f49ea695730100894f1a4758c31cf86dfa3cd86ede7ddfc4c877"
img_quem_somos = "https://cdn.discordapp.com/attachments/1460010000192639253/1460878653003927592/21_Sem_Titulo_20260114030709.png?ex=696d2204&is=696bd084&hm=2d17a2b24a15f49ea695730100894f1a4758c31cf86dfa3cd86ede7ddfc4c877"
img_cargos = "https://cdn.discordapp.com/attachments/1460010000192639253/1461597844480852002/21_Sem_Titulo_20260116024737.png?ex=696d1cd1&is=696bcb51&hm=f452556d0c664eb8cc177ef6d940b1eb54718f0ab39d746e3e0f340a06cb0bd1"
img_bot = "https://cdn.discordapp.com/attachments/1460010000192639253/1461542223714848995/21_Sem_Titulo_20260115230633.png?ex=696ce904&is=696b9784&hm=5962ef4849d069f3e7b0ba41f0c7f2c711d7573c8e2ec235b9eb2a8821712319"
thumb_bot = "https://cdn.discordapp.com/attachments/1426990937137086556/1457461509922750474/10.png?ex=695c164e&is=695ac4ce&hm=7781e514da0028fa3abc042eec6800cb50ee182c1819b486cf8f4c14b04e95a8&"
class Botoes(discord.ui.View):
  def __init__(self):
      super().__init__(timeout=None)
  @discord.ui.button(label=" Regras",emoji=BotaoRegras, style=discord.ButtonStyle.secondary, custom_id="botao1")
  async def botao1(self, interaction: discord.Interaction, button: discord.ui.Button):
      regrasEmbed = discord.Embed(title=None, description=f"## {BotaoRegras} • Regras do Servidor\n\n\n**1. Respeito acima de tudo**{emoji_bolinha} Trate todos com educação e respeito.\n{emoji_bolinha} Brincadeiras são permitidas, mas ofensas, preconceito, bullying, assédio ou discurso de ódio não serão tolerados.\n{emoji_triangulo} Liberdade de expressão não é desculpa para desrespeito.\n\n**2. Proibido spam ou flood**{emoji_bolinha} Não repita mensagens.\n{emoji_bolinha} Evite marcar @everyone ou @here sem necessidade.\n{emoji_bolinha} Não envie links, imagens, áudios ou mensagens em excesso ou fora de contexto.\n\n**3. Utilize os canais corretamente**{emoji_bolinha} Cada canal possui um propósito específico.\n{emoji_bolinha} Conteúdos fora do tema devem ser enviados ao canal apropriado.\n\n**4. Conteúdo impróprio é proibido**{emoji_bolinha} É proibido conteúdo NSFW, violento, ilegal ou que viole os Termos de Serviço do Discord e as Diretrizes da Comunidade.\n\n**5. Divulgação não é permitida**{emoji_bolinha} É proibida a divulgação de links de outros servidores, canais ou redes sociais sem autorização da staff e fora do canal correto isso pode resultar em ban ou kick dependendo da situação.\n{emoji_triangulo} Divulgação via DM para outros membros resulta em ban imediato.\n\n**6. Evite discussões tóxicas**{emoji_bolinha} Debates são permitidos, brigas não.\n{emoji_bolinha} Caso a conversa fique agressiva, chame um moderador.\n\n**7. Siga as orientações da staff**{emoji_bolinha} A equipe de moderação trabalha para manter um ambiente saudável.\n{emoji_bolinha} Decisões da staff devem ser respeitadas.\n\n**8. Punições**{emoji_bolinha} O descumprimento das regras pode resultar em aviso, mute, kick ou ban, dependendo da gravidade da infração.\n\n**9. Parcerias**{emoji_bolinha} Parcerias só são permitidas com autorização prévia da staff e seguindo os critérios do servidor.\n{emoji_triangulo} Não realizamos parcerias com lojas, serviços pagos ou anúncios comerciais.\n{emoji_triangulo} Divulgação de parcerias sem aprovação resultará em punição.\n\n||< Obrigado por fazer parte da nossa comunidade >||\n**Equipe neo.exe**", color=0x9f69e6)
      regrasEmbed.set_image(url=img_regras)
      await interaction.response.send_message(embed=regrasEmbed, ephemeral=True)
  @discord.ui.button(label=" Quem somos nós?",emoji="<:pasta_aberta:1458457347554017340>", style=discord.ButtonStyle.secondary, custom_id="botao2")
  async def botao2(self, interaction: discord.Interaction, button: discord.ui.Button):
      embedWhoweare = discord.Embed(title=None, description="## <:pasta_aberta:1458457347554017340> Quem somos nós?\n\nSomos a comunidade neo.exe, uma comunidade criada por <@1259110474142978058>, <@819918726732054578> e <@994989331263524866>, em 12/10/2025, feita pra reunir pessoas que compartilham o mesmo espírito de jogo, amizade e evolução. Nosso foco principal são os jogos, mas o servidor vai além disso — aqui é um espaço pra conversar, fazer amizades, se divertir e fazer parte de algo maior.\n\n## O que nos move?\n\nA ideia nasceu da vontade de criar um ambiente leve, ativo e com energia boa. Um lugar onde cada membro importa, onde o chat vive, os eventos acontecem e a galera se ajuda dentro e fora do jogo.\n\nMais do que um servidor, a neo.exe é uma comunidade em constante movimento **— feita por players, para players.**\n\n**Seja bem-vindo a nossa comunidade.** <:athos_triste_roxo:1458449923900178538>", color=0x9f69e6)
      embedWhoweare.set_image(url=img_quem_somos)
      await interaction.response.send_message(embed=embedWhoweare, ephemeral=True)
  @discord.ui.button(label=" Cargos",emoji=BotaoCargos, style=discord.ButtonStyle.secondary, custom_id="botao3")
  async def botao3(self, interaction: discord.Interaction, button: discord.ui.Button):
      embedCargos = discord.Embed(title=None, 
          description=f"""## {BotaoCargos} NOSSOS CARGOS
          {emoji_triangulo}Nosso servidor possui cargos que representam experiência, parcerias e criação de conteúdo.
          {emoji_triangulo}Alguns são obtidos automaticamente por XP, outros podem ser requisitados.\n\n### 🎥 Cargos de Divulgação & Criação
  {emoji_triangulo}Cargos voltados para divulgação, parcerias e criadores de conteúdo.
  {emoji_triangulo}Alguns cargos são concedidos automaticamente, outros precisam ser requisitados.
  
  <@&1427036601799934072>
  Cargo concedido a membros que fecharam parceria oficial com o servidor.
  
  <@&1450579532930220162>
  Cargo concedido a membros que patrocinaram sorteios no servidor.
  
  <@&1453793296257388626>
  Cargo requisitável
  {emoji_bolinha}Mínimo de 100 inscritos no canal
  {emoji_bolinha}Boa qualidade de imagem e áudio nos vídeos
  {emoji_bolinha}Média de 180 visualizações por vídeo ou 1.000 visualizações por Short
  
  <@&1453793410350841937>
  Cargo requisitável
  {emoji_bolinha}Mínimo de 1.000 inscritos no canal
  {emoji_bolinha}Boa qualidade de imagem e áudio nos vídeos
  {emoji_bolinha}Média de 2.000 visualizações por vídeo
  
  <@&1453793103533310033>
  Cargo requisitável
  {emoji_bolinha}Mínimo de 500 inscritos no canal
  {emoji_bolinha}Boa qualidade de imagem e áudio nas lives
  {emoji_bolinha}Frequência consistente de transmissões
  
  <@&1453793548016292049>
  Cargo requisitável
  Criadores de conteúdo em geral (design, edição, arte, etc.)
  {emoji_bolinha}Necessário comprovar perfil, conta ou trabalho autoral
  
  <@&1427036801218117632>
  Cargo requisitável
  {emoji_bolinha}Necessário apenas comprovar a conta, canal ou usuário em qualquer plataforma\n\n### 📊 Cargos por Experiência
  {emoji_triangulo}Os cargos por experiência são recebidos ao atingir uma quantidade específica de XP no servidor.
  {emoji_triangulo}O progresso pode ser acompanhado através do comando /xp view.
  
  <@&1427037471270506546>
  XP necessário: 0 XP
  
  <@&1427037677282267257>
  XP necessário: 250 XP
  
  <@&1427037749910831229>
  XP necessário: 500 XP
  
  <@&1427037934267142194>
  XP necessário: 750 XP
  
  <@&1427038022825939004>
  XP necessário: 1000 XP\n\n### 💫 Cargos de Hierarquia
  {emoji_triangulo}Os cargos gerais representam a hierarquia, organização e funcionamento do servidor.
  {emoji_triangulo}Cada cargo possui funções específicas dentro da comunidade.
  
  <@&1427024302125088909>
  {emoji_bolinha}Responsável máximo pelo servidor e decisões finais.
  
  <@&1432055249102835712>
  {emoji_bolinha}Equipe de confiança responsável pela administração geral.
  
  <@&1427024045781811320>
  {emoji_bolinha}Gerencia sistemas, configurações e coordena a equipe Staff.
  
  <@&1427023414928871455>
  {emoji_bolinha}Mantém a ordem, aplica regras e cuida da comunidade, também pode criar e gerenciar automações para o servidor.
  
  <@&1427023068727083018>
  {emoji_bolinha}Auxilia a moderação em tarefas do dia a dia.
  
  <@&1427022636273373335>
  {emoji_bolinha}Ajuda membros, tira dúvidas e orienta novos usuários.
  
  <@&1427022125192970332>
  {emoji_bolinha}Cargo exclusivo para bots oficiais do servidor.
  
  <@&1427020441981157456>
  {emoji_bolinha}Cargo padrão concedido automaticamente a todos os usuários.
                                  """, 
                                  color= 0x9f69e6)
      embedCargos.set_image(url=img_cargos)
      await interaction.response.send_message(embed=embedCargos, ephemeral=True)
  @discord.ui.button(label=" Bot",emoji=BotaoBots, style=discord.ButtonStyle.secondary, custom_id="botao4")
  async def botao4(self, interaction: discord.Interaction, button: discord.ui.Button):
      botEmbed = discord.Embed(title=None, description=f"## {BotaoBots} athosᵇᵒᵗ\n\n**neo.exe** é um servidor com um bot personalizado, chamado 𝗮𝘁𝗵𝗼𝘀ᵇᵒᵗ. Ele foi criado para facilitar a administração e interação dentro do servidor.\n\n### 🎲 Seus dados:\n {emoji_bolinha}Desenvolvedor responsável: <@1259110474142978058>\n{emoji_bolinha}Documentação/funções: /ajuda\n{emoji_bolinha}Prefixo híbrido: / e >\n{emoji_bolinha}Data de criação: 19/10/2025\n\n**Gostou? Menciona ele com <@1429564793462984775>**", color=0x9f69e6)
      botEmbed.set_image(url=img_bot)
      botEmbed.set_thumbnail(url=thumb_bot)
      await interaction.response.send_message(embed=botEmbed, ephemeral=True)


async def setup(bot):
    bot.add_view(Botoes())
    await bot.add_cog(Guia(bot))