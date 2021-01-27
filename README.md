# Gallery
A web app that allows users to get feedback on their projects. This will allow users to learn where they need to improve their apps in terms of design, usability, and content. To get this feedback, users can post their projects after signing up for the website.


**Author: Victor Lominyo**

**Live Link: https://todo.herokuapp.com/**


Technologies Used
=
- Python 
- Django


Setup Instructions and Installation
=
1. Clone the repository on to your computer

```
$ git clone https://github.com/victorlomi/Project-Awards
```

2. Navigate to the project directory 

```
$ cd Project-Awards
```

3. Create virtual environment and activate it

```
$ python3 -m venv venv
$ . venv/bin/activate
``` 

4. Install packages

```
$ pip install -r requirements.txt
```

5. Create a .env file with the following

```
SECRET_KEY=<key>
DB_NAME=<db_name>
USER=<db_user>
PASSWORD=<db_password>
```

6. Run the development server

```
$ python manage.py runserver
```

You are all set!

Contact
=
**Email:** victorlominyo@gmail.com

License
=
MIT License

Copyright (c) 2020 victorlomi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.