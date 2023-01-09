def PairsCount(songs):
  C=0
  for i in range(len(songs)): 
       song=songs[i]
       for j in range(i+1, len(songs)):
            if(song + songs[j]) % 60 ==0:
             C+=1
  return(C)

if __name__ == '__main__':
  SongsList= int(input())
  songs=[]
  for i in range(SongsList):
    songs.append(int(input()))
  print(PairsCount(songs))
