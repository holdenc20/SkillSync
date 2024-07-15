import urllib.request, json
import time
import json

def get_branches_from_repository(owner, repository_name):
    with urllib.request.urlopen(f"https://api.github.com/repos/{owner}/{repository_name}/branches") as url:
        data = json.loads(url.read().decode())
    names = []

    for branch in data:
        names.append(branch["name"])

    return names


def get_commits_from_branch(owner, repository_name, branch_name, author_name):
    url = f"https://api.github.com/repos/{owner}/{repository_name}/commits?sha={branch_name}&author={author_name}"

    req = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(req) as url:
        data = json.loads(url.read().decode())

    commits = []

    for commit in data:
        changes = get_code(commit["url"])

        data = {'date': commit['commit']["author"]["date"],
                'url': commit["url"],
                'changes': changes
                }
        
        commits.append(data)

    return commits

def get_code(url):
    time.sleep(75)
    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())
    code_snippits = []

    data = data['files']

    changes = []

    count = 0
    
    for file in data:
        count+=1
        print(count)
        if file and 'patch' in file:
            change = {'filename': file['filename'], 'code': file['patch']}
            changes.append(change)

    return changes

if __name__ == "__main__":
    time.sleep(360)
    repo_owner  = "airspeedswift"
    repo_name   = "swift"
    branch      = "main"
    author_name = "benrimmington"

    all_commits = []
    
    for branch in get_branches_from_repository(repo_owner, repo_name):
        print(f"Branch {branch}:")
        commits = get_commits_from_branch(repo_owner, repo_name, branch, author_name)
        all_commits.append(commits)

    data = {'repo_name': repo_name, 'author_name': author_name, 'commits': all_commits}

    print(data)
    with open("test2.json", "w") as outfile:
        json.dump(data, outfile, indent=4)
