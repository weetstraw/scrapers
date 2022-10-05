# import Libraries
import requests
import os
import shutil
from bs4 import BeautifulSoup

#urls array
urls = [
    [ 'https://www.rosicrucian.org/rosicrucian-digest-archive-1920s', '1920s' ],
    [ 'https://www.rosicrucian.org/rosicrucian-digest-archive-1930s', '' ],
    [ 'https://www.rosicrucian.org/rosicrucian-digest-archive-1940s', '1940s' ],
    [ 'https://www.rosicrucian.org/rosicrucian-digest-archive-1950s', '1950s' ],
    [ 'https://www.rosicrucian.org/rosicrucian-digest-archive-1960s', '1960s' ],
    [ 'https://www.rosicrucian.org/rosicrucian-digest-archive-1970s', '1970s' ], 
    [ 'https://www.rosicrucian.org/rosicrucian-digest-archive-1980s', '1980s' ],
    [ 'https://www.rosicrucian.org/rosicrucian-digest-archive-1990s', '1990s' ],
    [ 'https://www.rosicrucian.org/rosicrucian-digest-archive-2000s', '2000s' ]
]

print( "**********************" )
print( "THE SCRAPING HAS BEGUN" )
print( "**********************" )

i = 0
new_dir = 1
breaker = 0

for url in urls:
    
    #stop it!
    breaker+=1
    if breaker == 3:
        break

    response = requests.get( url[0] )

    soup = BeautifulSoup( response.text, 'html.parser' )

    links = soup.find_all('a')

    #Make Dir
    dir_mode = 0o666

    if url[1]:
        dir_name = url[1] 
    else:
        dir_name = "PDFs "+str(new_dir)
        new_dir+=1

    is_path = os.path.isdir( dir_name )

    if is_path:
        shutil.rmtree( dir_name )
        print( "Removed existing version of: "+dir_name )

    os.mkdir(dir_name)

    for link in links:
        if( '.pdf' in link.get( 'href', [] ) ):
            i += 1

            pdf_name = os.path.basename( link.get('href') ) 


            print( "Downloading file: ", dir_name+"/"+pdf_name )

            # Get response object
            response = requests.get( link.get('href') )

            # Write it
            pdf = open( pdf_name, 'wb' )
            pdf.write( response.content )
            pdf.close()


            # More PDF
            cur_dir = os.getcwd()
        
            shutil.move( os.path.join( os.getcwd(), pdf_name), dir_name )
            
            #if( i == 3 ):
            #    break

print( "**********************" )
print( "THE SCRAPING HAS ENDED" )
print( str(i)+" Files Downloaded" )
print( "**********************" )

