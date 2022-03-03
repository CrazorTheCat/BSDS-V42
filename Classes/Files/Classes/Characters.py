import csv


class Characters:

    def getBrawlersID():
        BrawlersID = []
        with open('Classes/Files/assets/csv_logic/characters.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if row[24] == 'Hero' and row[2].lower() != 'true' and row[0] != "MechaDudeBig":
                        BrawlersID.append(line_count - 2)
                    line_count += 1

            return BrawlersID