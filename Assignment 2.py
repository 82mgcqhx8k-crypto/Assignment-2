import numpy as np

# Load the data
player_data = np.genfromtxt('players_stats_by_season_full_details.csv', delimiter=',', skip_header=1)

field_goals_made = player_data[:, 7]
field_goals_attempted = player_data[:, 8]
three_points_made = player_data[:, 9]
three_points_attempted = player_data[:, 10]
free_throws_made = player_data[:, 11]
free_throws_attempted = player_data[:, 12]
points_scored = player_data[:, 21]
minutes_played = player_data[:, 6]
blocks = player_data[:, 20]
steals = player_data[:, 19]
games_played = player_data[:, 5]

# Calculate metrics
field_goal_accuracy = field_goals_made / field_goals_attempted
three_point_accuracy = three_points_made / three_points_attempted
free_throw_accuracy = free_throws_made / free_throws_attempted
average_points_per_minute = points_scored / minutes_played
overall_shooting_accuracy = (field_goals_made + three_points_made + free_throws_made) / (field_goals_attempted + three_points_attempted + free_throws_attempted)
average_blocks_per_game = blocks / games_played
average_steals_per_game = steals / games_played

# Combine metrics into a structured array
metrics = np.column_stack((field_goal_accuracy, three_point_accuracy, free_throw_accuracy, average_points_per_minute, overall_shooting_accuracy, average_blocks_per_game, average_steals_per_game))


top_100 = np.argsort(metrics)[100]


# Output the top 100 players and their metrics
print(top_100)
