

import requests , re , random 
import urllib , os 
from telethon.tl import functions
from userbot import ALIVE_NAME
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from userbot.utils import admin_cmd
import asyncio
from time import sleep

FONT_FILE_TO_USE = "Fonts/1942.ttf"



DEFAULTUSER = str(ALIVE_NAME)


AUTOPFP_PACK = os.environ.get("AUTOPFP_PACK", None)
if AUTOPFP_PACK is None:
  PACK = [
  "Epic-Space-Wallpaper",
   "Acoustic-Guitar-Wallpaper-HD",
   "Taylor-Guitar-Wallpaper",
   "Classical-Music-Wallpapers-for-Desktop",
   "Prs-Guitar-Wallpaper",
   "Iron-Man-Wallpaper-1920x1080",
   "Dodge-Challenger-Black-Hellcat-Wallpaper",
   "V-for-Vendetta-Mask-Wallpaper",
   "Toxic-Mask-Wallpapers",
   "Minion-Desktop-Wallpaper",
   "Epic-1080p-Wallpapers",
   "Japanese-Desktop-Wallpaper",
   "Cool-Gold-Cars-Wallpapers",
   "Pretty-Wallpapers-for-iPhone-Quotes",
   "dark-abstract-wallpaper",
   "abstract-dark-wallpaper",
   "abstract-wallpapers-and-screensavers",
   "roaring-lion-wallpaper",
   "wolves-screensavers-and-wallpaper",
   "cool-wallpaper-for-men",
   "Epic-1080p-Wallpapers",
   "hacker-background",
   "Vietnam-War-Wallpapers",
   "War-of-the-Worlds-Wallpaper",
   "War-Plane-Wallpaper",
   "World-War-Ii-Wallpaper",
   "Cool-War-Wallpapers",
   "World-War-2-Wallpaper-HD"

  ]
else:
  PACK = AUTOPFP_PACK
async def animepp():
    os.system("rm -rf donot.jpg")
    rnd = random.randint(0, len(PACK) - 1)
    pack = PACK[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile('/\w+/full.+.jpg')
    f = f.findall(pc)
    fy = "http://getwallpapers.com"+random.choice(f)
    print(fy)
    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve("https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf","f.ttf")
    urllib.request.urlretrieve(fy,"donottouch.jpg")
@borg.on(admin_cmd(pattern="wallpapers ?(.*)"))
async def main(event):
    await event.edit("**uploading wallpapers \ndone check ur DP.**") 
    downloaded_file_name = "./FRIDAY/original_pic.png"

    downloader = SmartDL(Var.DOWNLOAD_PFP_URL_CLOCK, downloaded_file_name, progress_bar=False)

    downloader.start(blocking=False)

    photo = "photo_pfp.png"

    while not downloader.isFinished():

        place_holder = None
    while True:

#RIP Danger zone Here no editing here plox

        R = random.randint(0,256)

        B = random.randint(0,256)

        G = random.randint(0,256)

        FR = (256 - R) 

        FB = (256 - B) 

        FG = (256 - G) 

        shutil.copy(downloaded_file_name, photo)

        image = Image.open(photo)

        image.paste( (R, G, B), [0,0,image.size[0],image.size[1]])

        image.save(photo)

        

        #Edit only Below part ð Or esle u will be responsible ð¤·ââ

        current_time = datetime.now().strftime("\n\n Time: %H:%M:%S \n \n Date: %d/%m/%y")

        img = Image.open(photo)

        drawn_text = ImageDraw.Draw(img)

        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 40)

        ofnt = ImageFont.truetype(FONT_FILE_TO_USE, 40)

        drawn_text.text((200, 400), current_time, font=fnt, fill=(FR,FG,FB))

        drawn_text.text((250, 250), f"{DEFAULTUSER}", font = ofnt, fill=(0,FG,0))

        img.save(photo)

        file = await event.client.upload_file(photo)  # pylint:disable=E0602




      try:
        await animepp()
        file = await event.client.upload_file("donottouch.jpg")
        await event.client(functions.photos.DeletePhotosRequest(await event.client.get_profile_photos("me", limit=1)))
        await event.client(functions.photos.UploadProfilePhotoRequest( file))
        os.system("rm -rf donottouch.jpg")
      except:
        pass
      await asyncio.sleep(60) #Edit this to your required needs
