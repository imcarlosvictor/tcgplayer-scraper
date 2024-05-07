import os
import csv
import time
from pytz import timezone
from datetime import datetime



def save_to_csv(category: str, data: list) -> None:
    # Create file name
    tz = timezone('America/Toronto')
    current_date = datetime.now(tz).strftime('%Y%m%d_%H%M%S')
    file_name = f'{current_date}_{category}.csv'

    # Create header
    fields = [
        'Category',
        'Card Set',
        'Rarity',
        'Title',
        'Market Price (USD)',
    ]

    # Create a csv file to store the data
    DIRECTORY_PATH = os.path.abspath(os.path.dirname(__file__))
    RAW_DATA_EXTRACT_FILE_PATH = os.path.abspath(os.path.join(DIRECTORY_PATH, f'../dataset/{file_name}'))
    with open(RAW_DATA_EXTRACT_FILE_PATH, 'w') as file:
        # Create title headers
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()

        # Add extracted data to the csv file
        for row in data:
            writer.writerow({
                fields[0]: row[0],
                fields[1]: row[1], 
                fields[2]: row[2], 
                fields[3]: row[3], 
                fields[4]: row[4], 
            })


x = [
    ['One Piece Card Game', 'Wings of the Captain', 'Super Rare · #OP06-107', 'Kouzuki Momonosuke', '$1.53'],
    ['One Piece Card Game', 'Ultra Deck: The Three Brothers', 'Super Rare · #ST13-015', 'Monkey.D.Luffy (015)', '$1.08'],
    ['One Piece Card Game', 'Ultra Deck: The Three Brothers', 'Super Rare · #ST13-008', 'Sabo (008)', '$0.77'],
]

save_to_csv('one_piece', x)
