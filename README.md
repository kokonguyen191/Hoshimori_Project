# Hoshimori-Project

**[The Battle Girl Highschhool Database and Community](http://hoshimorigakuen.pythonanywhere.com/)**

## Get Started

### Requirements

  - Debian, Ubuntu, and variants

    ```shell
    apt-get install libpython-dev libffi-dev python-virtualenv libmysqlclient-dev nodejs
    ```

  - Arch

    ```shell
    pacman -S libffi python-virtualenv libmysqlclient nodejs
    ```
    
  - OS X (install brew if you don't have it):
  
    ```shell
    brew install python node
    sudo pip install virtualenv
    npm install lessc bower
    ```
    
### Quick guide

1. Clone the repo:

    ```shell
    git clone https://github.com/kokonguyen191/Hoshimori-Project.git
    cd Hoshimori-Project
    ```

2. Create a virtualenv to isolate the package dependencies locally:

    ```shell
    virtualenv env
    source env/bin/activate
    ```

3. Install packages:

    ```shell
    pip install --upgrade setuptools
    pip install -r requirements.txt
    ```

4. Get the front-end dependencies:

    ```shell
    npm install -g bower
    bower install
    ```
  
5. Initialize the models and databse:

    ```shell
    python manage.py makemigrations hoshimori
    python manage.py migrate
    ```

6. Launch the server:

    ```shell
    python manage.py runserver
    ```

7. Open your browser to [http://localhost:8000/](http://localhost:8000/) to see the website

## Developers

* **[Koko191](https://github.com/kokonguyen191)** - Main dev
* **[duyson98](https://github.com/duyson98)** - Collaborator

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details
