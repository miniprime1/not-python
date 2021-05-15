import platform
import sys

if platform.system() == "Windows":
    print('Not Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 07:55:33) [MSC v.1916 32 bit (Intel)] on win32')
    print('Type "help", "copyright", "credits" or "license" for more information.')
    while True:
        i = input(">>> ")
        if i == "exit()": break
        print("Nope!")

elif platform.system() == "Drarwin":
    print('Not Python 3.7.8 (v3.7.8:4b47a5b6ba, Jun 27 2020, 04:47:50)')
    print('[Clang 6.0 (clang-600.0.57)] on darwin')
    print('Type "help", "copyright", "credits" or "license" for more information.')
    while True:
        i = input(">>> ")
        if i == "exit()": break
        print("Nope!")

elif platform.system() == "Linux":
    print('Not Python 3.7.8 (v3.7.8:4b47a5b6ba, Jun 27 2020, 09:53:43)')
    print('[GCC 8.4.0] on linux')
    print('Type "help", "copyright", "credits" or "license" for more information.')
    while True:
        i = input(">>> ")
        if i == "exit()": break
        print("Nope!")

else:
    print('Not Python 3.7.8 (v3.7.8:4b47a5b6ba, Jun 27 2020, 09:53:43)')
    print('[GCC 8.4.0]', 'on', sys.platform)
    print('Type "help", "copyright", "credits" or "license" for more information.')
    while True:
        i = input(">>> ")
        if i == "exit()": break
        print("Nope!")
