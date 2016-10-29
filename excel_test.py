# -*- coding: utf-8 -*-

import xlrd
import xlwt

def excel_test():
	open_book = xlrd.open_workbook('d:/test.xlsx')
	print(open_book.sheet_names())
	sheet1 = open_book.sheet_by_index(0)
	print(sheet1.nrows, sheet1.ncols)
	# sheet2 = open_book.sheet_by_name('Sheet2')
	# print(sheet2.ncols, sheet2.ncols)
	
	for i in range(sheet1.nrows):
		for j in range(sheet1.ncols):
			print(sheet1.cell(i, j).value, end = '| ')
		print('\n','-'*20)
	
	print(sheet1.merged_cells)  # read merged cells
	# read_merged_cell (row,row_end,col,col_end)  NOT include end
	for row, row_end, col, col_end in sheet1.merged_cells:
		print(sheet1.cell(row, col).value)


	write_book = xlwt.Workbook(encoding = 'utf-8')

	
	style = xlwt.XFStyle()
	# set font
	font = xlwt.Font()
	font.name = 'Times New Roman'
	font.height = 20 * 14 			# size = 14
	font.colour_index = 6   		# 0 = black, 1 = white, 2 = red, 3 = green, 4 = blue, 5 = yellow, 6 = magenta, 7 = cyan
	font.bold = False

	alignment = xlwt.Alignment()
	alignment.horz = xlwt.Alignment.HORZ_CENTER
	alignment.vert = xlwt.Alignment.VERT_CENTER
	# set style
	style.font = font
	style.alignment = alignment

	write_sheet1 = write_book.add_sheet('Sheet1')
	# write head
	for j in range(sheet1.ncols):
		write_sheet1.write(0, (j + 1) % sheet1.ncols, sheet1.cell(0,j).value, style)
		
	for row, row_end, col, col_end in sheet1.merged_cells:
		# write_merged_cell (row,row_end,col,col_end) include end
		write_sheet1.write_merge(row, row_end - 1,(col + 1) % sheet1.ncols,col_end % sheet1.ncols, sheet1.cell(row,col).value, style)
		for i in range(row, row_end):
			for j in range(col):
				write_sheet1.write(row + row_end - i - 1, j + 1, sheet1.cell(i,j).value, style)

	write_book.save('d:/test_rewrite.xls')

if __name__ == '__main__':
	excel_test()

