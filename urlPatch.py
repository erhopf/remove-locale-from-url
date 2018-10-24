#!/usr/bin/env python

# This simple script iterates through the current folder, searching all markdown
# files for a URL pattern that includes a country code, such as en-usself.
# Each instance is listed in terminal along with the offending file.
# Currently, the script contains basic logic to replace all instances with the
# correct URL pattern. However, currently it doesn't discriminate between links
# and URL patterns included in your code samples. For instance, if a Ruby
# quickstart includes a samples response with URLs that include the country code
# these will also be changed.

import sys, os, re

def findBadUrl():
    regex = re.compile(r'http[s]?:\/\/docs.microsoft.com\/[A-Za-z]{2}-[A-Za-z]{2}\/', re.M)
    for filename in os.listdir(os.getcwd()):
        if filename.endswith('.md'):
            file = open(filename, 'r')
            text = file.read()
            matches = regex.findall(text)
            matchCount = len(matches)
            print "\n%s contains %d offending URLs." % (filename, matchCount)
            print "Matches: \n", matches
            file.close()

def findReplace():
    while True:
        try:
            selection = raw_input("\nWould you like to fix these links now? (y/n): ").lower()
            if selection in ["y", "yes", "n", "no"]:
                break
        except 'incorrect':
            pass
        print "\n##############################################"
        print selection + " is not a valid selection. Try again."
        print "##############################################\n"
    if selection in ["y", "yes"]:
        print "\n##############################################"
        print "Hold please. Attempting to correct bad links."
        print "##############################################\n"
        for filename in os.listdir(os.getcwd()):
            if filename.endswith('.md'):
                file = open(filename, 'r')
                text = file.read()
                file.close()
                file = open(filename, "w")
                file.write(re.sub(r'http[s]?:\/\/docs.microsoft.com\/[A-Za-z]{2}-[A-Za-z]{2}\/', 'https://docs.microsoft.com/', text))
                file.close()
        print "\n\nScript successfully run.\n\n"
        findBadUrl()
    else:
        print "\n##############################################"
        print "Exiting the program. See ya later!"
        print "##############################################\n"
        exit()

if __name__ == "__main__":
    findBadUrl()
    findReplace()
