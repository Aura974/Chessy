from controller.tournament_controller import TournamentController


if __name__ == "__main__":
    tournamentController = TournamentController()
    # tournamentController.reload_tournament()

    tournamentController.new_tournament()
    # for round_number in range(2, 5):
    #     tournamentController.run_round(round_number)
