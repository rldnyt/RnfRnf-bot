import asyncio
from typing import List, Any, Dict

import discord
from discord.ext import commands

app = commands.Bot(command_prefix='!c')

nameok = 0  # type: int
uerssok = 0  # type: int
xyzok = 0  # type: int
name = {}  # type: Dict[Any, Any]
uers = {}  # type: Dict[Any, Any]
xyz = {}  # type: Dict[Any, Any]
id = {}  # type: Dict[Any, Any]
biob = 0  # type: int
vefa = 0  # type: int

def cls():
    for value in range(1,30):
        print("\n")

@app.event
async def on_ready():
    print("Start SYSTEM")

@app.event
async def on_message(message):
    await app.process_commands(message)
    global nameok
    global uerssok
    global xyzok
    global name
    global uers
    global xyz
    global id
    global biob
    global txte
    global vefa
    if message.content.startswith("!c도움말"):
        embed1 = discord.Embed(
            title = "명령어",
            description="유틸리티",
            colour = 0x7CC8FF
        )
        embed1.add_field(name="사유지 신청합니다. (DM전용)", value="`!c사유지신청`", inline=False)
        embed1.add_field(name="꿀꿀마을서버의 상태을 확인합니다.", value="`!c서버상태`", inline=False)
        embed1.add_field(name="꿀꿀마을 관리자분들의 상태을 확인합니다.", value="`!c관리자`", inline=False)
        embed1.add_field(name=f"꿀꿀마을 관리부 봇의 개발자을 확인합니다.", value="`!c개발자`", inline=False)

        embed2 = discord.Embed(
            title = "명령어",
            description="꿀꿀마을 관리자 전용 명령어",
            colour = 0x7CC8FF
        )
        embed2.add_field(name="꿀꿀마을 디스코드 연동시스템을 관리합니다. 기우전용", value="`!c디스코드연동 [명령어]`", inline=False)
        embed2.add_field(name="꿀꿀마을에서 추방시킵니다(kick)", value="`!c서버추방 [유저 마크 닉네임]`", inline=False)
        embed2.add_field(name="꿀꿀마을에서 밴시킵니다(ban)", value="`!c서버밴 [유저 마크 닉네임]`", inline=False)
        embed2.add_field(name="꿀꿀마을에서 서버가 말합니다(say)", value="`!c서버말하기 [말할네용]`", inline=False)
        embed2.add_field(name="꿀꿀마을에서 대상을 죽임니다(kill)", value="`!c서버죽이기 [유저 마크 닉네임]`", inline=False)
        msg = await message.channel.send(embed=embed1)
        page = [embed1, embed2]
        page2 = int(len(page)) - 1
        await msg.add_reaction("⏪")
        await msg.add_reaction("◀")
        await msg.add_reaction("▶")
        await msg.add_reaction("⏩")
        i = 0
        emoji = ''
        while True:
            try:
                reaction, user = await app.wait_for(
                    'reaction_add')  # Gets the reaction and the user with a timeout of 30 seconds + new Syntax
                if user == message.author:  # Test if the user is the author
                    emoji = str(reaction.emoji)
                    if emoji == '⏪':
                        i = 0
                        await msg.edit(embed=page[i])
                        await msg.remove_reaction(reaction, user)
                    elif emoji == '◀':
                        if i > 0:
                            i -= 1
                            await msg.edit(embed=page[i])
                            await msg.remove_reaction(reaction, user)
                    elif emoji == '▶':
                        if i < page2:
                            i += 1
                            await msg.edit(embed=page[i])
                            await msg.remove_reaction(reaction, user)
                    elif emoji == '⏩':
                        i = page2
                        await msg.edit(embed=page[i])
                        await msg.remove_reaction(reaction, user)
                if app.user != user:
                    await msg.remove_reaction(reaction, user)
            except asyncio.TimeoutError:
                break
    
    if message.content.startswith("!c서버추방"):
        name = message.content[7:]
        admin = [382790138444644353, 371959898814152717, 604927195772878878]
        saverbot = message.guild.get_member(int(708827526549602375))
        status_dict: dict = {discord.Status.online: '온라인',
                             discord.Status.offline: '오프라인',
                             discord.Status.idle: "자리비움",
                             discord.Status.do_not_disturb: "방해금지"}
        user_status = status_dict[saverbot.status]
        if not saverbot:
            embed = discord.Embed(
                title="ERROR!",
                description="서버을 찾을수 없습니다!",
                colour=0x7CC8FF
            )
            await message.channel.send(embed=embed)
            return
        if user_status == '오프라인':
            embed = discord.Embed(
                title="EROOR",
                description="서버가 오프라인입니다!",
                colour=0x7CC8FF
            )
            await message.channel.send(embed=embed)
            return
        if int(message.author.id) in admin:
            if not name:
                await message.channel.send("꿀꿀마을서버에서 추방할 유저의 마크닉네임을 입력하세요")
                return
            channel = app.get_channel(708829471117017138)
            await channel.send(f"kick {name}")
            await message.channel.send(f"{name}유저을 추방하였습니다.")
            await channel.send('tellraw @a [{"text":"[","color":"blue","bold":true},{"text":"디스코드 연동시스템","color":"aqua"},{"text":"]","color":"blue"},{"text":"' + f" {message.author.name}님이 {name}님을 추방하셨습니다." + '"}]')
            return
        await message.channel.send("관리자 전용입니다.")

    if message.content.startswith("!c서버상태"):
        saverbot = message.guild.get_member(int(708827526549602375))
        if not saverbot:
            embed = discord.Embed(
                title="ERROR!",
                description="서버을 찾을수 없습니다!",
                colour=0x7CC8FF
            )
            await message.channel.send(embed=embed)
            return
        status_dict: dict = {discord.Status.online: '온라인',
                             discord.Status.offline: '오프라인',
                             discord.Status.idle: "자리비움",
                             discord.Status.do_not_disturb: "방해금지"}
        user_status = status_dict[saverbot.status]
        if user_status == '오프라인':
            embed = discord.Embed(
                title="꿀꿀마을 서버상태",
                description="서버작동여부 : ☑️오프라인",
                colour=0x7CC8FF
            )
            await message.channel.send(embed=embed)
            return

        embed = discord.Embed(
            title = "꿀꿀마을 서버상태",
            description= "서버작동여부 : ✅온라인",
            colour = 0x7CC8FF
        )
        channel = app.get_channel(708828420922146877)
        saver1 = channel.topic
        channel = app.get_channel(708829471117017138)
        saver2 = channel.topic
        embed.add_field(name="서버정보", value=saver1, inline=True)
        embed.add_field(name="서버컴퓨터 정보", value=saver2, inline=True)
        await message.channel.send(embed=embed)

    if message.content.startswith("!c서버밴"):
        name = message.content[6:]
        admin = [382790138444644353, 371959898814152717, 604927195772878878]
        saverbot = message.guild.get_member(int(708827526549602375))
        status_dict: dict = {discord.Status.online: '온라인',
                             discord.Status.offline: '오프라인',
                             discord.Status.idle: "자리비움",
                             discord.Status.do_not_disturb: "방해금지"}
        user_status = status_dict[saverbot.status]
        if not saverbot:
            embed = discord.Embed(
                title="ERROR!",
                description="서버을 찾을수 없습니다!",
                colour=0x7CC8FF
            )
            await message.channel.send(embed=embed)
            return
        if user_status == '오프라인':
            embed = discord.Embed(
                title="EROOR",
                description="서버가 오프라인입니다!",
                colour=0x7CC8FF
            )
            await message.channel.send(embed=embed)
            return
        if int(message.author.id) in admin:
            if not name:
                await message.channel.send("꿀꿀마을서버에서 밴할 유저의 마크닉네임을 입력하세요")
                return
            channel = app.get_channel(708829471117017138)
            await channel.send(f"ban {name}")
            await message.channel.send(f"{name}유저을 밴하였습니다.")
            await channel.send('tellraw @a [{"text":"[","color":"blue","bold":true},{"text":"디스코드 연동시스템","color":"aqua"},{"text":"]","color":"blue"},{"text":"' + f" {message.author.name}님이 {name}님을 밴하셨습니다." + '"}]')
            return
        await message.channel.send("관리자 전용입니다.")


    if message.content.startswith("!c서버죽이기"):
        name = message.content[8:]
        admin = [382790138444644353, 371959898814152717, 604927195772878878]
        saverbot = message.guild.get_member(int(708827526549602375))
        status_dict: dict = {discord.Status.online: '온라인',
                             discord.Status.offline: '오프라인',
                             discord.Status.idle: "자리비움",
                             discord.Status.do_not_disturb: "방해금지"}
        user_status = status_dict[saverbot.status]
        if not saverbot:
            embed = discord.Embed(
                title="ERROR!",
                description="서버을 찾을수 없습니다!",
                colour=0x7CC8FF
            )
            await message.channel.send(embed=embed)
            return
        if user_status == '오프라인':
            embed = discord.Embed(
                title="EROOR",
                description="서버가 오프라인입니다!",
                colour=0x7CC8FF
            )
            await message.channel.send(embed=embed)
            return
        if int(message.author.id) in admin:
            if not name:
                await message.channel.send("꿀꿀마을서버에서 죽일할 유저의 마크닉네임을 입력하세요")
                return
            channel = app.get_channel(708829471117017138)
            await channel.send(f"kill {name}")
            await message.channel.send(f"{name}유저을 죽였습니다.")
            await channel.send('tellraw @a [{"text":"[","color":"blue","bold":true},{"text":"디스코드 연동시스템","color":"aqua"},{"text":"]","color":"blue"},{"text":"' + f" {message.author.name}님이 {name}님을 죽이셨습니다." + '"}]')
            return
        await message.channel.send("관리자 전용입니다.")
    
    if message.content.startswith("!c서버말하기"):
        name = message.content[8:]
        admin = [382790138444644353, 371959898814152717, 604927195772878878]
        saverbot = message.guild.get_member(int(708827526549602375))
        status_dict: dict = {discord.Status.online: '온라인',
                             discord.Status.offline: '오프라인',
                             discord.Status.idle: "자리비움",
                             discord.Status.do_not_disturb: "방해금지"}
        user_status = status_dict[saverbot.status]
        if not saverbot:
            embed = discord.Embed(
                title="ERROR!",
                description="서버을 찾을수 없습니다!",
                colour=0x7CC8FF
            )
            await message.channel.send(embed=embed)
            return
        if user_status == '오프라인':
            embed = discord.Embed(
                title="EROOR",
                description="서버가 오프라인입니다!",
                colour=0x7CC8FF
            )
            await message.channel.send(embed=embed)
            return
        if int(message.author.id) in admin:
            if not name:
                await message.channel.send("꿀꿀마을서버에 콘솔로 말할(say)할 내용을 입력하세요")
                return
            channel = app.get_channel(708829471117017138)
            await channel.send('tellraw @a [{"text":"[","color":"blue","bold":true},{"text":"디스코드","color":"aqua"},{"text":"]","color":"blue"},{"text":"' + f' {name}' + '"}]')
            await message.channel.send(f"{name}라고 발송했습니다!")
            return
        await message.channel.send("관리자 전용입니다.")

    if message.content.startswith("!c서버언밴"):
        name = message.content[7:]
        admin = [382790138444644353, 371959898814152717, 604927195772878878]
        saverbot = message.guild.get_member(int(708827526549602375))
        status_dict: dict = {discord.Status.online: '온라인',
                             discord.Status.offline: '오프라인',
                             discord.Status.idle: "자리비움",
                             discord.Status.do_not_disturb: "방해금지"}
        user_status = status_dict[saverbot.status]
        if not saverbot:
            embed = discord.Embed(
                title="ERROR!",
                description="서버을 찾을수 없습니다!",
                colour=0x7CC8FF
            )
            await message.channel.send(embed=embed)
            return
        if user_status == '오프라인':
            embed = discord.Embed(
                title="EROOR",
                description="서버가 오프라인입니다!",
                colour=0x7CC8FF
            )
            await message.channel.send(embed=embed)
            return
        if int(message.author.id) in admin:
            if not name:
                await message.channel.send("꿀꿀마을서버에서 언밴할 유저의 마크닉네임을 입력하세요")
                return
            channel = app.get_channel(708829471117017138)
            await channel.send(f"unban {name}")
            await message.channel.send(f"{name}유저을 언밴하였습니다.")
            await channel.send('tellraw @a [{"text":"[","color":"blue","bold":true},{"text":"디스코드 연동시스템","color":"aqua"},{"text":"]","color":"blue"},{"text":"' + f" {message.author.name}님이 {name}님을 언밴하셨습니다." + '"}]')
            return
        await message.channel.send("관리자 전용입니다.")
    
    if message.content.startswith("!c디스코드연동"):
        commmand = message.content[9:]
        saverbot = message.guild.get_member(int(708827526549602375))
        status_dict: dict = {discord.Status.online: '온라인',
                             discord.Status.offline: '오프라인',
                             discord.Status.idle: "자리비움",
                             discord.Status.do_not_disturb: "방해금지"}
        user_status = status_dict[saverbot.status]
        if not saverbot:
            embed = discord.Embed(
                title="ERROR!",
                description="서버을 찾을수 없습니다!",
                colour=0x7CC8FF
            )
            await message.channel.send(embed=embed)
            return
        if user_status == '오프라인':
            embed = discord.Embed(
                title="EROOR",
                description="서버가 오프라인입니다!",
                colour=0x7CC8FF
            )
            await message.channel.send(embed=embed)
            return
        if int(message.author.id) == 371959898814152717:
            if not commmand:
                embed = discord.Embed(
                    title = "!c디스코드연동 도움말",
                    colour = 0x7CC8FF
                )
                embed.add_field(name="마인크래프트 연동내역을 초기화하며 디스코드에서 마크로 채팅시 다시 연동이 필요합니다.", value="`!c디스코드연동 연동초기화`", inline=False)
                embed.add_field(name="디스코드연동을 리로드합니다", value="`!c디스코드연동 리로드`", inline=False)
                embed.add_field(name="디스코드연동을 디버그합니다", value="`!c디스코드연동 디버그`", inline=False)
                await message.channel.send(embed=embed)
                return
            if commmand == "리로드":
                await message.channel.send("리로드을 실행합니다!")
                channel = app.get_channel(708829471117017138)
                await channel.send("discord broadcast [디스코드 연동 시스템] 디스코드 연동시스템 리로드을 시작합니다")
                await channel.send('tellraw @a [{"text":"[","color":"blue","bold":true},{"text":"디스코드 연동시스템","color":"aqua"},{"text":"]","color":"blue"},{"text":" 디스코드 연동시스템 리로드을 시작합니다."}]')
                await channel.send("discord reload")
                await channel.send("discord broadcast [디스코드 연동 시스템] 디스코드 연동시스템 리로드을 완료했습니다.")
                await channel.send('tellraw @a [{"text":"[","color":"blue","bold":true},{"text":"디스코드 연동시스템","color":"aqua"},{"text":"]","color":"blue"},{"text":" 디스코드 연동시스템 리로드 완료되었습니다."}]')
            if commmand == "연동초기화":
                channel = app.get_channel(708829471117017138)
                await channel.send("discord clearlinked")
                await channel.send("discord broadcast [디스코드 연동 시스템] 디스코드 서버연동을 모두 제거하였습니다")
                await channel.send('tellraw @a [{"text":"[","color":"blue","bold":true},{"text":"디스코드 연동시스템","color":"aqua"},{"text":"]","color":"blue"},{"text":" 디스코드 연동시스템 마크 연동리스트을 초기화 하였습니다. 연동시스템 이용자분들은 다시 마크 연동을 해주시기 바람니다!"}]')

            if commmand == "디버그":
                await message.channel.send("리로드을 실행합니다!")
                channel = app.get_channel(708829471117017138)
                await channel.send("discord broadcast [디스코드 연동 시스템] 디스코드 연동시스템 디버그을 시작합니다")
                await channel.send('tellraw @a [{"text":"[","color":"blue","bold":true},{"text":"디스코드 연동시스템","color":"aqua"},{"text":"]","color":"blue"},{"text":" 디스코드 연동시스템 디버그을 시작합니다."}]')
                await channel.send("discord debug")
                await channel.send("discord broadcast [디스코드 연동 시스템] 디스코드 연동시스템 디버그을 완료했습니다.")
                await channel.send('tellraw @a [{"text":"[","color":"blue","bold":true},{"text":"디스코드 연동시스템","color":"aqua"},{"text":"]","color":"blue"},{"text":" 디스코드 연동시스템 디버그 완료되었습니다."}]')
        else:
            await message.channel.send("기우 전용입니다.")

    if message.content.startswith("!c관리자"):
        rhksflwk1 = message.guild.get_member(int(382790138444644353))
        rhksflwk2 = message.guild.get_member(int(371959898814152717))
        rhksflwk3 = message.guild.get_member(int(604927195772878878))
        if not rhksflwk1:
            embed = discord.Embed(
                title="ERROR!",
                description="꿀돼지님을 찾을수없습니다!",
                colour=0x7CC8FF
            )
            await message.channel.send(embed=embed)
            return
        elif not rhksflwk2:
            embed = discord.Embed(
                title="ERROR!",
                description="기우님을 찾을수없습니다!",
                colour=0x7CC8FF
            )
            await message.channel.send(embed=embed)
            return
        elif not rhksflwk3:
            embed = discord.Embed(
                title="ERROR!",
                description="랩님을 찾을수없습니다!",
                colour=0x7CC8FF
            )
            await message.channel.send(embed=embed)
            return
        status_dict: dict = {discord.Status.online: '온라인',
                             discord.Status.offline: '오프라인',
                             discord.Status.idle: "자리비움",
                             discord.Status.do_not_disturb: "방해금지"}
        user_status1 = status_dict[rhksflwk1.status]
        user_status2 = status_dict[rhksflwk2.status]
        user_status3 = status_dict[rhksflwk3.status]
        embed = discord.Embed(
            title="관리자",
            description=f"꿀돼지\n -{user_status1}\n\n랩\n -{user_status3}\n\n 기우\n -{user_status2}",
            colour=0x7CC8FF
        )
        await message.channel.send(embed=embed)

    if message.content.startswith("!c개발자"):
        embed = discord.Embed(
            title="개발자",
            description=f"개발자 : <@371959898814152717> | <@604927195772878878>\n\n-포로그래밍 언어(Py)\n Discord.py : {discord.__version__}",
            colour=0x7CC8FF
        )
        await message.channel.send(embed=embed)

app.run('NzIzMTA4MjI2Nzk4ODQ2MDAz.Xus27w.yF12PbsogRtNefUY4JTmadcqwac')