import os
import sys
import base64
import json
from termcolor import colored, cprint
from TwitterAPI import TwitterAPI, TwitterOAuth, TwitterRequestError, TwitterConnectionError
import requests
import pafy
import youtube_dl
from random_word import RandomWords
from pyfiglet import Figlet
import ffmpeg
from textblob import TextBlob
import numpy as np
import pandas as pd
import boto3
from RedditReader import Subreddit
from botocore.exceptions import NoCredentialsError
import threading
import asyncio
import schedule
import time
import random
import discord
from discord.ext import commands
consumer_key = os.environ["consumer_key"]
consumer_secret = os.environ["consumer_secret"]
access_token_key = os.environ["access_token_key"]
access_token_secret = os.environ["access_token_secret"]
api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
token = os.environ['BOT_TOKEN']
bot = commands.Bot(command_prefix='n!')
prefix = 'n!'
fartbaby = []
sanjay = []
ACCESS_KEY = 'AKIAI5VZR2QXQVFDZYZA'
SECRET_KEY = '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'
client = discord.Client()
d = {}
# Hello Horse it is trump justto see if it is even working
heylisten = 'trump'
df = pd.DataFrame(data=d)
nomoresayingcusswords = ["Why would you say such a thing.", "Swearing is bad, you know.",
                         "You really need your mouth washing young boy.", "No saying cuss words in this house!"]
steam = ["raping", "writing a diss track on elmo", "eating food", "being a swag dude"]
minion = ["http://shiretoko.miemasu.net/CgiStart?page=Single&Mode=Motion&",
          "http://61.211.241.239/CgiStart?page=Single&Mode=Motion&Language=1",
          "http://webcam.stanburyvillageschool.co.uk/top.htm?"]

os.system('')


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# test commit aheueheheuehheueh
# ok it works!
def log(message):
    print("[" + str(time.clock_gettime) + "]" + message)


@bot.event
async def on_ready():
    art = f"""{bcolors.OKCYAN}  __                          
   _________  / /_  ____  ____  __  ______ 
  / ___/ __ \/ __ \/ __ \/ __ \/ / / / __ \
 / /  / /_/ / /_/ / /_/ / / / / /_/ / /_/ /
/_/   \____/_.___/\____/_/ /_/\__,_/\____/ 
                                           """
    log(art)
    log(f'{bcolors.ENDC}' + 'i sent one {0.user}'.format(bot))
async def downloadyt(ctx,url):
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.cache.remove()
            info_dict = ydl.extract_info(url, download=False)
            ydl.prepare_filename(info_dict)
            with youtube_dl.YoutubeDL({'format': '136'}) as ydl:
                ydl.download([url])
            return True
    except Exception:
        await ctx.send("Something went wrong.")
        return False
    await ctx.send()
    log('hello! ' + arg)
    try:
        await ctx.send(video.title, file=discord.File("video.mp4"))
    except discord.HTTPException:
        await ctx.send("Da youtube video made like ya mom and was big and fat. \n So, it could not be sent. Sorry. Bitch.")
        os.remove('video.mp4')
    os.remove('video.mp4')
@bot.event
async def on_command_error(ctx, error):
    await ctx.channel.send("Free error for you! Contact bot owner if confused\n```" + str(error) + "```")
@bot.command(brief='Download a video from YouTube.')
async def dl(ctx, arg):
    await downloadyt(ctx,arg)

@bot.command(brief='Downloads a YouTube video with custom bitrate ("awesomify")')
async def awesomify(ctx, arg1, arg2, arg3):
    video = pafy.new(arg1)
    thepoopbaby = '```\n' + 'Video title: ' + video.title + '\nViews: ' + str(
        video.viewcount) + '\nUploaded by: ' + video.author + '```'
    await ctx.send(thepoopbaby)
    log('hello! ' + arg1)
    best = video.getbest()
    best.download(filepath="video." + best.extension, quiet=False)
    fartypants = "video." + best.extension
    stream = ffmpeg.input(fartypants)
    out = ffmpeg.output(stream, 'pee.mp4', video_bitrate=int(arg2), audio_bitrate=int(arg3))
    ffmpeg.run(out)
    await ctx.send(video.title, file=discord.File('pee.mp4'))
    os.remove('video.mp4')
    os.remove('pee.mp4')


@bot.command(brief='makes you a brand new kity just for you and you only!')
async def shuffle(ctx):
    r = RandomWords()
    img_data = requests.get('https://thiscatdoesnotexist.com').content
    with open('cat.jpg', 'wb') as handler:
        handler.write(img_data)
    with open('cat.jpg', 'rb') as f:
        peeface = f.read()
    await ctx.send('herei go')
    try:
        log('fdetu fgteev')
        await bot.user.edit(avatar=peeface)
    except:
        await ctx.send('EPIC FAIL!! try later')
    else:
        os.remove('cat.jpg')


