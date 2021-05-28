from multiprocessing import Process
import combine as c
import requests
import urllib.request as urllib2
from bs4 import BeautifulSoup
import os
#from selenium import webdriver
song = input("enter song name to download in High defination ")
videoName = song.replace(" ","+")
audioName = videoName+'1'
#videoName = videoName 
original = song.replace(" ","_") + "(original)"
#song = song.replace(" ","+")
archive_url = "https://www.genyt.net/search.php?q="+song
links = []
def VideoDownload(downloadLink):
    resp = urllib2.urlopen(downloadLink)
    respHtml = resp.read()
    binfile = open(videoName+'.mp4', "wb")
    binfile.write(respHtml)
    binfile.close()
    print("Download completed..!!")
#r = requests.get(downloadLink,stream = True)
    #with open(videoName + '.mp4','wb') as f:
        #for chunk in r.iter_content(chunk_size=512):
            #if chunk:
        #f.write(r.content)
    #download += 1
    #print("downloaded")

def AudioDownload(downloadLink):
    resp = urllib2.urlopen(downloadLink)
    respHtml = resp.read()
    binfile = open(audioName+'.mp3', "wb")
    binfile.write(respHtml)
    binfile.close()
    print("Download completed..!!")

    
def findingSong(archive_url):
    global links #, image_list
    # create response object 
    response = requests.get(archive_url)
    soup = BeautifulSoup(response.content,'html.parser')
    containers = soup.findAll("a",{"class":"moviea"})
    #pant = containers.findAll("href")
    #links = soup.findAll('a')

    info = containers[0].getText()
    for container in containers:
        #print(info)#tells the file name and quality
        #image_list.append(container.find("img").attrs['src'])
        #song_link.append(container.attrs['href'])
        #print(container)
        #print("#################################################################")
        links.append(container.attrs['href'])
    #print(links)
    #print(info)

def DownloadMusic():
    global links,song,downloadLinkV,downloadLinkA
    down = []
    link = []
    #response = requests.get(song_link)
    #driver.get(song_link[0])
    #try:
        #WebDriverWait(driver, 10).until(EC.presence_of_element_located
                                        #((By.CLASS_NAME, "")))
    #except TimeoutException:
        #print('Page timed out after 10 secs.')
    response = requests.get(links[0])
    soup = BeautifulSoup(response.content,'html.parser')
    #driver.close()
    download_buttons = soup.findAll("div", {"class":"col-md-3 col-sm-4 col-xs-6 text-center downbuttonbox"})
    #with open("never give up 2.txt",'wb') as f:
        #f.write(soup.encode('UTF-8'))
    #link = download_buttons.findAll('a')
    #for lin in link:
        #down.append(link.attrs['href'])
    for downloadButton in download_buttons:
        quality = downloadButton.find("span",{"class":"infow"})
        #print(quality.getText())
        if ("480p" in quality.getText()):
            downloadit = downloadButton
        elif "160abr" in quality.getText():
            downloadMp3 = downloadButton
        else:
            continue
    downloadGet = downloadit.find("a",{"rel":"nofollow"})
    downloadGat = downloadMp3.find("a",{"rel":"nofollow"})
    downloadLinkV = downloadGet.attrs['href']
    downloadLinkA = downloadGat.attrs['href']
    print(downloadLinkV)
    print(downloadLinkA)
        
findingSong(archive_url)
DownloadMusic()
Process(target=VideoDownload(downloadLinkV)).start()
Process(target=AudioDownload(downloadLinkA)).start()
c.Mux(videoName+'.mp4',audioName+'.mp3',original)
if os.path.exists(original+'.mkv'):
    os.remove(videoName+'.mp4')
    os.remove(audioName+'.mp3')

