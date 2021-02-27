# Flask Example 

This is a simple [flask](http://flask.pocoo.org/) example application Built using [pybuilder](http://pybuilder.github.com).

Templates use [twitter bootstrap](http://twitter.github.com/bootstrap/) via [bootstrap CDN](http://bootstrapcdn.com).

# How to build

## Create a virtual environment

Python allows to develop in [virtual environments](http://pypi.python.org/pypi/virtualenv).

```bash
virtualen deveve
```

Activate the virtual environment

```bash
source deveve/bin/activate
```

## Install pybuilder

```bash
pip install pybuilder
```

 Install dependencies using pybuilder
```bash
pyb install_dependencies
```

Run pybuilder `pyb` to build run the unit and integration tests and build the project.
```bash
pyb
```

# How to run

After installation you can run the application in debug mode using
```bash
python src/main/python/com/mycompany/start_system_analyzer.py
```

# How to run in production
Working on it...

# How to run in docker
1) pyb
2) docker build -t system-analyser .
3) docker run --name mysql -p 3307:3306 -e MYSQL_ROOT_PASSWORD=root -d mysql:5.7
4) login to container and create database system_analyzer
5) docker run --link mysql:mysql --name system-analyser -p 5000:5000 -e DB_HOST=mysql -e DB_USER=root -e DB_PASSWORD=root -e DB_PORT=3306 system-analyser


After Docker container is started, Insrtall the following depenedencies

1) apt-get install patch
2) apt-get install gcc
3) apt-get install make
4) apt-get install libmysqlclient-dev
5) apt-get install libssl-dev

# License

Licensed under [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0.html)
