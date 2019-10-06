# import xlsxwriter module
import xlsxwriter

workbook = xlsxwriter.Workbook('Example3.xlsx')

# By default worksheet names in the spreadsheet will be
# Sheet1, Sheet2 etc., but we can also specify a name.
worksheet = workbook.add_worksheet("My sheet")

# Some data we want to write to the worksheet.
scores = (
    ['ankit', 1000],
    ['rahul', 100],
    ['priya', 300],
    ['harshita', 50],
)

# Start from the first cell. Rows and
# columns are zero indexed.
row = 0
col = 0

# Iterate over the data and write it out row by row.
for name, surname, phone, nickname in (scores):
    worksheet.write(row, col, name)
    worksheet.write(row, col + 1, surname)
    worksheet.write(row, col + 2, phone)
    worksheet.write(row, col + 3, nickname)
    row += 1

workbook.close()