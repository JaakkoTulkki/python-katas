def goal_diff(scored, scored_against):
    return abs(int(scored) - int(scored_against))

def print_smallest_difference():
    table_data = []
    for row in  open('football.dat', 'r'):
        row = [d for d in row.split(" ") if d]
        table_data.append(row)
    table_data = table_data[1:]
    table_data = [d for d in table_data if len(d) > 1]

    goal_difference = ""
    team_with_smallest_diff = []
    for team in table_data:
        diff = goal_diff(team[6], team[8])
        if type(goal_difference) is str:
            goal_difference = diff
        elif diff < goal_difference:
            goal_difference = diff
            team_with_smallest_diff = team

    return "The team with the smallest difference is {team} with a difference of {diff}".format(**{'team': team_with_smallest_diff[1],
                                                                                                  'diff': goal_difference
                                                                                                  })
