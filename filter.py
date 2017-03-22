#!usr/bin/python2
# coding=utf-8

import re


if __name__ == "__main__":
    writeFile = open('/home/cikm/dbpedia/1504/mappingbased_object_en.ttl', 'w')
    try:
        sourceFile = open('/home/cikm/dbpedia/1504/mappingbased-properties_en.ttl', 'r')
    except Exception as e:
        print 'open file error', e

    pattern = re.compile('.*".*')
    for line in sourceFile.readlines():
        a = re.match(pattern, str(line))
        if a is None:
            writeFile.write(str(line))

    writeFile.close()
    sourceFile.close()
