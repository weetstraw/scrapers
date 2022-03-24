# import Libraries
import requests
from bs4 import BeautifulSoup

#urls array
urls = [
    'https://www.rosicrucian.org/rosicrucian-digest-archive-1920s',
    'https://www.rosicrucian.org/rosicrucian-digest-archive-1930s',
    'https://www.rosicrucian.org/rosicrucian-digest-archive-1940s',
    'https://www.rosicrucian.org/rosicrucian-digest-archive-1950s',
    'https://www.rosicrucian.org/rosicrucian-digest-archive-1960s',
    'https://www.rosicrucian.org/rosicrucian-digest-archive-1970s',
    'https://www.rosicrucian.org/rosicrucian-digest-archive-1980s',
    'https://www.rosicrucian.org/rosicrucian-digest-archive-1990s',
    'https://www.rosicrucian.org/rosicrucian-digest-archive-2000s'
]

for url in urls:
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    links = soup.find_all('a')

    i=0

    for link in links:
        if( '.pdf' in link.get( 'href', [] ) ):
            i += 1
            print( "Downloading file: ", i )

            # Get response object
            response = requests.get( link.get('href') )

            #write it
            pdf = open( "pdf"+str(i)+".pdf", 'wb' )
            pdf.write( response.content )
            pdf.close()
            print( "File ", i, " downloaded!" )

    print("all the files have been donwloaded")

