from urllib.request import urlopen
import urllib.request
import re

def main():
    #Make a request to the webpage and make it readable

    #Homepage
    with urlopen('https://clbokea.github.io/exam/index.html') as responseHome:
        htmlHome = responseHome.read()
    encoding = responseHome.headers.get_content_charset('utf-8')
    htmlTextHome = htmlHome.decode(encoding)

    #Assignment 1
    with urlopen('https://clbokea.github.io/exam/assignment_1.html') as responseAss1:
        htmlAss1 = responseAss1.read()
    encoding = responseAss1.headers.get_content_charset('utf-8')
    htmlTextAss1 = htmlAss1.decode(encoding)

    #Assignment 2
    with urlopen('https://clbokea.github.io/exam/assignment_2.html') as responseAss2:
        htmlAss2 = responseAss2.read()
    encoding = responseAss2.headers.get_content_charset('utf-8')
    htmlTextAss2 = htmlAss2.decode(encoding)

    #Assignment 3
    with urlopen('https://clbokea.github.io/exam/assignment_3.html') as responseAss3:
        htmlAss3 = responseAss3.read()
    encoding = responseAss3.headers.get_content_charset('utf-8')
    htmlTextAss3 = htmlAss3.decode(encoding)

    #Assignment 4
    with urlopen('https://clbokea.github.io/exam/assignment_4.html') as responseAss4:
        htmlAss4 = responseAss4.read()
    encoding = responseAss4.headers.get_content_charset('utf-8')
    htmlTextAss4 = htmlAss4.decode(encoding)

    saveToMd(htmlTextHome, htmlTextAss1, htmlTextAss2, htmlTextAss3, htmlTextAss4)

def saveToMd(urlHome, url1, url2, url3, url4):
    path = "C:\\Users\\janni\\Dropbox\\Datamatiker\\4. Semester\\Python\\Eksamen"
    mdFile = "WebScrape.md".format(path)

    #Header
    h1Home = h1TagOnSite(urlHome)
    h1Ass1 = h1TagOnSite(url1)
    h1Ass2 = h1TagOnSite(url2)
    h1Ass3 = h1TagOnSite(url3)
    h1Ass4 = h1TagOnSite(url4)
    #Get links and linktext as a DICTIONARY
    links = aLinkOnSite(urlHome)
    #List items
    listHome = listsOnSite(urlHome)
    listAss3 = listsOnSite(url3)
    #Paragraphs
    pAss1 = pTagsOnSite(url1)
    pAss2 = pTagsOnSite(url2)
    pAss4 = pTagsOnSite(url4)
    #Get image on side
    

    with open(mdFile, 'w') as fileMd:
            fileMd.write('# ' + ' '.join(h1Home) + '\n')
            fileMd.write('## Links\n')
            for key,value in links.items():
                fileMd.write('* ' + '[%s](%s)' % (key, value) + '\n')
            fileMd.write('### ' + str(list(links.keys())[0]) + '\n* ' + '\n* '.join(listHome) + '\n')
            fileMd.write('### ' + str(list(links.keys())[1]) + '\n#### ' + '\n '.join(h1Ass1))
            for line in pAss1[:5]:
                fileMd.write('\n* %s' % (line) + '\n')
            fileMd.write('### ' + str(list(links.keys())[2]) + '\n#### ' + '\n '.join(h1Ass2) + '\n* ' + '\n* '.join(pAss2) + '\n')
            fileMd.write('### ' + str(list(links.keys())[3]) + '\n#### ' + '\n '.join(h1Ass3) + '\n* ' + '\n* '.join(listAss3) + '\n')
            fileMd.write('### ' + str(list(links.keys())[4]) + '\n#### ' + '\n '.join(h1Ass4) + '\n* ' + '\n* '.join(pAss4) + '\n')
    
    

#Get H1 from site
def h1TagOnSite(url):
    regexFormat = '<h1>(.+?)</h1>'
    allH1Tags = re.findall(regexFormat, str(url))

    for h1 in allH1Tags:
        print(h1)

    return allH1Tags

#Get all the a-tags on the site with class="nav-link"
def aLinkOnSite(url):
    regexFormat = '<a class="nav-link".*?>(.+?)</a>'
    allATags = re.findall(regexFormat, str(url))

    regexFormat = 'class="nav-link" href="(.+?.html)"'
    allHrefTags = re.findall(regexFormat, str(url))
    url = 'https://clbokea.github.io/exam/'
    allLinks = [url + x for x in allHrefTags]

    aLinks = dict(zip(allATags, allLinks))
    
    return aLinks

#Get all the list items on the side
def listsOnSite(url):
    regexFormat = '(?s)<li>(.+?)</li>'

    allLists = re.findall(regexFormat, str(url))
    allListsMod = list()

    for liList in allLists:
        regexFormat = re.compile(r'<.*?>')
        newString = regexFormat.sub('', liList)
        allListsMod.append(newString)
    
    return allListsMod

#Get all the p-tags on site
def pTagsOnSite(url):
    regexFormat = '(?s)<p>(.+?)</p>'

    allP = re.findall(regexFormat, str(url))

    return allP

#Get image from site
def imageOnSite(url):
    regexFormat = '(<imag.*?>)'

    allImg = re.findall(regexFormat, url.decode())

    for image in allImg:
        print(image)
    return allImg


if __name__ == '__main__':
    main()
