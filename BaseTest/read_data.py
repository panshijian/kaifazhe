import yaml, os

class Op_Data:

    def __init__(self, file_name):
        self.file_path = os.getcwd() + os.sep + "Data" + os.sep + file_name

    def read_yaml(self):
        # 读yaml
        with open(self.file_path, "r",encoding= "utf-8") as f:
            return yaml.load(f)

    def wrire_yaml(self,data):
        # 写文件
        with open(self.file_path, "w") as f:
            return yaml.dump(data,f,encoding = "utf-8",allow_unicode=True)
