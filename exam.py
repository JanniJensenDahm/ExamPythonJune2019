from urllib.request import urlopen
import urllib.request
import re

#Global variable
mdFile = ''
htmlTextHome = ''
urlList = list()

def main():
    #Make a request to the webpage and make it readable
    #Homepage
    global htmlTextHome
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

    #Start web crawling
    saveToMd(htmlTextHome, htmlTextAss1, htmlTextAss2, htmlTextAss3, htmlTextAss4)

def saveToMd(urlHome, url1, url2, url3, url4):
    global mdFile
    global urlList
    path = "C:/Users/janni/Dropbox/Datamatiker/4. Semester/Python/Eksamen/"
    mdFile = "WebScrape.md".format(path)
    urlList = [url1, url2, url3, url4]

    #Headers
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
    #paragraphs
    pAss1 = pTagsOnSite(url1)
    pAss2 = pTagsOnSite(url2)
    pAss4 = pTagsOnSite(url4)
    #Images
    imgList = imageOnSite(urlList)

    #Save to .md file
    with open(mdFile, 'w') as fileMd:
        #Over all save to .md file
        fileMd.write('# ' + ' '.join(h1Home) + '\n')
        fileMd.write('## Links\n')
        for key,value in links.items():
            fileMd.write('* ' + '[%s](%s)' % (key, value) + '\n')
        fileMd.write('### ' + str(list(links.keys())[0]) + '\n* ' + '\n* '.join(listHome) + '\n')

        #Assignment 1, save to .md file
        fileMd.write('### ' + str(list(links.keys())[1]) + '\n#### ' + '\n '.join(h1Ass1) + '\n')
        fileMd.write('![](' + str(imgList[0]) + ')\n')
        for line in pAss1[:5]:
            fileMd.write('\n* %s' % (line) + '\n')

        #Assignment 2, save to .md file
        fileMd.write('### ' + str(list(links.keys())[2]) + '\n#### ' + ''.join(h1Ass2) + '\n')
        fileMd.write('![](' + str(imgList[1]) + ')\n')
        fileMd.write('* ' + '\n* '.join(pAss2) + '\n')

        #Assignment 3, save to .md file
        fileMd.write('### ' + str(list(links.keys())[3]) + '\n#### ' + '\n '.join(h1Ass3) + '\n')
        fileMd.write('![](' + str(imgList[2]) + ')\n')
        fileMd.write('* ' + '\n* '.join(listAss3) + '\n')

        #Assignment 4, save to .md file
        fileMd.write('### ' + str(list(links.keys())[4]) + '\n#### ' + '\n '.join(h1Ass4) + '\n')
        fileMd.write('![](' + str(imgList[3]) + ')\n')
        fileMd.write('* ' + '\n* '.join(pAss4) + '\n')
    
    

#Get H1
def h1TagOnSite(url):
    regexFormat = '<h1>(.+?)</h1>'
    allH1Tags = re.findall(regexFormat, str(url))

    return allH1Tags

#Get all the a-tags with class="nav-link"
def aLinkOnSite(url):
    regexFormat = '<a class="nav-link".*?>(.+?)</a>'
    allATags = re.findall(regexFormat, str(url))

    regexFormat = 'class="nav-link" href="(.+?.html)"'
    allHrefTags = re.findall(regexFormat, str(url))
    url = 'https://clbokea.github.io/exam/'
    allLinks = [url + x for x in allHrefTags]

    aLinks = dict(zip(allATags, allLinks))
    
    return aLinks

#Get all the list items
def listsOnSite(url):
    regexFormat = '(?s)<li>(.+?)</li>'

    allLists = re.findall(regexFormat, str(url))
    allListsMod = list()

    for liList in allLists:
        regexFormat = re.compile(r'<.*?>')
        newString = regexFormat.sub('', liList)
        allListsMod.append(newString)
    
    return allListsMod

#Get all the p-tags
def pTagsOnSite(url):
    regexFormat = '(?s)<p>(.+?)</p>'

    allP = re.findall(regexFormat, str(url))

    return allP

#Get img from webpage
def imageOnSite(urlList):
    regexFormat = 'img src="(.*?)"'
    baseUrl = 'https://clbokea.github.io/exam/'
    imgList = list()
    for url in urlList:
        allImg = re.findall(regexFormat, str(url))
        imgUrl = baseUrl + allImg[1]
        imgList.append(imgUrl)
    return imgList

if __name__ == '__main__':
    main()
