import re
import os
import codecs
from bs4 import BeautifulSoup
fout = open ("url0.proc.txt", "w", encoding='utf-8')
def clean_html(html):
	"""
		Copied from NLTK package.
		Remove HTML markup from the given string.

		:param html: the HTML string to be cleaned
		:type html: str
		:rtype: str
	"""

	# First we remove inline JavaScript/CSS:
	cleaned = re.sub(r"(?is)<(script|style).*?>.*?(</\1>)", "", html.strip())
	# Then we remove html comments. This has to be done before removing regular
	# tags since comments can contain '>' characters.
	cleaned = re.sub(r"(?s)<!--(.*?)-->[\n]?", "", cleaned)
	# Next we can remove the remaining tags:
	cleaned = re.sub(r"(?s)<.*?>", " ", cleaned)
	# Finally, we deal with whitespace
	cleaned = re.sub(r"&nbsp;", " ", cleaned)
	cleaned = re.sub(r"  ", " ", cleaned)
	cleaned = re.sub(r"  ", " ", cleaned)

	#my addition to remove blank lines
	cleaned = re.sub("\n\s*\n*", "\n", cleaned)

	return cleaned.strip()


for filename in os.listdir(os.getcwd()):
        try:
                f=codecs.open(filename, 'r', 'utf-8')
                url = BeautifulSoup(f.read(), "html.parser").get_text()
                plaintext = fout.write(clean_html(url) + "\n\n")
        except UnicodeDecodeError as e:
                print("Error on html: %e" % str(e))
fout.close()        
