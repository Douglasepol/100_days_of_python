'''
Problem: File Size Retrieval

This Python function, file_size, is designed to return the size of a file in bytes. It takes a single parameter, the name of the file, and uses Python's os module to access the file's metadata. Key points include:
- The function takes one parameter, fname, which is expected to be a string representing the file name (with extension, if any).
- It uses the os.stat function from the os module to get metadata of the file.
- The size of the file is extracted from the metadata using the st_size attribute.
- It returns the file size in bytes.

Example Output:
- The script will output the size of 'test.txt' in bytes. 
'''

def file_size(fname):
        import os
        file_info = os.stat(fname)
        return file_info.st_size

print("File size in bytes of a plain file: ",file_size("test.txt"))
