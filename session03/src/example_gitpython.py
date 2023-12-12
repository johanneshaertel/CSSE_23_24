import git
from datetime import datetime

# This feels like a good tutorial:
# https://gitpython.readthedocs.io/en/stable/tutorial.html

repo = git.Repo("temp/jjwt")
revisions = list(repo.iter_commits())

# This is an example how the list of revisions in the readme was generated.
i = 0
for revision in revisions:
    i += 1
    if i % 51 == 0:
        time = revision.committed_date
        formatted_time = datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')
        author = revision.author

        print("| " + str(revision) + " |" + str(formatted_time) + " | " + str(author) + " |")
