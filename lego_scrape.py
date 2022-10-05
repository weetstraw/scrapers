# import Libraries
import requests
import os
import shutil
from bs4 import BeautifulSoup

#urls array
urls = [
        [ 'https://www.lego.com/en-us/service/buildinginstructions/search?q=&theme=e2899f48-618a-4c00-9c19-57c29c0301d3&sort=relevance', 'lego_city' ]
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

    for link in links:
        print( link.get('href') )

    break

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

