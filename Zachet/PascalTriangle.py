def pascals_row(rowIndex):
    row = [1]
    for _ in range(rowIndex):
        row = [1] + [row[i] + row[i+1] for i in range(len(row)-1)] + [1]
    return row

print(pascals_row(int(input())))