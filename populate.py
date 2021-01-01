import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

import django
django.setup()

import random
from contactmanager.models import AccessRecord,WebPage,Topic
from faker import Factory, Faker

fakegen = Faker()

topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        top = add_topic()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webpage = WebPage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]
        AccessRecord.objects.get_or_create(name=webpage, date=fake_date)[0]


if __name__ == "__main__":
    print("Populating string")
    populate(20)
    print("Populate complete")