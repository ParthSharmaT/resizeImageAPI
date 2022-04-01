
# Resize Image API

It is an API to resize an image using Pillow library.

## Getting Started

### Fork and clone locally

Fork [Resize Image API](https://github.com/ParthSharmaT/resizeImageAPI.git) repository and clone at your local 

- Fork and Clone the repo using
```
$ git clone https://github.com/ParthSharmaT/resizeImageAPI.git
```

### Setting Environment First Time

#### Basic Requirements 
1. [Python](https://www.python.org/downloads/)
1. [pip](https://pip.pypa.io/en/stable/installation/)

#### Creating [Virtual Environment](https://docs.python.org/3/library/venv.html) 

A virtual environment is a tool that helps keep dependencies required and the project isolated. If you wish to install a new library and write
```
pip install name_of_library
``` 
on the terminal without activating an environment, all the packages will be installed globally which is not a good practice if you’re working with different projects on your computer.

If this sounds a bit complicated, don’t worry so much because a virtual environment is just a directory that will contain all the necessary files for our project to run.

**Installing venv (required once)**

**Windows**
```
py -m pip install --user virtualenv
py -m venv env
```
**Linux**
```
python3 -m pip install --user virtualenv
python3 -m venv env
```

You have to start virtual environment everytime you start new terminal -

**Windows**

Using gitbash
```
. env/Scripts/activate
```
Using Powershell
```
. env\Scripts\activate
```
**Linux**
```
source env/bin/activate
```

#### Installing Requirements 

**Windows**
```
pip install -r requirements.txt
```
**Linux**
```
pip install -r requirementstxt
```
#### Setting up Environment File

**Configuring Environment Variables**

Make environment file by copying the example file -


#### Migrating Database
**Windows**
```
python3 manage.py migrate
```
**Linux**
```
python3 manage.py migrate
```

#### Create Superuser
**Windows**
```
python3 manage.py createsupeser
```
**Linux**
```
python3 manage.py createsupeser
```

### Starting Development Server
**Windows**
```
py manage.py runserver
```
**Linux**
```
python3 manage.py runserver
``` 

### Leaving the virtual environment
```
deactivate
```

### Update requirements file (Critical)
If you have installed new dependency, the pip freeze command lists the third-party packages and versions installed in the environment. 

**Windows**
```
pip freeze > requirements.txt
```
**Linux**
```
pip3 freeze > requirements.txt
```

### Update Database  
Everytime you change db models, you need to run makemigrations and migrate to update on database.

**Windows**
```
py manage.py makemigrations
py manage.py migrate
```
**Linux**
```
python3 manage.py makemigrations
python3 manage.py migrate

```
## Approach
I have used Pillow to resize the image during record creation. So the two codes before and after are as follows:
**Before resize functionality**
```class FishRecord(models.Model):
    def nameFile(instance, filename):
       image_name = '/'.join(['images', str(instance.title), filename])
       full_path = os.path.join(settings.MEDIA_ROOT, image_name)

       if os.path.exists(full_path):
            os.remove(full_path)

       return image_name
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=nameFile,blank=True)
    weight= models.IntegerField()
    length= models.IntegerField()
    latitude = models.FloatField(default=0.000000)
    longitude = models.FloatField(default=0.000000)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
```

**After resize Functionality**
```class FishRecord(models.Model):
    def nameFile(instance, filename):
       image_name = '/'.join(['images', str(instance.title), filename])
       full_path = os.path.join(settings.MEDIA_ROOT, image_name)

       if os.path.exists(full_path):
            os.remove(full_path)

       return image_name
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=nameFile,blank=True)
    weight= models.IntegerField()
    length= models.IntegerField()
    latitude = models.FloatField(default=0.000000)
    longitude = models.FloatField(default=0.000000)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        if self.image:
            pic=Image.open(self.image.path)
            pic.thumbnail((140,140),Image.LANCZOS)
            pic.save(self.image.path)
            
    def __str__(self):
        return self.title
```
