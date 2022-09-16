from tokenize import Token
from discord.ext import commands
from discord.utils import get
from datetime import datetime
from PIL import Image,ImageDraw,ImageFont
from urllib import parse, request
from urllib.request import Request, urlopen
from botid import TOKEN
import discord
import random
import shutil
import re
import os
import youtube_dl
import asyncio

token=TOKEN

intents = discord.Intents.all()
intents.members = True
bot=commands.Bot(command_prefix=".",intents=intents)

aber=["No","Sí","Probablemente","Amén","´Tai cagao","Eso mismo!",
      "Ninguna de las anteriores","Dificilmente","No cuentes con ello"]

Coin=["Cara","Sello"]

Slaps=["https://c.tenor.com/iDdGxlZZfGoAAAAC/powerful-head-slap.gif",
       "https://c.tenor.com/FJsjk_9b_XgAAAAC/anime-hit.gif",
       "https://c.tenor.com/UDo0WPttiRsAAAAd/bunny-girl-slap.gif",
       "https://c.tenor.com/hNa8BhraaXsAAAAC/anime-nagatoro.gif",
       "https://c.tenor.com/ydg0wBHVDYYAAAAC/deku-x-uraraka-izuku-midoriya.gif",
       "https://c.tenor.com/UH8Jnl1W3CYAAAAC/anime-punch-anime.gif",
       "https://c.tenor.com/wOCOTBGZJyEAAAAS/chikku-neesan-girl-hit-wall.gif",
       "https://c.tenor.com/noSQI-GitQMAAAAC/mm-emu-emu.gif",
       "https://c.tenor.com/ra17G61QRQQAAAAC/tapa-slap.gif",
       "https://c.tenor.com/hs6GB44v8aQAAAAS/one-punch-man-%E3%83%AF%E3%83%B3%E3%83%91%E3%83%B3%E3%83%9E%E3%83%B3.gif",
       "https://c.tenor.com/laW-dCBdPUgAAAAC/dragon-ball-super-goku.gif",
       "https://c.tenor.com/6a42QlkVsCEAAAAS/anime-punch.gif",
       "https://c.tenor.com/ASTLdR-E020AAAAC/gurrenlagann-punch.gif",
       "https://c.tenor.com/zQ3NaKiTjPoAAAAC/jujutsu-kaisen-jjk.gif",
       "https://c.tenor.com/NIykTBbyUkkAAAAC/hit-in-the-face-vi.gif",
       "https://c.tenor.com/H7dQ7AbTE6AAAAAC/slap-vi.gif"]
badslaps=["https://c.tenor.com/1okecHTMcQAAAAAd/garou-saitama.gif",
          "https://c.tenor.com/vxN7L8zVMhcAAAAd/saitama-garou.gif",
          "https://c.tenor.com/4fvL1LlpS7YAAAAC/anime-seven-deadly-sins.gif",
          "https://c.tenor.com/Eh4n86g9bKQAAAAC/anime-anime-fight.gif",
          "https://c.tenor.com/Omso9-Xe5aEAAAAd/ruijerd-orsted.gif",
          "https://c.tenor.com/c9iW3pAPAggAAAAd/rudeus-eris.gif",
          "https://c.tenor.com/AZ4q5hoFhZMAAAAd/one-punch-man-checkmate.gif",
          "https://c.tenor.com/5VqKrI1_o3kAAAAd/vinland-saga-anime.gif"]

dead=["https://c.tenor.com/X13wwMFZN2YAAAAC/dies-cat.gif",
      "https://c.tenor.com/7crdHrZL5dsAAAAd/po-dies.gif",
      "https://c.tenor.com/rp8_FjK0CdAAAAAd/dies-of-death.gif",
      "https://c.tenor.com/B-x2kXqxJp8AAAAC/dies-over.gif",
      "https://c.tenor.com/x6RE2fM-x7sAAAAC/dia-kurosawa-dies-of-death.gif",
      "https://c.tenor.com/f5OyojGcVEkAAAAC/dies-cat.gif",
      "https://c.tenor.com/90o5KvIU83MAAAAC/cringe-dies.gif",
      "https://c.tenor.com/NUorFWMkXPwAAAAC/when-you.gif"]

rene=["https://c.tenor.com/afpd2HbAQiEAAAAd/me-rio-toda-la-noche-loco-rene.gif",
      "https://c.tenor.com/8VqY0bZefGMAAAAd/loco-rene.gif"]

risas=["https://c.tenor.com/NKixHpQovGkAAAAC/hououin-kyouma-laugh.gif",
       "https://c.tenor.com/_K0Ka3QwccYAAAAC/uzaki-laugh-xd.gif",
       "https://c.tenor.com/3kti9gaE4sUAAAAC/hayase-nagatoro-nagatoro-laughing.gif",
       "https://c.tenor.com/B-expmjx5R0AAAAC/natsu-lol.gif",
       "https://c.tenor.com/8nSbJK3j7EUAAAAC/laugh-anime.gif",
       "https://c.tenor.com/eOFR0yUSotEAAAAC/satania-laughing.gif",
       "https://c.tenor.com/An-9HfjvNkwAAAAC/kuroo-tetsurou-haikyuu.gif",
       "https://c.tenor.com/fqRNsILmXHQAAAAC/anime-girl.gif",
       "https://c.tenor.com/Ypo7sWozoyIAAAAC/laugh-evil-laugh.gif",
       "https://c.tenor.com/mw1lt6ibZKwAAAAC/zero-two-darling-in-the-franxx.gif",
       "https://c.tenor.com/E44Jsf5cgdAAAAAd/norman-the.gif",
       "https://c.tenor.com/9sDd42kV92YAAAAC/tet-ngnl.gif",
       "https://c.tenor.com/99eXblL5Ek4AAAAC/arcane-powder.gif"]

su=["https://c.tenor.com/jYOAyPGu6vcAAAAC/tft-league-of-legends.gif",
    "https://c.tenor.com/43Y-CzPrr-gAAAAd/league-of-legends-lol.gif",
    "https://c.tenor.com/ufGaFbf1s88AAAAM/jayce-viktor.gif",
    "https://c.tenor.com/NlQ8fVMoEYsAAAAC/apex-apex-legends.gif",
    "https://c.tenor.com/H92F0UxWhxYAAAAM/caitlyn-virtual-hug.gif",
    "https://c.tenor.com/OOWs4FTx3VcAAAAM/among-us-sonic.gif",
    "https://c.tenor.com/YFXFdb4GeYoAAAAM/rainbow-six-siege-wanna-play-r6.gif"]

bailes=["https://c.tenor.com/5lVS_Nyo0gcAAAAM/htncold.gif",
        "https://c.tenor.com/FaTqQp3C2DkAAAAM/dua-dance.gif",
        "https://c.tenor.com/EBTwivH-5z0AAAAM/blackpink-lisa.gif",
        "https://c.tenor.com/p39xFbUfMaMAAAAM/what-my-life-would-be-like-if-i-robbed-the-kwik-e-mart-the-simpsons.gif",
        "https://c.tenor.com/QM04KVsrJLYAAAAC/my-hero-academia-mina-ashido.gif",
        "https://c.tenor.com/AdyEJOsu4AcAAAAC/marge-simpson.gif",
        "https://c.tenor.com/rBYJOboc95EAAAAd/kun-aguero-kun.gif",
        "https://c.tenor.com/mKTS5nbF1zcAAAAd/cute-anime-dancing.gif",
        "https://c.tenor.com/Ub1tR0QeNqwAAAAM/jennie-jennie-kim.gif",
        "https://c.tenor.com/CVxkF4emy5AAAAAM/happy-dance-frog.gif",
        "https://c.tenor.com/zDng4N4u1CQAAAAC/dance-anime.gif",
        "https://c.tenor.com/_ORGJLIoHVQAAAAM/dancing-cat.gif",
        "https://c.tenor.com/ITYJApjoSpEAAAAd/nagatoro-hayase-nagatoro.gif"]

cring=["https://c.tenor.com/WarZqLGgTHoAAAAM/oh-no-cringe-cringe.gif",
       "https://c.tenor.com/6oSEDVpeB-YAAAAM/dies-of-cringe-cringe.gif",
       "https://c.tenor.com/umnf_HFnxCoAAAAM/pooh-bear-im-out.gif",
       "https://c.tenor.com/GoPVjDWYGqcAAAAd/cringe-garfield.gif",
       "https://c.tenor.com/A6iWuIvhjT4AAAAM/thanos-dies-of-cringe.gif",
       "https://c.tenor.com/UV6_Q8atJwwAAAAC/dies-from-cringe-pink.gif",
       "https://c.tenor.com/DSS-FPbgwVYAAAAC/turret-gun.gif",
       "https://c.tenor.com/mI6RzXAfbQQAAAAS/dies-from-cringe-voldemort.gif"]

sad=["https://c.tenor.com/YM3fW1y6f8MAAAAC/crying-cute.gif",
     "https://c.tenor.com/ZncIFM9jiMoAAAAC/anime-crying.gif",
     "https://c.tenor.com/NMiID29TUvIAAAAC/hunter-x-hunter-gon-freecs.gif",
     "https://c.tenor.com/7cpM0BTTbm0AAAAC/sad-face.gif",
     "https://c.tenor.com/zfmbNj3IpAgAAAAC/sorry-crying.gif",
     "https://c.tenor.com/QOHLNwiutPwAAAAd/sylphy-mushoku-tensei.gif",
     "https://c.tenor.com/h90-dQzIyVIAAAAd/dr-stone-ishigami-senku.gif",
     "https://c.tenor.com/1raYW_MZrMwAAAAM/dog-cute.gif",
     "https://c.tenor.com/CLiwStZHc_oAAAAd/sad-gibbon-sad.gif",
     "https://c.tenor.com/WtlvAQKd0s8AAAAC/anime-anime-cry.gif",
     "https://c.tenor.com/tbQSXR4MGU0AAAAC/aoi-todo.gif",
     "https://c.tenor.com/777c5_jRXLQAAAAC/dead-inside.gif",
     "https://c.tenor.com/Qa2sneWEWKIAAAAC/josee-to-tora-to-sakana-tachi.gif",
     "https://c.tenor.com/v_5yyCcy-noAAAAC/no-game-no-life-crying.gif",
     "https://c.tenor.com/xEg5mDYwWSoAAAAd/arcane-jinx.gif"]

mad=["https://c.tenor.com/rzDkOlEDun0AAAAC/hayase-nagatoro-nagatoro-angry.gif",
     "https://c.tenor.com/X3x3Y2mp2W8AAAAC/anime-angry.gif",
     "https://c.tenor.com/ikKAd57zDEwAAAAd/anime-mad.gif",
     "https://c.tenor.com/W9kzAnY4pQoAAAAd/ram-anime.gif",
     "https://c.tenor.com/7dWlqDyO8wYAAAAC/anime-angry.gif",
     "https://c.tenor.com/HzZIzXahdw0AAAAC/one-punch-man-saitama.gif",
     "https://c.tenor.com/MifS9QJUGA4AAAAC/anime-angry.gif",
     "https://c.tenor.com/SvQTNpCojFkAAAAC/umaru-himouto-umaru-chan.gif",
     "https://c.tenor.com/3Wb9efNi86EAAAAd/rat-clenches-fist-of-rage-rat.gif",
     "https://c.tenor.com/uM5_PN283uUAAAAC/pissed-saitama.gif",
     "https://c.tenor.com/t02NweN43-0AAAAd/eris-boreas-greyrat-mushoku-tensei.gif",
     "https://c.tenor.com/XfrqyR_-jzIAAAAC/anime-goku.gif",
     "https://c.tenor.com/d3aqVkS4LiQAAAAd/that-time-i-got-reincarnated-as-a-slime-reincarnated-as-a-slime.gif",
     "https://c.tenor.com/ndWcgemT5ZcAAAAd/vinland-saga-thorfinn.gif",
     "https://c.tenor.com/UAx2IDoQUMsAAAAd/komi-cant-communicate-komii.gif",
     "https://c.tenor.com/dpbf1nXNWK0AAAAC/league-of-legends-arcane.gif",
     "https://c.tenor.com/VrmPUt4uC14AAAAC/arcane-jinx.gif",
     "https://c.tenor.com/fFFtMNWjvf4AAAAC/eye-powder.gif"]

