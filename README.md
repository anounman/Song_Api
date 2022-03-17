<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://avatars.githubusercontent.com/u/71139852?v=4" alt="Project logo"></a>
</p>

<h3 align="center">Project Title</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/anounboy/Song_Api/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> Few lines describing your project.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [Authors](#authors)

## 🧐 About <a name = "about"></a>

This is a simple music and video downloading api , you can download any song by directly using the name it download it from youtube as a audio file even you can download youtube video also by the youtube video link.
## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them.

  - Python3
  - Pip Module

### Installing

A step by step series of examples that tell you how to get a development env running.

Say what the step will be

```
  pip install -r requierment.txt
```


End with an example of getting some data out of the system or using it for a little demo.

## 🔧 Running the tests <a name = "tests"></a>

```
  python app.py
```


## 🎈 Usage <a name="usage"></a>

### JavaScript
```
    fetch("https://songapiv1.herokuapp.com/" + {END_POINT})
      .then((res) => res.json())
      .then((data) => {
        setUrl(data);
        console.log(url);
      });
```
### Return Value Usges 
/?name={AUDIO_NAME}
```
data['audio'] = audio link
data['hd_audio'] = hd audio link
data['thumbnail'] = audio image link
```

/youtube_video?link={YOUTUBE_LINK}
```
data['author] = author name 
data['link'] = video link (medium quality)
data['thumbnail'] = video thumbnail
data['title'] = video title
data['view'] = total video views
```



### End Points
` 
  /?name={SONG_NAME} --> for download music by name
`
<br>
`
/youtube_video?link={YOUTUBE_VIDEO_LINK} -->for download yotube video
`

## ⛏️ Example 
### Audio Endpoint Return Value
`
url : https://songapiv1.herokuapp.com/?name=livitating
`
```
{
"audio": "https://rr1---sn-p5qs7n7z.googlevideo.com/videoplayback?expire=1647517410&ei=gsoyYoXaEI-18wT-gqPIAw&ip=44.197.219.192&id=o-AGwLrDE4P86fDeswzcdrWVzH9nkB9aKQqM2Psy8Xlw2u&itag=249&source=youtube&requiressl=yes&mh=OG&mm=31%2C29&mn=sn-p5qs7n7z%2Csn-p5qlsny6&ms=au%2Crdu&mv=m&mvi=1&pl=16&initcwndbps=648750&vprv=1&mime=audio%2Fwebm&ns=o8aA3Ms_qZqGVr-nfRC3fj0G&gir=yes&clen=1419696&dur=230.141&lmt=1629340846885383&mt=1647495669&fvip=1&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=5511222&n=LqlG_ZpVCCym_4MV4&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIga--QHO1CqNPvP8f3f89nu911Y40kYbgEcNVu0T4C4iICIQCayYosXjsFONwP8plgOIPFPqdwC_bRPfLQ6IydkhE-ww%3D%3D&sig=AOq0QJ8wRQIhALP7QDiBUdx2xTzaml0EmJNmkS1lgxEkA_QcXXPNDsTLAiA78s_bLtTZ1wdoeMOVsm75ZJi_8Ua4QK3ibUTLoA6MHA==",
"hd_audio": "https://rr1---sn-p5qs7n7z.googlevideo.com/videoplayback?expire=1647517410&ei=gsoyYoXaEI-18wT-gqPIAw&ip=44.197.219.192&id=o-AGwLrDE4P86fDeswzcdrWVzH9nkB9aKQqM2Psy8Xlw2u&itag=140&source=youtube&requiressl=yes&mh=OG&mm=31%2C29&mn=sn-p5qs7n7z%2Csn-p5qlsny6&ms=au%2Crdu&mv=m&mvi=1&pl=16&initcwndbps=648750&vprv=1&mime=audio%2Fmp4&ns=o8aA3Ms_qZqGVr-nfRC3fj0G&gir=yes&clen=3725595&dur=230.156&lmt=1629361825953515&mt=1647495669&fvip=1&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=5532434&n=LqlG_ZpVCCym_4MV4&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgKJuYU1YaH_atWcSM345Jx7-z81Oma_3E72JS89TmjFgCIAgly7ric-MYfhxNUyS_DDRF4v3aLuLvA28_QTHAC05Y&sig=AOq0QJ8wRgIhANF_QDHMlHwjAftGIwedVK3TKulLwPRWzxQ73UOyGZSxAiEAgMoBN3JEiWXcAcMRYPl6xYj74dzb83SQNpySIIb_YlM=",
"thumbnail": "https://i.ytimg.com/vi/TUVcZfQe-Kw/hqdefault.jpg?sqp=-oaymwEbCKgBEF5IVfKriqkDDggBFQAAiEIYAXABwAEG&rs=AOn4CLBDkvFx1Ipe9KbECajJy_axygOfSg"
}
```





## 🚀 Deployment <a name = "deployment"></a>

You can deploy it on any webserver wich allow to upload flask , recommendation is heroku
[![HeroKu](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)](https://www.heroku.com)

## ⛏️ Built Using <a name = "built_using"></a>

- [Flask](www.flask.palletsprojects.com/en/2.0.x/) - Backend
## ✍️ Authors <a name = "authors"></a>

- [@anounboy](https://github.com/anounboy) - Idea & Initial work

See also the list of [contributors](https://github.com/kylelobo/The-Documentation-Compendium/contributors) who participated in this project.
