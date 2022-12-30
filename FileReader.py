class FileReader():
    def __init__(self, args):
        self.args = args
        self.fp = args.input_file_path

    def read(self):
        data = self.fp.read() #ここ失敗した時の回避エラーを入れる
        self.fp.close()
        return data
