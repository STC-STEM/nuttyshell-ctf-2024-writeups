We are given an encrypted flag: `W2J1M9b{Hslh_phj1h_l01_Slnpv_5PPP_Jyv00pun_1ol_Y2ipjvu_9ggkafemlcdgalgkf9jhkhehdcecjcac}`

It is known that the flag has a format of `PUCTF24{...}`, we can compare the ASCII code points of the flag and the encrypted flag

| i | flag[i] | encrypted[i] | offset |
|---|---------|--------------|--------|
| 0 | P (80)  | W (87)       | 7      |
| 1 | U (85)  | 2 (50)       | -35    |
| 2 | C (67)  | J (74)       | 7      |
| 3 | T (84)  | 1 (49)       | -35    |
| 4 | F (70)  | M (77)       | 7      |
| 5 | 2 (50)  | 9 (57)       | 7      |
| 6 | 4 (52)  | b (98)       | -46    |

It became apparent that a rotational cipher (Caesar Cipher) is used.

Trying the ROT19 cipher gives us the following result: `P2C1F9u{Alea_iac1a_e01_Legio_5III_Cro00ing_1he_R2bicon_9zzdtyxfevwztezdy9cadaxawvxvcvtv}`.

Intelligible, but it seems like some characters are slightly off. Before spending loads of time to figure out which letter is missing from the character set of the cipher, we have decided to search for hints from the challenge title. Searching 'The dice is cast':

> Ālea iacta est (The dice is cast) is a variation of a Latin phrase attributed by Suetonius to Julius Caesar on 10 January 49 BCE, as he led his army across the Rubicon river in Northern Italy.

We also noticed that the 32-character string is the MD5 hash of the first part of the flag. Therefore, we guessed that the flag is
`PUCTF24{Alea_iacta_est_Legio_XIII_Crossing_the_Rubicon_299d387fe5693e9d82cada7a6575c535}`.
Note that the positions of repeating characters in the hash is same as that in the cipher text.

And the flag is correct!

Note: If we weren't that lucky and guessed the flag correctly, we would have figured out the missing character by considering the offsets that are different from others. e.g.,

- Most of the characters are offset by 7. Clearly the cipher works by shifting 7 letters rightward.
- `U -> ... -> Z -> 1 -> 2` have 7 shifts.
- `4 -> ... -> 9 -> a -> b` also have 7 shifts.
- With some trials and errors we can figure out the character set