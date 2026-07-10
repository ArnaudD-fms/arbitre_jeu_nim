import random


def init_game():
    while ((user_input := input("Voulez vous jouer contre un autre joueur ? (o/n) : ").strip().lower())
           not in ("oui", "o", "non", "n")):
        print("Veuillez répondre ""o"" ou ""n"".")

    is_versus_player = user_input in ("oui", "o")
    launch_two_player_game() if is_versus_player else launch_ia_game()


def launch_two_player_game():
    player_one = ask_name("Choisissez le pseudo du premier joueur : ")
    player_two = ask_name("Choisissez le pseudo du second joueur : ")

    starting_player = random.choice([player_one, player_two])
    print(f"Tirage au sort du joueur qui jouera en premier...\n{starting_player} commence la partie !")


def ask_name(prompt):
    while True:
        name = input(prompt).strip()

        if 1 <= len(name) <= 16:
            return name

        print("Le pseudo doit contenir 16 caractères au maximum.")


def launch_ia_game():
    pass


if __name__ == '__main__':
    # demande si le joueur ceux jouer contre l'ordinateur ou contre un humain
    # récupération du pseudo du/des joueurs
    # un joueur est désigné aléatoirement pour commencer

    # PARTIE JOUEUR CONTRE JOUEUR
    # On demande au joueur un combien d'allumette, il souhaite prendre (entre une et quatre).
    # On indique le nombre d'allumettes restantes
    # On continue la partie jusqu'à ce qu'il ne reste plus qu'une allumette. Le joueur dont c'est le tour
    # perd la partie
    # Attention à empêcher un joueur de prendre plus d'allumette que ce qu'il n'en reste.

    # PARTIE CONTRE ORDI
    # si le joueur démarre la partie alors l'ordinateur jouera systématiquement 5-n allumettes (n étant le nombre
    # d'allumettes enlevé par le joueur au tour précedant)
    # si le joueur commence l'ordinateur essaiera d'utiliser la même technique (ne fonctionnera pas si
    # le joueur connaît l'astuce)
    init_game()
