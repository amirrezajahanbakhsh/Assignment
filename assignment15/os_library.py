import os

#os.getcwd() The ** getcwd() function** helps to find the current working directory – it returns a string with the complete path. Below is a code snippet to see how this works
print(os.getcwd())

#os.mkdir() The mkdir() function is useful if you want to create a directory. This function accepts the path of your new directory that you wish to create. If you provide a path that already exists, the mkdir() function will throw a FileExistsError.
current_dir =  os.getcwd()
new_dir_path = current_dir + "/my_new_dir"
os.mkdir(path = new_dir_path)
print("New directory created successfully.") 

#chdir() The chdir() function changes your current directory to the path that you pass as an argument to this function. If you provide a path to a directory that does not exist, then you might get a FileNotFoundError. Similarly, if you are not authorized to access a directory, you will get a PermissionError. If you pass a path that is not a directory path, you may end up getting a NotADirectoryError.
current_dir = os.getcwd()
new_dir_path = current_dir + "/my_new_dir"
os.mkdir(path = new_dir_path)

print("Working directory: ", os.getcwd())
os.chdir(new_dir_path)
print("New working directory: ", os.getcwd())

#listdir()  Now, let’s say that you have some files in a directory and you want to list all of them. In this case, the listdir() function comes in handy. This function will return all the files and directories that are present in the path that you can pass as an argument.
current_dir = os.getcwd()
print(os.listdir(path = current_dir))

#remove()  Now, let’s suppose that you want to remove a file from a directory – you could use the remove() function to perform this operation. To do so, you need to pass the complete path of the file that you want to delete
current_dir = os.getcwd()
file_name = "sample1.txt"
file_path = current_dir + "/" + file_name

print("Files before deletion: ", os.listdir(path = current_dir))
os.remove(path = file_path)
print("Files after deletion: ", os.listdir(path = current_dir))

#rmdir() The remove() function only deletes a file, not a directory. If you wish to delete a directory, you can use the rmdir() function and pass the directory path to this function as an argument.
current_dir = os.getcwd()
dir_name = "/my_new_dir"
dir_path = current_dir + dir_name

print("Files before deletion: ", os.listdir(path = current_dir))
os.rmdir(path = dir_path)
print("Files after deletion: ", os.listdir(path = current_dir))