import json
import os

import requests as requests

if __name__ == '__main__':
    # 1. call bing api fetch all picture url
    url = "https://cn.bing.com/hp/api/model"
    res = requests.get(url, headers={
        "accept-language": "zh-CN,zh;q=0.9",
        "referer": "https://cn.bing.com/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    })
    if res.status_code != 200:
        pass
    print(url)
    print(res.text)
    image_info = json.loads(res.text)['MediaContents'][0]
    image_date = image_info['Ssd'].split('_')[0]
    image_content = image_info['ImageContent']
    image_title = image_content['Title']
    image_headline = image_content['Headline']
    image_description = image_content['Description']
    image_copyright = image_content['Copyright']
    image = image_content['Image']
    image_url = image['Url']
    if not str.startswith(image_url, "https://s.cn.bing.net/"):
        image_url = "https://s.cn.bing.net" + image_url
    # 格式组装
    text = f"### {image_title}" + "\r\n"
    text += f"> {image_headline}" + "\r"
    text += f"> " + "\r"
    text += f"> 日期: {image_date}" + "\r"
    text += f"> " + "\r"
    text += f"> 版权: {image_copyright}" + "\r\n"
    text += f"   \r\n"
    text += f" {image_description}" + "\r\n"
    text += f"![{image_title}]({image_url})"
    print(text)
    # 写入文件
    with open("README.md", 'w', encoding="UTF-8") as f:
        f.write(text)
    # 归档留存
    if not os.path.exists("archive"):
        os.makedirs("archive")
    archive_file = f"{image_date}.md"
    with open("archive/" + archive_file, 'w', encoding="UTF-8") as f:
        f.write(text)
