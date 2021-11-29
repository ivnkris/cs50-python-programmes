# Usage:
# python dna.py databases/large.csv sequences/5.txt
# Lavender

from csv import reader, DictReader
from sys import argv, exit


def main():
    # Check if number of command line arguments is 2
    if len(argv) != 3:
        # If not print an error message
        print("Usage: python dna.py databases/database.csv sequences/sequence.txt")
        exit(1)
    
    # Open the CSV file and read its contents into memory (name, STR sequences)
    with open(argv[1], "r") as csv_file:
        reader = DictReader(csv_file)
        people = list(reader)

    # Open the DNA sequence and read its contents into memory
    with open(argv[2], "r") as sequence_file:
        sequence = sequence_file.read()

    # For each of the STRs compute the longest run of consequtive repeats
    maximum_count = []
    
    # Loop through list of STRs
    for i in range(1, len(reader.fieldnames)):
        STR = reader.fieldnames[i]
        # Set maximum counts to zero
        maximum_count.append(0)
        
        # Loop through DNA sequence
        for j in range(len(sequence)):
            count = 0
            # if slice of sequence is a match with STR
            if sequence[j:(len(STR) + j)] == STR:
                position = 0
                # Count consequtive repeats
                while sequence[(j + position):(len(STR) + j + position)] == STR:
                    count += 1
                    position += len(STR)
                
                # if new highest count is found update maximum_count list
                if count > maximum_count[i - 1]:
                    maximum_count[i - 1] = count

    # If the STR counts match any individual in the CSV file print their name
    for i in range(len(people)):
        STR_match_count = 0
        for j in range(1, len(reader.fieldnames)):
            if int(maximum_count[j - 1]) == int(people[i][reader.fieldnames[j]]):
                STR_match_count += 1
            if STR_match_count == (len(reader.fieldnames) - 1):
                print(people[i]["name"])
                exit(0)

    # Else print "No match"
    print("No match")


if __name__ == "__main__":
    main()