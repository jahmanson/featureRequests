# featureRequests
Allow users to request a new feature

## Getting Started

This project uses Flask and MySQL. You will need to follow the instructions below to setup a MySQL Database before the app will run.

### Prerequisites
#### Python 3

The best way to install is using Homebrew. Open a terminal window and enter the following:

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Then, to install Python 3 run the command below:
```
brew install python3
```

#### Virtualenv

Best practice is creating a virtualenv. First, install virtualenv using:
```
sudo pip3 install virtualenv
```
Next, create a directory for the project and open that directory:

```
mkdir Features
cd Features
```
Create your virtual environment with the following:
```
virtualenv venv -p python2.7
```

Finally, activate your environment
```
source venv/bin/activate
```

### Installing

#### Dependencies
from your Features directory clone this repo:
```
git clone https://github.com/jahmanson/Features
```
Open this directory and install the requirements:
```
cd Features
pip install -r requirements.txt
```

#### Setting up MySQL Database
This webapp requires a local installation of MySQL, a DATABASE titled 'features', and a TABLE titled 'requests'. First, download a version of [MySQL Community Server](https://dev.mysql.com/downloads/mysql/) and follow the installation instructions for your machine.

Next, login to your MySQL instance from the command line:
```
mysql -u root -p
```
Enter your password when prompted. Upon success you should get a welcome message and a command prompt.
```
Welcome...
...
mysql>
```
To create our new database enter the following command.
```
CREATE DATABASE features;
```
Then switch to that database.
```
USE features;
```
Finally, enter the following code to setup a table for repos:
'''
CREATE TABLE requests (
  id int NOT NULL AUTO_INCREMENT,
  title varchar(255) NOT NULL,
  description text NOT NULL,
  client varchar(255) NOT NULL,
  priority int NOT NULL,
  target_date date NOT NULL,
  product_area varchar(255) NOT NULL,
  PRIMARY KEY (id)
);
'''

#### Update environment variables
In order the access your MySQL database, you'll need to update one of the environment variables. In the repo directory, rename the '.example.env' file to '.env'. Open the .env file in a text editor and replace 'password' with your MySQL password.

## Deployment

With your virtualenv running, from the github repo directory, start the app with the following command:
```
python app.py
```

Open your browser to localhost:5000. Click on the 'Add Feature Request' button to add a new feature request to your database. This will then populate the index page.


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
