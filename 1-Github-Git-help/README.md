# Git & Github 

Git is a version control system that lets you manage and keep track of your source code history. 
GitHub is a cloud-based hosting service that lets you manage Git repositories.

Basically, Git will help to make local repository on laptop/pc & also to send data to cloud i.e github 

### Remember these all you have to do first time after creation you need to only last three commands :)
First, Download GIT [Click Here](https://git-scm.com/downloads)  & install it
-----------------------------------------------------------------------------

You might need to login,
Open a terminal/shell and type:

**git config --global user.name "Your name here"**  
**git config --global user.email "your_email@example.com"**  

------------------------------------------------------------
Now, Follow me -> 

Make a new folder on your pc/laptop -> Right Click -> Select GitBash

![alt text](https://github.com/Ratndeepk/Competitive-Programming/blob/master/1-Github-Git-help/0.png?raw=true)


First Command -> **git init**  
This command will make a local repo in that folder  
---------------------------------------------------
![alt text](https://github.com/Ratndeepk/Competitive-Programming/blob/master/1-Github-Git-help/1.png?raw=true)

Second Command -> **git remote add origin https://github.com/Ratndeepk/Competitive-Programming.git** 
* This will connect your repo with this vary repo! 

Third Command -> **git pull origin master** 
* This will download everything from that repo

![alt text](https://github.com/Ratndeepk/Competitive-Programming/blob/master/1-Github-Git-help/2.png?raw=true)

(Now if you open folder you'll find everything copied from repo!) 
------------------------------------------------------------------
Now, You can add your folder (remember empty folder are not visible on github) add your programs. 
-------------------------------------------------------------------------------------------------
![alt text](https://github.com/Ratndeepk/Competitive-Programming/blob/master/1-Github-Git-help/4.png?raw=true)

Last but not the least!
You gotta do this everytime so learn it! 
* First Command **git add .**   (This will add all new changes to local repo) 
----------------------------------------------------------------------------
* Second command **git commit -m "Your Comment"** (This will finalize your commit)
--------------------------------------------------------------------------------
* Last Command   
When pushing first time -> **git push -u origin master**      
After first push is happened -> **git push**  
--------------------------------------------------------------------------------
![alt text](https://github.com/Ratndeepk/Competitive-Programming/blob/master/1-Github-Git-help/5.png?raw=true)