import csv


class Cards:
    def getStarpowersID():
        CardSkillsID = []
        with open('Classes/Files/assets/csv_logic/cards.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if row[7] == '4' and row[4].lower() != "true":
                        # print(line_count - 2, row[7], row[3], row[4], row[5])
                        CardSkillsID.append(line_count - 2)
                    line_count += 1

            return CardSkillsID

    def getBrawlerStarpowers(brawlerID):
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

                    cards_file = open('Classes/Files/assets/csv_logic/cards.csv')
                    csv_reader = csv.reader(cards_file, delimiter=',')
                    line_count = 0
                    for row in csv_reader:
                        if line_count == 0 or line_count == 1:
                            line_count += 1
                        else:
                            print(row)
                            if row[7].lower() == '4' and row[3] == name and row[4] != "true":
                                # print(row[0], line_count - 3)
                                id.append(line_count - 2)
                            line_count += 1

                    char_file.close()
                    cards_file.close()
                    return id

    def getBrawlerUnlockID(brawlerID):
        char_file = open('Classes/Files/assets/csv_logic/characters.csv')
        csv_reader = csv.reader(char_file, delimiter=',')
        line_count = 0
        id = 0

        for row in csv_reader:
            if line_count == 0 or line_count == 1:
                line_count += 1
            else:
                line_count += 1
                if line_count == brawlerID + 3:
                    name = row[0]
                    line_count += 1

                    cards_file = open('Classes/Files/assets/csv_logic/cards.csv')
                    csv_reader = csv.reader(cards_file, delimiter=',')
                    line_count = 0
                    for row in csv_reader:
                        if line_count == 0 or line_count == 1:
                            line_count += 1
                        else:
                            if row[7].lower() == '0' and row[3] == name and row[4].lower() != "true":
                                # print(row[0], line_count - 3)
                                id = line_count - 2
                            line_count += 1

                    char_file.close()
                    cards_file.close()
                    return id


    def getBrawlersUnlockID():
        CardUnlockID = []
        with open('Classes/Files/assets/csv_logic/cards.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if row[7] == '0' and row[4].lower() != "true":
                        # print(line_count - 2, row[7], row[3], row[4], row[5])
                        CardUnlockID.append(line_count - 2)
                    line_count += 1

            return CardUnlockID
