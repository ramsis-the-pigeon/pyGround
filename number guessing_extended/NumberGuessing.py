import csv
import random

# Define the CSV file name
FAME_FILE = 'fame.csv'

def load_players():
    """Load player data from the CSV file into a dictionary."""
    players = {}
    try:
        with open(FAME_FILE, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                players[row['username']] = {
                    'rank': float(row['rank']),
                    'best': int(row['best']),
                    'total_games': int(row['total_games'])
                }
    except FileNotFoundError:
        pass  # The file will be created when saving data
    return players

def save_players(players):
    """Save player data to the CSV file."""
    with open(FAME_FILE, mode='w', newline='') as file:
        fieldnames = ['username', 'rank', 'best', 'total_games']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for username, stats in players.items():
            writer.writerow({
                'username': username,
                'rank': stats['rank'],
                'best': stats['best'],
                'total_games': stats['total_games']
            })

def display_top_players(players):
    """Display the top 3 players based on their ranking score."""
    sorted_players = sorted(players.items(), key=lambda item: item[1]['rank'], reverse=True)
    print("\nTop 3 Players:")
    for i, (username, stats) in enumerate(sorted_players[:3], start=1):
        print(f"{i}. {username} - Best Score: {stats['best']} | Rank: {stats['rank']:.2f} | Total Games: {stats['total_games']}")

def calculate_rank(players):
    """Calculate the rank based on total games played and best score (for tie-breaking)."""
    # Sort players first by total games in descending order, then by best score (tie-breaking) in descending order
    sorted_players = sorted(players.items(), key=lambda item: (item[1]['total_games'], item[1]['best']), reverse=True)
    
    # Assign ranks based on the sorted list
    rank_dict = {}
    for idx, (username, stats) in enumerate(sorted_players, start=1):
        rank_dict[username] = idx  # Assign rank based on sorted position
    
    return rank_dict




def main():
    players = load_players()
    username = input('Enter your username: ')

    # Option to display top 3 players
    show_top = input('Would you like to see the top 3 players? (Y/N): ').upper()
    if show_top == 'Y':
        display_top_players(players)

    # Check if the username already exists in the CSV
    if username in players:
        print(f'Welcome back, {username}! Your current rank is {players[username]["rank"]}, best score is {players[username]["best"]}, and total games played is {players[username]["total_games"]}.')
    else:
        print(f'Welcome, {username}! This is your first game.')
        players[username] = {'rank': 0, 'best': 0, 'total_games': 0, 'games_won': 0}

    is_running = True
    attempts = 10
    random_number = random.randint(1, 100)
    current_score = 0

    while is_running:
        guess = int(input('Guess a number between 1 and 100: '))

        if guess < random_number:
            print("Too low")
            attempts -= 1
        elif guess > random_number:
            print("Too high")
            attempts -= 1
        elif guess == random_number:
            print('That\'s correct! \nYou win')
            current_score = attempts * 10
            print(f'Your score is {current_score}/100')
            
            # Update player stats
            players[username]['total_games'] += 1
            players[username]['games_won'] += 1  # Increment games won
            if current_score > players[username]['best']:
                players[username]['best'] = current_score

            # Recalculate rank for all players based on total games
            rank_dict = calculate_rank(players)
            players[username]['rank'] = rank_dict[username]  # Assign the player's new rank

            options = input('Press A to play again, Q to quit: ').upper()
            if options == 'A':
                attempts = 10
                random_number = random.randint(1, 100)
                continue
            elif options == 'Q':
                is_running = False

        if not attempts:
            print('You ran out of attempts')
            players[username]['total_games'] += 1
            # Recalculate rank for all players based on total games
            rank_dict = calculate_rank(players)
            players[username]['rank'] = rank_dict[username]

            options = input('Press A to play again, Q to quit: ').upper()
            if options == 'A':
                attempts = 10
                random_number = random.randint(1, 100)
            elif options == 'Q':
                is_running = False

    save_players(players)
    print('Thanks for playing! Your stats have been saved.')

if __name__ == "__main__":
    main()
