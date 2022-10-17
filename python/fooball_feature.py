# create a feature for team pairing

teams = [ 'Wolves fc', 'Liverpool', 'pandas fc', 'Arsenal', 'Dragons' ]
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)
