class Game:

    list_of_games = []

    def __init__(self, name, status, platform):
        self.name = name
        self.status = status
        self.platform = platform
        Game.list_of_games.append(self)

    def delete(self):
        if self in Game.list_of_games:
            Game.list_of_games.remove(self)

game1 = Game("minecraft", "active", "pc")
game2 = Game("cs2", "active", "pc")

def show_all_games():
    i = 0
    for game in Game.list_of_games:
        i += 1
        print(f'{i}. {game.name} {game.status} {game.platform}')

def create_record(name, status, platform):
    created_game = Game(name, status, platform)
    print(f'создана запись о игре: {name}: {status} {platform}')

def delete_record_by_name(name):
    for game in Game.list_of_games:
        if game.name == name:
            game.delete()
            del game
            print(f'игра {name} была удалена')
            return
    print("игра не найдена")

show_all_games()
create_record("stardew valley", "active", "pc")
show_all_games()
delete_record_by_name("cs2")
show_all_games()

delete_record_by_name("cs3")