import json
import colorama
from colorama import Fore, Back, Style
import requests
import time
import discord
from dhooks import Webhook
from discord.ext import commands
from listofitemstocheck import *

x = 0
colorama.init(autoreset= True)
client = commands.Bot(command_prefix= '.')




def isinStock():

    while x == 0:

        for modelnumber, lastnum in itemList.items():
            response = requests.get('https://www.newegg.com/product/api/ProductRealtime?ItemNumber='+ lastnum + '&RecommendItem=&BestSellerItemList=&IsVATPrice=true')
            jsonlist = json.loads(response.text)['MainItem']

            try:

                print(jsonlist['Instock'] , jsonlist['Stock'] ,  jsonlist['StockForCombo'])
                title = (jsonlist['Description']['Title'])
                print(title)
                price = str(jsonlist['OriginalUnitPrice'])
                urlKeyword = str(jsonlist['Description']['UrlKeywords'])

                pictureName = jsonlist['Image']['ItemCellImageName']

                link = 'http://c1.neweggimages.com/ProductImageOriginal/'+ pictureName
            except:

                print(Fore.RED + "Whoops Encountered and error!")






            while jsonlist['Stock'] == 0:

                print('Item is Out of Stock!' + lastnum)
                time.sleep(5)
                break



            else:

                print("Item is in stock!" + modelnumber)
                print('https://secure.newegg.com/Shopping/AddToCart.aspx?Submit=ADD&ItemList='+ modelnumber)
                notification = Webhook("https://discord.com/api/webhooks/788347459939991553/8dCS1ZgyYx-z9hjV1NC7wHsz5OBSgc4g_AeHDlCCZR_mkj2xHe8I96SKA-EN10HcdRvF")
                myEmbed = discord.Embed(title='' + title, description='One Just Popped in Stock!', color=0x8c00ff)
                myEmbed.add_field(name='Product Link',value= 'https://www.newegg.com/' + urlKeyword + '/p/' + modelnumber,inline=False)
                myEmbed.add_field(name='Add To Cart Link',value='https://secure.newegg.com/Shopping/AddToCart.aspx?Submit=ADD&ItemList=' + modelnumber,inline=False)
                myEmbed.add_field(name='Price', value='Price: $' + price, inline=False)
                myEmbed.set_image(url=link)  # get image from page
                myEmbed.set_footer(text="Thank Jimmy!")
                notification.send(embed=myEmbed)
                time.sleep(5)




isinStock()