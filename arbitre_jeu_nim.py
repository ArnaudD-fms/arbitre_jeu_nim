import random


def init_game():
    while ((user_input := input("Voulez vous jouer contre un autre joueur ? (o/n) : ").strip().lower())
           not in ("oui", "o", "non", "n")):
        print("Veuillez répondre \"o\" ou \"n\".")

    is_versus_player = user_input in ("oui", "o")
    two_player_game() if is_versus_player else ia_game()


def two_player_game():
    matches = 21
    player_one = ask_name("Choisissez le pseudo du premier joueur : ")
    player_two = ask_name("Choisissez le pseudo du second joueur : ")

    current_player = draws_first_player(player_one, player_two)

    while not game_over(matches, current_player):

        user_input = input(f"{current_player} combien d'allumettes voulez-vous retirer ? (1 à 4) : ")

        if user_input.isdigit() and 1 <= int(user_input) <= 4:

            if int(user_input) > matches >= 1:
                print(f"il ne reste que {matches} allumettes. Vous ne pouvez pes en retirer {user_input} !")
                continue
            else:
                matches -= int(user_input)
                print(f"il reste {matches} allumettes")

            if matches == 0:
                print(f"Oups ! Vous avez retirez toutes les allumettes restantes, vous "
                      f"perdez la partie {current_player}")
                break

        else:
            print("Veuillez entrer un nombre entre 1 et 4.")
            continue

        current_player = player_two if current_player == player_one else player_one
        print("\n###########################################\n")
        print(f"Au tour de {current_player} de jouer.")


def draws_first_player(player_one, player_two):
    current_player = random.choice([player_one, player_two])
    print(f"Tirage au sort du joueur qui jouera en premier...\n{current_player} commence la partie !")

    return current_player


def ask_name(prompt):
    while True:
        name = input(prompt).strip()

        if 1 <= len(name) <= 16:
            return name

        print("Le pseudo doit contenir 16 caractères au maximum.")


def game_over(matches, current_player):
    if matches == 1:
        print(f"il ne reste plus qu'une allumette à retirer...\nDésolé {current_player} vous perdez la partie !")
        return True
    else:
        return False


def ia_game():
    matches = 21
    player = ask_name("Choisissez votre pseudo : ")
    current_player = draws_first_player(player, "ordinateur")


if __name__ == '__main__':
    init_game()
