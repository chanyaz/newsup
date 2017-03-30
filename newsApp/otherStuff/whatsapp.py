
import urllib
from xlrd import open_workbook
import urllib2
from bs4 import BeautifulSoup





f = open_workbook('E:/whatsapp/urls.xlsx','r')
for line in f.sheets():
    values = []
    for row in range(line.nrows):
        col_value = []
        url  = (line.cell(row,1).value)
        name = (line.cell(row,0).value)
        print name
        html = urllib2.urlopen(url, None, 10)
        soup = BeautifulSoup(html)
        imgs = soup.find_all("p", {"class":"status"})
        outputFileName = 'E:/whatsapp/' + name +'.txt'
        fout = open(outputFileName, 'w')
        for img in imgs:
            status = img.string
            if status is not None:
                status = img.string + '\n'
                try:
                    a = fout.write(status)
                except:
                    print 'you fucked up'
        print 'done'
        fout.close()