''' You work at a company that receives daily data files from external partners. These files need to be processed and 
analyzed, but first, they need to be transferred to the company's internal network.

The goal of this project is to automate the process of transferring the files from an external FTP server to the 
company's internal network.

Here are the steps you can take to automate this process:

    Use the ftplib library to connect to the external FTP server and list the files in the directory.

    Use the os library to check for the existence of a local directory where the files will be stored.

    Use a for loop to iterate through the files on the FTP server and download them to the local directory using the ftplib.retrbinary() method.

    Use the shutil library to move the files from the local directory to the internal network.

    Use the schedule library to schedule the script to run daily at a specific time.

    You can also set up a log file to keep track of the files that have been transferred and any errors that may have occurred during the transfer process. '''
import os
import ftplib
import shutil 
import schedule     
import time
import logging

ftp_url = '127.0.0.1'
ftp_ser_dir = 'C:\Python\class\Session5\Proj\/ftp_home'
ftp_usr = "user"
ftp_pwd = "user"
local_dir = 'C:\Python\class\Session5\Proj\local_dir'

logging.basicConfig(filename= local_dir + '\\log.txt', level=logging.DEBUG, filemode="w")
def File_Transfer():
    # read files on the FTP server
    try:
        with ftplib.FTP(ftp_url) as ftp:
            ftp.login(user=ftp_usr, passwd = ftp_pwd)
            # connected to the external FTP server
            for filename, information in ftp.mlsd():
                print('files on FTP server:', filename)                                                     # files on FTP server
                with open(local_dir+ '\\'+ filename, 'wb') as downloaded_file:                              # opened a local file for writing in binary mode
                    ftp.retrbinary('RETR '+filename, downloaded_file.write)                                 # download files on the FTP server to the local directory    
                logging.info(filename+ ": file copied from FTP server to local directory successfully")     # log copy successfully done for each file into the log file 
    except Exception as e:
        print('Errorr of Connection is:', e)
        logging.error("The program encountered an error." + str(e))                                         # log error messages into the log file
        
    # check for the existence of a local directory   
    if os.path.exists(local_dir):
        print('Local path is OK')
    else:
        print('There is not this local folder on your local machine')

    # Move the content of source dir to destination dir using shutil.move()         
    # Source path 
    source = 'C:\Python\class\Session5\Proj\source' 
    # Destination path 
    destination = 'C:\Python\class\Session5\Proj\destination\\' 
    print("File list of destination folder before moving files:") 
    print(os.listdir(destination))  
    # A list of files in the source folder
    source_files = [f for f in os.listdir(source) ]
    print('Source files:', source_files)
    
    for file in source_files:
        shutil.move(source+'\\'+file, destination)              # Move each file of source dir to destination dir

    print("File list of destination folder after moving files: ") 
    print(os.listdir(destination)) 

# Every day at 20:48 the function will be called.
schedule.every().day.at("20:48").do(File_Transfer)

while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except Exception as e:
        # log each error occured while File_Transfer function is running every day at 7am into the log file
        logging.critical('Error occured while schudeling File_Transfer function is: '+ str(e))  
        



