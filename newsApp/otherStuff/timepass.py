import isodate
from dateutil import parser
#dur=isodate.parse_duration('PT6M9S')
#print str(dur)

#print (parser.parse('2015-10-01T08:14:02.000Z'))

'''try:
    dur = 'PT6M9S'
    try:
        minutes = int(dur[2:4]) * 60
        print minutes
    except:
        minutes = 0
    try:
        hours = int(dur[:2]) * 60 * 60
        print hours
    except:
        hours = 0

    secs = int(dur[4:6])
    print secs
    print hours, minutes, secs
    duration = hours + minutes + secs
    print duration
except Exception as e:
    print "Couldnt extract time: %s" % e
    pass'''
VIDEO_CATEGORY_FILE = 'E:/NewsApp/video_category.txt'

def isVideoAvailable(lang,category):
    f=open(VIDEO_CATEGORY_FILE,'r')
    found = False
    for line in f:
        if found == False:
            fileLang = line.split(' ')[0]
            fileCategory = ' '.join(line.split(' ')[1:]).rsplit('\n')[0]
            if fileLang.lower() == lang.lower():
                if fileCategory.lower() == category.lower():
                    found = True
    return found
isVideo = isVideoAvailable('English','Sports')
print isVideo