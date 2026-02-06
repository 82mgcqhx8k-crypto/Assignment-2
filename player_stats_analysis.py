"""
NBA Player Statistics Analysis
Analyzes player statistics from a CSV file using Python and NumPy only.

This script calculates:
- Field goal accuracy
- Three point accuracy
- Free throw accuracy
- Average points per minute
- Overall shooting accuracy
- Average blocks per game
- Average steals per game

And generates top 100 players lists for each metric.
"""

import numpy as np
import csv


def load_csv_with_numpy(filepath):
    """
    Load CSV file using numpy.
    
    Args:
        filepath: Path to the CSV file
        
    Returns:
        data: numpy array of data
        headers: list of column headers
    """
    # Read the CSV file
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader)  # Get header row
        data_list = []
        for row in reader:
            data_list.append(row)
    
    # Convert to numpy array
    data = np.array(data_list)
    
    return data, headers


def get_column_index(headers, column_name):
    """Get the index of a column by name."""
    try:
        return headers.index(column_name)
    except ValueError:
        return None


def safe_divide(numerator, denominator):
    """Safely divide two arrays, handling division by zero."""
    # Convert to float arrays
    num = np.array(numerator, dtype=float)
    denom = np.array(denominator, dtype=float)
    
    # Create result array filled with zeros
    result = np.zeros_like(num)
    
    # Only divide where denominator is not zero
    mask = denom != 0
    result[mask] = num[mask] / denom[mask]
    
    return result


def calculate_field_goal_accuracy(data, headers):
    """
    Calculate field goal accuracy for each player in each season.
    Field Goal Accuracy = FGM / FGA * 100
    """
    fgm_idx = get_column_index(headers, 'FGM')
    fga_idx = get_column_index(headers, 'FGA')
    
    if fgm_idx is None or fga_idx is None:
        print("Warning: FGM or FGA columns not found")
        return None
    
    fgm = data[:, fgm_idx].astype(float)
    fga = data[:, fga_idx].astype(float)
    
    accuracy = safe_divide(fgm, fga) * 100
    return accuracy


def calculate_three_point_accuracy(data, headers):
    """
    Calculate three point accuracy for each player in each season.
    Three Point Accuracy = 3PM / 3PA * 100
    """
    tpm_idx = get_column_index(headers, '3PM')
    tpa_idx = get_column_index(headers, '3PA')
    
    if tpm_idx is None or tpa_idx is None:
        print("Warning: 3PM or 3PA columns not found")
        return None
    
    tpm = data[:, tpm_idx].astype(float)
    tpa = data[:, tpa_idx].astype(float)
    
    accuracy = safe_divide(tpm, tpa) * 100
    return accuracy


def calculate_free_throw_accuracy(data, headers):
    """
    Calculate free throw accuracy for each player in each season.
    Free Throw Accuracy = FTM / FTA * 100
    """
    ftm_idx = get_column_index(headers, 'FTM')
    fta_idx = get_column_index(headers, 'FTA')
    
    if ftm_idx is None or fta_idx is None:
        print("Warning: FTM or FTA columns not found")
        return None
    
    ftm = data[:, ftm_idx].astype(float)
    fta = data[:, fta_idx].astype(float)
    
    accuracy = safe_divide(ftm, fta) * 100
    return accuracy


def calculate_points_per_minute(data, headers):
    """
    Calculate average points scored per minute for each player in each season.
    Points Per Minute = PTS / MIN
    """
    pts_idx = get_column_index(headers, 'PTS')
    min_idx = get_column_index(headers, 'MIN')
    
    if pts_idx is None or min_idx is None:
        print("Warning: PTS or MIN columns not found")
        return None
    
    pts = data[:, pts_idx].astype(float)
    minutes = data[:, min_idx].astype(float)
    
    ppm = safe_divide(pts, minutes)
    return ppm


def calculate_overall_shooting_accuracy(data, headers):
    """
    Calculate overall shooting accuracy for each player in each season.
    Overall Shooting Accuracy = Total Made Shots / Total Attempted Shots * 100
    Total Made = FGM + FTM (FGM already includes 3PM)
    Total Attempted = FGA + FTA (FGA already includes 3PA)
    """
    fgm_idx = get_column_index(headers, 'FGM')
    fga_idx = get_column_index(headers, 'FGA')
    ftm_idx = get_column_index(headers, 'FTM')
    fta_idx = get_column_index(headers, 'FTA')
    
    if None in [fgm_idx, fga_idx, ftm_idx, fta_idx]:
        print("Warning: Required columns for overall shooting accuracy not found")
        return None
    
    fgm = data[:, fgm_idx].astype(float)
    fga = data[:, fga_idx].astype(float)
    ftm = data[:, ftm_idx].astype(float)
    fta = data[:, fta_idx].astype(float)
    
    total_made = fgm + ftm  # FGM already includes 3PM
    total_attempted = fga + fta  # FGA already includes 3PA
    
    accuracy = safe_divide(total_made, total_attempted) * 100
    return accuracy


def calculate_blocks_per_game(data, headers):
    """
    Calculate average blocks per game for each player in each season.
    Blocks Per Game = BLK / GP
    """
    blk_idx = get_column_index(headers, 'BLK')
    gp_idx = get_column_index(headers, 'GP')
    
    if blk_idx is None or gp_idx is None:
        print("Warning: BLK or GP columns not found")
        return None
    
    blk = data[:, blk_idx].astype(float)
    gp = data[:, gp_idx].astype(float)
    
    bpg = safe_divide(blk, gp)
    return bpg


