class Student():
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.age = 0
        self.cohort_number = 0



# Define getters for all properties.

    @property # The first name getter
    def first_name(self):
        try:
            return self.__first_name # Note there are 2 underscores here
        except AttributeError:
            return ""
    @property # The last name getter
    def last_name(self):
        try:
            return self.__last_name # Note there are 2 underscores here
        except AttributeError:
            return ""
    @property # The age getter
    def age(self):
        try:
            return self.__age # Note there are 2 underscores here
        except AttributeError:
            return ""
    @property # The cohort number getter
    def cohort_number(self):
        try:
            return self.__cohort_number # Note there are 2 underscores here
        except AttributeError:
            return ""

# The full name property should return first name and last name separated by a space. It's value cannot be set.
    @property # The full name getter
    def full_name(self):
            try:
                return self.__first_name + " " + self.__last_name
            except AttributeError:
                return ""

# Define a setter for all but the read only property. Ensure that only the appropriate value can be assigned to each.

    @first_name.setter # The first name  setter
    def first_name(self, new_first_name):
        if type(new_first_name) is str:
            self.__first_name = new_first_name
        else:
            raise TypeError('A')
    @last_name.setter # The first name  setter
    def last_name(self, new_last_name):
        if type(new_last_name) is str:
            self.__last_name = new_last_name
        else:
            raise TypeError('B')
    @age.setter # The age setter
    def age(self, new_age):
        if type(new_age) is int:
            self.__age = new_age
        else:
            raise TypeError('C')
    @cohort_number.setter # The age setter
    def cohort_number(self, new_cohort_number):
        if type(new_cohort_number) is int:
            self.__cohort_number = new_cohort_number
        else:
            raise TypeError('D')
    def __str__(self):
        return f"{self.full_name}"




mike = Student()
mike.first_name = "Mike"
mike.last_name = "Esllis"
mike.age = 35
mike.cohort_number = 39

print(mike)
print(f"{mike.full_name} is {mike.age} years old and is in cohort {mike.cohort_number}.")