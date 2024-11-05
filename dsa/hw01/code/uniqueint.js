const fs = require('fs');
const path = require('path');

class UniqueInt {
    constructor() {
        this.uniqueIntegers = new Set();
    }

    readFromFile(line) {
        line = line.trim();
        if (line === "") {
            return null;
        }

        const parts = line.split(/\s+/); 
        if (parts.length !== 1) {
            return null;
        }
        
        const number = parseInt(parts[0], 10);
        return isNaN(number) ? null : number; 
    }

    processFile(inputFilePath, outputFilePath) {
        const data = fs.readFileSync(inputFilePath, 'utf8').split('\n');
        data.forEach(line => {
            const number = this.readFromFile(line);
            if (number !== null) {
                this.uniqueIntegers.add(number);
            }
        });

        const sortedUniqueIntegers = Array.from(this.uniqueIntegers).sort((a, b) => a - b);
        fs.writeFileSync(outputFilePath, sortedUniqueIntegers.join('\n') + '\n');
        this.uniqueIntegers.clear();
    }
}


const inputDir = path.join('dsa', 'hw01', 'sample_inputs');
const outputDir = path.join('dsa', 'hw01', 'sample_results');


fs.readdir(inputDir, (err, files) => {
    if (err) {
        console.error(`Error reading directory: ${err.message}`);
        return;
    }

    files.forEach(filename => {
        if (filename.endsWith(".txt")) {
            const inputFile = path.join(inputDir, filename);
            const outputFile = path.join(outputDir, `${filename}_results.txt`);
            
            const uniqueIntProcessor = new UniqueInt();
            uniqueIntProcessor.processFile(inputFile, outputFile);
            console.log(`Processed ${filename} -> ${outputFile}`);
        }
    });
});
