#nuttyshell-ctf-2024-writeups
My friend extracted this file from a 3D printed Save icon, I don't know what that meant and what file this is but I heard it is music, can you help decode it?
Hint: Can you recover the hidden track?
Decoded flag is in this format: PUCTF24!INSERT=FLAG=HERE=RANDOM! PLEASE convert the Exclaimation to Curly brackets on both ends and Equal signs to Underscore to match formatting
Flag format: PUCTF24{INSERT_FLAG_HERE_RANDOM}

We are given a .mid file in this challenge
I downloaded midiEditor to look at the file.
![image](https://github.com/STC-STEM/nuttyshell-ctf-2024-writeups/assets/94276358/8bc68a78-db9d-415f-a378-a83ee075afae)
It can be seen that there are 16 tracks.However, after looking at each track, there is no obvious pattern for the flag.(btw, good music)
I decided to look at the file in hex.(https://hex-works.com/)
![image](https://github.com/STC-STEM/nuttyshell-ctf-2024-writeups/assets/94276358/681a36b4-e107-4980-b4b4-d8c2804dbc96)
![image](https://github.com/STC-STEM/nuttyshell-ctf-2024-writeups/assets/94276358/a679dbb3-8fbb-40c4-9fc5-97de96bc9d40)
can be seen that every channel there is a marking
![image](https://github.com/STC-STEM/nuttyshell-ctf-2024-writeups/assets/94276358/e8ea6673-90aa-49d9-b879-66a5930b5899)
at the bottom there is the word flag, after /.mtrk, and a bunch of stuff follows.
I think i have to read that bunch of stuff.
So i ctrl+x them and put them under a channel at the top
after that, i read the resultant .mid file
at that channel, it looks like morse code
![image](https://github.com/STC-STEM/nuttyshell-ctf-2024-writeups/assets/94276358/a672dd88-85d3-4c74-840f-b0ce21b93980)
after decoding, i get PUCTF24{F4NCY_S0M3_TE4?_A5DFEB0}

