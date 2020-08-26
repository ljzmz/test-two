import configparser

config = configparser.Configparser()
config = config.read(self.path,encoding="UTF8")

config.set(pro,val_name,val)
f = open(self.path,"w",enconfig="utf8")
config.write(f)
f.close()
