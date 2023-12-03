class BagCubeGameFormater:
    """
    This class is responsible for format the input file
    into a dict with the id of the game and the list of games

    The input file is a list of games, each game is a list of cubes by color

    Example:
    File lines input: Game 1: 2 blue, 4 green; 7 blue, 1 red, 14 green; 5 blue, 13 green, 1 red; 1 red, 7 blue, 11 green
    Formated input: { "1": [ { "blue": 2, "green": 4 }, { "blue": 7, "red": 1, "green": 14 }, { "blue": 5, "green": 13, "red": 1 }, { "red": 1, "blue": 7, "green": 11 } ] }
    """
    def __init__(self, file_path: str):
        try:
            file = open(file_path, "r")
            self.__input__ = file.readlines()
        except:
            self.__input__ = []

    def get_formated_input(self):
        """
        This method return the formated input as a dict
        """
        self.__formated_input__ = { id: games for id, games in map(self.format_line, self.__input__) }
        return self.__formated_input__


    def format_line(self, line: str):
        """
        This method format a line of the input file into a tuple with the id and the list of games
        """
        raw_id, raw_games = line.split(":")

        id = self.get_id(raw_id)

        games = self.format_games(raw_games)

        return id, games
    
    def get_id(self, dirty_id: str):
        """
        This method return the id of the game as a string without the "Game" word
        For example: "Game 1" -> "1"
        """
        return dirty_id.split(" ")[1]
    
    def format_games(self, raw_games: str):
        """
        This method format the list of games into a list of dicts. Each dict is a game

        For example: "2 blue, 4 green; 7 blue, 1 red, 14 green; 5 blue, 13 green, 1 red; 1 red, 7 blue, 11 green"
        to [ { "blue": 2, "green": 4 }, { "blue": 7, "red": 1, "green": 14 }, { "blue": 5, "green": 13, "red": 1 }, { "red": 1, "blue": 7, "green": 11 } ]
        """
        raw_games_in_line = raw_games.split("; ")
        games = []

        for raw_game in raw_games_in_line:
            # clean first and last character (space and \n)
            pre_cleaned_game = raw_game.strip()

            games.append(self.format_game(pre_cleaned_game))

        return games
    
    def format_game(self, game: str):
        """
        This method format a game into a dict with the number of cubes by color

        For example: "2 blue, 4 green" to { "blue": 2, "green": 4 }
        """
        dict_game = { }
        cubes_by_color= game.split(", ")

        for cube_and_color in cubes_by_color:
            number, color = cube_and_color.split(" ")
            dict_game[color] = int(number)

        return dict_game
    
class BagCubeGameProcesor:
    """
    This class is responsible for process the list of games for get the sum of all valid games.

    A valid game is a game where the number of cubes by color is less or equal than the valid number of cubes by color
    """
    valid_cubes_by_color = {
            "red": 12,
            "green": 13,
            "blue": 14
        }
    
    def __init__(self, games: dict):
        self.__games__ = games

    def set_list_of_valid_games(self):
        """
        This method set the list of valid games and return the sum of all valid games
        """
        self.__valid_games__ = [
            int(id)  for id, games in self.__games__.items() if self.list_of_games_is_valid(games)
            ]
        #return the sum of all valid games
        return sum(self.__valid_games__)

    
    def list_of_games_is_valid(self, games: list):
        for game in games:
            if not self.game_is_valid(game):
                return False
        
        return True
    
    def game_is_valid(self, game: dict):
        """
        This method return if a game is valid or not based on the number of cubes by color
        """
        for color, number in game.items():
            if number > self.valid_cubes_by_color[color]:
                return False
        
        return True

path = "./input.txt"
formater = BagCubeGameFormater(path)
games = formater.get_formated_input()
procesor = BagCubeGameProcesor(games)
print(procesor.set_list_of_valid_games())