chao=["https://c.tenor.com/46LtwneNFb8AAAAC/logging-off-discord-discord.gif",
      "https://c.tenor.com/JA1FUwUy1t8AAAAC/run-away-im-out.gif",
      "https://c.tenor.com/01cElrH1Ed8AAAAC/anime-shiro.gif",
      "https://c.tenor.com/pD1kmkC501UAAAAC/naruto-akatsuki.gif",
      "https://c.tenor.com/gBz7kkp8T08AAAAC/evangelion-shinji-ikari.gif",
      "https://c.tenor.com/zyvSgcRyXDkAAAAC/spirited-away-studio-ghibli.gif",
      "https://c.tenor.com/VPRdxgMr2l8AAAAC/anime.gif",
      "https://c.tenor.com/0X-69vStx4QAAAAd/truck-hit.gif",
      "https://c.tenor.com/TcIloOWn9HMAAAAC/emoji-bye.gif",
      "https://c.tenor.com/1Uy3ws0JNT0AAAAd/jinx-bye.gif",
      "https://c.tenor.com/QzmDc6v-lvAAAAAC/jinx-arcane.gif",
      "https://c.tenor.com/K7bUrVCka5YAAAAd/bye-k-bye.gif",
      "https://c.tenor.com/UuZmQv3YdoIAAAAC/dahliabunni-angel-beats.gif"]

flop=["https://c.tenor.com/QBV3pyz4NLEAAAAd/floppa-kimbo.gif",
      "https://c.tenor.com/ASPoZ-hJLNQAAAAd/caracal-big.gif",
      "https://c.tenor.com/32KwNDctmFMAAAAC/funni-flop.gif",
      "https://c.tenor.com/RFmgfvXWOsAAAAAd/floppa-big-floppa.gif",
      "https://c.tenor.com/w2y8CR5qAiYAAAAd/floppa-big-floppa.gif",
      "https://c.tenor.com/_2YXV8CEP_4AAAAd/floppa-floppa-run.gif",
      "https://c.tenor.com/nnaKnfHYvUIAAAAd/floppa-cat-fight.gif",
      "https://c.tenor.com/c0nqR17b06gAAAAd/flopa-floppa.gif",
      "https://c.tenor.com/mZDUs7-HijkAAAAd/elisttm-rhc.gif",
      "https://c.tenor.com/QFvn_7hsiQcAAAAM/floppa-big.gif",
      "https://c.tenor.com/kVfrg-iSDEsAAAAd/floppa-hiss-floppa-angery.gif",
      "https://c.tenor.com/VSo1vJy0cK0AAAAd/floppa-based.gif",
      "https://c.tenor.com/P5_R8eEwvlcAAAAd/floppa-big-floppa.gif",
      "https://c.tenor.com/QLs7l7ZcXz8AAAAd/caracal-big-floppa.gif"]

zeta=["https://c.tenor.com/TzkLlnAZZfUAAAAC/zzz-sleeping.gif",
      "https://c.tenor.com/xlTcO7a7X30AAAAC/cat-sleep.gif",
      "https://c.tenor.com/pHiHzQRlxV4AAAAd/zzzzz-sleepy-dog.gif",
      "https://c.tenor.com/IbrIdOgbqDIAAAAC/bunny-rabbit.gif",
      "https://c.tenor.com/p-eFrJqiEhEAAAAC/emoji-sleepy.gif",
      "https://c.tenor.com/3QSDIxvUNw0AAAAC/boring-sleep.gif",
      "https://c.tenor.com/KxJJ9DSWBbwAAAAC/mr-bean-bean.gif",
      "https://c.tenor.com/M1fCfdEehOIAAAAC/boring-dormido.gif",
      "https://c.tenor.com/8f942lxw95QAAAAC/sleepy-sleepy-fall.gif",
      "https://c.tenor.com/r26BPVTzWWIAAAAC/bored-boring.gif",
      "https://c.tenor.com/ZzNztJJSUCgAAAAC/snorlax-tired.gif"]

losk=[["1","https://cdn5.dibujos.net/dibujos/pintados/202009/numero-1-letras-y-numeros-numeros-11714504.jpg",0],
      ["2","https://cdn5.dibujos.net/dibujos/pintados/201609/numero-2-letras-y-numeros-numeros-10452244.jpg",1],
      ["3","https://cdn5.dibujos.net/dibujos/pintados/201605/numero-3-letras-y-numeros-numeros-10408662.jpg",2],
      ["4","https://cdn5.dibujos.net/dibujos/pintados/201549/numero-4-letras-y-numeros-numeros-10286035.jpg",3]]

def to_upper(argument):
    return argument.upper()

def listaboni(lista):
    for i in range(len(lista)):
        listacoma = lista[i].split(" ")
        lista[i] = listacoma
    return lista

def listaboni2(lista):
    for i in range(len(lista)):
        listacoma = lista[i].split("↔")
        lista[i] = listacoma
    return lista


def victory(tablero):
        for i in tablero:
            if (i[0] == "X" and i[1] == "X" and i[2] == "X"):
                return "X"
            elif (i[0] == "O" and i[1] == "O" and i[2] == "O"):
                return "O"
        for j in range(3):
            if (tablero[0][j] == "O" and tablero[1][j] == "O" and tablero[2][j] == "O"):
                return "O"
            elif (tablero[0][j] == "X" and tablero[1][j] == "X" and tablero[2][j] == "X"):
                return "X"
        if (tablero[0][0] == "O" and tablero[1][1] == "O" and tablero[2][2] == "O") or (
                tablero[2][0] == "O" and tablero[1][1] == "O" and tablero[0][2] == "O"):
            return "O"
        elif (tablero[0][0] == "X" and tablero[1][1] == "X" and tablero[2][2] == "X") or (
                tablero[2][0] == "X" and tablero[1][1] == "X" and tablero[0][2] == "X"):
            return "X"


@bot.command()
async def ping(ctx):
    embed=discord.Embed(title="pong",color=discord.Color.red())
    embed.set_image(url="https://media2.giphy.com/media/fvA1ieS8rEV8Y/200.gif")
    await ctx.send(embed=embed)

@bot.command()
async def eightball(ctx,*,msg):
    a=random.choice(aber)
    embed=discord.Embed(title=msg,description=a,color=discord.Color.red())
    embed.set_image(url="https://c.tenor.com/FLV7sGtaM9oAAAAC/toy-story-woody.gif")
    await ctx.send(embed=embed)

@bot.command()
async def coin(ctx):
    a=random.choice(Coin)
    embed=discord.Embed(title="Resultado",description=a,color=discord.Color.red())
    await ctx.send("https://i.imgur.com/PdcSA9G.gif?noredirect")
    await asyncio.sleep(3)
    if a=="Cara":
        embed.set_image(url="https://pepeschile.com/wp-content/uploads/2018/05/n100a.jpg")
    elif a=="Sello":
        embed.set_image(url="https://pepeschile.com/wp-content/uploads/2018/05/n100r.jpg")
    await ctx.send(embed=embed)

@bot.command()
async def info(ctx):
    embed=discord.Embed(title=f"{ctx.guild.name}",description="[Frase motivacional]",timestamp=datetime.utcnow(), color=discord.Color.red())
    embed.add_field(name="El servidor fue creado el", value=str(ctx.guild.created_at)[:len(str(ctx.guild.created_at))-16])
    embed.add_field(name="El dueño es", value=str(ctx.guild.owner)[:len(str(ctx.guild.owner))-5])
    embed.add_field(name="Region del server",value=ctx.guild.region)
    embed.add_field(name="ID del servidor",value=ctx.guild.id)
    embed.set_image(url=ctx.guild.icon_url)
    await ctx.send(embed=embed)

@bot.command()
async def avatar(ctx,*, member: discord.Member):
    a=member.avatar_url
    embed=discord.Embed(title="Contemplen la preciosura de "+str(member)[:len(str(member))-5],color=discord.Color.red())
    embed.set_image(url=a)
    await ctx.send(embed=embed)

@bot.command()
async def say(ctx,*,msg):
    a=msg
    embed=discord.Embed(title=a,color=discord.Color.red())
    embed.set_image(url="https://i.pinimg.com/originals/64/8e/ac/648eac9c33c4042c28a702d1889a8a8f.gif")
    await ctx.send(embed=embed)

@bot.command()
async def gritar(ctx,*,content):
    a=to_upper(content)
    embed=discord.Embed(title=a,color=discord.Color.red())
    embed.set_image(url="https://img-s1.onedio.com/id-59bfc7f5f6ee3e9811ace75a/rev-0/w-900/h-661/f-gif/s-4e83005103e2581dbf0676c2e89e564765894ddc.gif")
    await ctx.send(embed=embed)

@bot.command()
async def jelp(ctx):
    out="ping\neightball {pregunta}\ncoin\ninfo\nsay {mensaje}\ngritar {mensaje}\nunidoel {@usuario}\nslap {@usuario}\ndies\nrenepuente\nmatch {@usuario} {@usuario} (falta enchular)\nsalesu\nreir\ndance\ncringe\nfloppa\nclear {cantidad de mensajes a borrar}\ntriste\nenojao\nzzz\nbye\navatar {@usuario}\ngato {y} {x}\nreset (resetea la partida de .gato)\nyoutube {busqueda}\nepic {busqueda}\nanime {busqueda}\nepicfree\nminas {accion (e: explorar/m: marcar/d: desmarcar)} {posición (1-64})\nreset2 (reseta la partida de .minas)\nsudoku {número de datos no iniciales}"
    await ctx.send(out)

@bot.command()
async def unidoel(ctx, *, member: discord.Member): #arreglar la resta
    a="{0.joined_at}".format(member)
    anou=a[:4]
    mesu=a[5:7]
    diau=a[8:10]
    b=str(datetime.today())
    ano=b[:4]
    mes=b[5:7]
    dia=b[8:10]
    entro=False
    if (int(mesu)<=int(mes) and int(ano)!=int(anou) and int(ano)>int(anou)) or int(ano)-int(anou)>1:
        aa=abs(int(ano)-int(anou))
    else:
        aa=0
    if ano!=anou and int(mesu)>int(mes):
        mm=(12-int(mesu))+int(mes)
    else:
        mm=abs(int(mes)-int(mesu))
    if int(mes)<int(mesu) and aa!=0:
        aa-=1
    if int(dia)<int(diau):
        mm-=1
        entro=True
    dd=abs(int(dia)-int(diau))
    if entro==True:
        dd=30-dd
    c="Y es "+str(aa)+" año(s) "+str(mm)+" mes(es) y "+str(dd)+" dia(s) de viejo"
    d='{0} se unió el {0.joined_at}'.format(member)
    await ctx.send(d[:len(d)-15])
    await ctx.send(c)

