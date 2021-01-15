from pathlib import Path

# SRP SOC
class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

# Bad Design, too many responsibilities
#    def save(self, filename):
#        file = open(filename, 'w')
#        file.write(str(self))
#        file.close
#
#    def load(self, filename):
#        pass
#
#    def load_from_web(self, uri):
#        pass


class PersistenceManager:

    @staticmethod
    def save_to_file(journal, filename):
        with open(filename, 'w+') as fh:
            fh.write(str(journal))


if __name__ == '__main__':

    j = Journal()
    j.add_entry('I cried today')
    j.add_entry('I ate a bug')
    print(f"Journal entries: \n{j}")

    file_path = 'test.csv'
    PersistenceManager.save_to_file(j, file_path)

    with open(file_path) as fh:
        print(fh.read())