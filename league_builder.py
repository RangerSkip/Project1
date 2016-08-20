import csv

def Dictinator():
    '''Assigns the information from 'soccer_players.csv' to the Players dictionary.'''
    i = 1

    with open("soccer_players.csv", newline='') as csvfile:
        soccerreader = csv.DictReader(csvfile, delimiter=',')
        rows = list(soccerreader)
        for row in rows[:]:
            Players[i] = {}
            Players[i]['Name'] = row['Name']
            Players[i]['Height (inches)'] = row['Height (inches)']
            Players[i]['Soccer Experience'] = row['Soccer Experience']
            Players[i]['Guardian Name(s)'] = row['Guardian Name(s)']
            i = i + 1

def Sharks(Dict):
    '''Assigns players to Team Sharks, first finding 3 children with prior soccer
       experience and then 3 children with none.'''

    i = 1
    experienced_players = []
    nonexperienced_players = []

    for player in Dict:
        if Dict[player]['Soccer Experience'] == 'YES' and len(experienced_players) < 3:
            Team_Sharks[i] = {}
            Team_Sharks[i]['Name'] = Dict[player]['Name']
            Team_Sharks[i]['Height (inches)'] = Dict[player]['Height (inches)']
            Team_Sharks[i]['Soccer Experience'] = Dict[player]['Soccer Experience']
            Team_Sharks[i]['Guardian Name(s)'] = Dict[player]['Guardian Name(s)']
            i = i + 1
            experienced_players.append(Dict[player]["Name"])
        elif Dict[player]['Soccer Experience'] == 'NO' and len(nonexperienced_players) < 3:
            Team_Sharks[i] = {}
            Team_Sharks[i]['Name'] = Dict[player]['Name']
            Team_Sharks[i]['Height (inches)'] = Dict[player]['Height (inches)']
            Team_Sharks[i]['Soccer Experience'] = Dict[player]['Soccer Experience']
            Team_Sharks[i]['Guardian Name(s)'] = Dict[player]['Guardian Name(s)']
            i = i + 1
            nonexperienced_players.append(Dict[player]["Name"])


    # Deletes children already assigned to Team Sharks from the list of available players.
    for item in Team_Sharks:
        assigned_players.append(Team_Sharks[item]['Name'])

    for i in range(1, 18):
        if Dict[i]["Name"] in assigned_players:
            del Dict[i]


def Dragons(Dict):
    '''Assigns players to Team Sharks, first finding 3 children with prior soccer
       experience and then 3 children with none.'''

    i = 1
    experienced_players = []
    nonexperienced_players = []


    for player in Dict:
        if Dict[player]['Soccer Experience'] == 'YES' and len(experienced_players) < 3:
            Team_Dragons[i] = {}
            Team_Dragons[i]['Name'] = Dict[player]['Name']
            Team_Dragons[i]['Height (inches)'] = Dict[player]['Height (inches)']
            Team_Dragons[i]['Soccer Experience'] = Dict[player]['Soccer Experience']
            Team_Dragons[i]['Guardian Name(s)'] = Dict[player]['Guardian Name(s)']
            i = i + 1
            experienced_players.append(Dict[player]["Name"])
        elif Dict[player]['Soccer Experience'] == 'NO' and len(nonexperienced_players) < 3:
            Team_Dragons[i] = {}
            Team_Dragons[i]['Name'] = Dict[player]['Name']
            Team_Dragons[i]['Height (inches)'] = Dict[player]['Height (inches)']
            Team_Dragons[i]['Soccer Experience'] = Dict[player]['Soccer Experience']
            Team_Dragons[i]['Guardian Name(s)'] = Dict[player]['Guardian Name(s)']
            i = i + 1
            nonexperienced_players.append(Dict[player]["Name"])

    # Deletes children already assigned to Team Sharks from the list of available players.


    for item in Team_Dragons:
        assigned_players.append(Team_Dragons[item]['Name'])

    i = 1


    for i in range(len(Team_Sharks)+1, 18):
        if Dict[i]["Name"] in assigned_players:
            del Dict[i]
        i += 1


def Raptors(Dict):
    '''Assigns players to Team Sharks, first finding 3 children with prior soccer
       experience and then 3 children with none.'''

    i = 1
    experienced_players = []
    nonexperienced_players = []

    for player in Dict:
        if Dict[player]['Soccer Experience'] == 'YES' and len(experienced_players) < 3:
            Team_Raptors[i] = {}
            Team_Raptors[i]['Name'] = Dict[player]['Name']
            Team_Raptors[i]['Height (inches)'] = Dict[player]['Height (inches)']
            Team_Raptors[i]['Soccer Experience'] = Dict[player]['Soccer Experience']
            Team_Raptors[i]['Guardian Name(s)'] = Dict[player]['Guardian Name(s)']
            i = i + 1
            experienced_players.append(Dict[player]["Name"])
        elif Dict[player]['Soccer Experience'] == 'NO' and len(nonexperienced_players) < 3:
            Team_Raptors[i] = {}
            Team_Raptors[i]['Name'] = Dict[player]['Name']
            Team_Raptors[i]['Height (inches)'] = Dict[player]['Height (inches)']
            Team_Raptors[i]['Soccer Experience'] = Dict[player]['Soccer Experience']
            Team_Raptors[i]['Guardian Name(s)'] = Dict[player]['Guardian Name(s)']
            i = i + 1
            nonexperienced_players.append(Dict[player]["Name"])

    # Deletes children already assigned to Team Sharks from the list of available players.
    for item in Team_Raptors:
        assigned_players.append(Team_Raptors[item]['Name'])

    i = 1


def Letters(Dict, String1, String2):
    for item in Dict:
        name = Dict[item]["Name"]
        filename = name.replace(" ",'_') + ".txt"
        with open(filename.lower(), 'a') as file:
            file.write(
            "Dear {}, \n"
            "\tCongratulations on your child making Team {}!"
            " Don't forget, team practice will be at \n"
            "The Derek Zoolander Center For Kids Who Can't Read Good And Wanna Learn To Do Other Stuff Good Too \n"
            "on {}.\n\n"
            "Sincerely,\n"
            "Your Friendly Neighborhood Soccer Club".format(Dict[item]["Guardian Name(s)"], String1, String2))

if __name__ =='__main__':
    # Variables
    Players = {}
    Team_Sharks = {}
    Team_Dragons = {}
    Team_Raptors = {}
    assigned_players = []
    v = 1
    i = 1

    Dragons_Practice = "March 17 at 1pm"
    Sharks_Practice = "March 17 at 3pm"
    Raptors_Practice = "March 18 at 1pm"

    Dictinator()
    Player_Roster = Players

    # Assigning players to teams
    Sharks(Players)
    Dragons(Players)
    Raptors(Players)

    # Writing letters to guardians
    Letters(Team_Sharks, "Sharks", Sharks_Practice)
    Letters(Team_Dragons, "Dragons", Dragons_Practice)
    Letters(Team_Raptors, "Raptors", Raptors_Practice)
