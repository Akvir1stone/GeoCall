# GeoCall
## Description
This is educational project, main task for this project is creating API for given database
Along with main task there was several additional tasks such as:
* Optimization of given database
* Use of environmental variables for secret data
* Deploying project on online hosting
* Creating tests
* Creating documentation with swagger
* Correct work with git

## What was done
* Created API
  * **POST** method for creating new object
    ```
    POST /Pereval/
    ```
    It takes ***JSON*** from request with all needed data and creates new object
    Example of ***JSON***:
    ```
    {
    "beauty_title": "qwe",
    "title": "qew",
    "other_titles": "qwe",
    "connect": "qwe",
    "user": {
        "email": "qwe@qwe.qwe",
        "fam": "qwe",
        "name": "qwe",
        "otc": "qwe",
        "phone": "1234"
    },
    "coords": {
        "latitude": 13234,
        "longitude": 1341243,
        "height": 134
    },
    "levels": {
        "winter": "lvl1",
        "summer": null,
        "autumn": null,
        "spring": null
    },
    "images": [{
        "image": "<picture url>",
        "title": "pic"
    },
    {
        "image": "<picture url>",
        "title": "pic2"
    }]
    }
    ```
  * **GET** method that retuns list of all existing objects
    ```
    GET /Pereval/
    ```
  * **GET** method that retuns list of all objects that was created by user with email = `<email>`
    ```
    GET /Pereval/?user__email=<email>
    ```
  * **GET** method that retuns object with id = `<id>`
    ```
    GET /Pereval/<id>
    ```
  ----
  * More detailed documentation created by swagger is availavle on [*pythonanywhere*](https://akvir.pythonanywhere.com/swagger)
* Database was optimized
* Used **dotenv** for storing secret data in environmental variables
* Deployed project on [*pythonanywhere*](https://akvir.pythonanywhere.com/) service
* Test coverage report
  ```
  Name                                                                             Stmts   Miss  Cover
  ----------------------------------------------------------------------------------------------------
  geocall\__init__.py                                                                  0      0   100%
  geocall\asgi.py                                                                      4      4     0%
  geocall\settings.py                                                                 21      0   100%
  geocall\urls.py                                                                      9      0   100%
  geocall\wsgi.py                                                                      4      4     0%
  geocall\yasg.py                                                                      5      0   100%
  manage.py                                                                           11      2    82%
  perevals\__init__.py                                                                 0      0   100%
  perevals\admin.py                                                                    5      0   100%
  perevals\apps.py                                                                     4      0   100%
  perevals\migrations\0001_initial.py                                                  6      0   100%
  perevals\migrations\0002_alter_images_image_alter_puser_email.py                     4      0   100%
  perevals\migrations\0003_alter_pereval_status.py                                     4      0   100%
  perevals\migrations\0005_images_add_time.py                                          4      0   100%
  perevals\migrations\0006_alter_images_image_alter_images_per_and_more.py             5      0   100%
  perevals\migrations\0007_alter_pereval_user.py                                       5      0   100%
  perevals\migrations\0008_alter_pereval_coords_alter_pereval_levels_and_more.py       5      0   100%
  perevals\migrations\__init__.py                                                      0      0   100%
  perevals\models.py                                                                  33      0   100%
  perevals\serializers.py                                                             52      0   100%
  perevals\tests.py                                                                   83      0   100%
  perevals\views.py                                                                   35      8    77%
  ----------------------------------------------------------------------------------------------------
  TOTAL                                                                              304     18    94%
  ```
