# Write a Python program to access and print a URL's content to the console.
from http.client import HTTPConnection
class contentURL:
    def consoleURL(self):
        conn=HTTPConnection("example.com")
        conn.request("GET","/")
        result=conn.getresponse()
        contents=result.read()
        print(contents)
obj=contentURL()
obj.consoleURL()