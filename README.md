# Important notes for Django Projects
1. Open terminal and create a folder to store the project (e.g. Code/SDGKU/blog)
2. Move to the respective folder (make sure you are on the right location)
3. Create a virtual environment (python3 -m venv venv)
4. Install django (pip3 install django)
5. Save dependencies into requirements.txt file (pip3 freeze > requirements.txt) 
6. Create the project (django-admin startproject config .)
7. Create the respective structure
    - Create the static, templates, img, css, js folders -> mkdir command
    - Create the .gitignore, README.md (optional)  -> touch command
# Additional notes
- All of the subcommands for django are going to called followed by python3 manage.py (e.g. python3 manage.py runserver, python3 manage.py migrate...)
- If we want to check the full list, we can run python3 manage.py
- To create an app we need to run "python3 manage.py startapp NAME_OF_THE_APP" (remember to change NAME_OF_THE_APP for the actual name)    