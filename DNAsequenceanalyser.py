# *** DNA Sequence Analyser ***
# This program, is a tool designed for the analysis of DNA sequences. 
# It offers a range of functionalities, from basic nucleotide counting  
# to advanced sequence manipulation and trait prediction.

########### LIbraries, dictionaries, variables and functions ###########
import matplotlib.pyplot as plt
from colorama import Fore, Style

# Dictionary of genetic markers and their corresponding traits
genetic_markers = {
    "ATCG": "Blue eye color ",
    "CGAT": "Blonde hair color",
    "GATC": "Susceptibility to hair loss",
    "GCTA": "AB blood type",
    "TCGA": "Tall height",
    "GGTA": "Freckles",
    "CATG": "Susceptibility to Type 2 Diabetes"
}

# Defining menu with options available for the user to select.
menu = """\nHere are available options:
        1. Sequence length
        2. Nucleotide frequencies
        3. Segmenting the DNA
        4. Reverse complementation
        5. DNA Transcription
        6. Find specific pattern 
        7. Replace pattern in the sequence
        8. Identify genetic markers and predicts traits
"""

# This function calculates the length of the DNA sting using function len().
def calculate_sequence_length(dna_string):
    """
    Calculates length of DNA string.
    """
    return len(dna_string)

# This function counts frequency of each nucleotide in DNA string.
def nucleotide_frequency(dna_string):
    """
    This function counts the occurrences of A, C, G, and T in a DNA string.
    """
    frequency = {"A" : 0, "C" : 0, "G" : 0, "T" : 0}
    for base in dna_string:
        frequency[base] += 1
    return frequency

# This function creates bar chart of nucleotide frequencies in provided DNA string.
def plot_nucleotide_frequency(dna_string):
    frequency = nucleotide_frequency(dna_string)
    bases = list(frequency.keys())
    counts = list(frequency.values())
    plt.bar(bases, counts, color=['blue', 'orange', 'green', 'red'])
    plt.xlabel('Nucleotide')
    plt.ylabel('Frequency')
    plt.title('Nucleotide Frequency')
    plt.show()

# This function splits the DNA string into segments for more detailed analysis
def split_sequence(dna_string, marker):
    """
    Segments DNA string into sections by specified marker
    """
    segments = dna_string.split(marker)
    return segments

# This function performs DNA transcription which converts DNA sequence into its RNA equivalent (replaces T with U).
def transcribe(dna_string):
    """
    Converts DNA into RNA sequence.
    """
    return dna_string.replace('T', 'U')

# This function performs reverse complementation: iterates over the sequence in reverse order using slicing and each replaces each base in the original sequence with its complementary base.
def reverse_complement(dna_string):
    """
    Creates reverse complement DNA sequence.
    """
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    reverse_comp_seq = ''
    for base in dna_string[::-1]:
        reverse_comp_seq += complement[base]
    return reverse_comp_seq

# This function searches for patterns specified by user in the DNA sequence.
def find_pattern(dna_string, pattern):
    """
    Search for nucleotide pattern in DNA sequence.
    """
    if pattern in dna_string:
        return "Pattern {} found in provided DNA sequence".format(pattern)
    else:
        return "Pattern {} not found in provided DNA sequence".format(pattern)

# This function replaces specified nucleotide pattern in the sequence with new pattern provided by user
def replace_pattern(dna_string, old_pattern, new_pattern):
    """
    Replaces nucleotide pattern in DNA sequence.
    """
    return dna_string.replace(old_pattern, new_pattern)

# This function identifies genetic markers in the DNA sting and predicts traits
def predict_traits(dna_string):
    """
    Identifies genetic markers and predicts traits.
    """
    predicted_traits = []
    for marker, trait in genetic_markers.items():
        if marker in dna_string:
            predicted_traits.append(trait)
    return predicted_traits

# This function checks whether the input string consists only of the letters A, C, G, and T, and also checks if the input string is not empty.
# bool: True if the input string contains only A, C, G, and T and is not empty, False otherwise.
def validate_nucleotides(input_string):
    """
    Validates whether the input string consists only of the letters A, C, G, and T and if input is not empty.

    """
    valid_nucleotides = {'A', 'C', 'G', 'T'}
    return bool(input_string) and set(input_string).issubset(valid_nucleotides)

# This function will display the DNA sequence in colors. 
def display_colored_sequence(dna_sequence):
    """
    Displays the DNA sequence with each nucleotide in a different color.

    """
    for nucleotide in dna_sequence:
        if nucleotide == 'A':
            print(Fore.RED + nucleotide, end='')
        elif nucleotide == 'T':
            print(Fore.GREEN + nucleotide, end='')
        elif nucleotide == 'G':
            print(Fore.YELLOW + nucleotide, end='')
        elif nucleotide == 'C':
            print(Fore.BLUE + nucleotide, end='')
        else:
            print(nucleotide, end='')
    print(Style.RESET_ALL)  # Reset color after displaying the sequence


########### User Interface ###########

# Welcome message and program description
print("""
        Welcome to the DNA Sequence Analyser.
    This program is tailored to address a range of DNA sequence analysis tasks, 
    from basic nucleotide counting to advanced comparative genomics.

    Key features:

    - Sequence Input: \t\tEasily input DNA sequences via direct text entry.
    - Basic Sequence Analysis: \tObtain fundamental information such as sequence length, nucleotide frequencies with graphical representation of the data, segmenting the DNA.
    - Sequence Manipulation: \tPerform essential sequence manipulations including reverse complementation and transcription.
    - Sequence Search: \t\tSearch for specific patterns, replace nucleotide patterns in the sequence, match the pattern to known genetic markers and predict possible traits within DNA sequences. 
""")

