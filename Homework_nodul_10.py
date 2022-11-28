from collections import UserDict
  
class Field:
    def __init__(self, value):
        self.value = value

class Name(Field):
    pass

class Phone(Field):
    pass

class AddressBook(UserDict):
    
    def add_record(self, record):
        self.data[record.name.value] = record

    def get_all_record(self):
        return self.data

    def has_record(self, name):
        return bool(self.data.get(name))

    def get_record(self, name):
        return self.data.get(name)

    def remove_record(self, name):
        del self.data[name]

    def search(self, value):
        if self.has_record(value):
            return self.get_record(value)

        for record in self.get_all_record().values():
            for phone in record.phones:
                if phone.value == value:
                    return record

        raise ValueError("Contact with this value does not exist.")


class Record:

    def __init__(self, name: Name, phone: Phone = None):
        self.name  = Name(name)
        self.phones: list[Phone] = [phone] if phone is not None else []
    
    def get_info(self):
        phones_info = ''

        for phone in self.phones:
            phones_info += f'{phone}, '

        return f'{self.name.value} : {phones_info[:-2]}'

    def add_phone(self, phone_number: Phone):
        self.phones.append(phone_number)

    

    def delete_contact(self, phone: Phone):
        try:
            for record_phone in self.phones:
                if record_phone == phone:
                    self.phones.remove(record_phone)
                    return True
            return False
        except ValueError:
            return f'{phone} is not exists'

    def change_phone(self, old_number: Phone, new_number: Phone):
        try:
            self.delete_contact(old_number)
            self.add_phone(new_number)
        except ValueError:
            return f'{old_number} does not exists'

