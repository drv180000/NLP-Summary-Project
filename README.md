# NLP Summary Project
Goal of project is a summarization of given text. Extracts text from a file and writes a summary to a new file.

To use:
call file in terminal using "python summarize.py filename.extension --model MODEL --max_length MAX_LENGTH --min_length MIN_LENGTH"

filename.extension is any file the program can read (txt, docx, pdf) 
--model MODEL where MODEL is the name of the LLM used for summarization
--max_length MAX_LENGTH where MAX_LENGTH is the maximum word length of the summary
--min_length MIN_LENGTH where MIN_LENGTH is the minimum word length of the summary


Main() parses given arguments and sorts them into appropriate places.
get_file_contents() is called and gets the file extension and opens the file, extracting is contents and adding it to a variable
the file contents are then added to the summarize_text() arguments along with the parsed user input arguments
summarize_text() uses a pipeline on the given text with an LLM to summarize the text
the summarized text is then written to a txt file

DEMO: https://youtu.be/P9wL3mgWe2E
