import discord
from discord.ext import commands

target_word = [""] # 抜けたいグループの名前
token = "" # あなたのトークン
client = commands.Bot(command_prefix="!",self_bot=True)

@client.event
async def on_ready():
    print(f"ログインしました: {client.user}")
    count = 0
    for dm in client.private_channels:
        if dm.type == discord.ChannelType.group:
            if dm.name in target_word:
                await dm.leave()
                print(f'退出完了：{dm.id}')
                count+=1
    print(f"合計 {count} 個のグループDMから退出しました。")
    await client.close()

client.run()