siLocker v1.0.3  Windows/Linux
Developer: Ilia Abbasi
-----------------------------------


What this program does:

- siLocker can encrypt/decrypt your files using a key you give it.
- siLocker uses the Fernet algorithm from the cryptography module in Python.
- siLocker only encrypts/decrypts the files in the directory which it's running.
- siLocker hashes your key with sha256 algorithm and turns the result into a 64base encoding
string, then it uses that string as the real Fernet key for encrypting/decrypting your files.
- There is a "safe" folder called "NO_LOCK_FOLDER" that is immune to this program's effects. If
you name a folder "NO_LOCK_FOLDER", then nothing in that folder (recursively) is affected by
siLocker. If siLocker itself has a "NO_LOCK_FOLDER" in its parent folders, then the program
will do nothing at all.
- siLocker will not encrypt/decrypt itself.
- In the "Strict Mode", siLocker also uses your BIOS information as a unique key representing
your device, to make the encryption much more safer. In this case even if someone steals your
encrypted files and also your key, they will still not be able to decrypt your data, as they
don't have your BIOS information. If you use Strict Mode and then for any reason change
something related to your BIOS, your data will pretty much be inaccessible forever. so:

USE STRICT MODE AT YOUR OWN RISK. I DO NOT TAKE ANY RESPONSIBILITIES IF ANY OF YOUR FILES GET LOST, DELETED OR CORRUPTED, AFTER USING THE "STRICT MODE".


How to use:

- siLocker can be used on Windows or Linux.
- You can give arguments to the program. To see the list of arguments use '-h' in CMD/Terminal.
- First you are asked if you want to use "Strict Mode" or not. You can enter "N" to say no, or
enter "Y" to say yes. If you don't enter anything then siLocker will not use the "Strict Mode"
by default.
- Then you are asked to enter the key. You can enter anything you want here.
- Then you are asked if you want to lock the files or unlock them. Enter "L" to lock and "U" to
unlock. If you enter nothing then the program will raise an error.
- Then siLocker will display what it is doing. White text means OK. Red text means Error. If
for any reason you can't see the colors, there is also a + or - sign at the start of
each entry which + means OK and - is Error.
- At the end siLocker will output the result. If there was no error then the text will be
green and if any error happened, the program will print the error in white text with
red background.
- If you saw this text: "Exception caught" while running the program and you didn't know what
the error was, contact the developer.
- siLocker uses my own module called "toolbox". You should have this module to run the script:
https://github.com/ilia-abbasi/Python-projects/tree/main/Modules/toolbox


Privacy Policy:

- siLocker is written in Python and compiled with Pyinstaller. If you want the source code you
can visit the developer's GitHub page: https://github.com/ilia-abbasi
- siLocker never saves, shares or manipulates your device's information.
- siLocker never saves, shares or manipulates your BIOS information.
- siLocker never saves, shares or manipulates your files' information.
- siLocker uses your BIOS information only to encrypt/decrypt your files.
- If there are still any uncertainties for you on how this program functions on your device,
you can get the source code yourself in my GitHub page: https://github.com/ilia-abbasi


-----------------------------------
Thanks for using my program!
