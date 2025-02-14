import discord
from discord.ext import commands

# Ersetze 'BOT_TOKEN_HIER' durch den Token deines Discord-Bots
TOKEN = 'BOT_TOKEN_HIER'
# Ersetze 'LOG_CHAT_ID' durch die ID des Textkanals, in den die Logs gepostet werden sollen
LOG_CHANNEL_ID = LOG_CHAT_ID

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name} hat sich eingeloggt!')


@bot.event
async def on_voice_state_update(member, before, after):
    log_channel = bot.get_channel(LOG_CHANNEL_ID)

    if log_channel is None:
        print(f"Konnte den Kanal mit der ID {LOG_CHANNEL_ID} nicht finden.")
        return

    embed = None

    if before.channel is None and after.channel is not None:
        embed = discord.Embed(
            title="📥Sprachkanal Beitritt📥",
            description=f'{member.mention} ist dem Sprachkanal **{after.channel.name}** beigetreten.',
            color=discord.Color.green()
        )
    elif before.channel is not None and after.channel is None:
        embed = discord.Embed(
            title="📤Sprachkanal Verlassen📤",
            description=f'{member.mention} hat den Sprachkanal **{before.channel.name}** verlassen.',
            color=discord.Color.red()
        )
    elif before.channel != after.channel:
        embed = discord.Embed(
            title="📥Sprachkanal Wechsel📤",
            description=f'{member.mention} hat den Sprachkanal von **{before.channel.name}** zu **{after.channel.name}** gewechselt.',
            color=discord.Color.orange()
        )

    if embed:
        await log_channel.send(embed=embed)


@bot.event
async def on_member_join(member):
    log_channel = bot.get_channel(LOG_CHANNEL_ID)
    if log_channel:
        embed = discord.Embed(
            title="🙋Mitglied Beigetreten🙋‍♂️",
            description=f'{member.mention} ist dem Server beigetreten.',
            color=discord.Color.green()
        )
        await log_channel.send(embed=embed)


@bot.event
async def on_member_remove(member):
    log_channel = bot.get_channel(LOG_CHANNEL_ID)
    if log_channel:
        embed = discord.Embed(
            title="🤦‍♀️Mitglied Verlassen🤦‍♂️",
            description=f'{member.mention} hat den Server verlassen.',
            color=discord.Color.red()
        )
        await log_channel.send(embed=embed)


@bot.event
async def on_message_delete(message):
    log_channel = bot.get_channel(LOG_CHANNEL_ID)
    if log_channel:
        embed = discord.Embed(
            title="🗑️Nachricht Gelöscht🗑️",
            description=f'{message.author.mention} hat eine Nachricht in **{message.channel.name}** gelöscht.',
            color=discord.Color.red()
        )
        if message.content:
            embed.add_field(name="Nachricht", value=message.content, inline=False)
        await log_channel.send(embed=embed)


@bot.event
async def on_message_edit(before, after):
    log_channel = bot.get_channel(LOG_CHANNEL_ID)
    if log_channel:
        embed = discord.Embed(
            title="⚙️Nachricht Bearbeitet⚙️",
            description=f'{before.author.mention} hat eine Nachricht in **{before.channel.name}** bearbeitet.',
            color=discord.Color.orange()
        )
        embed.add_field(name="Vorher", value=before.content, inline=False)
        embed.add_field(name="Nachher", value=after.content, inline=False)
        await log_channel.send(embed=embed)


@bot.event
async def on_guild_role_update(before, after):
    log_channel = bot.get_channel(LOG_CHANNEL_ID)
    if log_channel:
        embed = discord.Embed(title="🗂️Rolle Aktualisiert🗂️", color=discord.Color.blue())
        if before.name != after.name:
            embed.add_field(name="Name geändert", value=f'Von {before.name} zu {after.name}', inline=False)
        if before.permissions != after.permissions:
            embed.add_field(name="Berechtigungen geändert",
                            value=f'Die Berechtigungen der Rolle {before.name} wurden geändert.', inline=False)
        await log_channel.send(embed=embed)


@bot.event
async def on_member_update(before, after):
    log_channel = bot.get_channel(LOG_CHANNEL_ID)
    if log_channel:
        embed = None
        if before.roles != after.roles:
            # Finden der hinzugefügten Rollen
            new_roles = [role for role in after.roles if role not in before.roles]
            removed_roles = [role for role in before.roles if role not in after.roles]

            if new_roles:
                embed = discord.Embed(
                    title="Rolle Hinzugefügt",
                    description=f'{after.mention} hat die Rolle(n) {", ".join([role.name for role in new_roles])} erhalten.',
                    color=discord.Color.green()
                )
            if removed_roles:
                embed = discord.Embed(
                    title="Rolle Entfernt",
                    description=f'{after.mention} hat die Rolle(n) {", ".join([role.name for role in removed_roles])} verloren.',
                    color=discord.Color.red()
                )

        if embed:
            await log_channel.send(embed=embed)


@bot.event
async def on_member_ban(guild, user):
    log_channel = bot.get_channel(LOG_CHANNEL_ID)
    if log_channel:
        ban_entry = await guild.fetch_ban(user)
        embed = discord.Embed(
            title="Mitglied Gebannt",
            description=f'{user.mention} wurde vom Server gebannt.',
            color=discord.Color.red()
        )
        if ban_entry.reason:
            embed.add_field(name="Begründung", value=ban_entry.reason, inline=False)
        await log_channel.send(embed=embed)


@bot.event
async def on_member_unban(guild, user):
    log_channel = bot.get_channel(LOG_CHANNEL_ID)
    if log_channel:
        embed = discord.Embed(
            title="Mitglied Entbannt",
            description=f'{user.mention} wurde auf dem Server entbannt.',
            color=discord.Color.green()
        )
        await log_channel.send(embed=embed)


@bot.event
async def on_member_kick(member, reason):
    log_channel = bot.get_channel(LOG_CHANNEL_ID)
    if log_channel:
        embed = discord.Embed(
            title="Mitglied Gekickt",
            description=f'{member.mention} wurde vom Server gekickt.',
            color=discord.Color.orange()
        )
        if reason:
            embed.add_field(name="Begründung", value=reason, inline=False)
        await log_channel.send(embed=embed)


bot.run(TOKEN)
