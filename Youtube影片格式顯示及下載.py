from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=QsmePfJhwvM")

print("\n============================================")
print("*** thumbnail:",yt.thumbnail_url)

print("\n============================================")
print("*** 所有影片格式:")
streams = yt.streams
print(streams)

print("\n============================================")
print('*** First stream:',streams[0])
strvideo = str(streams[0])

start1 = strvideo.find('video/')
end1 = strvideo.find('" res')
strftype = strvideo[start1+6 : end1]
print("***** type", strftype)

start2 = strvideo.find('res="')
end2 = strvideo.find('p"')
strresolution = strvideo[start2+5 : end2+1]
print("***** resolution: ", strresolution)

print("\n============================================")
stream = streams.filter(file_extension='mp4', res='480p').first()
print('*** First mp4 480p stream: ', stream)

print("\n============================================")
stream.download('C:/:Users/qwuoo', "pytube mp4 480p.mp4")
print("*** 影片名稱:"+yt.title+"，存在C:/:Users/qwuoo資料夾，檔案名稱為資料夾，檔案名稱為 pytube mp4 480p.mp4")
input("BYE")

