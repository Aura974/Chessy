import datetime


def error_message(text):
    print(text)


def print_text(text):
    print(text)


def get_age(birthday):
    birthday = datetime.datetime.strptime(birthday, "%d/%m/%Y")
    days_in_year = 365.2425
    today = datetime.datetime.today()
    delta = today - birthday
    age = int(delta.days / days_in_year)
    return age


def is_date_valid(date_string):
    format = "%d/%m/%Y"
    try:
        datetime.datetime.strptime(date_string, format)
        return True
    except ValueError:
        return False


def set_date():
    date = datetime.datetime.now()
    date = date.strftime("%d/%m/%Y")
    return date


def set_round_time():
    time = datetime.datetime.now()
    time = time.strftime("%d/%m/%Y -- %H:%M:%S")
    return time


def is_tournament_name_valid(name_string):
    if any(x.isalnum() or x.isspace() or x == "-" for x in name_string):
        return True
    else:
        return False


def is_place_valid(place_string):
    allowed_punc = ["(", ")", "-"]
    if any(x.isalpha() or x.isspace() or x in allowed_punc for x in place_string):
        return True
    else:
        return False


def is_time_control_valid(tc_string):
    if (tc_string != "b" and tc_string != "bz" and tc_string != "r"):
        return True
    else:
        return False


def time_control_def(tc_string):
    letter_ref = {"b": "Bullet", "bz": "Blitz", "r": "Rapide"}
    for letter, word in letter_ref.items():
        if letter == tc_string:
            return word


def is_player_name_valid(name_string):
    if any(x.isalpha() or x.isspace() or x == "-" for x in name_string):
        return True
    else:
        return False


def is_elo_valid(elo_string):
    if any(x.isnumeric() for x in elo_string):
        return True
    else:
        return False


def is_gender_valid(gender_string):
    if (gender_string == "f" or gender_string == "m"):
        return True
    else:
        return False


def get_index(my_list):
    for index, elem in enumerate(my_list, start=1):
        index = index
        return index


def view_score(score):
    result = "Pas de résultat"
    if(score == 1):
        result = "Gagnant joueur 1"
    elif(score == 0):
        result = "Gagnant joueur 2"
    else:
        result = "Match nul"
    return result


def get_tournament_matches(tournament):
    tournament_rounds = tournament.rounds

    round_matches = list()

    for round in tournament_rounds:
        round_matches.append(round.matches)

    return tournament_rounds, round_matches


def is_query_empty(query):
    if len(query) == 0:
        return True
    else:
        return False


def is_continue_or_quit(quit):
    if (quit == "" or quit == "q"):
        return True
    else:
        return False


def is_update_player_elo_valid(update_elo):
    if (update_elo == "o" or update_elo == "n"):
        return True
    else:
        return False
