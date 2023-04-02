# TeleCipher

- This system combines two applications, one is the client app responsible for sending files through `SFTP` to the receiver end and the other one needs to be installed on the computer which is receiving files.
- The client app prompts users to enter the host computer IP address, sftp username and password. After a successfull connection user can choose either `ROT13 Cipher` or `AES Encryption` mechanism to encrypt a file. Later on a file upload, a dialogue box will appear and the user can send the file to the host(Additionally an indication of the encryption algorithm is also sent to the host)
- The receiver application is a service that must be run before sending a file. It basically monitors any file creation event on a specific directory path. As soon as a file is received it will catch the file detect the encryption mechanism applied earlier, applies the appropriate decryption algorithm to get back the original data.

## Watch this a demo [video](https://youtu.be/QnuAnOgVisU 'YouTube').

[Here](https://tecadmin.net/how-to-create-sftp-only-user-in-ubuntu-20-04 'Techadmin blog') is an article on how you can create sftp user on Ubuntu.
