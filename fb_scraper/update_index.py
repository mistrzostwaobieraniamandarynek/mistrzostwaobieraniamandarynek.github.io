#!/usr/bin/env python3

import os
import webbrowser
from dotenv import load_dotenv
from bs4 import BeautifulSoup, Comment
from fb_api import get_last_post_from_fb

load_dotenv()
URL = "https://graph.facebook.com/{ID}/feed?access_token={token}&fields=id,message,attachments,created_time".format(ID = os.getenv('PAGE_ID'), token = os.getenv('ACCESS_TOKEN'))
IDS_FILE = 'post_ids.txt'

def write_output(infile, output):
    tempname = infile + ".new"
    try:
        try:
            of = open(tempname, mode='w', encoding='utf-8') 
            of.write(output)
        finally:
            of.close()
    except: 
        print("Warning: Exception occurred: ", infile)


def create_soup(htmlFile, message, date, post_title, post_url):
    soup = BeautifulSoup(htmlFile, "lxml", from_encoding="utf-8")
    try:
        comments = soup.find_all(text=lambda text:isinstance(text, Comment))
        comment_to_replace = comments[0]
        comment_to_replace.replaceWith("""<!--NEW_POST_HERE-->
        <div class="row justify-content-center px-4">
            <div class="col-md-10 col-lg-6 article-container">
                <div class="article-date">
                    {article_date}
                </div>
                <div class="article-title">
                    {article_title}
                </div>
                <div class="article-content">
                    {article_content}
                </div>
                <div class="article-link">
                    <a href="{post_url}" target="_blank">Czytaj dalej <i class="fas fa-arrow-alt-circle-right"></i><i class="fab fa-facebook-square pl-2"></i></a>
                </div>
            </div>
        </div>""".format(article_content=message, article_date=date, article_title=post_title, post_id=id, post_url=post_url))
        return soup
    except IndexError:
        print("\nERROR: File does not contain the comment to be replaced")
        os.sys.exit(2)
def write_id_to_txt(filePath, id):
    with open(filePath, 'r+') as file:
        content = file.read()
        file.seek(0,0)
        file.write(id.rstrip('\r\n') + '\n' + content)


id, message, date, post_url = get_last_post_from_fb(URL)

last_published_id = -1
with open(IDS_FILE, 'r') as file:
    last_published_id = file.readline().strip()
if last_published_id == id:
    print("Nothing to update! The page is already up to date!")
else:
    print('----------------------------------------')
    print('A new post was found!')
    print('----------------------------------------')
    print("Inserting new Post")
    print('----------------------------------------')
    post_title = input("Enter title for the new post:>")
    currentDIR = os.path.dirname(os.path.realpath('__file__'))
    htmlFilePath = os.path.join(currentDIR, '../index.html')
    htmlFile = open(htmlFilePath, 'r', encoding='utf-8')
    soup = create_soup(htmlFile, message, date, post_title, post_url)
    output = soup.encode(formatter=None)
    output = output.decode("utf-8")
    #quick hack to replace async="" with async
    #in javascript tag
    output = output.replace('async=""','async')
    write_output(htmlFilePath, output)
    htmlFile.close()
    os.replace(htmlFilePath + ".new", htmlFilePath)
    print('----------------------------------------')
    print("Post inserted successfuly!")
    print('----------------------------------------')
    print("Updating post_ids.txt...")
    write_id_to_txt(IDS_FILE, id)
    print('----------------------------------------')
    print("Showing results in firefox...")
    print('----------------------------------------')
    webbrowser.open_new("file:///{}".format(htmlFilePath))
    print('DONE!')
    print('----------------------------------------')
    input("Press enter to exit:>")
