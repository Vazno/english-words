'''Generates letter frequency json file.'''
import json
from collections import Counter
from re import sub
from os import path


ROUND_NUM = 20
RE_FILTER = r"[\d]|[\W]" # Deletes digits, and punctuation
LANG_FILE = path.join(path.dirname(path.realpath(__file__)), "en.txt")
FREQUENCY_FILE = "frequency.json"

def percentage(part, whole):
	percentage = 100 * float(part)/float(whole)
	return percentage

def main(file):
	with open(file, "r") as f:
		text = sub(RE_FILTER, "", f.read())

	c = Counter(text)
	most_common = c.most_common()
	total = c.total()

	percentages = dict()
	for char, occurrence in most_common:
		percentages[char] = round(percentage(occurrence, total), ROUND_NUM)

	with open(FREQUENCY_FILE, "w") as f:
		json.dump(percentages, f, indent=4)

if __name__ == "__main__":
	main(LANG_FILE)