@bot.command()
async def slap(ctx,*,member: discord.Member):
    b=str(ctx.author)
    d=str(member)
    if str(member)!="tutulio#4162":
        a=random.choice(Slaps)
        embed = discord.Embed(title=b[:len(b)-5] + " golpea a " + d[:len(d)-5], color=discord.Color.red())
    else:
        a=random.choice(badslaps)
        embed = discord.Embed(title=b[:len(b)-5] + " intenta golpear a " + d[:len(d)-5]+" pero sale mal", color=discord.Color.red())
    embed.set_image(url=a)
    await ctx.send(embed=embed)

@bot.command()
async def dies(ctx):
    b=str(ctx.author)
    a=random.choice(dead)
    embed=discord.Embed(title=str(b)[:len(b)-5]+" se muere",color=discord.Color.red())
    embed.set_image(url=a)
    await ctx.send(embed=embed)

@bot.command()
async def renepuente(ctx):
    a=random.choice(rene)
    embed = discord.Embed(title="Simplemente Rene Puente", color=discord.Color.red())
    embed.set_image(url=a)
    await ctx.send(embed=embed)

@bot.command()
async def reir(ctx):
    a=random.choice(risas)
    b=str(ctx.author)
    embed = discord.Embed(title=b[:len(b)-5]+" se rie", color=discord.Color.red())
    embed.set_image(url=a)
    await ctx.send(embed=embed)

@bot.command()
async def zzz(ctx):
    a=random.choice(zeta)
    b=str(ctx.author)
    embed = discord.Embed(title=b[:len(b)-5]+" esta zzz", color=discord.Color.red())
    embed.set_image(url=a)
    await ctx.send(embed=embed)

@bot.command()
async def salesu(ctx):
    a=random.choice(su)
    b=str(ctx.author)
    embed = discord.Embed(title=b[:len(b)-5]+" busca pene", color=discord.Color.red())
    embed.set_image(url=a)
    await ctx.send(embed=embed)

@bot.command()
async def dance(ctx):
    a=random.choice(bailes)
    b=str(ctx.author)
    embed = discord.Embed(title=b[:len(b)-5]+" baila de pana", color=discord.Color.red())
    embed.set_image(url=a)
    await ctx.send(embed=embed)

@bot.command()
async def cringe(ctx):
    a=random.choice(cring)
    b=str(ctx.author)
    embed = discord.Embed(title=b[:len(b)-5]+" se siente cringeado", color=discord.Color.red())
    embed.set_image(url=a)
    await ctx.send(embed=embed)

@bot.command()
async def triste(ctx):
    a=random.choice(sad)
    b=str(ctx.author)
    embed = discord.Embed(title=b[:len(b)-5]+" se siente sad", color=discord.Color.red())
    embed.set_image(url=a)
    await ctx.send(embed=embed)

@bot.command()
async def enojao(ctx):
    a=random.choice(mad)
    b=str(ctx.author)
    embed = discord.Embed(title=b[:len(b)-5]+" ´ta enojao", color=discord.Color.red())
    embed.set_image(url=a)
    await ctx.send(embed=embed)

@bot.command()
async def bye(ctx):
    a=random.choice(chao)
    b=str(ctx.author)
    embed = discord.Embed(title=b[:len(b)-5]+" cba", color=discord.Color.red())
    embed.set_image(url=a)
    await ctx.send(embed=embed)

@bot.command()
async def floppa(ctx):
    a=random.choice(flop)
    b=str(ctx.author)
    embed = discord.Embed(title=b[:len(b)-5]+" ha invocado a floppa", color=discord.Color.red())
    embed.set_image(url=a)
    await ctx.send(embed=embed)

@bot.command()
async def match(ctx,*,msg):
    r=str(msg)
    t=r.split()
    d=t[0]
    e=t[1]
    c=random.randint(0,100)
    b="La compatibilidad entre "+d+" y "+e+" es del "+str(c)+"%"
    await ctx.send(b)

