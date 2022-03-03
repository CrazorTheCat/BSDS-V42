import csv


class Regions:
    def getRegionByID(self, regionID):
        RegionID = 0
        with open('Classes/Files/assets/csv_logic/regions.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count <= 1:
                    line_count += 1
                elif line_count - 2 == regionID:
                    RegionID = row[0]
                    break
                else:
                    line_count += 1

            return RegionID

    def getIDByRegion(self, regionName):
        RegionID = 0
        with open('Classes/Files/assets/csv_logic/regions.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count <= 1:
                    line_count += 1
                elif row[0] == regionName:
                    RegionID = line_count - 2
                    break
                else:
                    line_count += 1

            return RegionID