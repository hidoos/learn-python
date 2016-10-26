# TASK
#
# make the function query() below return:
# - a list of Links submitted by user 62443
# - sorted by ascending submission time

from collections import namedtuple

# make a basic Link class
Link = namedtuple('Link', ['id', 'submitter_id', 'submitted_time', 'votes',
                           'title', 'url'])

# list of Links to work with
links = [
    Link(1, 62443, 1333962645.0, 62443,
         "This explains why technical books are all ridiculously thick and overpriced",
         "http://prog21.dadgum.com/65.html"),
    Link(0, 62443, 1334014208.0, 62443,
         "C overtakes Java as the No. 1 programming language in the TIOBE index.",
         "http://pixelstech.net/article/index.php?id=1333969280"),
    ]
   

# links is a list of Link objects. Links have a handful of properties. For
# example, a Link's number of votes can be accessed by link.votes if "link" is a
# Link.

# make the function query() return a list of Links submitted by user 62443, by
# submission time ascending
def query():
    submissions = []
    new_r = []
    for item in links:
        if item.submitter_id == 62443:
            submissions.append(item)
    submissions.sort(key = lambda x:x.submitted_time)
    return submissions
print query()
    