@bot.command()
async def gato(ctx,*,msg):
    archivo = open("recursos/game.txt", "r")
    data = archivo.readlines()
    archivo.close()
    a = ""
    mm=msg
    msg=msg.split(" ")
    for j in data:
        a += j.strip()
    a = a.split(",")
    tablero = listaboni(a)
    archivo = open("recursos/value.txt", "r")
    data = archivo.readlines()
    archivo.close()
    for j in data:
        value=int(j)

    class Bot:
        def __init__(self, fila, columna, tablero):
            self.fila = fila
            self.columna = columna
            self.tablero = tablero
            self.turno = 0
            self.alfa = False
            self.beta1 = False
            self.gama = False
            if (fila==4 and columna==4):
                self.alfa=True
            elif (fila==5 and columna==5):
                self.beta1=True
            elif (fila==6 and columna==6):
                self.gama=True
            if (fila == 0 and columna == 0) or (fila == 2 and columna == 0) or (fila == 0 and columna == 2) or (
                    fila == 2 and columna == 2):
                tablero[1][1] = "X"
                im = Image.open("recursos/d.png")
                font_type = ImageFont.truetype("arial.ttf", 100)
                draw = ImageDraw.Draw(im)
                draw.text(xy=(145, 140), text="X", fill=(0, 0, 0), font=font_type)
                im.save("recursos/d.png")
                archivo = open("recursos/daada.txt", "w")
                archivo.write("4 4")
                archivo.close()
                self.alfa = True
            elif (fila == 0 and columna == 1) or (fila == 1 and columna == 0) or (fila == 1 and columna == 2) or (
                    fila == 2 and columna == 1):
                tablero[1][1] = "X"
                im = Image.open("recursos/d.png")
                font_type = ImageFont.truetype("arial.ttf", 100)
                draw = ImageDraw.Draw(im)
                draw.text(xy=(145, 140), text="X", fill=(0, 0, 0), font=font_type)
                im.save("recursos/d.png")
                archivo = open("recursos/daada.txt", "w")
                archivo.write("5 5")
                archivo.close()
                self.beta1 = True
            elif fila == 1 and columna == 1:
                num = [0, 2]
                posy = int(random.choice(num))
                posx= int(random.choice(num))
                while tablero[posy][posx] != "-":
                    if tablero[posy][posx] != "-":
                        posy = int(random.choice(num))
                        posx=int(random.choice(num))
                tablero[posy][posx] = "X"
                im = Image.open("recursos/d.png")
                font_type = ImageFont.truetype("arial.ttf", 100)
                draw = ImageDraw.Draw(im)
                if posy==0 and posx==0:
                    draw.text(xy=(15, 20), text="X", fill=(0, 0, 0), font=font_type)  # 0 0
                elif posy==0 and posx==2:
                    draw.text(xy=(275, 20), text="X", fill=(0, 0, 0), font=font_type)  # 0 2
                elif posy==2 and posx==0:
                    draw.text(xy=(15, 255), text="X", fill=(0, 0, 0), font=font_type)  # 2 0
                elif posy==2 and posx==2:
                    draw.text(xy=(275, 255), text="X", fill=(0, 0, 0), font=font_type)  # 2 2
                im.save("recursos/d.png")
                archivo = open("recursos/daada.txt", "w")
                archivo.write("6 6")
                archivo.close()
                self.gama = True

        def jugar_bot(self, tablero):
            import random
            num = [0, 2]
            if self.secuencia(tablero) != True:
                archivo = open("recursos/turnos 2.txt", "r")
                data = archivo.readlines()
                archivo.close()
                tt = 0
                for i in data:
                    tt += int(i)
                tt += 1
                archivo = open("recursos/turnos 2.txt", "w")
                archivo.write(str(tt))
                archivo.close()
                if self.peligro(tablero) != True:
                    if self.alfa == True:
                        if tt == 1:
                            pos = int(random.choice(num))
                            while tablero[1][pos] != "-":
                                if tablero[1][pos] != "-":
                                    pos = int(random.choice(num))
                            tablero[1][pos] = "X"
                            if pos==0:
                                draw.text(xy=(15, 140), text="X", fill=(0, 0, 0), font=font_type)
                            elif pos==2:
                                draw.text(xy=(275, 140), text="X", fill=(0, 0, 0), font=font_type)
                            im.save("recursos/d.png")
                        elif tt >= 2:
                            self.random_move()
                    elif self.beta1 == True:
                        if tt == 1:
                            if self.peligro2(tablero) != True:
                                if (tablero[0][1] == "O" and (tablero[2][0] == "O" or tablero[2][1] == "O" or tablero[2][2] == "O")) or (tablero[2][1] and (tablero[0][0] == "O" or tablero[0][1] == "O" or tablero[0][2] == "O")):
                                    pos = int(random.choice(num))
                                    while tablero[1][pos] != "-":
                                        if tablero[1][pos] != "-":
                                            pos = int(random.choice(num))
                                    if  pos == 0:
                                        draw.text(xy=(15, 140), text="X", fill=(0, 0, 0), font=font_type)  # 1 0
                                    elif pos == 1:
                                        draw.text(xy=(145, 140), text="X", fill=(0, 0, 0), font=font_type)  # 1 1
                                    elif pos == 2:
                                        draw.text(xy=(275, 140), text="X", fill=(0, 0, 0), font=font_type)  # 1 2
                                    tablero[1][pos] = "X"
                                elif (tablero[1][0] == "O" and (tablero[0][2]=="O" or tablero[1][2]=="O" or tablero[2][2=="O"])) or (tablero[1][2]=="O" and (tablero[0][0]=="O" or tablero[1][0]=="O" or tablero [2][0]=="O")):
                                    pos = int(random.choice(num))
                                    while tablero[pos][1] != "-":
                                        if tablero[pos][1] != "-":
                                            pos = int(random.choice(num))
                                    if pos == 0:
                                        draw.text(xy=(145, 20), text="X", fill=(0, 0, 0), font=font_type)  # 0 1
                                    elif pos == 1:
                                        draw.text(xy=(145, 140), text="X", fill=(0, 0, 0), font=font_type)  # 1 1
                                    elif pos == 2:
                                        draw.text(xy=(145, 255), text="X", fill=(0, 0, 0), font=font_type)  # 2 1
                                    tablero[pos][1] = "X"
                                im.save("recursos/d.png")
                        elif tt >= 2:
                            if self.peligro2(tablero) != True:
                                self.random_move()
                    elif self.gama == True:
                        if tt == 1:
                            if tablero[0][0]=="X":
                                tablero[0][2] = "X"
                                draw.text(xy=(275, 20), text="X", fill=(0, 0, 0), font=font_type)  # 0 2
                            elif tablero[0][2]=="X":
                                tablero[0][0]="X"
                                draw.text(xy=(15, 20), text="X", fill=(0, 0, 0), font=font_type)  # 0 0
                            elif tablero[2][0]=="X":
                                tablero[2][2]="X"
                                draw.text(xy=(275, 255), text="X", fill=(0, 0, 0), font=font_type)  # 2 2
                            elif tablero[2][2]=="X":
                                tablero[2][0]="X"
                                draw.text(xy=(15, 255), text="X", fill=(0, 0, 0), font=font_type)  # 2 0
                            im.save("recursos/d.png")
                        else:
                            self.random_move()

        def random_move(self):
            import random
            im = Image.open("recursos/d.png")
            font_type = ImageFont.truetype("arial.ttf", 100)
            draw = ImageDraw.Draw(im)
            x = random.randint(0, 2)
            y = random.randint(0, 2)
            while tablero[y][x] != "-":
                if tablero[y][x] != "-":
                    x = random.randint(0, 2)
                    y = random.randint(0, 2)
            tablero[y][x] = "X"
            if y==0 and x==0:
                draw.text(xy=(15, 20), text="X", fill=(0, 0, 0), font=font_type) # 0 0
            elif y==0 and x==1:
                draw.text(xy=(145, 20), text="X", fill=(0, 0, 0), font=font_type) # 0 1
            elif y==0 and x==2:
                draw.text(xy=(275, 20), text="X", fill=(0, 0, 0), font=font_type)  # 0 2
            elif y==1 and x==0:
                draw.text(xy=(15, 140), text="X", fill=(0, 0, 0), font=font_type)  # 1 0
            elif y==1 and x==1:
                draw.text(xy=(145, 140), text="X", fill=(0, 0, 0), font=font_type)  # 1 1
            elif y==1 and x==2:
                draw.text(xy=(275, 140), text="X", fill=(0, 0, 0), font=font_type)  # 1 2
            elif y==2 and x==0:
                draw.text(xy=(15, 255), text="X", fill=(0, 0, 0), font=font_type)  # 2 0
            elif y==2 and x==1:
                draw.text(xy=(145, 255), text="X", fill=(0, 0, 0), font=font_type)  # 2 1
            elif y==2 and x==2:
                draw.text(xy=(275, 255), text="X", fill=(0, 0, 0), font=font_type)  # 2 2
            im.save("recursos/d.png")

        def peligro(self, tablero):
            cp = 0
            for i in range(len(tablero)):
                for j in range(3):
                    if tablero[i][j] == "O":
                        cp += 1
                    elif tablero[i][j] == "X":
                        cp -= 1
                    elif tablero[i][j] == "-":
                        pos = j
                if cp == 2:
                    im = Image.open("recursos/d.png")
                    font_type = ImageFont.truetype("arial.ttf", 100)
                    draw = ImageDraw.Draw(im)
                    if i == 0 and pos == 0:
                        draw.text(xy=(15, 20), text="X", fill=(0, 0, 0), font=font_type)  # 0 0
                    elif i == 0 and pos == 1:
                        draw.text(xy=(145, 20), text="X", fill=(0, 0, 0), font=font_type)  # 0 1
                    elif i == 0 and pos == 2:
                        draw.text(xy=(275, 20), text="X", fill=(0, 0, 0), font=font_type)  # 0 2
                    elif i == 1 and pos == 0:
                        draw.text(xy=(15, 140), text="X", fill=(0, 0, 0), font=font_type)  # 1 0
                    elif i == 1 and pos == 1:
                        draw.text(xy=(145, 140), text="X", fill=(0, 0, 0), font=font_type)  # 1 1
                    elif i == 1 and pos == 2:
                        draw.text(xy=(275, 140), text="X", fill=(0, 0, 0), font=font_type)  # 1 2
                    elif i == 2 and pos == 0:
                        draw.text(xy=(15, 255), text="X", fill=(0, 0, 0), font=font_type)  # 2 0
                    elif i == 2 and pos == 1:
                        draw.text(xy=(145, 255), text="X", fill=(0, 0, 0), font=font_type)  # 2 1
                    elif i == 2 and pos == 2:
                        draw.text(xy=(275, 255), text="X", fill=(0, 0, 0), font=font_type)  # 2 2
                    tablero[i][pos] = "X"

                    im.save("recursos/d.png")
                    return True
                cp = 0
            for j in range(3):
                for i in range(3):
                    if tablero[i][j] == "O":
                        cp += 1
                    elif tablero[i][j] == "X":
                        cp -= 1
                    elif tablero[i][j] == "-":
                        pos = i
                if cp == 2:
                    im = Image.open("recursos/d.png")
                    font_type = ImageFont.truetype("arial.ttf", 100)
                    draw = ImageDraw.Draw(im)
                    if pos == 0 and j == 0:
                        draw.text(xy=(15, 20), text="X", fill=(0, 0, 0), font=font_type)  # 0 0
                    elif pos == 0 and j == 1:
                        draw.text(xy=(145, 20), text="X", fill=(0, 0, 0), font=font_type)  # 0 1
                    elif pos == 0 and j == 2:
                        draw.text(xy=(275, 20), text="X", fill=(0, 0, 0), font=font_type)  # 0 2
                    elif pos == 1 and j == 0:
                        draw.text(xy=(15, 140), text="X", fill=(0, 0, 0), font=font_type)  # 1 0
                    elif pos == 1 and j == 1:
                        draw.text(xy=(145, 140), text="X", fill=(0, 0, 0), font=font_type)  # 1 1
                    elif pos == 1 and j == 2:
                        draw.text(xy=(275, 140), text="X", fill=(0, 0, 0), font=font_type)  # 1 2
                    elif pos == 2 and j == 0:
                        draw.text(xy=(15, 255), text="X", fill=(0, 0, 0), font=font_type)  # 2 0
                    elif pos == 2 and j == 1:
                        draw.text(xy=(145, 255), text="X", fill=(0, 0, 0), font=font_type)  # 2 1
                    elif pos == 2 and j == 2:
                        draw.text(xy=(275, 255), text="X", fill=(0, 0, 0), font=font_type)  # 2 2
                    tablero[pos][j] = "X"
                    im.save("recursos/d.png")
                    return True
                cp = 0
            for i in range(3):
                if tablero[i][i] == "O":
                    cp += 1
                elif tablero[i][i] == "X":
                    cp -= 1
                elif tablero[i][i] == "-":
                    pos = i
            if cp == 2:
                im = Image.open("recursos/d.png")
                font_type = ImageFont.truetype("arial.ttf", 100)
                draw = ImageDraw.Draw(im)
                if pos == 0 and pos == 0:
                    draw.text(xy=(15, 20), text="X", fill=(0, 0, 0), font=font_type)  # 0 0
                elif pos == 1 and pos == 1:
                    draw.text(xy=(145, 140), text="X", fill=(0, 0, 0), font=font_type)  # 1 1
                elif pos == 2 and pos == 2:
                    draw.text(xy=(275, 255), text="X", fill=(0, 0, 0), font=font_type)  # 2 2
                tablero[pos][pos] = "X"
                im.save("recursos/d.png")
                return True
            if cp != 2:
                cp = 0
                y = 2
                x = 0
                for j in range(3):
                    if tablero[y][x] == "O":
                        cp += 1
                    elif tablero[y][x] == "X":
                        cp -= 1
                    elif tablero[y][x] == "-":
                        posx = x
                        posy = y
                    y -= 1
                    x += 1
                if cp == 2:
                    im = Image.open("recursos/d.png")
                    font_type = ImageFont.truetype("arial.ttf", 100)
                    draw = ImageDraw.Draw(im)
                    if posy == 0 and posx == 0:
                        draw.text(xy=(15, 20), text="X", fill=(0, 0, 0), font=font_type)  # 0 0
                    elif posy == 0 and posx == 1:
                        draw.text(xy=(145, 20), text="X", fill=(0, 0, 0), font=font_type)  # 0 1
                    elif posy == 0 and posx == 2:
                        draw.text(xy=(275, 20), text="X", fill=(0, 0, 0), font=font_type)  # 0 2
                    elif posy == 1 and posx == 0:
                        draw.text(xy=(15, 140), text="X", fill=(0, 0, 0), font=font_type)  # 1 0
                    elif posy == 1 and posx == 1:
                        draw.text(xy=(145, 140), text="X", fill=(0, 0, 0), font=font_type)  # 1 1
                    elif posy == 1 and posx == 2:
                        draw.text(xy=(275, 140), text="X", fill=(0, 0, 0), font=font_type)  # 1 2
                    elif posy == 2 and posx == 0:
                        draw.text(xy=(15, 255), text="X", fill=(0, 0, 0), font=font_type)  # 2 0
                    elif posy == 2 and posx == 1:
                        draw.text(xy=(145, 255), text="X", fill=(0, 0, 0), font=font_type)  # 2 1
                    elif posy == 2 and posx == 2:
                        draw.text(xy=(275, 255), text="X", fill=(0, 0, 0), font=font_type)  # 2 2
                    tablero[posy][posx] = "X"
                    im.save("recursos/d.png")
                    return True

        def peligro2(self, tablero):
            cp = 0
            if (tablero[0][1] == "O" and tablero[1][0] == "O") and (tablero[0][0]=="-"):
                cp += 1
                y = 0
                x = 0
            if (tablero[1][0] == "O" and tablero[2][1] == "O") and (tablero[2][0]=="-"):
                cp += 1
                y = 2
                x = 0
            if (tablero[2][1] == "O" and tablero[1][2] == "O") and (tablero[2][2]=="-"):
                cp += 1
                y = 2
                x = 2
            if (tablero[1][2] == "O" and tablero[0][1] == "O") and (tablero[0][2]=="-"):
                cp += 1
                y = 0
                x = 2
            if cp >= 1:
                if y == 0 and x == 0:
                    draw.text(xy=(15, 20), text="X", fill=(0, 0, 0), font=font_type)  # 0 0
                elif y == 0 and x == 2:
                    draw.text(xy=(275, 20), text="X", fill=(0, 0, 0), font=font_type)  # 0 2
                elif y == 2 and x == 0:
                    draw.text(xy=(15, 255), text="X", fill=(0, 0, 0), font=font_type)  # 2 0
                elif y == 2 and x == 2:
                    draw.text(xy=(275, 255), text="X", fill=(0, 0, 0), font=font_type)  # 2 2
                im.save("recursos/d.png")
                tablero[y][x] = "X"
                return True

        def secuencia(self, tablero):
            cp = 0
            for i in range(len(tablero)):
                for j in range(3):
                    if tablero[i][j] == "X":
                        cp += 1
                    elif tablero[i][j] == "O":
                        cp -= 1
                    elif tablero[i][j] == "-":
                        pos = j
                if cp == 2:
                    im = Image.open("recursos/d.png")
                    font_type = ImageFont.truetype("arial.ttf", 100)
                    draw = ImageDraw.Draw(im)
                    if i == 0 and pos == 0:
                        draw.text(xy=(15, 20), text="X", fill=(0, 0, 0), font=font_type)  # 0 0
                    elif i == 0 and pos == 1:
                        draw.text(xy=(145, 20), text="X", fill=(0, 0, 0), font=font_type)  # 0 1
                    elif i == 0 and pos == 2:
                        draw.text(xy=(275, 20), text="X", fill=(0, 0, 0), font=font_type)  # 0 2
                    elif i == 1 and pos == 0:
                        draw.text(xy=(15, 140), text="X", fill=(0, 0, 0), font=font_type)  # 1 0
                    elif i == 1 and pos == 1:
                        draw.text(xy=(145, 140), text="X", fill=(0, 0, 0), font=font_type)  # 1 1
                    elif i == 1 and pos == 2:
                        draw.text(xy=(275, 140), text="X", fill=(0, 0, 0), font=font_type)  # 1 2
                    elif i == 2 and pos == 0:
                        draw.text(xy=(15, 255), text="X", fill=(0, 0, 0), font=font_type)  # 2 0
                    elif i == 2 and pos == 1:
                        draw.text(xy=(145, 255), text="X", fill=(0, 0, 0), font=font_type)  # 2 1
                    elif i == 2 and pos == 2:
                        draw.text(xy=(275, 255), text="X", fill=(0, 0, 0), font=font_type)  # 2 2
                    tablero[i][pos] = "X"
                    im.save("recursos/d.png")
                    return True
                cp = 0
            for j in range(3):
                for i in range(3):
                    if tablero[i][j] == "X":
                        cp += 1
                    elif tablero[i][j] == "O":
                        cp -= 1
                    elif tablero[i][j] == "-":
                        pos = i
                if cp == 2:
                    im = Image.open("recursos/d.png")
                    font_type = ImageFont.truetype("arial.ttf", 100)
                    draw = ImageDraw.Draw(im)
                    if pos==0 and j == 0:
                        draw.text(xy=(15, 20), text="X", fill=(0, 0, 0), font=font_type)  # 0 0
                    elif pos == 0 and j == 1:
                        draw.text(xy=(145, 20), text="X", fill=(0, 0, 0), font=font_type)  # 0 1
                    elif pos == 0 and j == 2:
                        draw.text(xy=(275, 20), text="X", fill=(0, 0, 0), font=font_type)  # 0 2
                    elif pos == 1 and j == 0:
                        draw.text(xy=(15, 140), text="X", fill=(0, 0, 0), font=font_type)  # 1 0
                    elif pos == 1 and j == 1:
                        draw.text(xy=(145, 140), text="X", fill=(0, 0, 0), font=font_type)  # 1 1
                    elif pos == 1 and j == 2:
                        draw.text(xy=(275, 140), text="X", fill=(0, 0, 0), font=font_type)  # 1 2
                    elif pos == 2 and j == 0:
                        draw.text(xy=(15, 255), text="X", fill=(0, 0, 0), font=font_type)  # 2 0
                    elif pos == 2 and j == 1:
                        draw.text(xy=(145, 255), text="X", fill=(0, 0, 0), font=font_type)  # 2 1
                    elif pos == 2 and j == 2:
                        draw.text(xy=(275, 255), text="X", fill=(0, 0, 0), font=font_type)  # 2 2
                    tablero[pos][j] = "X"
                    im.save("recursos/d.png")
                    return True
                cp = 0
            for i in range(3):
                if tablero[i][i] == "X":
                    cp += 1
                elif tablero[i][i] == "O":
                    cp -= 1
                elif tablero[i][i] == "-":
                    pos = i
            if cp == 2:
                im = Image.open("recursos/d.png")
                font_type = ImageFont.truetype("arial.ttf", 100)
                draw = ImageDraw.Draw(im)
                if pos == 0 and pos == 0:
                    draw.text(xy=(15, 20), text="X", fill=(0, 0, 0), font=font_type)  # 0 0
                elif pos == 0 and pos == 1:
                    draw.text(xy=(145, 20), text="X", fill=(0, 0, 0), font=font_type)  # 0 1
                elif pos == 0 and pos == 2:
                    draw.text(xy=(275, 20), text="X", fill=(0, 0, 0), font=font_type)  # 0 2
                elif pos == 1 and pos == 0:
                    draw.text(xy=(15, 140), text="X", fill=(0, 0, 0), font=font_type)  # 1 0
                elif pos == 1 and pos == 1:
                    draw.text(xy=(145, 140), text="X", fill=(0, 0, 0), font=font_type)  # 1 1
                elif pos == 1 and pos == 2:
                    draw.text(xy=(275, 140), text="X", fill=(0, 0, 0), font=font_type)  # 1 2
                elif pos == 2 and pos == 0:
                    draw.text(xy=(15, 255), text="X", fill=(0, 0, 0), font=font_type)  # 2 0
                elif pos == 2 and pos == 1:
                    draw.text(xy=(145, 255), text="X", fill=(0, 0, 0), font=font_type)  # 2 1
                elif pos == 2 and pos == 2:
                    draw.text(xy=(275, 255), text="X", fill=(0, 0, 0), font=font_type)  # 2 2
                tablero[pos][pos] = "X"
                im.save("recursos/d.png")
                return True
            if cp != 2:
                cp = 0
                y = 2
                x = 0
                for j in range(3):
                    if tablero[y][x] == "X":
                        cp += 1
                    elif tablero[y][x] == "O":
                        cp -= 1
                    elif tablero[y][x] == "-":
                        posx = x
                        posy = y
                    y -= 1
                    x += 1
                if cp == 2:
                    im = Image.open("recursos/d.png")
                    font_type = ImageFont.truetype("arial.ttf", 100)
                    draw = ImageDraw.Draw(im)
                    if posy == 0 and posx == 0:
                        draw.text(xy=(15, 20), text="X", fill=(0, 0, 0), font=font_type)  # 0 0
                    elif posy == 0 and posx == 1:
                        draw.text(xy=(145, 20), text="X", fill=(0, 0, 0), font=font_type)  # 0 1
                    elif posy == 0 and posx == 2:
                        draw.text(xy=(275, 20), text="X", fill=(0, 0, 0), font=font_type)  # 0 2
                    elif posy == 1 and posx == 0:
                        draw.text(xy=(15, 140), text="X", fill=(0, 0, 0), font=font_type)  # 1 0
                    elif posy == 1 and posx == 1:
                        draw.text(xy=(145, 140), text="X", fill=(0, 0, 0), font=font_type)  # 1 1
                    elif posy == 1 and posx == 2:
                        draw.text(xy=(275, 140), text="X", fill=(0, 0, 0), font=font_type)  # 1 2
                    elif posy == 2 and posx == 0:
                        draw.text(xy=(15, 255), text="X", fill=(0, 0, 0), font=font_type)  # 2 0
                    elif posy == 2 and posx == 1:
                        draw.text(xy=(145, 255), text="X", fill=(0, 0, 0), font=font_type)  # 2 1
                    elif posy == 2 and posx == 2:
                        draw.text(xy=(275, 255), text="X", fill=(0, 0, 0), font=font_type)  # 2 2
                    tablero[posy][posx] = "X"
                    im.save("recursos/d.png")
                    return True

    jugador = "Jugador (O),Bot (X)"
    jugador = jugador.split(",")
    p = 0
    pp = 0
    pppp=0
    pa=0
    t = 0
    if " " in mm and int(msg[0])<3 and int(msg[0])>=0 and int(msg[1])<3 and int(msg[1])>=0:
        for j in range(2):
            archivo = open("recursos/turnos.txt", "r")
            data = archivo.readlines()
            archivo.close()
            t = 0
            for i in data:
                t += int(i)
            t+=1
            archivo=open("recursos/turnos.txt","w")
            archivo.write(str(t))
            archivo.close()
            if victory(tablero) != "X" and victory(tablero) != "O" and t != 10:
                o="Turno "+str(jugador[j])
                if j == 0:
                    while pp == 0:
                        if pp == 0:
                            fila = int(msg[0])
                            columna = int(msg[1])
                            if tablero[fila][columna] == "-":
                                tablero[fila][columna] = "O"
                                im = Image.open("recursos/d.png")
                                font_type = ImageFont.truetype("arial.ttf", 100)
                                draw = ImageDraw.Draw(im)
                                if fila == 0 and columna == 0:
                                    draw.text(xy=(15, 20), text="O", fill=(0, 0, 0), font=font_type)  # 0 0
                                elif fila == 0 and columna == 1:
                                    draw.text(xy=(145, 20), text="O", fill=(0, 0, 0), font=font_type)  # 0 1
                                elif fila == 0 and columna == 2:
                                    draw.text(xy=(275, 20), text="O", fill=(0, 0, 0), font=font_type)  # 0 2
                                elif fila == 1 and columna == 0:
                                    draw.text(xy=(15, 140), text="O", fill=(0, 0, 0), font=font_type)  # 1 0
                                elif fila == 1 and columna == 1:
                                    draw.text(xy=(145, 140), text="O", fill=(0, 0, 0), font=font_type)  # 1 1
                                elif fila == 1 and columna == 2:
                                    draw.text(xy=(275, 140), text="O", fill=(0, 0, 0), font=font_type)  # 1 2
                                elif fila == 2 and columna == 0:
                                    draw.text(xy=(15, 255), text="O", fill=(0, 0, 0), font=font_type)  # 2 0
                                elif fila == 2 and columna == 1:
                                    draw.text(xy=(145, 255), text="O", fill=(0, 0, 0), font=font_type)  # 2 1
                                elif fila == 2 and columna == 2:
                                    draw.text(xy=(275, 255), text="O", fill=(0, 0, 0), font=font_type)  # 2 2
                                im.save("recursos/d.png")
                                pp = 1
                                pa=0
                            else:
                                if pa==0:
                                    archivo = open("recursos/turnos.txt", "r")
                                    data = archivo.readlines()
                                    archivo.close()
                                    t = 0
                                    for i in data:
                                        t += int(i)
                                    t -= 2
                                    archivo = open("recursos/turnos.txt", "w")
                                    archivo.write(str(t))
                                    archivo.close()
                                    await ctx.send("Seleccione una posición valida")
                                    pp=1
                                    pa=1
                if j == 1 and pa==0:
                    if value == 0:
                        Bot(fila, columna, tablero)
                        archivo=open("recursos/value.txt","w")
                        archivo.write("1")
                        archivo.close()
                        archivo=open("recursos/value.txt","r")
                        data=archivo.readlines()
                        archivo.close()
                        for k in data:
                            value=int(k)
                    elif value == 1:
                        archivo=open("recursos/daada.txt","r")
                        data=archivo.readlines()
                        l=""
                        for j in data:
                            l+=j
                            l=l.split()
                            y=int(l[0])
                            x=int(l[1])
                            bot=Bot(y,x,tablero)
                            bot.jugar_bot(tablero)
                u = ""
                for i in tablero:
                    u += i[0] + " " + i[1] + " " + i[2]+"\n"
                embed = discord.Embed(title="Gato", description=o,color=discord.Color.red())
                file = discord.File("recursos/d.png",filename="image.png")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/895678665042567249/924402621668810833/imagen_2021-12-25_173950.png")
                embed.set_image(url="attachment://image.png")
                await ctx.send(file=file,embed=embed)
                pp = 0
                g = ""
                c=0
                for i in tablero:
                    c+=1
                    g += i[0] + " " + i[1] + " " + i[2]
                    if c!=len(tablero):
                        g+=",\n"
                archivo = open("recursos/game.txt", "w")
                archivo.write(g)
                archivo.close()
            if victory(tablero) == "O" and pppp==0:
                o="Ganó el jugador 1"
                embed = discord.Embed(title="Gato", description=o, color=discord.Color.red())
                file = discord.File("recursos/d.png",filename="image.png")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/895678665042567249/924402621668810833/imagen_2021-12-25_173950.png")
                embed.set_image(url="attachment://image.png")
                await ctx.send(file=file,embed=embed)
                pppp=1
            elif victory(tablero) == "X" and pppp==0:
                o="Ganó el bot"
                embed = discord.Embed(title="Gato", description=o, color=discord.Color.red())
                file = discord.File("recursos/d.png",filename="image.png")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/895678665042567249/924402621668810833/imagen_2021-12-25_173950.png")
                embed.set_image(url="attachment://image.png")
                await ctx.send(file=file,embed=embed)
                pppp=1
            elif t == 10 and pppp==0:
                o="Empate"
                embed = discord.Embed(title="Gato", description=o, color=discord.Color.red())
                file = discord.File("recursos/d.png",filename="image.png")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/895678665042567249/924402621668810833/imagen_2021-12-25_173950.png")
                embed.set_image(url="attachment://image.png")
                await ctx.send(file=file,embed=embed)
                pppp=1
            if pppp==1:
                archivo=open("recursos/game.txt","w")
                archivo.write("- - -,\n- - -,\n- - -")
                archivo.close()
                archivo=open("recursos/value.txt","w")
                archivo.write("0")
                archivo.close()
                archivo=open("recursos/daada.txt","w")
                archivo.write("")
                archivo.close()
                archivo=open("recursos/turnos.txt","w")
                archivo.write("0")
                archivo.close()
                archivo=open("recursos/turnos 2.txt","w")
                archivo.write("0")
                archivo.close()
                fuente = "original/d.png"
                destino = "recursos/d.png"
                shutil.copyfile(fuente, destino)
    else:
        await ctx.send("Introduzca una coordenada valida (entre 0 y 2)")

