
# QIPU Challenge

Challenge provide by QIPU

* **Contents**
    * [Task 1](#Task1)
    * [Task 2](#Task2)
    * [Task 3](#Task3)


# Run Locally

Clone the project and access the project folder

```bash
git clone https://github.com/gabriel-henriq/qipu_challenge.git
```
then
```bash
 cd qipu_challenge/
```

## [Task 1](./qipu_project/Task_1)

Run the following commands:

```bash
cd Task_1/
```

```python
python linkedlist.py
```

After that you should be able to see the final assertions result

```bash
100%
```

## [Task 2](./qipu_project/Task_2)

```bash
cd Task_2/
```

You can run this task in two ways
* Docker
* venv


### Docker

```docker
 docker-compose up --build
```

If the application build has succefully completed, you should be able to see in your browser

http://localhost:8080/


### venv

Creating the virtual environment

```python
 python -m venv venv
```

Activating the venv

```bash
 source venv/bin/activate
```

then

```python
 pip install -r requirements.txt
```

finally

```python
 python manage.py runserver localhost:8080
```

Now you should be able to see the application in your browser

http://localhost:8080/



## [Task 3](./qipu_project/Task_3)

```bash
cd Task_3/
```

Creating the virtual environment

```python
 python -m venv venv
```

Activating the venv

```bash
 source venv/bin/activate
```

then

```python
 pip install -r requirements.txt
```

finally

```python
 python __init__.py
```