# This loop will repeatedly prompt the user for input until a valid DNA sequence is entered
while True:
    # Prompts the user to enter a DNA sequence and convert it to uppercase
    dna_sequence = input("\nPlease enter DNA sequence you would like to analyse: ").upper()

    # Checks if input consists of A,C,G,T and is not empty
    if validate_nucleotides(dna_sequence):
        # If the input sequence contains only valid DNA letters, exit the loop
        break
    else:
        # If the input sequence contains invalid characters, print an error message
        print("\nInvalid DNA sequence. Please enter only letters A, T, G, and C.")

# Prints out the validated DNA sequence with colored nucleotides
print("\nThe entered DNA sequence is:")
display_colored_sequence(dna_sequence)

# Prints out the selection menu
print(menu)

# This loop asks the user to select a menu option, and it will run until 'q' is entered
while True:
    # Prompts the user to select a menu option
    menu_selection = input("Select an option by typing the corresponding number (1-8) or type 'q' to exit: ")

    # Checks if 'q' is entered to exit the program
    if menu_selection.lower().strip() == 'q':
        print("\nThank you for using DNA Analyser. Goodbye!")
        exit()  # Exits the program

    try:  # Attempts to convert entered value to an integer to ensure only valid numbers are entered
        option = int(menu_selection)
        
        # Checks if the entered option is within the range 1-8
        if 1 <= option <= 8:
            # Handles each menu option
            if option == 1:    # Calculates the length of the DNA sequence
                sequence_length = calculate_sequence_length(dna_sequence)
                print("\nLength of DNA sequence:", sequence_length)
            
            elif option == 2:    # Calculates frequency of each nucleotide in the DNA sequence
                nucleotide_frequency(dna_sequence)
                print(f"\nThe frequency of nucleotides in the DNA sequence: {nucleotide_frequency(dna_sequence)}")
                plot_nucleotide_frequency(dna_sequence)

            elif option == 3:    # Segments the DNA sequence based on provided nucleotide
                # This loop ensures that the user provides a valid nucleotide marker
                while True:
                    marker = input("\nPlease specify the nucleotide by which you want to segment the DNA sequence: ").upper()
                    # Checks if input consists of A, C, G, T and is not empty
                    if validate_nucleotides(marker):
                        segments = split_sequence(dna_sequence, marker)
                        print(f"\nSegments of the DNA sequence segmented by '{marker}' are:", segments)
                        break
                    else:
                        print("\nInvalid nucleotide. Please enter only letters A, C, G, and T.")

            elif option == 4:    # Reverse complement 
                reverse_comp_sequence = reverse_complement(dna_sequence)
                print("\nOriginal sequence:", dna_sequence)
                print("Reverse complement:", reverse_comp_sequence)

            elif option == 5:    # Transcribes DNA into RNA sequence
                rna_sequence = transcribe(dna_sequence)
                print("\nOriginal DNA sequence:", dna_sequence)
                print("Transcribed RNA sequence:", rna_sequence)

            elif option == 6:    # Searches for a specific pattern in the DNA sequence
                # This loop ensures that the user provides a valid nucleotide pattern
                while True:
                    pattern = input("\nPlease enter the nucleotide pattern you want to search for: ").upper()
                    # Checks if input consists of A, C, G, T and is not empty
                    if validate_nucleotides(pattern):
                        print(find_pattern(dna_sequence, pattern))
                        break
                    else:
                        print("\nInvalid nucleotide pattern. Please enter only letters A, C, G, and T.")

            elif option == 7:    # Replaces nucleotide pattern in the DNA sequence
                # This loop ensures that the user provides valid old and new nucleotide patterns
                while True:
                    old_pattern = input("\nPlease enter the old nucleotide pattern you want to replace: ").upper()
                    new_pattern = input("Please enter the new nucleotide pattern: ").upper()
                    # Checks if input consists of A, C, G, T and is not empty for both old and new patterns
                    if validate_nucleotides(old_pattern) and validate_nucleotides(new_pattern):
                        updated_sequence = replace_pattern(dna_sequence, old_pattern, new_pattern)
                        print("\nOriginal sequence:", dna_sequence)
                        print("Updated sequence:", updated_sequence)
                        break
                    else:
                        print("\nInvalid nucleotide pattern. Please enter only letters A, C, G, and T.")

            elif option == 8:    # Predicts traits based on the DNA sequence
                traits = predict_traits(dna_sequence)
                if traits:
                    print("\nPredicted traits based on sequence:", traits)
                else:
                    print("\nNo traits predicted based on the provided sequence.")

        else:
            print("\nInvalid selection. Please enter a number between 1 and 8 or 'q' to exit.")
    
    except ValueError:  # Handles all invalid input
        print("\nInvalid input. Please enter a valid number or type 'q' to exit.")



"""
Exmple DNA sequence:
dna_sequence = "ATCGTACGATCGATCGATCGTAGCTAGCTAGCTGCGCGCGCTAGCTAGCTAGCTAGCTAGCT"

After completing an operation, provide the user with clear prompts or options to either 
choose another operation or exit the program. 
This will enhance user experience and guide them through the process more effectively.


"""
