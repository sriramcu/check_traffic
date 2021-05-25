import webbrowser
import os
import re

username_file = open("username.txt",'r')
username = username_file.read().strip()
username_file.close()

os.system("curl -s https://api.github.com/users/{}/repos | jq '.[]|.html_url'>repo_urls.txt".format(username))

urls_file = open("repo_urls.txt",'r')

lines = urls_file.read().split('\n')
lines = [x for x in lines if x.strip()!='']
urls_file.close()

url_re = re.compile(r'https://github.com/{}/(.*)"'.format(username))


repos = []

for line in lines:
    mo = url_re.search(line)
    repo = mo.group(1)
    repos.append(repo)


i=1
for repo in repos:
    url = 'https://github.com/{}/{}/graphs/traffic'.format(username,repo)
    webbrowser.get(using='google-chrome').open(url,new=i)
    i=2
    
