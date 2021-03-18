You need to get the top k frequent words in given story.
1. Get the story (Alice’s Adventures in Wonderland): http://www.gutenberg.org/files/11/11-0.txt
(if you look at this in a browser you may need to enter to “Plain Text UTF-8 “tab but it should
work from python).
2. Collect The top k frequent words and save them into a csv file and a SQLite DB:
In each line the first element is the word (string) and the second is the count. for example (for k=3):

Word Count
word_1 word_1_count
word_2 word_2_count
word_3 word_3_count

implementation guidelines:

a. Add the ability to pass words to be ignore.
b. Clear-out stop words and punctuation marks.
c. Use a Lemmatizer.
d. Add code that logs the mean and the median of the word count.

Design guidelines:
• Make sure the design is flexible enough to handle additional storage options.
• Make the storage options configurable in a way they can be composed/chosen in a “simple” way.
• Make sure this code can be executed in bulk (for many text sources).
• Please do not reinvent the wheel.
Coding guidelines:
1. Try to write clear reusable code with short functions.
2. Use python 3.6 or above.
3. Submit the resulting for k=100.
4. Use type hint, even if it's not a must when using python.
Good luck!