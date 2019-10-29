## Ikerriz Blog
## Description
This is a web application that allows users to  post their blogs. They they have create an account then log in to start creating blogs of their choice

### By IKERRIZ
The user can:

* See various blog posts
* View blogposts they like
* See the latests posts
* Subscribe to latest post service
* Generate quotes from various historic people e.g martin king luther jnr.
## Setup/Installation Requirements
* python3.6
* pip
* Virtual environment(virtualenv)
## Cloning and running
Clone the application using git clone(this copies the app onto your device). In terminal:

    *  $ git clone https://github.com/IKERRIZ/blog
    * $ cd blog
Creating the virtual environment

   *  $ python3.6 -m venv --without-pip virtual
   * $ source virtual/bin/env
   * $ curl https://bootstrap.pypa.io/get-pip.py | python
Installing Flask and other Modules

   * $ python3.6 -m pip install Flask
   * $ python3.6 -m pip install Flask-Bootstrap
   * $ python3.6 -m pip install Flask-Script
   * $ python3.6 -m pip install -r requirements.txt
   * $ python3.6 -m pip install flask-login
Run the application:

  *  $ chmod a+x start.sh
  *  $ ./start.sh
## Testing the Application
To run the tests for the class files:

  *  $ python3.6 manage.py test
## Technologies Used
* Python 3.6
* Flask
## Live link
https://usher54.herokuapp.com/
## Specifications
|Behaviour       | Input        | Output             |
|----------------|--------------|--------------------|
|Display latest blogs|	On page load|A 	list of various blogs appears|
|Registration |	Submit regitration form|	User creates an account and receives welcome email|
|Edit posts |	Submit edit post|	The post is updated with new data from user|
|New Quotes	 |Click new quotes	|it takes you to another page with random quotes|
|Adding comments|	Click create comment|	Comment is ceated|
 ## Support and contact details

For any questions or contributions, find me on:

Email: okothfaith94@gmail.com

## License
MIT License Copyright (c) {2019} ikerriz