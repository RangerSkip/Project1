import csv

def Dictinator():
    '''Assigns the information from 'soccer_players.csv' to the league dictionary.'''
    i = 1

    with open("soccer_players.csv", newline='') as csvfile:
        soccerreader = csv.DictReader(csvfile, delimiter=',')
        rows = list(soccerreader)
        for row in rows[:]:
            league[i] = {}
            league[i]['Name'] = row['Name']
            league[i]['Height (inches)'] = row['Height (inches)']
            league[i]['Soccer Experience'] = row['Soccer Experience']
            league[i]['Guardian Name(s)'] = row['Guardian Name(s)']
            i = i + 1

def Sharkinator(Dict):
    '''Assigns players to Team Sharks, first finding 3 children with prior soccer
       experience and then 3 children with none.'''

    i = 1
    experienced_players = []
    nonexperienced_players = []

    for player in Dict:
        if Dict[player]['Soccer Experience'] == 'YES' and len(experienced_players) < 3:
            Sharks[i] = {}
            Sharks[i]['Name'] = Dict[player]['Name']
            Sharks[i]['Height (inches)'] = Dict[player]['Height (inches)']
            Sharks[i]['Soccer Experience'] = Dict[player]['Soccer Experience']
            Sharks[i]['Guardian Name(s)'] = Dict[player]['Guardian Name(s)']
            i = i + 1
            experienced_players.append(Dict[player]["Name"])
        elif Dict[player]['Soccer Experience'] == 'NO' and len(nonexperienced_players) < 3:
            Sharks[i] = {}
            Sharks[i]['Name'] = Dict[player]['Name']
            Sharks[i]['Height (inches)'] = Dict[player]['Height (inches)']
            Sharks[i]['Soccer Experience'] = Dict[player]['Soccer Experience']
            Sharks[i]['Guardian Name(s)'] = Dict[player]['Guardian Name(s)']
            i = i + 1
            nonexperienced_players.append(Dict[player]["Name"])


    # Deletes children already assigned to Team Sharks from the list of available players.
    for item in Sharks:
        assigned_players.append(Sharks[item]['Name'])

    for i in range(1, 18):
        if Dict[i]["Name"] in assigned_players:
            del Dict[i]


def Dragonator(Dict):
    '''Assigns players to Team Sharks, first finding 3 children with prior soccer
       experience and then 3 children with none.'''

    i = 1
    experienced_players = []
    nonexperienced_players = []


    for player in Dict:
        if Dict[player]['Soccer Experience'] == 'YES' and len(experienced_players) < 3:
            Dragons[i] = {}
            Dragons[i]['Name'] = Dict[player]['Name']
            Dragons[i]['Height (inches)'] = Dict[player]['Height (inches)']
            Dragons[i]['Soccer Experience'] = Dict[player]['Soccer Experience']
            Dragons[i]['Guardian Name(s)'] = Dict[player]['Guardian Name(s)']
            i = i + 1
            experienced_players.append(Dict[player]["Name"])
        elif Dict[player]['Soccer Experience'] == 'NO' and len(nonexperienced_players) < 3:
            Dragons[i] = {}
            Dragons[i]['Name'] = Dict[player]['Name']
            Dragons[i]['Height (inches)'] = Dict[player]['Height (inches)']
            Dragons[i]['Soccer Experience'] = Dict[player]['Soccer Experience']
            Dragons[i]['Guardian Name(s)'] = Dict[player]['Guardian Name(s)']
            i = i + 1
            nonexperienced_players.append(Dict[player]["Name"])

    # Deletes children already assigned to Team Sharks from the list of available players.


    for item in Dragons:
        assigned_players.append(Dragons[item]['Name'])

    i = 1


    for i in range(len(Sharks)+1, 18):
        if Dict[i]["Name"] in assigned_players:
            del Dict[i]
        i += 1


def Raptorator(Dict):
    '''Assigns players to Team Sharks, first finding 3 children with prior soccer
       experience and then 3 children with none.'''

    i = 1
    experienced_players = []
    nonexperienced_players = []

    for player in Dict:
        if Dict[player]['Soccer Experience'] == 'YES' and len(experienced_players) < 3:
            Raptors[i] = {}
            Raptors[i]['Name'] = Dict[player]['Name']
            Raptors[i]['Height (inches)'] = Dict[player]['Height (inches)']
            Raptors[i]['Soccer Experience'] = Dict[player]['Soccer Experience']
            Raptors[i]['Guardian Name(s)'] = Dict[player]['Guardian Name(s)']
            i = i + 1
            experienced_players.append(Dict[player]["Name"])
        elif Dict[player]['Soccer Experience'] == 'NO' and len(nonexperienced_players) < 3:
            Raptors[i] = {}
            Raptors[i]['Name'] = Dict[player]['Name']
            Raptors[i]['Height (inches)'] = Dict[player]['Height (inches)']
            Raptors[i]['Soccer Experience'] = Dict[player]['Soccer Experience']
            Raptors[i]['Guardian Name(s)'] = Dict[player]['Guardian Name(s)']
            i = i + 1
            nonexperienced_players.append(Dict[player]["Name"])

    # Deletes children already assigned to Team Sharks from the list of available players.
    for item in Raptors:
        assigned_players.append(Raptors[item]['Name'])

    i = 1


def Letters(Dict, String1, String2):
    for item in Dict:
        name = Dict[item]["Name"]
        filename = name.replace(" ",'_') + ".txt"
        with open(filename.lower(), 'a') as file:
            file.write(
            "Dear {}, \n"
            "\tCongratulations on little {} making Team {}!"
            " Don't forget, team practice will be at \n"
            "The Derek Zoolander Center For Kids Who Can't Read Good And Wanna Learn To Do Other Stuff Good Too \n"
            "on {}.\n\n"
            "Sincerely,\n"
            "Your Friendly Neighborhood Soccer Club".format(Dict[item]["Guardian Name(s)"], Dict[item]["Name"], String1, String2))

if __name__ =='__main__':
    # Variables
    league = {}
    Sharks = {}
    Dragons = {}
    Raptors = {}
    assigned_players = []
    v = 1
    i = 1

    Dragons_Practice = "March 17 at 1pm"
    Sharks_Practice = "March 17 at 3pm"
    Raptors_Practice = "March 18 at 1pm"

    Dictinator()
    Player_Roster = league

    # Assigning players to teams
    Sharkinator(league)
    Dragonator(league)
    Raptorator(league)

    # Writing letters to guardians
    Letters(Sharks, "Sharks", Sharks_Practice)
    Letters(Dragons, "Dragons", Dragons_Practice)
    Letters(Raptors, "Raptors", Raptors_Practice)
