import requests
import json
import os
from subprocess import call, Popen, PIPE

def fake_repository(url):
    print("Faking " + url)
    git_url = 'https://github.com/scarlett1130/' + url + '.git'

    # os.system('git clone ' + git_url) # clone
    os.chdir(url)
    os.system('git branch -M main')
    os.system("""
                git filter-branch -f --env-filter \
                    "GIT_AUTHOR_NAME='scarlett1130'\
                     GIT_AUTHOR_EMAIL='businessx.free2000@gmail.com'\
                     GIT_COMMITTER_NAME='scarlett1130'\
                     GIT_COMMITTER_EMAIL='businessx.free2000@gmail.com'\
                     " HEAD\
                """)
    os.system('git push --force --set-upstream origin main')
    os.chdir('../')

    print("Success fake " + url)

def push_repository(url):
    print("Pushing " + url)
    os.chdir(url)
    os.system('git push --force --set-upstream origin main')
    os.chdir('../')

    print("Success push " + url)

if __name__ == '__main__':
    #response = requests.get('https://api.github.com/users/scarlett1130/repos')
    #repositories = json.loads(response.text)

    f = open("need_unfork.txt", "r", encoding='utf8')
    repositories = f.readlines()

    print(repositories)
    for repo in repositories:
        url_list = repo.split("scarlett1130/")
        url = url_list[1].replace("\n", "")
        fake_repository(url)
        # push_repository(url)

    f.close()