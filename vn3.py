import yaml
f = open('config.yml','r')
y = yaml.load(f, Loader=yaml.FullLoader)
print(y)
