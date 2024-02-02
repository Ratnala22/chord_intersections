import itertools
import numpy as np

def calculate_chord_intersections(input_list):
    # Initialize a dictionary to store radian measures for each chord identifier
    chord_dict = {}
    radian_measures=list(input_list[0])
    chord_ids=list(input_list[1])
    # Populate the dictionary with radian measures for each chord
    for radian, identifier in zip(radian_measures, chord_ids):
        # Extract the unique identifier for the chord, excluding the 's' or 'e' prefix
        chord_key = identifier[1:]

        # Check if the chord identifier already exists in the dictionary
        if chord_key in chord_dict:
            # Append the current radian measure to the list and sort it for better comparison
            chord_dict[chord_key].append(radian % (2 * np.pi))
            chord_dict[chord_key].sort()
        else:
            # If the identifier is not in the dictionary, create a new entry with a list containing the current radian measure
            chord_dict[chord_key] = [radian % (2 * np.pi)]

    # Initialize a counter for intersections
    intersections_count = 0

    # Convert the dictionary values to a list for easier iteration
    chord_list = list(chord_dict.values())

    # Iterate through the list of chords to check for intersections
    for i, (start_1, end_1) in enumerate(chord_list):
        # Iterate through remaining chords to compare with the current chord
        for start_2, end_2 in chord_list[i+1:]:
            # Use XOR to check if the chords intersect
            if (start_1 < start_2 < end_1) ^ (start_1 < end_2 < end_1):
                # Increment the intersection counter if an intersection is found
                intersections_count += 1

    # Return the final count of chord intersections
    return intersections_count

if __name__ == "__main__":
  #test case 1:
  input_list=[(0.78, 1.47, 1.77, 3.92),('s0', 's1', 'e0', 'e1')]
  print(calculate_chord_intersections(input_list))
  #test case 2:

  
  