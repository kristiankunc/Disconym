import discord
import asyncio
from discord.ext import commands
from db_actions import Database
from discord.utils import get

class Database_ctr(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def db(self, ctx):
        author = ctx.message.author
        pfp = author.avatar_url

        emoji_one = "1️⃣"
        emoji_two = "2️⃣"
        emoji_three = "3️⃣"
        emoji_four = "4️⃣"
        emoji_five = "5️⃣"

        if ctx.author.id == 289411795423199232:
                
            channel = ctx.channel

            def define_embed(title, desc):
                embed=discord.Embed(title=title, description=desc, color=0xf49b01)
                embed.set_footer(text=f"Executed by {ctx.author.name}", icon_url=pfp)
                return embed

            embed = await ctx.send(embed = define_embed("Chose category", f"{emoji_one} - Prefix\n{emoji_two} - Blacklist"))
            await embed.add_reaction(emoji_one)
            await embed.add_reaction(emoji_two)

            def check(reaction, user):
                return user == ctx.author

            try:
                reaction, user = await self.client.wait_for('reaction_add', timeout=15.0, check=check)
            except asyncio.TimeoutError:
                pass
            else:
                await embed.clear_reactions()
                if str(reaction.emoji) == emoji_one:
                    # PREFIX

                    await embed.edit(embed = define_embed("Chose action for Prefix", f"{emoji_one} - Add prefix\n{emoji_two} - remove prefix\n{emoji_three} - replace prefix"))
                    await embed.add_reaction(emoji_one)
                    await embed.add_reaction(emoji_two)
                    await embed.add_reaction(emoji_three)

                    try:
                        reaction, user = await self.client.wait_for('reaction_add', timeout=15.0, check=check)
                    except asyncio.TimeoutError:
                        pass
                    else:
                        await embed.clear_reactions()
                        if str(reaction.emoji) == emoji_one:
                            # ----- ADD PREFIX -----

                            await embed.edit(embed = define_embed("Please send the guild/server ID", f"Example - `174837853778345984`"))

                            guild_id_msg = await self.client.wait_for("message", check=lambda m:m.author==ctx.author and m.channel.id==ctx.channel.id)
                            await guild_id_msg.delete()

                            await embed.edit(embed = define_embed("Please send the prefix", f"Example - `!`"))

                            prefix_msg = await self.client.wait_for("message", check=lambda m:m.author==ctx.author and m.channel.id==ctx.channel.id)
                            await prefix_msg.delete()

                            Database.add_prefix(guild_id_msg.content, prefix_msg.content)

                            await embed.edit(embed = define_embed("Prefix set", f"Guild ID - `{guild_id_msg.content}`\nPrefix - `{prefix_msg.content}`"))


                        elif str(reaction.emoji) == emoji_two:
                            # ----- REMOVE PREFIX -----

                            await embed.edit(embed = define_embed("Please send the guild/server ID", f"Example - `174837853778345984`"))

                            guild_id_msg = await self.client.wait_for("message", check=lambda m:m.author==ctx.author and m.channel.id==ctx.channel.id)
                            await guild_id_msg.delete()

                            Database.remove_prefix(guild_id_msg.content)

                            await embed.edit(embed = define_embed("Prefix removed", f"Guild ID - `{guild_id_msg.content}`"))


                        elif str(reaction.emoji) == emoji_three:
                            # ----- REPLACE PREFIX -----

                            await embed.edit(embed = define_embed("Please send the guild/server ID", f"Example - `174837853778345984`"))

                            guild_id_msg = await self.client.wait_for("message", check=lambda m:m.author==ctx.author and m.channel.id==ctx.channel.id)
                            await guild_id_msg.delete()

                            await embed.edit(embed = define_embed("Please send the prefix", f"Example - `!`"))

                            prefix_msg = await self.client.wait_for("message", check=lambda m:m.author==ctx.author and m.channel.id==ctx.channel.id)
                            await prefix_msg.delete()

                            Database.replace_prefix(guild_id_msg.content, prefix_msg.content)

                            await embed.edit(embed = define_embed("Prefix replaced", f"Guild ID - `{guild_id_msg.content}`\nPrefix - `{prefix_msg.content}`"))

                elif str(reaction.emoji) == emoji_two:
                    # ---------- BLACKLIST ----------
                    
                    await embed.edit(embed = define_embed("Chose action for Blacklist", f"{emoji_one} - Add user to blacklist\n{emoji_two} - Remove user from blacklist"))

                    await embed.add_reaction(emoji_one)
                    await embed.add_reaction(emoji_two)

                    try:
                        reaction, user = await self.client.wait_for('reaction_add', timeout=15.0, check=check)
                    except asyncio.TimeoutError:
                        pass
                    else:
                        await embed.clear_reactions()
                        if str(reaction.emoji) == emoji_one:
                            # ----- ADD TO BLACKLIST -----

                            await embed.edit(embed = define_embed("Please send the user ID", f"Example - `289411795423199232`"))

                            user_id_msg = await self.client.wait_for("message", check=lambda m:m.author==ctx.author and m.channel.id==ctx.channel.id)
                            await user_id_msg.delete()

                            await embed.edit(embed = define_embed("Please send the blacklist reason", f"Example - `harassment`"))

                            reason_msg = await self.client.wait_for("message", check=lambda m:m.author==ctx.author and m.channel.id==ctx.channel.id)
                            await reason_msg.delete()

                            Database.add_blacklist(user_id_msg.content, reason_msg.content)

                            await embed.edit(embed = define_embed("User added to blacklist", f"User ID - `{user_id_msg.content}`\nUser profile - <@{user_id_msg.content}>\nBlacklist reason - `{reason_msg.content}`"))


                        elif str(reaction.emoji) == emoji_two:
                            # ----- REMOVE FROM BLACKLIST -----

                            await embed.edit(embed = define_embed("Please send the user ID", f"Example - `289411795423199232`"))

                            user_id_msg = await self.client.wait_for("message", check=lambda m:m.author==ctx.author and m.channel.id==ctx.channel.id)
                            await user_id_msg.delete()

                            Database.remove_blacklist(user_id_msg.content)
                            await embed.edit(embed = define_embed("User removed from blacklist", f"User ID - `{user_id_msg.content}`\nUser profile - <@{user_id_msg.content}>"))


def setup(client):
    client.add_cog(Database_ctr(client))