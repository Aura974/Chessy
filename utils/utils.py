import datetime


def error_message(text):
    print(text)


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
