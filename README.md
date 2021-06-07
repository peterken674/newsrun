# Newsrun
#### Newsrun, 2021.
#### By **Peter Kennedy**
## Description
A Flask powered application where the user can:
- See various news sources on the homepage of the application.
- Select a news source and see all news articles from the selected news source in the application.
- See the image, description and the time a news article was created.
- Click on an article and read the full article on the source website.

## Setup/Installation
On your terminal, clone the project.
    
    $ git clone git@github.com:peterken674/newsrun.git

Navigate into the cloned project.

    $ cd newsrun

Create a `start.sh` file.

    $ touch start.sh

Inside `start.sh`, add your API key from [https://newsapi.org/](https://newsapi.org/) and the command for executing `manage.py`, which will start the server.

```python
export NEWS_API_KEY='<YOUR_API_KEY>'

python manage.py server
```
Give the file execution permissions.

    $ chmod a+x start.sh

Run the program.

    $ ./start.sh
## Known Bugs
- UI is not completely responsive to very large screens.
- Does not perform check to see whether the news request returns something in the response.
## Technologies Used
- Flask(Python)
- Jinja2
- Unittest
## Support and contact details
If you have any suggestions, questions or in case of a fire, you can reach the developer via [email](mailto:peterken.ngugi@gmail.com).
### License
 [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Copyright &copy; 2021 **[peterken674](www.github.com/peterken674)**