# -*- coding: utf-8 -*-
import operator

def main():
	index = []
	keyword_main = []
	book = []
	page = []
	
	print "-----------------------------------------------------------------------"
	print "|                        SANS Index Generator                         |"
	print "-----------------------------------------------------------------------"
	print "Please specify the current book that you are indexing (Ex. '542.2')"
	working_book = raw_input("Current Book: ")
	print "Please enter the book page keyword(s) and then the page number(s) for each entry."
	print "Type 'quit' or 'exit' to save progress, generate html file, and exit this script.\n"

	with open('index.html', 'w') as file:
		file.write("<style>.title{color: black;font-weight: bold;}</style>\n")
		file.write("<style>.topic{color: blue;font-weight: bold;}</style>\n")
		file.write("<style>.command{color: red;font-weight: bold;}</style>\n\n")
	
	while True:
		keyword = ''
		keyword = raw_input('Enter topic keyword(s)	: ')
		if keyword == 'quit':
			break
		elif keyword == 'exit':
			break
		
		insert_book = str(working_book).strip()
		insert_page = raw_input('Enter page number(s)	: ')
		
		line = keyword + '\t' + insert_book + '\t' + insert_page
		
		with open('data_file', 'a') as output_file:
			output_file.write(line)
			output_file.write('\n')
		
		print 'Entry Added...\n'
	
	with open('data_file', 'r') as out_file:
		for line in out_file:
			line_list = line.strip().split('\t')
			keyword_list = line_list[0].split(' ')
			keyword_list[0] = keyword_list[0].capitalize()
			keyword_list = ' '.join(keyword_list)
			keyword_main.append(keyword_list)
			book.append(line_list[1])
			page.append(line_list[2])

	items = len(keyword_main)
	i = 0
	while items > 0:
		index.append([keyword_main[i], book[i], page[i]])
		i += 1
		items -= 1

	pos = 0
	sorted_list = sorted(index, key=operator.itemgetter(0))

	with open('index.html', 'a') as file:
		for item in sorted_list:
			key = item[0].strip('"').rstrip('"')

            # Create Section Header
			if key.startswith("A"):
				if pos == 0:
					file.write("<span class = 'title'>A</span><br>\n")
					pos = 1
			elif key.startswith("B"):
				if pos != 2:
					file.write("<br><span class = 'title'>B</span><br>\n")
					pos = 2
			elif key.startswith("C"):
				if pos != 3:
					file.write("<br><span class = 'title'>C</span><br>\n")
					pos = 3
			elif key.startswith("D"):
				if pos != 4:
					file.write("<br><span class = 'title'>D</span><br>\n")
					pos = 4
			elif key.startswith("E"):
				if pos != 5:
					file.write("<br><span class = 'title'>E</span><br>\n")
					pos = 5
			elif key.startswith("F"):
				if pos != 6:
					file.write("<br><span class = 'title'>F</span><br>\n")
					pos = 6
			elif key.startswith("G"):
				if pos != 7:
					file.write("<br><span class = 'title'>G</span><br>\n")
					pos = 7
			elif key.startswith("H"):
				if pos != 8:
					file.write("<br><span class = 'title'>H</span><br>\n")
					pos = 8
			elif key.startswith("I"):
				if pos != 9:
					file.write("<br><span class = 'title'>I</span><br>\n")
					pos = 9
			elif key.startswith("J"):
				if pos != 10:
					file.write("<br><span class = 'title'>J</span><br>\n")
					pos = 10
			elif key.startswith("K"):
				if pos != 11:
					file.write("<br><span class = 'title'>K</span><br>\n")
					pos = 11
			elif key.startswith("L"):
				if pos != 12:
					file.write("<br><span class = 'title'>L</span><br>\n")
					pos = 12
			elif key.startswith("M"):
				if pos != 13:
					file.write("<br><span class = 'title'>M</span><br>\n")
					pos = 13
			elif key.startswith("N"):
				if pos != 14:
					file.write("<br><span class = 'title'>N</span><br>\n")
					pos = 14
			elif key.startswith("O"):
				if pos != 15:
					file.write("<br><span class = 'title'>O</span><br>\n")
					pos = 15
			elif key.startswith("P"):
				if pos != 16:
					file.write("<br><span class = 'title'>P</span><br>\n")
					pos = 16
			elif key.startswith("Q"):
				if pos != 17:
					file.write("<br><span class = 'title'>Q</span><br>\n")
					pos = 17
			elif key.startswith("R"):
				if pos != 18:
					file.write("<br><span class = 'title'>R</span><br>\n")
					pos = 18
			elif key.startswith("S"):
				if pos != 19:
					file.write("<br><span class = 'title'>S</span><br>\n")
					pos = 19
			elif key.startswith("T"):
				if pos != 20:
					file.write("<br><span class = 'title'>T</span><br>\n")
					pos = 20
			elif key.startswith("U"):
				if pos != 21:
					file.write("<br><span class = 'title'>U</span><br>\n")
					pos = 21
			elif key.startswith("V"):
				if pos != 22:
					file.write("<br><span class = 'title'>V</span><br>\n")
					pos = 22
			elif key.startswith("W"):
				if pos != 23:
					file.write("<br><span class = 'title'>W</span><br>\n")
					pos = 23
			elif key.startswith("X"):
				if pos != 24:
					file.write("<br><span class = 'title'>X</span><br>\n")
					pos = 24
			elif key.startswith("Y"):
				if pos != 25:
					file.write("<br><span class = 'title'>Y</span><br>\n")
					pos = 25
			elif key.startswith("Z"):
				if pos != 26:
					file.write("<br><span class = 'title'>Z</span><br>\n")
					pos = 26

			if item[0] != "":
				file.write("<br><span class = 'topic'>%s </span><i>[book: %s / page(s): %s]</i><br>\n"
							% (item[0].strip('"').rstrip('"'), item[1], item[2]))
			else:
				pass


if __name__ == "__main__":
    main()

