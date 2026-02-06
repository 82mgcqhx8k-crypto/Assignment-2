# Assignment-2: NBA Player Statistics Analysis

This repository contains a Python script to analyze NBA player statistics from a CSV file using only Python standard library and NumPy.

## Features

The script calculates the following metrics for each player in each season:

1. **Field Goal Accuracy**: FGM / FGA × 100
2. **Three Point Accuracy**: 3PM / 3PA × 100
3. **Free Throw Accuracy**: FTM / FTA × 100
4. **Average Points Per Minute**: PTS / MIN
5. **Overall Shooting Accuracy**: (FGM + FTM) / (FGA + FTA) × 100
6. **Average Blocks Per Game**: BLK / GP
7. **Average Steals Per Game**: STL / GP

The script also generates a list of the top 100 players for each metric.

## Requirements

- Python 3.x
- NumPy

## Installation

```bash
pip install numpy
```

## Usage

```bash
python player_stats_analysis.py <path_to_csv_file>
```

### Example

```bash
python player_stats_analysis.py /Users/yoshi_zen25/Downloads/players_stats_by_season_full_details.csv
```

## Expected CSV Format

The CSV file should contain the following columns:

- `Player` or `PLAYER`: Player name
- `Season` or `SEASON`: Season identifier
- `FGM`: Field Goals Made
- `FGA`: Field Goals Attempted
- `3PM`: Three Points Made
- `3PA`: Three Points Attempted
- `FTM`: Free Throws Made
- `FTA`: Free Throws Attempted
- `PTS`: Points
- `MIN`: Minutes Played
- `BLK`: Blocks
- `STL`: Steals
- `GP`: Games Played

## Output

The script generates 7 text files containing the top 100 players for each metric:

1. `top_100_field_goal_accuracy.txt`
2. `top_100_three_point_accuracy.txt`
3. `top_100_free_throw_accuracy.txt`
4. `top_100_points_per_minute.txt`
5. `top_100_overall_shooting_accuracy.txt`
6. `top_100_blocks_per_game.txt`
7. `top_100_steals_per_game.txt`

Each file contains a ranked list with player name, season, and the calculated metric value.

## Implementation Notes

- The script uses only Python standard library (csv module) and NumPy for calculations
- Handles division by zero safely (returns 0 when denominator is 0)
- All accuracy calculations are expressed as percentages
- Top 100 lists are sorted in descending order (highest values first)