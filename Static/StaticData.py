import json

class StaticData:
    ShopData = None

    def Preload():
        StaticData.ShopData = json.loads(open("Static/Shop.json", 'r').read())