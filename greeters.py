class Greeters:
    def switchHour(self, heure):
        switcher = {
            "matin": "Bonjour",
            "aprem": "Bonne après midi",
            "soir": "Bonne soirée",
            "nuit": "Bonne nuit"
        }
        return switcher.get(heure, "Bienvenue")

    def welcome(self, username, heure):
        # version apres refactoring
        return self.switchHour(heure) + " " + username

        # ancienne version du code
        # if heure == "matin":
        #     return "Bonjour " + username
        # elif heure == "aprem":
        #     return "Bonne après midi " + username
        # elif heure == "soir":
        #     return "Bonne soirée " + username
        # else:
        #     return "Bienvenue " + username
