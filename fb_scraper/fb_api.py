import requests
import json
import os

def get_last_post_from_fb(URL):
    result = requests.get(URL)
    if int(result.status_code) == 400:
        print("ERROR 400! Token expired!")
        os.sys.exit(1)
    json_data = json.loads(result.text)
    last_post = json_data['data'][0]
    return format_fb_post_data(last_post)

def format_fb_post_data(last_post):
    date = last_post['created_time'].split('T')[0].replace('-','.').split('.')
    date = date[2] + '.' + date[1] + '.' + date[0]
    message = last_post['message'].replace('\n', '<br/>')
    id = last_post['id']
    post_url = last_post['attachments']['data'][0]['url']
    return id, message, date, post_url

if __name__ == '__main__':
    print("Warning: you tried to execute fb_api.py module instead of importing it")