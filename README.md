# SANS-Index-Helper-Tool
Python command line tool used for generating GIAC Certification indexes. Provides a command line interface to create a SANS book index for your GIAC certification attempts.

## Usage and Requirements
The tool requires Python 2.7 at a minimal. To start the program, create a folder and place the script within. Run the script with the following syntax:
```
$ python sans_index_generator.py
```
## Instructions
On start, the tool will prompt you for the current book that you're studying. This will mark each new entry with a book number. If you want to switch books, exit out of the script and re-open.
```
-----------------------------------------------------------------------
|                    Cain's SANS Index Generator                      |
-----------------------------------------------------------------------
Please specify the current book that you are indexing (Ex. '542.2')
Current Book:
```
After a book has been specified, the tool will ask you to enter a topic keyword and its associated page number.
```
Please enter the page keyword(s) and then the page number(s) for each entry.
Type 'quit' or 'exit' to save progress, generate html file, and exit this script.

Enter topic keyword     : WebSocket, Implementation
Enter page number       : 139
Entry Added...
```
