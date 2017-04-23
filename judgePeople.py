# coding=utf-8

import re


if __name__ == "__main__":
    writeFile = open('/home/cikm/dbpedia/1604/field/MBO&IT_Scientist_Match.ttl', 'w')

    try:
        sourceFile1 = open('/home/cikm/dbpedia/1604/field/IT_scientist.ttl', 'r')
        sourceFile2 = open('/home/cikm/dbpedia/1604/field/MBO_scientist.ttl', 'r')
    except Exception as e:
        print 'open file error', e

    for line in sourceFile.readlines():
        a = re.match(pattern, str(line))
        if a is None:
            writeFile.write(str(line))

    writeFile.close()
    sourceFile.close()
