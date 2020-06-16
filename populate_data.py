import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','backend.settings')

import django
# Import settings
django.setup()

import random
from farmer.models import Farmer
from faker import Faker
from django.contrib.auth.models import User
from django.utils import timezone

fakegen = Faker()

# Create Fake Data for the Farmers
def populateFarmer(N):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):

        # Create Fake Data for entry
        fake_name = fakegen.first_name()
        fake_lastname = fakegen.last_name()
        fake_description = fakegen.text(max_nb_chars=30, ext_word_list=None)
        fake_location= fakegen.street_address()
        fake_city= fakegen.city()
        fake_state = fakegen.state()
        fake_country = fakegen.country()
        fake_postal_code = fakegen.postcode()
        fake_fax= fakegen.phone_number()
        fake_telephone = fakegen.phone_number()
        fake_website = fakegen.url()
        fake_twitter = fakegen.url()
        fake_facebook = fakegen.url()
        fake_linkedin = fakegen.url()
        fake_email = fakegen.email()
        last_updated = timezone.now()

        # Create new Post Entry
        farm = Farmer.objects.get_or_create(  name = fake_name,
                                            lastname = fake_lastname,
                                            full_description = fake_description,
                                            location = fake_location,
                                            city = fake_city,
                                            state = fake_state,
                                            country = fake_country,
                                            postal_code = fake_postal_code,
                                            fax= fake_fax,
                                            telephone = fake_telephone,
                                            website = fake_website,
                                            twitter = fake_twitter,
                                            facebook = fake_facebook,
                                            linkedin = fake_linkedin,
                                            email = fake_email,
                                            last_updated = last_updated)[0]



if __name__ == '__main__':
    
    print("The Farmer contains {} data".format(len(Farmer.objects.all())))
    value = input("Would you like to add more data? (y/n) ")
    if value == "y":
        populateFarmer(int(input("How many Farmers you want to create? ")))
        print('Populating Farmer Complete')
        print('')
        print('*************************************')
    
    

    print('All Populating process is Completed')