@bot.command(brief='reddit searcher', description=prefix + "reddit <subreddit to be searched>")
async def reddit(ctx, arg):
    fgteev = Subreddit(arg)
    fgteev.get_random()
    url = fgteev.url
    await ctx.send(url)


@bot.command(brief='Figlet art',
             description='Figlet art, Examples of fonts are located at http://www.figlet.org/examples.html')
async def fart(ctx, font, text):
    f = Figlet(font=font)
    art2 = '```\n' + f.renderText(text) + '```'
    await ctx.send(art2)

admins = ("","")
@bot.command(brief='popentime')
async def exec(ctx, arg):
    if (ctx.author.id == 511989134043381760) or (ctx.author.id == 258401707556470785):
        exe = os.popen(arg)
        output = exe.read()
        print(output)
        try:
            await ctx.send('```\n' + output + '```')
        except discord.HTTPException:
            print('Farto Mode.')
            with open('output.txt', 'a+') as out:
                out.write(output)
            await ctx.send(file=discord.File('output.txt'))
            os.remove('output.txt')


@bot.command(brief='What guilds am I in?')
async def guilds(ctx):
    if ctx.author.id == 511989134043381760:
        guildz = []
    for guild in bot.guilds:
        guildz.append(guild.name)
    await ctx.send('```\n' + '\n'.join(guildz) + '```')
@bot.command(brief='tweeter')
async def tweet(ctx, arg):
    jsony = {'status':arg}
    r = api.request('statuses/update', jsony)
    erwe = r.text
    internationalassday = json.loads(erwe)
    await ctx.send('https://twitter.com/i/status/' + internationalassday['id_str'])
@bot.command(brief='listen', aliases=['changelistener'])
async def listen(ctx, arg):
    global heylisten
    await ctx.send('was listening to ' + '``' + heylisten + '``')
    heylisten = arg
    await ctx.send('Now listening to ' + '``' + heylisten + '``')
@bot.command(brief='retweet')
async def retweet(ctx, id):
    jsony = {'id':id}
    r = api.request('statuses/retweet/' + id, jsony)
    erwe = r.text
    internationalassday = json.loads(erwe)
    await ctx.send('https://twitter.com/i/status/' + internationalassday['id_str'])
@bot.command(brief='quote retweet')
async def qretweet(ctx, id, qt):
    fartm4rio = qt + ' https://twitter.com/i/status/' + id
    jsony = {'status':fartm4rio}
    r = api.request('statuses/update', jsony)
    erwe = r.text
    internationalassday = json.loads(erwe)
    await ctx.send('https://twitter.com/i/status/' + internationalassday['id_str'])
@bot.command(brief='tweeter with media')
async def mediatweet(ctx, arg):
    attachment = ctx.message.attachments[0]
    img_data = requests.get(attachment.url).content
    with open('image', 'wb+') as handler:
        handler.write(img_data)
    with open('image', 'rb') as handler:
        data = handler.read()
    jsony = {'status':arg}
    r = api.request('statuses/update_with_media', jsony, {'media[]':data})
    erwe = r.text
    internationalassday = json.loads(erwe)
    await ctx.send('https://twitter.com/i/status/' + internationalassday['id_str'])
    os.remove('image')
@bot.command(brief='like a twitter p0st')
async def like(ctx, id):
    jsony = {'id':id}
    r = api.request('favorites/create', jsony)
    erwe = r.text
    internationalassday = json.loads(erwe)
    await ctx.send('i liked it')
@bot.command(brief='unlike a twitter p0st')
async def unlike(ctx, id):
    jsony = {'id':id}
    r = api.request('favorites/destroy', jsony)
    erwe = r.text
    internationalassday = json.loads(erwe)
    await ctx.send('i unliked it')
@bot.command(brief='change twitter avatar')
async def avatar(ctx):
    attachment = ctx.message.attachments[0]
    img_data = requests.get(attachment.url).content
    with open('image', 'wb+') as handler:
        handler.write(img_data)
    with open('image', 'rb') as handler:
        data = handler.read()
        encoded_string = base64.b64encode(data)
    jsony = {'image':encoded_string}
    r = api.request('account/update_profile_image', jsony)
    erwe = r.text
    internationalassday = json.loads(erwe)
    await ctx.send('i did it')
    os.remove('image')
bot.run(token)