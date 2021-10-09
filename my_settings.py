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
        'NAME': 'SCTC_BMS_DB',
        'USER': 'sctc',                      
        'PASSWORD': 'sctcbms1!',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}