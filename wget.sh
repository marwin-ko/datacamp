# find your location of wget (if not return, then need to install)
which wget

# installs
sudo apt-get install wget  # linux
brew install wget  # OSX
# windows download via gnuwin32


# downloading a single file
-b  # go to background immediately after startup
-q  # turn off the wget output
-c  # resume broken download (i.e. continue getting partially-downloaded file)
wget -bqc https://websitename.com/datafilename.txt


# pull multiple urls from text file
wget -i url_list.txt
# where txt files has only 1 url per line


# set bandwidth limit
wget --limit-rate=200k -i url_list.txt

# set pause time (in seconds) between file downloads
wget --wait=2.5 -i url_list.txt
