import sys

sys.path.append("C:\\Users\\marco\\OneDrive\\Documentos\\PadraoMVC_Python\\src\\model\\DAO")
sys.path.append("C:\\Users\\marco\\OneDrive\\Documentos\\PadraoMVC_Python\\src\\model\\entities")

from AuthorDAOFile import AuthorDAOFile
from Author import Author
from User import User
from UserDAOFile import UserDAOFile

authorArchive = AuthorDAOFile("AuthorList.json")

author = Author()

authors = authorArchive.findAll()

for author in authors:
    author.print()

userArchive = UserDAOFile("UserList.json")

user = User()

users = userArchive.findAll()

for user in users:
    user.print()