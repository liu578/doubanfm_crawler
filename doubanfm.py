# -*- coding: utf-8 -*-
import requests
url = 'https://douban.fm/j/v2/redheart/basic'
cook = {
    "Cokkie":
    'bid=1; flag="ok"; ac="2"; dbcl2="3"; ck=MLKW'
}
r = requests.post(url, cookies=cook)
r.encoding = 'utf-8'
json_data = r.json()
songs = json_data['songs']
sids_str = ''
for song in songs[::-1]:
    sids_str += song['sid'] + '|'
# print(sids_str[:-1])
# print(len(songs))

# headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}#构造头部
formData = {
    'sids': sids_str[:-1],
    'kbps': '192',
    'ck': 'MLKW',
}

cs = {
    "Cokkie":
    'flag="ok"; bid=1; ac="2"; _ga=GA3; dbcl2="4"; ck=MLKW; _gid=GA5"'
}
r = requests.post(
    "https://douban.fm/j/v2/redheart/songs", cookies=cs, data=formData)
# print(r.status_code,r.encoding,r.apparent_encoding)
r.encoding = 'utf-8'
# print(type(r.json()),type(r.text))
json_data = r.json()  # r.json == json.loads(r.text)
for i, entry in enumerate(json_data[:3]):
    print(i + 1, entry['title'] + '-----' + entry['artist'])
# print(len(json_data))