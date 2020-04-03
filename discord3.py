import discord

import openpyxl

client = discord.Client()





@client.event

async def on_ready():

    print(client.user.id)

    print("ready")

    game = discord.Game("")

    await client.change_presence(status=discord.Status.online, activity=game)







@client.event

async def on_message(message):

    if message.content.startswith("양승훈 따묵 ㄱㄴ?"):

         await message.channel.send("쌉가능")

    if message.content.startswith("권순혁 따묵 ㄱㄴ?"):

         await message.channel.send("쌉가능")

    if message.content.startswith("김의진 따묵 ㄱㄴ?"):

         await message.channel.send("쌉가능")    

    if message.content.startswith("이진표 따묵 ㄱㄴ?"):

         await message.channel.send("씨발")           

    if message.content.startswith("임동현 따묵 ㄱㄴ?"):

         await message.channel.send("쌉가능")

    if message.content.startswith("조우빈 따묵 ㄱㄴ?"):

         await message.channel.send("쌉가능")

    if message.content.startswith("반서준 따묵 ㄱㄴ?"):

         await message.channel.send("쌉가능")

    if message.content.startswith("박현태 따묵 ㄱㄴ?"):

         await message.channel.send("쌉가능")
















































client.run("Njk1MjIxMzQzNzU0NTE4NTU5.XoYROw.PNqmyp9q5uZkzrDStmFM8B7vdyA")

