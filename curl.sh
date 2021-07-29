# get manual
man curl

# syntax
# curl [option flags] [URL]

# rename with -o
curl -o newfilename001.txt https://website.com/datafile001.txt

# flags for in case of timeouts during download
# -L redirects the HTTP URL if 300 error code occurs.
# -C Resumes a previous file transfer if it times out before completion.
curl -L -O -C https://website.com/datafile[001-100].txt
