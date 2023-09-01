import os
import random

class SecureFileShredder:

    def __init__(self):
        self.log = []

    def overwrite_file(self, filepath, passes=3):
        try:
            filesize = os.path.getsize(filepath)
            with open(filepath, 'rb+') as file:
                for _ in range(passes):
                    file.seek(0)
                    file.write(os.urandom(filesize))
            return True
        except Exception as e:
            print(f'Error overwriting file: {e}')
            return False

    def delete_file(self, filepath):
        try:
            os.remove(filepath)
            self.log.append(f'Securely deleted: {filepath}')
            return True
        except Exception as e:
            print(f'Error deleting file: {e}')
            return False

    def shred(self, filepath, passes=3):
        if self.overwrite_file(filepath, passes):
            if self.delete_file(filepath):
                print(f'File {filepath} has been securely shredded.')
            else:
                print(f'Failed to delete {filepath} after overwriting.')
        else:
            print(f'Failed to securely shred {filepath}.')

    def run(self):
        filepath = input('Enter the path of the file you want to securely delete: ')
        passes = int(input('Enter the number of overwrite passes (default is 3): ') or 3)
        self.shred(filepath, passes)
        print('\n'.join(self.log))

if __name__ == '__main__':
    shredder = SecureFileShredder()
    shredder.run()
