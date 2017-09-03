import exifread
from manager import Manager

manager = Manager()

def dms2dd(degrees, minutes, seconds, direction):
    if seconds and seconds.index('/') != -1:
        sec = seconds.split('/')
        seconds = float(sec[0])/float(sec[1])
    dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60);
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

@manager.command
def loc(path):
    loc = parse_lat_lon(path).location()
    print(loc)

if __name__ == '__main__':
    manager.main()




