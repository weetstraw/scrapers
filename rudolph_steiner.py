# import Libraries
import requests
import os
import string
import shutil
from bs4 import BeautifulSoup

url = 'http://www.rudolfsteineraudio.com/lecturesimagebased.html'

print( "~~~~~~~~~ THE SCRAPING HAS BEGUN ~~~~~~~~~~~~" )

base_url="http://www.rudolfsteineraudio.com/"

response = requests.get( url )
soup = BeautifulSoup( response.content, 'html.parser' )

links = soup.find_all('a')

for link in links:

    if( '.html' in link.get( 'href' ) ):

        book_url = base_url+str( link.get( 'href' ) )
        #book_url_split = book_url.rsplit('/',1)[0]+"/"

        b = requests.get( book_url)
        book = BeautifulSoup( b.content, 'html.parser' )
        
        # Get page title
        book_title = book.title.get_text().lower()
        
        #print( 'book title: '+str( book_title ) )

        # Make book directory
        is_dir = os.path.isdir( book_title )

        if is_dir:
            shutil.rmtree( book_title )
            print( "Removed existing directory" )

        os.mkdir( book_title )

        # Get all links on page
        book_links = book.find_all( 'a' )

        # Now just the mp3 links 
        for book_link in book_links:

            if( '.mp3' in book_link.get( 'href' ) ):

                book_url_base = book_url.rsplit('/',1)[0]+"/"

                mp3_link = book_link.get( 'href' )
                mp3_url = book_url_base+mp3_link
                #print( "mp3 url: "+str( mp3_url ) )

                mp3_text = book_link.get_text()
                #mp3_text = textwrap.shorten( mp3_text, 70 )
                mp3_text = mp3_text[:70].lower()
                #mp3_text = clean( mp3_text, replace_with_punct="" )

                
                mp3_text = mp3_text.translate( str.maketrans( { key: None for key in string.punctuation } ) ) 

                # Get response object
                mp3_file = requests.get( mp3_url )

                print( "Downloading: "+str(mp3_text) )

                # Write it
                mp3_file_name = mp3_text+'.mp3'
                mp3 = open( mp3_file_name, 'wb' )
                mp3.write( mp3_file.content )
                mp3.close()

                # Move MP#
                cur_dir = os.getcwd()

                shutil.move( os.path.join( cur_dir,mp3_file_name ), book_title ) 

        print( str( book_title )+" done downloading!" )

print( "~~~~~~~~~ THE SCRAPING HAS ENDED ~~~~~~~~~~~~" )

