from  flask import Flask , request , render_template , url_for , jsonify
from youtubesearchpython import Search
import requests
import youtube_dl
from datetime import datetime
import os
import pafy
from flask_cors import CORS
download_link = ""
title = ""
app = Flask(__name__)
CORS(app)



def link(name):
   try:
    download_link = ""
    url_data = ""
    allSearch = Search(str(name), limit = 3)
    data = allSearch.result()
    link = data["result"][0]["link"]
    while True:
        if "https://www.youtube.com/channel/" in link:
            link =  data["result"][1]["link"]
            alt_link = data["result"][2]["link"]
        else:
            link =  data["result"][1]["link"]
            alt_link = data["result"][2]["link"]
            break
    return (link , alt_link)
   except Exception as e:
     print("Error"+str(e))
     return josnify(error="Enter the name properly")
def fetch_data(link):
    try:    
        if "/watch?v=" in link:
            data = link.split("?v=")
            data = data[-1]
            print(data)
        else:
            data = link.split("/")
            data = data[-1]
        video = pafy.new(str(data))
        title = video.title
        thumbnail = video.thumb
        view = video.viewcount
        author  =  video.author
        streams = video.getbest()
        return (title , thumbnail , view , author , streams)
    except Exception as e:
        print("Error=>"+str(e))
@app.route("/youtube_video" , methods=['GET', 'POST'])
def index():
        try:
            url = request.args.get("link")
            
            title , thumbnail , view, author , streams = fetch_data(url)
           
            return jsonify(title = title , thumbnail=thumbnail , view=view, author=author ,link=streams.url)
        except Exception as e:
            print("Error(index)==>"+str(e))

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
            url , alt_url = link(str(name+"song"))
        with youtube_dl.YoutubeDL() as ydl:
            url_data = ydl.extract_info(url, download=False)
        thumbnail = url_data["thumbnails"][0]["url"]
        download_link = url_data["formats"][0]["url"]
        hd_link = url_data["formats"][3]["url"]
        title = url_data["title"]
        # responce = requests.get(download_link)
        # if not responce:
        #     with youtube_dl.YoutubeDL() as ydl:
        #         url_data = ydl.extract_info(alt_url, download=False)
        #         thumbnail = url_data["thumbnails"][0]["url"]
        #         download_link = url_data["formats"][0]["url"]
        #         hd_link = url_data["formats"][3]["url"]
        #         title = url_data["title"]
        # else:
        #     pass
    
        return jsonify(thumbnail=thumbnail , audio=(str(download_link)),hd_audio=str(hd_link))
     except Exception as e:
        print("ERROR==>"+str(e))
        return jsonify(error="Enter the name properly")

if __name__ == '__main__':
    app.run(debug=True)
