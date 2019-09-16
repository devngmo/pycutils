import os, sys, yaml

def loadText(fp):
    f = open(fp)
    text = f.read()
    f.close()
    return f

def loadYaml(fp):
    stream = open(fp, 'r')
    o = yaml.safe_load(stream)
    stream.close()
    return o


def writeText(text, fp):
    f = open(fp, 'w')
    f.write(text)
    f.close()    
