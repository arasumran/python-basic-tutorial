import ftplib
import glob
import os
import random
import string
import zipfile
from datetime import datetime

import pandas as pd


class FtpStorage(object):
    def __init__(self, host=None, port=None, username=None, password=None):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def connect_ftp(self):
        server = ftplib.FTP()
        server.connect(self.host, self.port)
        server.login(self.username, self.password)

    def download_file(self, file_name):
        self.connect_ftp().retrbinary("RETR" + file_name, open(file_name, 'wb').write)
        self.connect_ftp().quit()
    def send_file_to_ftp(self,file_name):
        session= ftplib.FTP(user=self.username,passwd=self.password,host=self.host)
        file = open(file_name,'rb')
        session.storbinary('STOR ' +file_name,file)
        file.close()
        session.quit()




class MergeFiles(object):
    def __init__(self, files_list, col_count):
        self.files_list = files_list
        self.col_count = col_count
        self.format_type = '.csv'

    def extract_files_by_format(self, format_type):
        """
        :param self:
        :param format_type: default = .csv
        :param kwargs:
        :return:

        """
        try:
            for i in range(self.col_count):
                with open(self.files_list[i], 'r'):
                    col_file_name_list = zipfile.ZipFile(self.files_list[i], 'r')
                    matches = [x for x in col_file_name_list if os.path.splitext(x)[1] == format_type]
                    if matches.__len__() > 0:
                        col_file_name_list.extract(matches[0])
                        col_file_name_list.close()
        except IOError as io:
            print(io)

    def merge_files(self):
        path = os.getcwd()
        allFiles = glob.glob(path + "/*.csv")
        list_ = []
        for file_ in allFiles:
            df = pd.read_csv(file_, index_col=None, header=0)
            list_.append(df)
        frame = pd.concat(list_, axis=0, ignore_index=True)
        frame.to_csv("find_result", sep='\t')
    def archive_as_zip(self,list_of_file):
        with zipfile.ZipFile(str(self.name_generator()) + '.zip', 'w') as z:
            for f in list_of_file:
                z.write(f)
    def name_generator(self, size=5, chars=string.ascii_lowercase + string.digits):
        random_ = ''.join(random.choice(chars) for _ in range(size))
        return random_ + "-" + datetime.timestamp()
    def delete_unused_files(self):
        os.chdir(os.getcwd())
        for csv_f in glob.glob("*.csv"):
            os.remove(csv_f)
        for zip_f in glob.glob("*.zip"):
            os.remove(zip_f)