def calculate_steals_per_game(data, headers):
    """
    Calculate average steals per game for each player in each season.
    Steals Per Game = STL / GP
    """
    stl_idx = get_column_index(headers, 'STL')
    gp_idx = get_column_index(headers, 'GP')
    
    if stl_idx is None or gp_idx is None:
        print("Warning: STL or GP columns not found")
        return None
    
    stl = data[:, stl_idx].astype(float)
    gp = data[:, gp_idx].astype(float)
    
    spg = safe_divide(stl, gp)
    return spg


def get_top_100(data, headers, metric_values, metric_name, min_threshold=None):
    """
    Get top 100 players for a given metric.
    
    Args:
        data: numpy array of all data
        headers: list of column headers
        metric_values: numpy array of calculated metric values
        metric_name: name of the metric
        min_threshold: optional minimum threshold for filtering (e.g., minimum attempts)
        
    Returns:
        top_100: list of tuples (player, season, value)
    """
    if metric_values is None:
        print(f"Cannot generate top 100 for {metric_name}: metric not calculated")
        return []
    
    player_idx = get_column_index(headers, 'Player')
    season_idx = get_column_index(headers, 'Season')
    
    if player_idx is None or season_idx is None:
        # Try alternative column names
        player_idx = get_column_index(headers, 'PLAYER')
        season_idx = get_column_index(headers, 'SEASON')
        
        if player_idx is None or season_idx is None:
            print(f"Warning: Player or Season columns not found")
            # Use index as fallback
            player_idx = 0
            season_idx = 1 if len(headers) > 1 else 0
    
    # Create array of indices sorted by metric value (descending)
    sorted_indices = np.argsort(metric_values)[::-1]
    
    # Get top 100 (or fewer if less data available)
    top_count = min(100, len(sorted_indices))
    top_indices = sorted_indices[:top_count]
    
    top_100 = []
    for idx in top_indices:
        player = data[idx, player_idx]
        season = data[idx, season_idx]
        value = metric_values[idx]
        top_100.append((player, season, value))
    
    return top_100


def save_top_100_to_file(top_100, metric_name, filename):
    """Save top 100 list to a file."""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"Top 100 Players by {metric_name}\n")
        f.write("=" * 80 + "\n")
        f.write(f"{'Rank':<6} {'Player':<30} {'Season':<10} {'Value':<15}\n")
        f.write("-" * 80 + "\n")
        
        for rank, (player, season, value) in enumerate(top_100, 1):
            f.write(f"{rank:<6} {player:<30} {season:<10} {value:<15.2f}\n")


def main(csv_filepath):
    """
    Main function to analyze player statistics.
    
    Args:
        csv_filepath: Path to the CSV file containing player statistics
    """
    print("Loading CSV file...")
    data, headers = load_csv_with_numpy(csv_filepath)
    print(f"Loaded {len(data)} rows with {len(headers)} columns")
    print(f"Headers: {headers}\n")
    
    # Calculate all metrics
    print("Calculating field goal accuracy...")
    fg_accuracy = calculate_field_goal_accuracy(data, headers)
    
    print("Calculating three point accuracy...")
    tp_accuracy = calculate_three_point_accuracy(data, headers)
    
    print("Calculating free throw accuracy...")
    ft_accuracy = calculate_free_throw_accuracy(data, headers)
    
    print("Calculating points per minute...")
    pts_per_min = calculate_points_per_minute(data, headers)
    
    print("Calculating overall shooting accuracy...")
    overall_accuracy = calculate_overall_shooting_accuracy(data, headers)
    
    print("Calculating blocks per game...")
    blocks_pg = calculate_blocks_per_game(data, headers)
    
    print("Calculating steals per game...")
    steals_pg = calculate_steals_per_game(data, headers)
    
    print("\nGenerating top 100 lists...")
    
    # Generate top 100 lists
    metrics = [
        (fg_accuracy, "Field Goal Accuracy (%)", "top_100_field_goal_accuracy.txt"),
        (tp_accuracy, "Three Point Accuracy (%)", "top_100_three_point_accuracy.txt"),
        (ft_accuracy, "Free Throw Accuracy (%)", "top_100_free_throw_accuracy.txt"),
        (pts_per_min, "Points Per Minute", "top_100_points_per_minute.txt"),
        (overall_accuracy, "Overall Shooting Accuracy (%)", "top_100_overall_shooting_accuracy.txt"),
        (blocks_pg, "Blocks Per Game", "top_100_blocks_per_game.txt"),
        (steals_pg, "Steals Per Game", "top_100_steals_per_game.txt")
    ]
    
    for metric_values, metric_name, filename in metrics:
        print(f"  - {metric_name}")
        top_100 = get_top_100(data, headers, metric_values, metric_name)
        save_top_100_to_file(top_100, metric_name, filename)
    
    print("\nAnalysis complete! Top 100 lists saved to individual files.")
    print("\nFiles created:")
    for _, metric_name, filename in metrics:
        print(f"  - {filename}")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python player_stats_analysis.py <path_to_csv_file>")
        print("\nExample:")
        print("  python player_stats_analysis.py /Users/yoshi_zen25/Downloads/players_stats_by_season_full_details.csv")
        sys.exit(1)
    
    csv_file = sys.argv[1]
    main(csv_file)
