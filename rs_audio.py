import requests,csv,re
from bs4 import BeautifulSoup

site = requests.get('http://www.rudolfsteineraudio.com/cycleoftheyear/cycleoftheyearpage.html')

soup = BeautifulSoup(site.content, 'html.parser')

#Page Title
page_title = soup.title.string

#Grab MP3 links
audio_links = []
links = soup.findAll('a', href=re.compile('^(.*).mp3') )

for link in links:
    src = link.get( 'href' )
    name = link.string
    audio_links.append( { "page title":page_title, "name":name, "src":src } )


print(audio_links)


#images_list = []
#images = soup.select('img')

#for image in images:
#    src = image.get('src')
#    alt = image.get('alt')
#    images_list.append({ "src" : src, "alt" : alt })


#for image in images_list:
#    print(image)

filename = 'scrapey.csv'
with open( filename, 'w', newline='' ) as f:
    w = csv.DictWriter( f, [ 'page title','name','src'] )
    w.writeheader()
    w.writerows( audio_links )

