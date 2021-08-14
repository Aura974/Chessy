from controller.tournament_controller import TournamentController


if __name__ == "__main__":
    tournamentController = TournamentController()
    tournamentController.new_tournament()
    tournamentController.run_first_round()
    for round_number in range(2, 5):
        tournamentController.run_round(round_number)
