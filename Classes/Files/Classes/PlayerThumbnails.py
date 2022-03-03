import csv


class PlayerThumbnails:
    def getThumbnailsID():
        ThumbnailsID = []
        with open('Classes/Files/assets/csv_logic/player_thumbnails.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if row[8].lower() == 'true':
                        ThumbnailsID.append(line_count - 2)
                    if row[0] != "":
                        line_count += 1
            return ThumbnailsID