Be a cat and be a dog. Meowoof.
Flag format: PUCTF24{xxx}
做隻貓做隻狗
Flag 格式: PUCTF24{xxx}
We are given a jpg file in this challenge
 ![image](https://github.com/STC-STEM/nuttyshell-ctf-2024-writeups/assets/94276358/4580768a-8f82-4fc7-af71-c4d8e7f47437)

After counting, it contains 75x75 little pictures. 
I am thinking it is a QR code. 
But after investigation, I found that there is only 73x73(ver.14) or 77x77(ver.15) QR codes.
Then I tried to find out the patterns in the file manually in a excel.
Mark cat as 0 and dog as 1
 ![image](https://github.com/STC-STEM/nuttyshell-ctf-2024-writeups/assets/94276358/f2afd892-005c-42f9-add0-055b4ed5dc8c)

From this, we can easily understand that each 3X3 is a block in a 25X25 QR code(Ver.2)
With 3x3 being the same, the counting is much easier 75x75=5625 becomes 25x25=625
Replace of 0 with black
 ![image](https://github.com/STC-STEM/nuttyshell-ctf-2024-writeups/assets/94276358/e28c94a6-6bc9-4cdf-a9f1-0f9bb4a2880d)

Scanning the QR code, we get the flag, PUCTF24{ILikeHum4nsM0re:P_8e0af}

