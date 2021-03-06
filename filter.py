#!usr/bin/python2
# coding=utf-8

import re


if __name__ == "__main__":
    writeFile = open('/home/cikm/dbpedia/1604/instance_types_dbtax_dbo_en_artist.ttl', 'w')
    try:
        sourceFile = open('/home/cikm/dbpedia/1604/instance_types_dbtax_dbo_en.ttl', 'r')
    except Exception as e:
        print 'open file error', e

    pattern = re.compile('.*http://dbpedia.org/ontology/Artist.*')
    for line in sourceFile.readlines():
        a = re.match(pattern, str(line))
        if a is None:
            writeFile.write(str(line))

    writeFile.close()
    sourceFile.close()
