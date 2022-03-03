import csv


class Skins:
    def getSkinsID():
        SkinsID = []
        with open('Classes/Files/assets/csv_logic/skins.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:

                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if row[2].lower() != "true":
                        (line_count - 2)
                        SkinsID.append(line_count - 2)
                    if row[0] != "":
                        line_count += 1

            return SkinsID

    def getBrawlerBySkin(self, skinID):
        with open('Classes/Files/assets/csv_logic/skins.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:

                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if line_count - 2 == skinID:
                        confName = row[1]
                        with open('Classes/Files/assets/csv_logic/skin_confs.csv') as csv_file:
                            csv_reader = csv.reader(csv_file, delimiter=',')
                            line_count2 = 0
                            for row2 in csv_reader:

                                if line_count2 == 0 or line_count2 == 1:
                                    line_count2 += 1
                                else:
                                    if row2[0] == confName:
                                        brawlerName = row2[1]
                                        with open('Classes/Files/assets/csv_logic/characters.csv') as csv_file:
                                            csv_reader = csv.reader(csv_file, delimiter=',')
                                            line_count3 = 0
                                            for row3 in csv_reader:
                                                if line_count3 == 0 or line_count3 == 1:
                                                    line_count3 += 1
                                                else:
                                                    if row3[0] == brawlerName:
                                                        return line_count3 - 2
                                                    if row3[0] != "":
                                                        line_count3 += 1
                                    if row2[0] != "":
                                        line_count2 += 1
                    if row[0] != "":
                        line_count += 1

    def getSkinInfoByID(id):
        with open('Classes/Files/assets/csv_logic/skins.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:

                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if line_count - 2 == id:
                        formatedRow = []
                        formatedRow.append(line_count - 2)
                        for i in row:
                            if i != '':
                                formatedRow.append(i)
                        print(formatedRow)
                        break
                    if row[0] != "":
                        line_count += 1

    def getSkinInfoByName(name):
        with open('Classes/Files/assets/csv_logic/skins.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:

                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if row[0] == name:
                        formatedRow = []
                        formatedRow.append(line_count - 2)
                        for i in row:
                            if i != '':
                                formatedRow.append(i)
                        print(formatedRow)
                        break
                    if row[0] != "":
                        line_count += 1

    def getSkinsInfo():
        with open('Classes/Files/assets/csv_logic/skins.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:

                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    formatedRow = []
                    formatedRow.append(line_count - 2)
                    for i in row:
                        if i != '':
                            formatedRow.append(i)
                    print(formatedRow)
                    if row[0] != "":
                        line_count += 1

    def getSkinsForBrawler(name):
        name = name + '_'
        with open('Classes/Files/assets/csv_logic/skins.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:

                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if row[2].lower() != "true" and row[21].startswith(name.lower()):
                        formatedRow = []
                        formatedRow.append(line_count - 2)
                        for i in row:
                            if i != '':
                                formatedRow.append(i)
                        print(formatedRow)
                    if row[0] != "":
                        line_count += 1

    def getBrawlerSkins(brawlerID):
        char_file = open('Classes/Files/assets/csv_logic/characters.csv')
        csv_reader = csv.reader(char_file, delimiter=',')
        line_count = 0
        id = []

        for row in csv_reader:
            if line_count == 0 or line_count == 1:
                line_count += 1
            else:
                line_count += 1
                if line_count == brawlerID + 3:
                    name = row[0]
                    line_count += 1

                    cards_file = open('Classes/Files/assets/csv_logic/skin_confs.csv')
                    csv_reader = csv.reader(cards_file, delimiter=',')
                    line_count = 0
                    for row in csv_reader:
                        if line_count == 0 or line_count == 1:
                            line_count += 1
                        else:
                            if row[1] == name:
                                conf_name = row[0]
                                skins_file = open('Classes/Files/assets/csv_logic/skins.csv')
                                csv_reader = csv.reader(skins_file, delimiter=',')
                                line_count = 0
                                for row in csv_reader:

                                    if line_count == 0 or line_count == 1:
                                        line_count += 1
                                    else:
                                        if row[1] == conf_name:
                                            id.append(line_count - 2)
                                        if row[0] != "":
                                            line_count += 1

                    char_file.close()
                    cards_file.close()
                    skins_file.close()
                    return id
