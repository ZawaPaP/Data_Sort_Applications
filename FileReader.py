from DataExample import data_example
import os
class FileReader():
    def __init__(self, args):
        self.args = args
        self.fp = args.infile

    def read(self):
        if self.args.nums:
            data = self.args.nums
        elif os.path.isfile(self.args.infile.name):
            data = self.fp.read() #ここ失敗した時の回避エラーを入れる
            self.fp.close()
        else:
            data = data_example()  # import dummy data
            print('data is dummy')
        return data

    def close(self):
        self.fp.close()