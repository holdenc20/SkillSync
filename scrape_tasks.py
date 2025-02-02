import urllib.request, json
import time

if __name__ == "__main__":
    repo_owner  = "airspeedswift"
    repo_name   = "swift"
    url = f"https://api.github.com/search/issues?q=repo:{repo_owner}/{repo_name}+state:open"

    req = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(req) as url:
        data = json.loads(url.read().decode())

    tasks = []

    for row in data:
        tasks.append(row)

    with open("tasks.json", "w") as outfile:
        json.dump(tasks, outfile, indent=4)


    

