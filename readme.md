### Personal Flask Website

### virtualenv setup:

$ virtualenv -p python3 .

$ pip3 install -r requirements.txt

Then:

$ source bin/activate


### Running the web app with Docker Compose:

To run the web app, simply do:

$ docker-compose up

in the directory containing the docker compose yaml file.

You can then see the web app at:
http://0.0.0.0:8000
or:
http://localhost:8000/

### Cloning this project with all submodules

Follow the recommendations on the Git official documentation:

https://git-scm.com/book/en/v2/Git-Tools-Submodules

For the impatient, you can do the following when checking
out this main project:

$ git clone --recurse-submodules git@github.com:joshuamhtsang/personal_flask_website.git
