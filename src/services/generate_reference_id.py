import string
import random

class GenerateReferenceID:

    def generate_reference_id(self, author, year, title, info):
        """ Generates reference ID """

        reference_id = (author[0:4] + year + title[0:4]).lower()

        reference_id_in_db = self.is_duplicate_reference_id(reference_id, info)

        # if reference id already exists, add random string to end
        while reference_id_in_db:
            letters = string.ascii_lowercase
            random_number = random.randint(0,100)

            random_string = "".join(random.choice(letters) for letter in range(5))
            random_string = random_string + str(random_number)

            reference_id = reference_id + random_string

            reference_id_in_db = self.is_duplicate_reference_id(reference_id, info)
        return reference_id

    def is_duplicate_reference_id(self, reference_id, info):
        """ Checks if reference id is already in the database """

        for rf_id in info:
            if reference_id == rf_id[0]:
                return True
        return False
