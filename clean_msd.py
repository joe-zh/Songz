#code taken from https://labrosa.ee.columbia.edu/millionsong/sites/default/files/tutorial1.py.txt 
#updated 04/30 for less overlap
# usual imports
import os
import sys
import time
import glob
import datetime
import numpy as np # get it at: http://numpy.scipy.org/
# path to the Million Song Dataset subset (uncompressed)
# CHANGE IT TO YOUR LOCAL CONFIGURATION
msd_subset_path='/home/michael/Downloads/MillionSongSubset'
msd_subset_data_path=os.path.join(msd_subset_path,'data')
msd_subset_addf_path=os.path.join(msd_subset_path,'AdditionalFiles')
# path to the Million Song Dataset code
# CHANGE IT TO YOUR LOCAL CONFIGURATION
msd_code_path='/home/michael/penn/senior year/cis450/cis450Project/MSongsDB-master'
# we add some paths to python so we can import MSD code
# Ubuntu: you can change the environment variable PYTHONPATH
# in your .bashrc file so you do not have to type these lines
sys.path.append( os.path.join(msd_code_path,'PythonSrc') )

# imports specific to the MSD. download from https://github.com/tbertinmahieux/MSongsDB/blob/master/PythonSrc/hdf5_getters.py which it is given out for free with the ability to use / redistribute for free. it is used to read hdf5 files, and MSD has you download it to use their database.
import hdf5_getters as GETTERS


# we define the function to apply to all files
def func_to_get_data(filename):
    #had to change the line 41 in hdf_getters to use open_file( instead of openFile(
    h5 = GETTERS.open_h5_file_read(filename)
    data = {}
    data2 = {}
    data3 = {}
    data['artist_familiarity'] = GETTERS.get_artist_familiarity(h5)
    data['artist_hotness'] = GETTERS.get_artist_hotttnesss(h5)
    data['artist_id'] = GETTERS.get_artist_id(h5)
    data['artist_mbid'] = GETTERS.get_artist_mbid(h5)
    data['artist_name'] = GETTERS.get_artist_name(h5)
    data['release'] = GETTERS.get_release(h5)
    data['song_id'] = GETTERS.get_song_id(h5)
    data['song_hotness'] = GETTERS.get_song_hotttnesss(h5)
    data['song_title'] = GETTERS.get_title(h5)
    data2['similar_artists'] = GETTERS.get_similar_artists(h5)
    data['danceability'] = GETTERS.get_danceability(h5)
    data['duration'] = GETTERS.get_duration(h5)
    data['energy'] = GETTERS.get_energy(h5)
    data['track_id'] = GETTERS.get_track_id(h5)
    data3['mbtags'] = GETTERS.get_artist_mbtags(h5)
    data['year'] = GETTERS.get_year(h5)

    L = ['artist_familiarity', 'artist_hotness','artist_id','artist_mbid','artist_name','release','song_id','song_hotness','song_title','danceability','duration','energy','track_id','year']

    with open('msd_clean.csv', 'a') as f:
      for i in range(0, len(L)):
        s = str(data[L[i]])
        clean = s.lower()
        clean = clean.strip()
        if i == len(L)-1:
          clean = clean + '\n'
        else:
          clean = clean + '\t'
        f.write(clean)

    a_id = str(data['artist_id']).lower().strip()
    with open('similar_artists_clean.csv', 'a') as f:
      for art in data2['similar_artists']:
        clean_art = str(art).lower().strip()
        f.write(a_id + '\t' + clean_art +'\n')
    with open('msd_mbtags_clean.csv','a') as f:
      for tag in data3['mbtags']:
        clean_tag = str(tag).lower().strip()
        f.write(a_id + '\t' + clean_tag +'\n')

    h5.close()

with open('msd_clean.csv','w') as f:
  f.write('"artist_familiarity"\t"artist_hotness"\t"artist_id"\t"artist_mbid"\t"artist_name"\t"release"\t"song_id"\t"song_hotness"\t"song_title"\t"danceability"\t"duration"\t"energy"\t"track_id"\t"year"\n')

with open('similar_artists_clean.csv','w') as f:
  f.write('"artist_id"\t"similar_artists"\n')
with open('msd_mbtags_clean.csv','w') as f:
  f.write('"artist_id"\t"mbtags"\n')
for root, dirs, files in os.walk(msd_subset_data_path):
    files = glob.glob(os.path.join(root,'*.h5'))
    # apply function to all files
    for f in files :
        func_to_get_data(f)