@bot.command()
async def youtube(ctx,*,search):
    query_string=parse.urlencode({"search_query": search})
    html_content=request.urlopen("http://www.youtube.com/results?"+query_string)
    search_results=re.findall('watch\?v=(.{11})',html_content.read().decode('utf-8'))
    print(search_results)
    await ctx.send("http://www.youtube.com/watch?v="+search_results[0])

@bot.command()
async def epic(ctx,*,search):
    q=parse.urlencode({"q": search})
    html_content=request.urlopen("https://www.epicgames.com/store/es-ES/browse?"+q+"&sortBy=relevancy&sortDir=DESC&count=40")
    search_results=re.findall('p/(.{100})',html_content.read().decode())
    for j in range(len(search_results)):
        p=0
        c=(-1)
        for k in search_results[j]:
            c+=1
            if k==">" and p==0:
                search_results[j]=search_results[j][:c-1]
                p=1
    print(search_results)
    await ctx.send("https://www.epicgames.com/store/es-ES/p/"+search_results[1])

@bot.command()
async def epicfree(ctx):
    html_content = Request("https://www.epicgames.com/store/es-ES/browse?sortBy=currentPrice&sortDir=ASC&priceTier=tierDiscouted&count=40&start=0",
                           headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(html_content)
    search_results = re.findall(r'(?<=href="/store/es-ES/p/)\S+', webpage.read().decode())
    for j in range(len(search_results)):
        p = 0
        c = (-1)
        for k in search_results[j]:
            c += 1
            if k == ">" and p == 0:
                search_results[j] = search_results[j][:c - 1]
                p = 1
    print(search_results)
    await ctx.send("https://www.epicgames.com/store/es-ES/p/" + search_results[0])

def epicfreee():
    html_content = Request("https://www.epicgames.com/store/es-ES/browse?sortBy=currentPrice&sortDir=ASC&priceTier=tierDiscouted&count=40&start=0",
                           headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(html_content)
    search_results = re.findall(r'(?<=href="/store/es-ES/p/)\S+', webpage.read().decode())
    for j in range(len(search_results)):
        p = 0
        c = (-1)
        for k in search_results[j]:
            c += 1
            if k == ">" and p == 0:
                search_results[j] = search_results[j][:c - 1]
                p = 1
    print(search_results)
    a="https://www.epicgames.com/store/es-ES/p/" + search_results[0]
    return a

@bot.command()
async def anime(ctx,*,search):
    query_string=parse.urlencode({"q": search})
    html_content = Request("https://www3.animeflv.net/browse?"+query_string,
        headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(html_content)
    search_results = re.findall(r'(?<=href="/anime/)\S+', webpage.read().decode())
    print(search_results)
    for j in range(len(search_results)):
        p=0
        c=(-1)
        for k in search_results[j]:
            c+=1
            if k==">" and p==0:
                search_results[j]=search_results[j][:c-1]
                p=1
    if search_results!=[]:
        await ctx.send("https://www3.animeflv.net/anime/"+search_results[0])
    else:
        await ctx.send("No se han encontrado resultados")

@bot.command()
async def conectar(ctx, url:str):
    if not ctx.author.voice:
        await ctx.send("teni que estar conectao culiao")
        return
    else:
        canal = ctx.message.author.voice.channel
        voz = get(bot.voice_clients, guild=ctx.guild)
        if voz and voz.is_connected():
            await voz.move_to(canal)
        else:
            voz=await canal.connect()
        cancionactiva = os.path.isfile("C:/Users/Erick/AppData/Local/Programs/Microsoft VS Code/ola")
        try:
            if cancionactiva:
                os.remove("C:/Users/Erick/AppData/Local/Programs/Microsoft VS Code/ola/cancion.mp3")
                print("se fue")
        except PermissionError:
            await ctx.send("Error: Canción reproduciendose")
            return
        print("todo listo")
        ydl_op={"format":"bestaudio/best","postprocessors":[{"key":"FFmpegExtractAudio","preferredcodec":"mp3","preferredquality":"192"}]}

        with youtube_dl.YoutubeDL(ydl_op) as ydl:
            print("Descargando")
            ydl.download([url])

        for file in os.listdir("C:/Users/Erick/AppData/Local/Programs/Microsoft VS Code/ola"):
            if file.endswith("mp3"):
                name=file
                print("Renombrando")
                os.rename(file,"cancion.mp3")

        voz.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="C:/Users/Erick/AppData/Local/Programs/Microsoft VS Code/ola/cancion.mp3"),after=lambda e: os.remove("C:/Users/Erick/AppData/Local/Programs/Microsoft VS Code/ola/cancion.mp3")
)
        voz.source=discord.PCMVolumeTransformer(voz.source)
        voz.source.volume=1

        nombre=name.rsplit("-",2)
        await ctx.send(f"Reproduciendo: {nombre[0]}")

@bot.command()
async def conectard(ctx):
    if not ctx.author.voice:
        await ctx.send("teni que estar conectao culiao")
        return
    else:
        canal = ctx.message.author.voice.channel
        voz = get(bot.voice_clients, guild=ctx.guild)
        if voz and voz.is_connected():
            voz=await voz.move_to(canal)
        else:
            voz=await canal.connect()

        voz.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="https://b.ppy.sh/preview/1598150.mp3"),after=lambda e: print("Ha terminao"))
        voz.source=discord.PCMVolumeTransformer(voz.source)
        voz.source.volume=0.1

