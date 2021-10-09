# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1emj5*2t%yxisb!&bjw#3v21ca-a89xnn3%y1qsyx9!m_llivq'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    #'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': BASE_DIR / 'db.sqlite3',
    #}
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'team5_db',
        'USER': 'team5',                      
        'PASSWORD': 'team5',
        'HOST': '163.152.216.248',
        'PORT': '3306',
    }
}