def main():
    with open("userInputFile.txt", "r") as f:
        userIn = f.read()
    lines = userIn.splitlines()

    columnNum = len(lines[0].split())
    columns = [[] for _ in range(columnNum)]

    for line in lines:
        values = line.split()
        for i, values in enumerate(values):
            columns[i].append(float(values))

    with open("outputFile.txt", "w") as f:
        for col in columns:
            f.write(str(col) + "\n")
            
if __name__ == "__main__":
    main()