@bot.command()
async def reset(ctx):
    archivo = open("recursos/game.txt", "w")
    archivo.write("- - -,\n- - -,\n- - -")
    archivo.close()
    archivo = open("recursos/value.txt", "w")
    archivo.write("0")
    archivo.close()
    archivo = open("recursos/daada.txt", "w")
    archivo.write("")
    archivo.close()
    archivo = open("recursos/turnos.txt", "w")
    archivo.write("0")
    archivo.close()
    archivo = open("recursos/turnos 2.txt", "w")
    archivo.write("0")
    archivo.close()
    fuente = "original/d.png"
    destino = "recursos/d.png"
    shutil.copyfile(fuente, destino)

@bot.command()
async def minas(ctx,*,msg):
    upperfield = [["🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳"],
                  ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳"],
                  ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳"],
                  ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳"],
                  ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳"],
                  ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳"],
                  ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳"],
                  ["🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳", "🔳"]]

    lowerfield = [["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
                  ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
                  ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
                  ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
                  ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
                  ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
                  ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
                  ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"]]

    def comprobar(lowerfield, fila, columna):
        arriba = False
        if fila - 1 >= 0:
            if lowerfield[fila - 1][columna] == "🔲":
                arriba = True
        abajo = False
        if (fila + 1) <= len(lowerfield) - 1:
            if lowerfield[fila + 1][columna] == "🔲":
                abajo = True
        derecha = False
        if (columna + 1) <= len(lowerfield[fila]) - 1:
            if lowerfield[fila][columna + 1] == "🔲":
                derecha = True
        izquierda = False
        if columna - 1 >= 0:
            if lowerfield[fila][columna - 1] == "🔲":
                izquierda = True
        return arriba, abajo, derecha, izquierda

    def rellenar(upperfield, fila, columna,im):
        if fila - 1 >= 0:
            if upperfield[fila - 1][columna] != "🔲":
                upperfield[fila - 1][columna] = lowerfield[fila - 1][columna]
                imagen(upperfield, fila-1, columna,im)

        if (fila + 1) <= len(upperfield) - 1:
            if upperfield[fila + 1][columna] != "🔲":
                upperfield[fila + 1][columna] = lowerfield[fila + 1][columna]
                imagen(upperfield, fila+1, columna,im)

        if (columna + 1) <= len(upperfield[fila]) - 1:
            if upperfield[fila][columna + 1] != "🔲":
                upperfield[fila][columna + 1] = lowerfield[fila][columna + 1]
                imagen(upperfield, fila, columna+1,im)

        if columna - 1 >= 0:
            if upperfield[fila][columna - 1] != "🔲":
                upperfield[fila][columna - 1] = lowerfield[fila][columna - 1]
                imagen(upperfield, fila, columna-1,im)

        if (fila + 1) <= len(upperfield) - 1 and (columna + 1) <= len(upperfield[fila]) - 1:
            if upperfield[fila+1][columna + 1] != "🔲":
                upperfield[fila+1][columna + 1] = lowerfield[fila+1][columna + 1]
                imagen(upperfield, fila+1, columna+1,im)

        if (fila + 1) <= len(upperfield) - 1 and columna - 1 >= 0:
            if upperfield[fila+1][columna - 1] != "🔲":
                upperfield[fila+1][columna - 1] = lowerfield[fila+1][columna - 1]
                imagen(upperfield, fila+1, columna - 1,im)

        if (columna + 1) <= len(upperfield[fila]) - 1 and fila - 1 >= 0:
            if upperfield[fila - 1][columna + 1] != "🔲":
                upperfield[fila - 1][columna + 1] = lowerfield[fila - 1][columna + 1]
                imagen(upperfield, fila - 1, columna + 1,im)

        if fila - 1 >= 0 and columna - 1 >= 0:
            if upperfield[fila - 1][columna - 1] != "🔲":
                upperfield[fila - 1][columna - 1] = lowerfield[fila - 1][columna - 1]
                imagen(upperfield, fila - 1, columna - 1,im)

    def imagen(field,fila,columna,im):
        font_type = ImageFont.truetype("seguiemj.ttf", 200)
        draw = ImageDraw.Draw(im)
        if field[fila][columna]=="🔲" or field[fila][columna]=="💥" or field[fila][columna]=="🏳️":
            for j in range(8):
                for k in range(8):
                    if j==fila and k==columna:
                        draw.text(xy=(10+280*k, 70+280*j), text=field[fila][columna], fill=(255, 255, 255), font=font_type)
        else:
            for j in range(8):
                for k in range(8):
                    if j==fila and k==columna:
                        draw.text(xy=(105+280*k, 70+280*j), text=field[fila][columna], fill=(255, 255, 255), font=font_type)

    def escribir(upperfield):
        g = ""
        c = 0
        for i in upperfield:
            c += 1
            g += i[0] + " " + i[1] + " " + i[2] + " " + i[3] + " " + i[4] + " " + i[5] + " " + i[6] + " " + i[7]
            if c != len(upperfield):
                g += ",\n"
        archivo = open("recursos/upperfield.txt", "w", encoding="utf-8")
        archivo.write(g)
        archivo.close()

    minas = 0
    num = [0, 1, 2, 3, 4, 5, 6, 7]

    while minas != 10:
        fila = random.choice(num)
        columna = random.choice(num)
        if lowerfield[fila][columna] != "💥":
            lowerfield[fila][columna] = "💥"
            minas += 1

    for filas in range(len(lowerfield)):
        for columna in range(len(lowerfield[filas])):
            celda = lowerfield[filas][columna]
            if celda != "💥":
                danger = 0
                if (filas + 1) <= len(lowerfield) - 1:
                    if lowerfield[filas + 1][columna] == "💥":
                        danger += 1
                if (columna + 1) <= len(lowerfield[filas]) - 1:
                    if lowerfield[filas][columna + 1] == "💥":
                        danger += 1
                if (filas - 1) >= 0:
                    if lowerfield[filas - 1][columna] == "💥":
                        danger += 1
                if (columna - 1) >= 0:
                    if lowerfield[filas][columna - 1] == "💥":
                        danger += 1
                if ((filas - 1) >= 0) and ((columna - 1) >= 0):
                    if lowerfield[filas - 1][columna - 1] == "💥":
                        danger += 1
                if ((filas - 1) >= 0) and ((columna + 1) <= len(lowerfield[filas]) - 1):
                    if lowerfield[filas - 1][columna + 1] == "💥":
                        danger += 1
                if ((filas + 1) <= len(lowerfield) - 1) and ((columna - 1) >= 0):
                    if lowerfield[filas + 1][columna - 1] == "💥":
                        danger += 1
                if ((filas + 1) <= len(lowerfield) - 1) and ((columna + 1) <= len(lowerfield[filas]) - 1):
                    if lowerfield[filas + 1][columna + 1] == "💥":
                        danger += 1
                if danger != 0:
                    lowerfield[filas][columna] = str(danger)

    archivo = open("recursos/created.txt", "r")
    data = archivo.readlines()
    for j in data:
        created=int(j)
    archivo.close()

    minasmarcadas = 0
    banderas=0

    archivo = open("recursos/minasmarcadas.txt", "r")
    data = archivo.readlines()
    for i in data:
        minasmarcadas += int(i)
    archivo.close()
    archivo = open("recursos/minasmarcadas.txt", "w", encoding="utf-8")
    archivo.write(str(minasmarcadas))
    archivo.close()

    archivo = open("recursos/banderas.txt", "r")
    data = archivo.readlines()
    for i in data:
        banderas += int(i)
    archivo.close()
    archivo = open("recursos/banderas.txt", "w", encoding="utf-8")
    archivo.write(str(banderas))
    archivo.close()


    if created==0:
        archivo = open("recursos/created.txt", "w")
        archivo.write("1")
        archivo.close()

        g = ""
        c = 0
        for i in lowerfield:
            c += 1
            g +=i[0] + " " +i[1] + " " + i[2] +" " + i[3] + " " + i[4] + " " + i[5]+" "+ i[6] + " " + i[7]
            if c != len(lowerfield):
                g += ",\n"
        archivo = open("recursos/lowerfield.txt", "w",encoding="utf-8")
        archivo.write(g)
        archivo.close()
    else:
        archivo = open("recursos/lowerfield.txt", "r",encoding="utf-8")
        data = archivo.readlines()
        archivo.close()
        a = ""
        for j in data:
            a += j.strip()
        a = a.split(",")
        lowerfield = listaboni(a)

        archivo = open("recursos/upperfield.txt", "r",encoding="utf-8")
        data = archivo.readlines()
        archivo.close()
        a = ""
        for j in data:
            a += j.strip()
        a = a.split(",")
        upperfield = listaboni(a)

    campo = ""
    for j in range(len(lowerfield)):
        for k in lowerfield[j]:
            campo += k + " "
        if j != len(lowerfield) - 1:
            campo += "\n"
    print(campo,"\n")

    over=False
    if minasmarcadas != 10:
        msg=msg.split(" ")
        accion = msg[0]
        fila=80
        columna=80
        for j in range(8):
            for k in range(8):
                if str(j * 8 + (k + 1)) == msg[1]:
                    fila = j
                    columna = k
        if fila==80 and columna==80:
            await ctx.send("seleccione una posición valida")

        elif accion == "m":
            upperfield[fila][columna] = "🏳️"
            im = Image.open("recursos/t.png")
            imagen(upperfield,fila,columna,im)
            im.save("recursos/t.png")
            escribir(upperfield)

            banderas += 1
            archivo = open("recursos/banderas.txt", "w", encoding="utf-8")
            archivo.write(str(banderas))
            archivo.close()

            if lowerfield[fila][columna] == "💥":
                minasmarcadas += 1
                archivo = open("recursos/minasmarcadas.txt", "w", encoding="utf-8")
                archivo.write(str(minasmarcadas))
                archivo.close()

        elif accion == "d":
            if upperfield[fila][columna] == "🏳️":
                upperfield[fila][columna]="🔳"
                escribir(upperfield)
                banderas -= 1
                archivo = open("recursos/banderas.txt", "w", encoding="utf-8")
                archivo.write(str(banderas))
                archivo.close()

                if lowerfield[fila][columna]=="💥":
                    minasmarcadas -= 1
                    archivo = open("recursos/minasmarcadas.txt", "w", encoding="utf-8")
                    archivo.write(str(minasmarcadas))
                    archivo.close()

                if (fila+columna)%2==0:
                    img2 = Image.new("RGB", (270, 270), color=(31, 25, 23))
                    img2.save("recursos/orange.png")
                    img = Image.open("recursos/t.png")
                    for j in range(8):
                        for k in range(8):
                            if j==fila and k==columna:
                                img.paste(img2, (5+284*k, 5+284*j))
                else:
                    img2 = Image.new("RGB", (270, 270), color=(0, 0, 0))
                    img2.save("recursos/orange.png")
                    img = Image.open("recursos/t.png")
                    for j in range(8):
                        for k in range(8):
                            if j==fila and k==columna:
                                img.paste(img2, (5+284*k, 5+284*j))

                img.save("recursos/t.png")

            else:
                await ctx.send("No existe una bandera en esta posición")

        elif accion == "e":
            if upperfield[fila][columna]!="🏳️":
                upperfield[fila][columna] = lowerfield[fila][columna]
                im = Image.open("recursos/t.png")
                imagen(lowerfield, fila, columna,im)
                im.save("recursos/t.png")
                if lowerfield[fila][columna] == "💥":
                    embed = discord.Embed(title="GameOver",color=discord.Color.red())
                    embed.set_image(url="https://i.pinimg.com/originals/11/bf/9c/11bf9c144c0ad3c418721c99a35961ca.gif")
                    await ctx.send(embed=embed)
                    over=True
                elif lowerfield[fila][columna] == "🔲":
                    if comprobar(lowerfield, fila, columna)[0] == True or comprobar(lowerfield, fila, columna)[1] == True or comprobar(lowerfield, fila, columna)[2] == True or comprobar(lowerfield, fila, columna)[3] == True:
                        p = 0
                        d = 0
                        w = 0
                        l = 0
                        im = Image.open("recursos/t.png")
                        for j in range(8):
                            if (columna + j) <= len(lowerfield[fila]) - 1 and p == 0:
                                upperfield[fila][columna + j] = lowerfield[fila][columna + j]
                                imagen(upperfield,fila,columna+j,im)
                                if lowerfield[fila][columna + j] != "🔲":
                                    p = 1
                            if (columna - (j)) >= 0 and d == 0:
                                upperfield[fila][columna - (j)] = lowerfield[fila][columna - (j)]
                                imagen(upperfield,fila,columna-j,im)
                                if lowerfield[fila][columna - (j)] != "🔲":
                                    d = 1
                            if (fila + (j)) <= len(lowerfield) - 1 and w == 0:
                                upperfield[fila + (j)][columna] = lowerfield[fila + (j)][columna]
                                imagen(upperfield,fila+j,columna,im)
                                if lowerfield[fila + (j)][columna] != "🔲":
                                    w = 1
                            if (fila - (j)) >= 0 and l == 0:
                                upperfield[fila - (j)][columna] = lowerfield[fila - (j)][columna]
                                imagen(upperfield,fila-j,columna,im)
                                if lowerfield[fila - (j)][columna] != "🔲":
                                    l = 1
                        im.save("recursos/t.png")

                    im = Image.open("recursos/t.png")
                    for j in range(7):
                        for y in range(8):
                            for x in range(8):
                                if upperfield[y][x] == "🔲":
                                    rellenar(upperfield, y, x,im)
                    im.save("recursos/t.png")
                escribir(upperfield)
            else:
                await ctx.send("Para marcar en una posición ya marcada, debes desmarcarla primero (.minas d {posición})")
        else:
            await ctx.send("Seleccione una accion valida")

        im = Image.open("recursos/t.png")
        font_type = ImageFont.truetype("seguiemj.ttf", 60)
        draw = ImageDraw.Draw(im)
        for j in range(8):
            for k in range(8):
                if upperfield[j][k]=="🔳":
                    if k>=4:
                        o=35
                    else:
                        o=0
                    draw.text(xy=(220 + 270 * k+o, 70 + 280 * j), text=str(j*8+(k+1)), fill=(255, 255, 255),font=font_type)
        im.save("recursos/t.png")

    campo = ""
    for j in range(len(upperfield)):
        for k in upperfield[j]:
            campo += k + " "
        if j != len(upperfield) - 1:
            campo += "\n"

    embed = discord.Embed(title="Buscaminas", description="Quedan "+str(10-banderas)+" minas por marcar", color=discord.Color.red())
    file = discord.File("recursos/t.png", filename="image.png")
    embed.set_image(url="attachment://image.png")
    await ctx.send(file=file, embed=embed)
    print(minasmarcadas)
    if minasmarcadas==10 or over==True:
        if minasmarcadas==10:
            await ctx.send("Ganaste!")
        fuente = "original/t.png"
        destino = "recursos/t.png"
        shutil.copyfile(fuente, destino)
        archivo = open("recursos/created.txt", "w")
        archivo.write("0")
        archivo.close()
        archivo = open("recursos/minasmarcadas.txt", "w")
        archivo.write("0")
        archivo.close()
        archivo = open("recursos/banderas.txt", "w", encoding="utf-8")
        archivo.write("0")
        archivo.close()
        archivo = open("recursos/upperfield.txt", "w",encoding="utf-8")
        archivo.write("🔳 🔳 🔳 🔳 🔳 🔳 🔳 🔳,\n🔳 🔳 🔳 🔳 🔳 🔳 🔳 🔳,\n🔳 🔳 🔳 🔳 🔳 🔳 🔳 🔳,\n🔳 🔳 🔳 🔳 🔳 🔳 🔳 🔳,\n🔳 🔳 🔳 🔳 🔳 🔳 🔳 🔳,\n🔳 🔳 🔳 🔳 🔳 🔳 🔳 🔳,\n🔳 🔳 🔳 🔳 🔳 🔳 🔳 🔳,\n🔳 🔳 🔳 🔳 🔳 🔳 🔳 🔳")
        archivo.close()

@bot.command()
async def sudoku(ctx,*,msg):
    import random
    fuente = "original/sudoku.jpg"
    destino = "recursos/sudoku.jpg"
    shutil.copyfile(fuente, destino)
    n=int(msg)
    def tableroboni(tablero):
        tab = ""
        for j in range(len(tablero)):
            for k in range(len(tablero[j])):
                for i in range(len(tablero[j][k])):
                    tab += str(tablero[j][k][i])
                    if i != len(tablero[j][k]) - 1:
                        tab += " "
                if k != len(tablero[j]) - 1:
                    tab += "|"
            tab += "\n"
            if (j == 2 or j == 5 or j == 8) and j != len(tablero) - 1:
                tab += "-" * 17 + "\n"
        return tab

    def comprobar_horizontal(tablero, pos1):
        usados = []
        for pos2 in range(3):
            for pos3 in range(3):
                num = tablero[pos1][pos2][pos3]
                if num not in usados and num != "-":
                    usados.append(tablero[pos1][pos2][pos3])
                elif num in usados:
                    return True
        return False

    def comprobar_vertical(tablero, pos2, pos3):
        usados = []
        for pos1 in range(9):
            num = tablero[pos1][pos2][pos3]
            if num not in usados and num != "-":
                usados.append(tablero[pos1][pos2][pos3])
            elif num in usados:
                return True
        return False

    def comprobar_cuadro(tablero, fila, pos2):
        usados = []
        n1 = 0
        n2 = 0
        if fila <= 2:
            n1 = 0
            n2 = 3
        elif fila > 2 and fila <= 5:
            n1 = 3
            n2 = 6
        elif fila > 5 and fila <= 8:
            n1 = 6
            n2 = 9
        for pos1 in range(n1, n2):
            for pos3 in range(3):
                num = tablero[pos1][pos2][pos3]
                if num not in usados and num != "-":
                    usados.append(tablero[pos1][pos2][pos3])
                elif num in usados:
                    return True
        return False

    def juego():
        numerote = 1
        numeros_puestos = 0
        grupo = 0
        fila = 0
        fail = 0
        entro_fila = False
        tablero = [[["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]],
                   [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]],
                   [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]],
                   [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]],
                   [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]],
                   [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]],
                   [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]],
                   [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]],
                   [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]]

        while numeros_puestos != 81:
            pos1 = random.randint(0 + fila, 2 + fila)
            pos2 = grupo
            pos3 = random.randint(0, 2)
            numero = numerote

            if tablero[pos1][pos2][pos3] == "-":
                tablero[pos1][pos2][pos3] = numero
                if comprobar_cuadro(tablero, pos1, pos2) == True or comprobar_vertical(tablero, pos2,
                                                                                       pos3) == True or comprobar_horizontal(
                        tablero, pos1) == True:
                    tablero[pos1][pos2][pos3] = "-"
                    fail += 1
                    if fail >= 100:
                        tablero = juego()
                        numeros_puestos = 81
                else:
                    entro_fila = False
                    numeros_puestos += 1
                    fail = 0
                    grupo += 1
                    if grupo == 3:
                        grupo = 0

            if (numeros_puestos % 3 == 0 and entro_fila == False):
                fila += 3
                entro_fila = True
                if fila > 8:
                    fila = 0
                    numerote += 1
        return tablero

    def juegorial(tablero):
        numeros_quitados = 0
        print(n)
        while numeros_quitados != n:
            pos1 = random.randint(0, 8)
            pos2 = random.randint(0, 2)
            pos3 = random.randint(0, 2)

            if tablero[pos1][pos2][pos3] != "":
                tablero[pos1][pos2][pos3] = ""
                numeros_quitados += 1
        return tablero

    tablero = juego()
    tablero=juegorial(tablero)
    tab=tableroboni(tablero)

    im = Image.open("recursos/sudoku.jpg")
    font_type = ImageFont.truetype("seguiemj.ttf", 60)
    draw = ImageDraw.Draw(im)
    o=0
    oo=0
    for j in range(9):
        for k in range(3):
            yy= 20+65*j+oo
            for l in range(3):
                xx = 25 + 65 * l+ o
                draw.text(xy=(xx, yy), text=str(tablero[j][k][l]), fill=(0, 0, 0),
                        font=font_type)
            o+=210
            if o==630:
                o=0
        if j==2 or j==5:
            oo+=12
    print(tab)
    im.save("recursos/sudoku.jpg")

    embed = discord.Embed(title="Sudoku", color=discord.Color.red())
    file = discord.File("recursos/sudoku.jpg", filename="image.png")
    embed.set_image(url="attachment://image.png")

    await ctx.send(file=file, embed=embed)

