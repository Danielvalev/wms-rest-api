<p align="center">
  <h2 align="center">WMS REST API</h2>

  <p align="center">
    Warehouse Management System
    <br />
    <br />
    <a href="https://documenter.getpostman.com/view/4790348/Uz5CNJxd">View Documentation</a>
    ·
    <a href="https://github.com/Danielvalev/wms-rest-api/issues">Report Bug</a>
    ·
    <a href="https://github.com/Danielvalev/wms-rest-api/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#application-requirements">Application Requirements</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

### Built With

* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/2.1.x/)
* [PostreSQL](https://www.postgresql.org/)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Application Requirements

1. Python 3.7 or newer
2. Pip
3. Virtual Environment
4. Other packages listed in requiremtns.txt

### Installation
Make sure you have already downloaded and install python3 and pip

1. The first thing to do is to clone the repository:
 ```sh
$ git clone https://github.com/Danielvalev/wms-rest-api
$ cd wms-rest-api
`````````````

2. Create a virtual environment to install dependencies:
- For MacOS: 
 ```sh
$ python3 -m venv env 
`````````````

- For Windows:
 ```sh
C:\Users\Name\wms-rest-api> py -m venv env
`````````````

3. Activate your Virtual Environment
- For MacOS:
 ```sh
$ source env/bin/activate
`````````````
- For Windows:
 ```sh
C:\Users\Name\wms-rest-api> env\Scripts\activate 
`````````````

4. Install dependencies listed in the requirement.txt:
 ```sh
(env)$ pip install -r requirements.txt 
`````````````
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `py -m venv env`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd wms-rest-api
```

5. Run Server
```sh
(env)$ python app.py
```
Expected result: 
```
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
 * Restarting with stat
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Debugger is active!
 * Debugger PIN: XXX-XXX-XXX

```


#### Other syntaxes
To kill/stop the server 
> Ctrl + c

To deactivate the Virtual Environment
```sh
(env)$ deactivate
```

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/Danielvalev/wms-rest-api/issues) for a list of proposed features (and known issues).


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Daniel Valev - danielvalev89@gmail.com
