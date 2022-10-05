# import Libraries
import requests
import os
import shutil
import urllib.request
from bs4 import BeautifulSoup

#urls array
url = 'http://www.rudolfsteineraudio.com/lecturesimagebased.html'

print( "**********************" )
print( "THE SCRAPING HAS BEGUN" )
print( "**********************" )

i = 0
base_url="http://www.rudolfsteineraudio.com/"
new_dir = 1
book_url = []


response = requests.get( url )
soup = BeautifulSoup( response.content, 'html.parser' )

#soup = bs( urllib.request.urlopen( url ), "html.parser" )

links = soup.find_all('a')

for link in links:

    if( '.html' in link.get( 'href' ) ):
        i+=1
    

        link = base_url+str( link.get( 'href' ) )
        t=link.get_text()
        print('text: '+t)
        #print("base: "+base_url)
        
        link=link.rsplit('/',1)[0]+"/"
        #print(link)

        b = requests.get( link )
        soup = BeautifulSoup( b.content, 'html.parser' )
        #soup = bs( urllib.request.urlopen( b.content ), "html.parser" )

        book_links = soup.find_all( 'a' )

        for x in book_links:
            print( x.string )

        
        for book in book_links:
            
            if( '.zip' in book.get( 'href') ):
                zip_title=book.contents

            if( '.mp3' in book.get( 'href' ) ):
                book_title = book.attrs
                book_link=link+book.get('href')
                print(book_title)

                # Get response object
                #book_mp3 = requests.get( book_link )

                #print( "Downloading: "+book_title )

                # Write it
                #mp3 = open( book_title, 'wb' )
                #mp3.write( book_mp3.content )
                #mp3.close()

        
        if( i == 1 ):
            break
    break

    #Make Dir
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
print( str(i)+" Book Downloaded" )

