"""
    parse exif information from image, get city and time information, just chinese city for now

    解析图片中的经纬度信息，获取城市和时间信息,使用腾讯地图api，仅支持中国地区

    use:
        python lcimg.py loc [image_file_path]
"""
import exifread
import requests
import re
import json
from manager import Manager

manager = Manager()

def dms2dd(degrees, minutes, seconds, direction):
    if seconds and seconds.index('/') != -1:
        sec = seconds.split('/')
        seconds = float(sec[0])/float(sec[1])
    dd = round(float(degrees) + float(minutes)/60 + float(seconds)/(60*60),5)
    if direction == 'S' or direction == 'W':
        dd *= -1
    return dd

class Location(object):

    def __init__(self):
        pass

    def location(self):
        def _loc(dim,dir):
            if hasattr(self,dim) and hasattr(self,dir):
                dimval = str(getattr(self,dim))
                dimval = dimval.strip('[').strip(']').split(',')
                if type(dimval) == list and len(dimval) == 3:
                    return dms2dd(dimval[0],dimval[1],dimval[2],str(getattr(self,dir)))
            return None
        return (_loc('lat','latr'),_loc('lon','lonr'),getattr(self,'datetime'))

def parse_lat_lon(img_path):
    with open(img_path,'rb') as f:
        tags = exifread.process_file(f)
        loc = Location()
        for tag in tags.keys():
            if tag == 'EXIF DateTimeOriginal':
                loc.datetime = tags[tag]
            elif tag == 'GPS GPSLatitude':
                loc.lat = tags[tag]
            elif tag == 'GPS GPSLatitudeRef':
                loc.latr = tags[tag]
            elif tag == 'GPS GPSLongitude':
                loc.lon = tags[tag]
            elif tag == 'GPS GPSLongitudeRef':
                loc.lonr = tags[tag]
        return loc

def _loc_city(lat,lon):
    url = 'http://apis.map.qq.com/jsapi?qt=pos&tp=lonlat&wd={}%2C{}&output=jsonp&pf=jsapi&ref=jsapi&cb=qq.maps._svcb3.city_service_0'.format(lat,lon)
    res = requests.get(url)
    return res.text

@manager.command
def loc(path):
    loc = parse_lat_lon(path).location()
    if None in loc:
        print('Latitude and longitude info is not complete')
        return
    # get city infor from loc
    loc_info = _loc_city(loc[1],loc[0])
    # get path information with regex
    cpl = re.compile('{(.*)}')
    loc_city = re.search(cpl,loc_info).group(0)
    if loc_city is None:
        print('Map api failed...')
        return
    try:
        city_json = json.loads(loc_city)
        path = city_json['detail']['path']
    except :
        print('Map api changed,parse method need to update')
        return
    loc_list = []
    for p in path:
        loc_list.append(p['cname'])
    loc_list = reversed(loc_list)
    print(','.join(loc_list))
    print(loc)

if __name__ == '__main__':
    manager.main()




