import os
from random import randint

github_username = os.getenv("GITHUB_USERNAME")
github_token = os.getenv("GITHUB_TOKEN")

if not github_username or not github_token:
    print("GitHub credentials not found. Please set the GITHUB_USERNAME and GITHUB_TOKEN environment variables.")
    exit(1)

repository_url = "https://" + github_username + ":" + github_token + "@github.com/frankyiga/con.git"

for i in range(1, 365):
    for j in range(0, randint(1, 10)):
        d = str(i) + ' days ago'
        with open('file.txt', 'a') as file:
            file.write(d)
        os.system('git add .')
        os.system(f'GIT_AUTHOR_DATE="{d}" GIT_COMMITTER_DATE="{d}" git commit -m "commit"')
        os.system(f'git push {repository_url} main')

