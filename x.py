# Script to clean up requirements.txt by removing Conda-managed packages
input_file = "requirements.txt"
output_file = "requirements1.txt"

with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for line in infile:
        if "file:///" not in line:  # Skip Conda-managed packages
            outfile.write(line)

print(f"Cleaned requirements saved to {output_file}")
