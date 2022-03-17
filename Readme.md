# MAAVUC- Mobile App Assets Vulnerability Checker :

Enter app id and using  Osint Api it generates hostnames and IP address disclosed in the app.
Using dns_resolver it resolves IP of hostnames from assets and by using Internet DB Shodan API to 
generate vulnerability report of Disclosed IP and IP found in hostname assets of the APP in HTML format 
which is generated using FLASK API and can be viewed in web browser.


## Installation


* clone the repo and type `flask run` in the terminal directory.
* * `pip install requirements.txt`
* Enter your BeVigil Api key generated from https://bevigil.com in the config.py file



## Usage


Run `flask run` to :
* Generate report of Vulnerabilities found in the APP asset in tabular form.
* Displays the report in html and can be viewed in web browser.
* generates the report in tabular form.


![alt text](https://github.com/saifkwik/MAAVUC/blob/main/report_screenshot.png)
