import os
import shutil

# this code assume that you have 6 teams
t1 = [19033380,19025376,19004781,19020303]
t2 = [19004457,19008424,19042545,19024292]
t3 = [19032208,19040408,18044455,19045784]
t4 = [19034097,19020844,16042230,19007556]
t5 = [19047241,19016011,19046696,19037610]
t6 = [19030685,19031965,19032275,19047433]

# if you only have 5 teams, you can remove t6
students = [t1, t2, t3, t4, t5, t6]

files = os.listdir('.')

# Remove empty folder
for afile in files:
   #check that the file is a directory
   if os.path.isdir(afile):
      #remove directory, only empty directory can be removed, which is our intention
      try:
         os.rmdir(afile)
      except OSError:
         pass

# Create Team Folder
for i in range(1, 7): # change to 6 if you only have 5 teams
   filename = "Team " + str(i)
   if not os.path.exists (filename):
      os.mkdir(filename)

# Copy folder
count = 1
for tt in students:
    for t in tt:
        t = str(t)

        for f in files:
           if f.find(t) != -1:
              t = f
        
        if os.path.exists(t):
            desc = 'Team ' + str(count) + '/' + t + '/'
            print (desc)
            if not os.path.exists(desc):
                shutil.copytree(t, desc)

        # remove student folder
        if os.path.exists(t):
            shutil.rmtree(t)

    count += 1
