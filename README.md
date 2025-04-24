# NLP Summary Project
Goal of project is a summarization of given text. Extracts text from a 'docx', 'pdf', or 'txt' file and writes a summary to a new file.

To run:
Install dependencies 'pip install transformers torch python-docx pdfplumber'
call file in terminal using 'python summarize.py filename.extension --model MODEL --max_length MAX_LENGTH --min_length MIN_LENGTH'

Optional arguments:
filename.extension is any file the program can read (txt, docx, pdf) 
--model MODEL where MODEL is the name of the LLM used for summarization (default facebook/bart-large-cnn)
--max_length MAX_LENGTH where MAX_LENGTH is the maximum word length of the summary (default 130)
--min_length MIN_LENGTH where MIN_LENGTH is the minimum word length of the summary (default 30)

examples: 
'python summarize.py notes.docx --model google/pegasus-xsum --max_length 100 --min_length 20'

or

'python summarize.py path/to/file.pdf'


Main() parses given arguments and sorts them into appropriate places.
get_file_contents() is called and gets the file extension and opens the file, extracting is contents and adding it to a variable
the file contents are then added to the summarize_text() arguments along with the parsed user input arguments
summarize_text() uses a pipeline on the given text with an LLM to summarize the text
the summarized text is then written to a txt file 'summary_yourFile.txt'

DEMO: https://youtu.be/P9wL3mgWe2E

Author: drv180000