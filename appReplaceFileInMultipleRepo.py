import git
import os
from shutil import copyfile

ms=["repoName"]
nodejs_lambda=["reponame"]

def processRepo(repoName, src):    
    # Check out via HTTPS
    git.Repo.clone_from('REPOURL'+repoName, repoName)
    repo = git.Repo(repoName)
    path = './'+ repoName
    owd = os.getcwd()
    os.chdir(path)
    print('printing current path')
    print(os.getcwd())

    # Create a new branch
    repo.git.branch('BRANCHNAME')

    # You need to check out the branch after creating it if you want to use it
    repo.git.checkout('BRANCHNAME')

    ##Copy Template
    #identify template location based on type
    #src = "C://Project//repo//delete//temp//config//ms//Jenkinsfile"
    dst = "C://Project//repo//delete//temp//" + repoName +"//Jenkinsfile"
    copyfile(src, dst)

    # List remotes
    print('Remotes:')
    for remote in repo.remotes:
        print(f'- {remote.name} {remote.url}')

    # Provide a list of the files to stage
    repo.index.add(['Jenkinsfile'])

    # Provide a commit message
    repo.index.commit('COMMIT MESSAGE')
    origin = repo.remote()
    repo.create_head('BRANCHNAME')
    # Push changes
    origin.push('BRANCHNAME')
    os.chdir(owd)

for x in ms: 
    print(x)
    #processRepo(x, "C://Project//repo//delete//temp//config//ms//Jenkinsfile")
    
for y in nodejs_lambda: 
    print(y)
    processRepo(y, "C://Project//repo//delete//temp//config//lambda//Jenkinsfile")
  

    