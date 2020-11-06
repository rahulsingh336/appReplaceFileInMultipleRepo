import git
import os
from shutil import copyfile

ms=["repoName"]
nodejs_lambda=["reponame"]

def processRepo(repoName, src):    
    # Check out via HTTPS
    git.Repo.clone_from('https://github.com/nice-cxone/'+repoName, repoName)
    repo = git.Repo(repoName)
    path = './'+ repoName
    owd = os.getcwd()
    os.chdir(path)
    print('printing current path')
    print(os.getcwd())

    # Create a new branch
    repo.git.branch('UH-10393')

    # You need to check out the branch after creating it if you want to use it
    repo.git.checkout('UH-10393')

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
    repo.index.commit('https://tlvjira02.nice.com/browse/UH-10393 Updated jenkins file')
    origin = repo.remote()
    repo.create_head('UH-10393')
    # Push changes
    origin.push('UH-10393')
    os.chdir(owd)

for x in ms: 
    print(x)
    #processRepo(x, "C://Project//repo//delete//temp//config//ms//Jenkinsfile")
    
for y in nodejs_lambda: 
    print(y)
    processRepo(y, "C://Project//repo//delete//temp//config//lambda//Jenkinsfile")
  

    