# import required modules
import os
import time
import datetime
import pipes
import gzip


#database info and backup file
BACKUP_DIR_NAME ='/mongo_backups'
DBHOST = '127.0.0.1'
PORT = '27017'
DBUSER = 'root'
DBUSERPASSWORD = '123456'
DBNAME = 'admin'

# Getting current DateTime
DATETIME = time.strftime('%Y%m%d-%H%M')
TODAYBACKUPPATH = BACKUP_DIR_NAME + "/" +DATETIME

# check if the backup folder exist or not
try:
    os.stat(TODAYBACKUPPATH)
except:
    os.mkdir(TODAYBACKUPPATH)

#starting backups
db = DBNAME
dumpcmd = "mongodump --host=" + DBHOST + " --port=" + PORT + " --username="+ DBUSER + " --password=" + DBUSERPASSWORD +  " --db=" + db + " --out=" + pipes.quote(TODAYBACKUPPATH) + "/" + db + ".bson"
os.system(dumpcmd)
#gzipcmd = "gzip " + pipes.quote(TODAYBACKUPPATH) + "/" + db + ".json"
#os.system(gzipcmd)

print("Backup completed and have been created in" + TODAYBACKUPPATH + "directory")
