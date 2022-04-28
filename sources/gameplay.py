from gameinfo import Truck, parse_argument, GameInfo
import random


class GamePlay:
    def __init__(self) -> None:
        self.args = parse_argument()
        self.game_info = GameInfo(self.args.game_number, self.args.output_file)
        self.game_info.init_game_info()

    def get_truck_actions_available(self, truck: Truck):
        truck.actions_available.clear()

        if self.game_info.is_crystal_available(truck.pos_x, truck.pos_y):
            truck.actions_available.append(truck.action_dig())

        truck.actions_available = self.game_info.is_movable(
            truck, truck.pos_x, truck.pos_y
        )

    def get_next_trucks_action(self, truck: Truck):
        self.get_truck_actions_available(truck)
        print(truck.actions_available)

        return random.choice(truck.actions_available)

    def play_trucks(self):
        for truck in self.game_info.get_trucks():
            if truck.last_turn_played != self.game_info.nb_turn:
                # self.get_truck_actions_available(truck)
                tr_action = self.get_next_trucks_action(truck)
                truck.set_move(tr_action)
                # print("Camion {} play {}".format(truck.id, tr_action))
                self.game_info.add_actions(tr_action)

                truck.last_turn_played += 1

        self.game_info.nb_turn += 1

    def run(self):
        while (
            self.game_info.is_crystal_available_on_map() and self.game_info.nb_turn < 25
        ):
            self.play_trucks()
        self.game_info.save_actions("test.txt")


if __name__ == "__main__":
    gp = GamePlay()
    gp.run()