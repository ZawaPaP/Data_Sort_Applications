class FileReader():
    def __init__(self, args):
        self.args = args
        self.fp = args.infile

    def read(self):
        data = self.fp.read() #ここ失敗した時の回避エラーを入れる
        self.close()
        return data

    def close(self):
        self.fp.close()