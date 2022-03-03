class ClientsManager:

    PlayersList = {}

    def AddPlayer(playerID, socket):
        if ClientsManager.PlayersList.keys().__contains__(playerID[1]):
            ClientsManager.RemovePlayer(playerID)
        ClientsManager.PlayersList[playerID[1]] = {"Socket": socket}

    def RemovePlayer(PlayerID):
        try:
            ClientsManager.PlayersList.pop(PlayerID[1])
        except KeyError:
            print(f"Cannot remove socket with id: {PlayerID} Reason: {PlayerID} is not in the list.")

    def GetAll():
        return ClientsManager.PlayersList

    def GetCount():
        return len(ClientsManager.PlayersList)