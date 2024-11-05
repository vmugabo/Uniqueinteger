import os


class UniqueInt:
    def __init__(self):
        self.unique_integers = set()

    def readFromFile(self, line):

        line = line.strip()
        if line == "":
            return None

        parts = line.split()
        if len(parts) != 1:
            return None
        try:
            number = int(parts[0])
            return number
        except ValueError:
            return None

    def processFile(self, inputFilePath, outputFilePath):
        with open(inputFilePath, 'r') as infile:
            for line in infile:
                number = self.readFromFile(line)
                if number is not None:
                    self.unique_integers.add(number)

        with open(outputFilePath, 'w') as outfile:
            for num in sorted(self.unique_integers):
                outfile.write(f"{num}\n")
        self.unique_integers.clear()


input_folder = 'dsa\hw01\sample_inputs'
output_folder = 'dsa\hw01\sample_results'


for filename in os.listdir(input_folder):
    if filename.endswith(".txt"):
        input_file = os.path.join(input_folder, filename)
        output_file = os.path.join(output_folder, f"{filename}_results.txt")

        unique_int_processor = UniqueInt()
        unique_int_processor.processFile(input_file, output_file)
        print(f"Processed {filename} -> {output_file}")
