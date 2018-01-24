### READING EXCEL FILES WITH XLRD ###

import xlrd     
# the 'rd' stands for 'read only', there is also a module 'wt' that allows you to write files

# Example parsing:

datafile = 'file_name.xls'

def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)     # opens the xls file
    sheet = workbook.sheet_by_index(0)      # specifies which excel 'sheet' within the file you want to work with
    # note: xlrd is 0-based indexing, i.e. the first sheet is at index = 0

    # 'list comprehension': loop through all the rows and col's and read all of the data into a structured Python list
    data = [
    [sheet.cell_value(r,col) 
    for col in range sheet.ncols()] 
    for r in range sheet.nrows()
    ]

    return data


# Here are some useful functions in the 'xlrd' module along with a brief description:

sheet.nrows     # returns the number of rows
sheet.ncols     # returns the number of columns
sheet.cell_type(3,2)    # returns the TYPE of the data in row 3, column 2
sheet.cell_value(4,7)   # returns the VALUE in the cell at row 4, column 7
sheet.col_values(3, start_rowx=1, end_rowx=5)   # returns a slice of the values in col 3 from row 1 to row 4
xlrd.xldate_as_tuple(excel_date, 0)     # returns a Python datetime tuple from the floating point date 'excel_date'
