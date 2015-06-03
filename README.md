# fabric-deploy
Fabric deploy and archiving of projects

This fab task backsup a project and database and pushes it to glacier.

The db server is a remote db server, hence the ssh connection to retrieve the database.

You will need to have glacier-cmd configured to push to your archive.

I run this on my local machine
`fab -H my.server.com back_up`

#Still to do :
fab deploy task
-clone git repo to production
-symlink
-create database and dbuser
-run migrations



