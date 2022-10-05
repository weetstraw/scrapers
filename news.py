import requests,csv,re
from bs4 import BeautifulSoup

site = requests.get('https://www.digiday.com')

soup = BeautifulSoup(site.content, 'html.parser')

#Page Title
page_title = soup.title.string
print( page_title )

#Grab MP3 links
#links = soup.findAll('a')
all_links = []

#top_class = soup.find( 'div', class_=re.compile('^HomepageLayout_container(.*)') )
news_classes = [
    #"HomepageLayout_container__GwxXx",
    "news-list",
    "posts"
]
#top_class = soup.find( 'div', class_=re.compile('') )

for news in news_classes:
    top_class = soup.find( class_=news )
    top_links = top_class.find_all('a')


for link in top_links:
    link_title = link.text
    link_url = link.get( 'href' )
    print( link.attrs )
    #print( link_title+": "+link_url )

#print(all_links)

#print(all_links)
print("Done!")


#images_list = []
#images = soup.select('img')

#for image in images:
#    src = image.get('src')
#    alt = image.get('alt')
#    images_list.append({ "src" : src, "alt" : alt })


#for image in images_list:
#    print(image)

# filename = 'news.csv'
# with open( filename, 'w', newline='' ) as f:
#     w = csv.DictWriter( f, [ 'name','src'] )
#     w.writeheader()
#     w.writerows( all_links )

