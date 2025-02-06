import pandas as pd
import os
import Levenshtein
from utils import clean_text, apostro_space, get_timestamp



# Set file path dynamically to ensure cross-platform compatibility
csv_path = os.path.join(os.path.dirname(__file__), 'sentences.csv')

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_path)

# List to hold all new rows
new_data_list = []

while True:
    # Prompt for user inputs
    user_input = input("Your sentence: ").strip()
    correct_input = input("Correct sentence: ").strip()

    u_i = user_input
    c_i = apostro_space(correct_input)
    u_i_c = clean_text(u_i)
    c_i_c = clean_text(c_i)

    # Append the new data to the list
    new_data_list.append({
        'user_input': u_i,
        'correct_input': c_i,
        'distance': Levenshtein.distance(u_i, c_i),
        'ratio': Levenshtein.ratio(u_i, c_i),
        'user_input_clean': u_i_c,
        'correct_input_clean': c_i_c,
        'distance_clean': Levenshtein.distance(u_i_c, c_i_c),
        'ratio_clean': Levenshtein.ratio(u_i_c, c_i_c),
        'timestamp': get_timestamp()
    })

    # Ask if the user wants to input more pairs
    continue_input = input("Do you want to enter another pair? (y/n): ").strip().lower()
    if continue_input != 'y':
        break

# Convert the list to a DataFrame and concatenate it with the existing DataFrame
new_data_df = pd.DataFrame(new_data_list)
df = pd.concat([df, new_data_df], ignore_index=True)


# Save the DataFrame to the CSV file
df.to_csv(csv_path, index=False)