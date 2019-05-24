Package Installation 
	-pip install Flask
	-pip install lxml
Flask Deployment
	-in bash:
		-export FLASK_APP=main.py
	-in powershell:
		-$env:FLASK_APP = "main.py"
Run Web Server
	-flask run
	-ctrl+ click http://127.0.0.1:5000/