@bot.command(pass_context=True)
async def reset2(ctx):
    fuente = "original/t.png"
    destino = "recursos/t.png"
    shutil.copyfile(fuente, destino)
    archivo = open("recursos/created.txt", "w")
    archivo.write("0")
    archivo.close()
    archivo = open("recursos/minasmarcadas.txt", "w")
    archivo.write("0")
    archivo.close()
    archivo = open("recursos/banderas.txt", "w", encoding="utf-8")
    archivo.write("0")
    archivo.close()
    archivo = open("recursos/upperfield.txt", "w",encoding="utf-8")
    archivo.write("🔳 🔳 🔳 🔳 🔳 🔳 🔳 🔳,\n🔳 🔳 🔳 🔳 🔳 🔳 🔳 🔳,\n🔳 🔳 🔳 🔳 🔳 🔳 🔳 🔳,\n🔳 🔳 🔳 🔳 🔳 🔳 🔳 🔳,\n🔳 🔳 🔳 🔳 🔳 🔳 🔳 🔳,\n🔳 🔳 🔳 🔳 🔳 🔳 🔳 🔳,\n🔳 🔳 🔳 🔳 🔳 🔳 🔳 🔳,\n🔳 🔳 🔳 🔳 🔳 🔳 🔳 🔳")
    archivo.close()
    await ctx.send("campo reseteado")

