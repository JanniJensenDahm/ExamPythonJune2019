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

def saveToMd(urlHome, url1, url2, url3, url5):
    path = "C:\\Users\\janni\\Dropbox\\Datamatiker\\4. Semester\\Python\\Eksamen"
    mdFile = "README.md".format(path)

    #Save header
    h1Home = h1TagOnSite(urlHome)
    #Save assignments
    aTag = aTagOnSite(urlHome)

    with open(mdFile, 'w') as fileMd:
            fileMd.write('#' + ' '.join(h1Home) + '\n* ')
            fileMd.write('\n* '.join(aTag))
    
    

#Get H1 from site
def h1TagOnSite(url):
    regexFormat = '<h1>(.+?)</h1>'
    allH1Tags = re.findall(regexFormat, str(url))

    for h1Tag in allH1Tags: 
        print(h1Tag)

    return allH1Tags

#Get all a-tags on the site with class="nav-link"
def aTagOnSite(url):
    regexFormat = '<a class="nav-link".*?>(.+?)</a>'
    allATags = re.findall(regexFormat, str(url))

    for aTag in allATags:
        print(aTag)
    
    return(allATags)

    

#Get all list items on the side
def listsOnSite(url):
    regexFormat = '<li>(.+?)</li>'

    allLists = re.findall(regexFormat, str(url))

    print("What to fullfill before the exam")
    for liList in allLists:
        escapeReplaced = re.sub("\\\\.|[^a-zA-Z' ]+", '', liList)
        print(liList)

if __name__ == '__main__':
    main()