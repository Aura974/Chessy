from controller.tournament import TournamentController


if __name__ == "__main__":
    tournamentController = TournamentController()
    tournamentController.run_first_round()
    tournamentController.run_other_rounds()
