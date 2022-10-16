class city:
    def __init__(self) -> None:
        self.STREETS_WIDTH = 5
        self.CONSTRUCTIONS_SIZE = 20
        self.HOR_STREETS = 4
        self.VER_STREETS = 4
        self.CARS_NUM = 1
        self.USERS_NUM = 1
        self.cars_positions = []
        self.users_positions = []
        self.city_dimensions = [
            2*self.HOR_STREETS*self.STREETS_WIDTH + 2* (self.HOR_STREETS-1)*self.CONSTRUCTIONS_SIZE,
            2*self.VER_STREETS*self.STREETS_WIDTH + 2* (self.VER_STREETS-1)*self.CONSTRUCTIONS_SIZE
        ]
        
    def setup(self):
        #self.HOR_STREETS = input("How many horizontal streets?")
        #self.VER_STREETS = input("How many vertical streets?")
        self.CARS_NUM = input("How many cars at the beginning?")
        for i in range(int(self.CARS_NUM)):
            self.cars_positions.append(list(map(int, input(f"What are the coordinates of the #{i+1} car?").split())))
        self.USERS_NUM = input("How many users at the beginning?")
        for i in range(int(self.USERS_NUM)):
            self.users_positions.append(list(map(int, input(f"What are the coordinates of the #{i+1} user?").split())))
        self.city_dimensions = [
            2*self.HOR_STREETS*self.STREETS_WIDTH + 2* (self.HOR_STREETS-1)*self.CONSTRUCTIONS_SIZE,
            2*self.VER_STREETS*self.STREETS_WIDTH + 2* (self.VER_STREETS-1)*self.CONSTRUCTIONS_SIZE
        ]
        
                    