@bot.command(pass_context=True)
async def clear(ctx,amount=5):
    await ctx.channel.purge(limit=int(amount))

@bot.command(pass_context=True)
async def mauro(ctx):
    await ctx.send("chupalo")
    await ctx.send("https://c.tenor.com/uXaTrkqlphUAAAAd/mauricio-meme.gif")

@bot.command(pass_context=True)
async def jona(ctx):
    await ctx.send("https://c.tenor.com/3c2t3tQEUDQAAAAd/kingdomcord-jonah.gif")

@bot.command(pass_context=True)
async def seba(ctx):
    await ctx.send("https://c.tenor.com/0krtD6jJQnIAAAAd/moon-festival-seba-culiao.gif")

@bot.command(pass_context=True)
async def pato(ctx):
    await ctx.send("https://c.tenor.com/VOwaCgTnl_sAAAAC/quak-pato.gif")

@bot.command(pass_context=True)
async def erick(ctx):
    await ctx.send("https://upload.wikimedia.org/wikipedia/commons/7/7c/Cima_da_Conegliano%2C_God_the_Father.jpg")

@bot.command(pass_context=True)
async def esteban(ctx):
    await ctx.send("https://pbs.twimg.com/media/Ex-2m_TWQAIBUfy.jpg")

@bot.command(pass_context=True)
async def muga(ctx):
    await ctx.send("https://c.tenor.com/pE_Ab4lv9BkAAAAC/bugsbunny-tired.gif")

@bot.command(pass_context=True)
async def maceta(ctx):
    await ctx.send("https://c.tenor.com/Lglx3ARI5xMAAAAC/orchid-pots-pots.gif")

@bot.command(pass_context=True)
async def nacho(ctx):
    await ctx.send("https://c.tenor.com/-lVTREK1ruMAAAAC/nacho-pop-fuerte.gif")

@bot.command(pass_context=True)
async def tutulio(ctx):
    await ctx.send("https://youtu.be/0EM6j7wpVmM")

@bot.command()
async def wa(ctx):
    autor=str(ctx.author)
    print(autor)

    archivo = open("mumuda", "r",encoding="utf-8")
    data = archivo.readlines()
    archivo.close()
    a = ""
    for j in data:
        a += j.strip()
    print(a)
    if a!="":
        a = a.split(",")
        a=a[:-1]
        print(a)
        datos = listaboni2(a)
        print(datos)
        esta=False
        for j in datos:
            for k in j:
                if autor==k:
                    esta=True
        if esta==True:
            aber=random.choice(losk)
            embed = discord.Embed(title=aber[0], description="Reaccione al emoji para reclamar! (en proceso)",color=discord.Color.red())
            embed.set_image(url=aber[1])
            msg=await ctx.send(embed=embed)
            await msg.add_reaction("✅")
        else:
            nuevalista = [autor, 0]
            datos.append(nuevalista)
            print(datos)
            k = ""
            c = 0
            for i in a:
                c += 1
                k += str(i[0]) + "↔" + str(i[1])
                if c != len(a):
                    k += ","
            k+=","
            archivo = open("mumuda", "w", encoding="utf-8")
            archivo.write(k)
            archivo.close()
            await ctx.send("bienvenido a mumuda")
    else:
        datos=[]
        nuevalista=[autor,0]
        datos.append(nuevalista)
        print(datos)
        k=""
        c=0
        for i in datos:
            c+=1
            k+=str(i[0])+"↔"+str(i[1])
            k+=","
        archivo = open("mumuda", "w",encoding="utf-8")
        archivo.write(k)
        archivo.close()
        await ctx.send("bienvenido a mumuda")

@bot.event
async def epico():
    import datetime
    await bot.wait_until_ready()
    while not bot.is_closed():
        fecha=str(datetime.datetime.now())
        hora = int(datetime.datetime.now().time().strftime("%H"))
        weekday=datetime.date(int(fecha[:4]),int(fecha[5:7]),int(fecha[8:10])).weekday()
        if weekday==3 and hora >=13:
            channel = bot.get_channel(692538110902272061)
            await channel.send(epicfreee())
        await asyncio.sleep(585360)

@bot.event
async def hora():
    import datetime
    await bot.wait_until_ready()
    while not bot.is_closed():
        hora = int(datetime.datetime.now().time().strftime("%H"))
        min=int(datetime.datetime.now().time().strftime("%M"))
        if hora ==21 and min==4:
            channel = bot.get_channel(692538110902272061)
            await channel.send("alive")
        await asyncio.sleep(585360)

@bot.event
async def on_ready():
    game = discord.Game("´ta exquisito fijate")
    channel = bot.get_channel(924501814928367636)
    print("vamo chile")
    await channel.send("bot online")
    await bot.change_presence(status=discord.Status.online, activity=game)


was=[934946733652328458] #convertirlo en archivo
@bot.event
async def on_reaction_add(reaction,user):
    c=reaction.message
    aidi=c.id
    agregar(aidi, user, aber, was,reaction)

def agregar(aidi, user, aber, was,reaction):
    print(user)
    if str(user) != "tutulio#4162" and str(reaction) =="✅":
        sacado=aber[2]
        archivo=open("usadoos","r")
        data=archivo.readlines()
        archivo.close()
        usados=""
                            #revisar la caga que hay con el flujo
        for j in data:
            usados+=j
        if usados!="":
            usados=usados.split(",")
        if sacado not in usados:
            usados+=str(sacado)+","
            archivo=open("usadoos","w")
            archivo.write(usados)
            archivo.close()

            archivo=open("mumuda","r",encoding="utf-8")
            data=archivo.readlines()
            eltipo=len(str(user))
            c=0
            for j in range(len(data)):
                print(data[c:eltipo+c])
                if data[c:eltipo+c]==user:
                    print("a")
                c+=1
        else:
            return
    else:
        was.append(aidi)

bot.run(token)
