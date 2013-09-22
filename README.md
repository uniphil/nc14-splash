nc14-splash
===========

splash page (phase 1)

making it live:

there is a git remote (accra) on phil's computer notdeadyet.

the remote repo has to be switched off master first. this can be with a -b flag so the site doesn't die

`git checkout -b lookaway`

then from notdeadyet

`git push accra master`

then on accra

`git checkout master`


..

or, alternately, maybe a sequence like:

notdeadyet: `git checkout -b deploy`, `git push accra deploy`, `git checkout master`, `git branch -d deploy`

accra: `git merge deploy`, `git branch -d deploy`


..

decent chance the site does die when trying this.
