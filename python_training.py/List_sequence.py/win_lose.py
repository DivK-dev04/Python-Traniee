# r = ["W","L","W","W","L","W","W","W","L","L","L","L"]            How many time does W or L come continously an din what count

def find_longest_streak(r):
    max_streak = 0  # Keeps track of the longest streak
    current_streak = 1  # Keeps track of the current streak (starts at 1)
    longest_char = r[0]  # Stores the character with the longest streak

    for i in range(1, len(r)):
        if r[i] == r[i - 1]:
            current_streak += 1  # If the current element is the same as the previous, increase streak
        else:
            # If a new streak is starting, check if the current streak is the longest so far
            if current_streak > max_streak:
                max_streak = current_streak
                longest_char = r[i - 1]  # Set the character that has the longest streak
            current_streak = 1  # Reset the current streak

    # Final check after loop to account for the last streak
    if current_streak > max_streak:
        max_streak = current_streak
        longest_char = r[-1]  # Set the character for the last streak

    return longest_char, max_streak

# Example usage
r = ["W","L","W","W","L","W","W","W","L","L","L","L"]
longest_char, streak = find_longest_streak(r)
print(f"The longest continuous sequence is '{longest_char}' with a streak of {streak}.")