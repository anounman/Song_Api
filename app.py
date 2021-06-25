from flask import Flask , request , render_template , url_for , jsonify
from youtubesearchpython import Search
import requests
import youtube_dl
from datetime import datetime
import urllib.request
import os
download_link = ""
title = ""
app = Flask(__name__)
 


i = 0
def link(name):
   try:
    global i
    print(i)
    download_link = ""
    url_data = ""
    allSearch = Search(str(name), limit = 2)
    data = allSearch.result()
    link = data["result"][0]["link"]
    while True:
        if "https://www.youtube.com/channel/" in link:
            link =  data["result"][i]["link"]
        else:
            link =  data["result"][i]["link"]
            break
        i += 1
    return (link)
   except Exception as e:
     print("Error"+str(e))
     return josnify(error="Enter the name properly")


@app.route('/update', methods=["POST", "GET"])
def install():
    import os
    os.system("pip3 install flask nyoutube_dl")
    return "Update Successfull"


@app.route('/', methods=["POST", "GET"])
def video_link():
     try:
        global download_link
        global hd_link
        name  = str(request.args.get("name"))
        if "https://youtu." in name:
            url = name
        else:
            url = link(str(name+"song"))
        with youtube_dl.YoutubeDL() as ydl:
            url_data = ydl.extract_info(url, download=False)
        thumbnail = url_data["thumbnails"][0]["url"]
        download_link = url_data["formats"][0]["url"]
        hd_link = url_data["formats"][3]["url"]
        title = url_data["title"]
        responce = requests.get(download_link)
        if not responce and i<=2:
            video_link()
            i += 1
        else:
            pass
        i = 0  
        return jsonify(thumbnail=thumbnail , audio=(str(download_link)),hd_audio=str(hd_link))
     except Exception as e:
        print("ERROR==>"+str(e))
        return jsonify(error="Enter the name properly")

if __name__ == '__main__':
    app.run(debug=True)
