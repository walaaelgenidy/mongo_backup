# import required modules
import os
import time
import datetime
import pipes
import gzip


#database info and backup file
BACKUP_DIR_NAME ='/mongo_backups'
DBHOST = '3.19.232.40'
PORT = '8080'
DBUSER = 'mongoAdmin'
DBUSERPASSWORD = 'changeMe'
DBNAME = 'admin'

# Getting current DateTime
DATETIME = time.strftime('%Y%m%d-%H%M%S')
TODAYBACKUPPATH = BACKUP_DIR_NAME + '/'+ DATETIME

# check if the backup folder exist or not
try:
    os.stat(TODAYBACKUPPATH)
except:
    os.mkdir(TODAYBACKUPPATH)

#starting backups
db = DBNAME
dumpcmd = "mongoexport --host=" + DBHOST + "--port=" + PORT + "--username=" + DBUSER + "--password=" + DBUSERPASSWORD + "--pretty" +  "--db=" + db + "--out=" + pipes.quote(TODAYBACKUPPATH) + "/" + db + ".json"
os.system(dumpcmd)
gzipcmd = "gzip" + pipes.quote(TODAYBACKUPPATH) + "/" + db + ".json"
os.system(gzipcmd)

print("Backup completed and have been created in" + TODAYBACKUPPATH + "directory")
