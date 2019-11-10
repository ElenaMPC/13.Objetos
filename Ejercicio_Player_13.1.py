import json

class Player():
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds


class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists


class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards

def get_players_list():
    import json
    with open("Players.txt", "r") as players_file:
        players_list = json.loads(players_file.read())
        return players_list


players_list = get_players_list()

nombre = input("¿Nombre del jugador?")
apellido = input("¿Apellido del jugador?")
altura = float(input("¿Altura del jugador (en cm)?"))
peso = float(input("¿Peso del jugador (en kg)?"))
goles = int(input("¿Número de goles?"))
tarjetas_amarillas = int(input("¿Número de tarjetas amarillas?"))
tarjetas_rojas = int(input("¿Número de tarjetas rojas?"))

jugador = FootballPlayer(first_name=nombre,
                         last_name=apellido,
                         height_cm=altura,
                         weight_kg=peso,
                         goals=goles,
                         yellow_cards=tarjetas_amarillas,
                         red_cards=tarjetas_rojas)

players_list.append(jugador.__dict__)

with open("Players.txt", "w") as players_file:
    players_file.write(json.dumps(players_list))