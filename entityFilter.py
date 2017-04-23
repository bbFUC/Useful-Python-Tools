# coding=utf-8


if __name__ == '__main__':
    writeFile = open('/home/cikm/1604/field/MBO&IT_Scientist_Match.ttl', 'w')

    with open("/home/cikm/1604/field/IT_scientist.ttl") as fa:
        for a in fa:
            with open("/home/cikm/1604/field/MBO_Scientist.ttl") as fb:
                for b in fb:
                    print a, b
                    if a == b:
                        writeFile.writelines(str(a))

    writeFile.close()
