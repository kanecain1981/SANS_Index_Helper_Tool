# SANS-Index-Helper-Tool
Python command line tool used for generating GIAC Certification book indexes. Provides a command line interface to create a SANS book index for your GIAC certification attempts. This is a simpler evolution of Matthew Toussain's tool at https://github.com/0sm0s1z/Xenocrates.
## Usage and Requirements
The tool requires Python 2.7 at a minimal. To start the program, create a folder and place the script within. Run the script with the following syntax:
```
$ python sans_index_generator.py
```
## Purpose
From experience, I've noticed that a GIAC index needs to be light and easy to use. On average, you will have 1:00-2:00 minutes to answer each question on the tests. This tool allows you to create a basic index that is more than sufficient for use. An index that is too verbose can lead to longer lookup times resulting in test time loss. Nothing replaces knowing the material, but a good index can allow you to quickly search for information if needed.
On start, the tool will prompt you for the current book that you're studying. This will mark each new entry with a book number. If you want to designate a new book, exit out of the script and re-open, specifying the new book. This will prevent you from having to type the book number for all 200 pages of a SANS book (trust me, typing '560.1' 200 times gets old).
## Instructions
```
-----------------------------------------------------------------------
|                        SANS Index Generator                         |
-----------------------------------------------------------------------
Please specify the current book that you are indexing (Ex. '542.2')
Current Book:
```
After a book has been specified, the tool will ask you to enter a topic keyword and its associated page number. 
```
Please enter the book page keyword(s) and then the page number(s) for each entry.
Type 'quit' or 'exit' to save progress, generate html file, and exit this script.

Enter topic keyword(s)  : WebSocket, Implementation
Enter page number(s)    : 139
Entry Added...

Enter topic keyword     :
```
After pressing Enter, the entry will be added and the tool prompts for another entry. This is an infinite loop that can be closed by typing 'exit' or 'quit' at the keyword prompt. This action will save the data file (CVS format) and generate an html file from the data file.
## Data File
This is the CSV file generated from your data input. Keep a backup of this file just in case, as it holds all of your data. Here is an example of what the file looks like:
The tab seperated values are 'keyword', 'book#', 'page#'.
```
DNS	542.1	33
DNS - Reverse Scan	542.1	36
DNS - Brute Force	542.1	37
DNS - Recon Tools	542.1	38
```
## HTML File
The HTML file can be opened with the browser of your choice. From here, you can print your index as a single column data string, or you can copy and paste the data into a word processor (preserving the colors) and convert it into a two column document for a more professional appearance.

