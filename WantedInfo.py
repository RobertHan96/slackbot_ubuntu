class WantedInfo:
    name = ''
    location = ''
    position_name = ''
    reward = ''
    url = ''

    def __init__(self, name, location, position_name, reward, url):
        self.name = name
        self.location = location
        self.position_name = position_name
        self.reward = reward
        self.url = url