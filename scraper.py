from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from shutil import copyfileobj
import requests
import sys
import os

class WebPage():

    def __init__(self, url):

        self.url = url
        self.files = self.filenames()
        # produce list of pdf URLs from base URL and relative path
        self.link_list = [self.url + file for file in self.files if not file.startswith('http')]

    def filenames(self):
        '''
        Produces list of PDF filenames linked within body of webpage.
        '''
        html = requests.get(self.url).content
        bs = BeautifulSoup(html, 'lxml')

        links = bs.findAll('a')

        final_links = set()
        for link in links:
            text = link.attrs['href']
            if text.endswith(".pdf"):
                final_links.add(text)

        return final_links


    def download(self, save_dir=''):
        '''
        Downloads PDFs into specified directory (or current directory
        if none specified)
        '''
        if not os.path.exists(save_dir):
            print('Specified directory does not exist')
            print('Attempting to create path to directory')
            try:
                os.makedirs(save_dir)  
                print('Path to {} created successfully'.format(save_dir))
            except OSError as error:  
                print(error)
                return save_dir

        if self.link_list:
            for pdf in self.link_list:
                filename = pdf.split('/')[-1]
                filepath = save_dir + filename

                if not os.path.exists(filepath):
                    print('Copying {} to {}'.format(filename, save_dir))
                    print()
                    try:
                        urlretrieve(pdf, filename=filepath)
                    except ValueError as error:
                        print(error)
  
                else:
                    print('{} already exists in {}'.format(filename, save_dir))


if __name__ == "__main__":

    if len(sys.argv) == 1:
        print("Please enter a URL to parse")
    else:
        url = sys.argv[1]
        page = WebPage(url)
        if page.files:
            if len(sys.argv) == 3:
                path = sys.argv[2]
                print('Found {} PDF files to copy to the {} directory'.format(len(page.files), path))
                print()
                page.download(path)
            else:
                print('Copying {} PDF files to the current directory'.format(len(page.files)))
                page.download()
            print('Scraping of {} complete.'.format(page.url))
        else:
            print('No PDF files found on {}'.format(url))
            
