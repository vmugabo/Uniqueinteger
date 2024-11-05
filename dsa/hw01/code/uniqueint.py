import os
import re


class UniqueInt:
    def __init__(self):
        self.unique_integers = {}

    def processFile(self, inputFilePath, outputFilePath):

        with open(inputFilePath, 'r') as file:
            for line in file:
                self.readNextItemFromFile(line)

        sorted_unique_integers = self.sort_integers(
            self.unique_integers.keys())
        with open(outputFilePath, 'w') as output_file:
            for integer in sorted_unique_integers:
                output_file.write(f"{integer}\n")

    def readNextItemFromFile(self, line):

        line = line.strip()
        if re.fullmatch(r'-?\d+', line):
            integer = int(line)
            if integer not in self.unique_integers:
                self.unique_integers[integer] = True

    def sort_integers(self, integers):
        sorted_integers = list(integers)
        for i in range(len(sorted_integers)):
            for j in range(i + 1, len(sorted_integers)):
                if sorted_integers[i] > sorted_integers[j]:
                    sorted_integers[i], sorted_integers[j] = sorted_integers[j], sorted_integers[i]
        return sorted_integers


input_folder = "dsa\hw01\sample_inputs"
output_folder = "dsa\hw01\sample_results"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for input_file in os.listdir(input_folder):
    if input_file.endswith(".txt"):
        input_path = os.path.join(input_folder, input_file)
        output_file = input_file.replace(".txt", "_results.txt")
        output_path = os.path.join(output_folder, output_file)

        unique_int_processor = UniqueInt()
        unique_int_processor.processFile(input_path, output_path)
print('-----Program Complete -----')
