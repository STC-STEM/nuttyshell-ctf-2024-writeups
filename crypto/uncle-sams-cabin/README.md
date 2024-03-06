We are given an encrypted flag: `RIOXW24{Wavznuga_Angwj_mt_loi_Jqa_Fhqczcs_Ywxsh_Gvdwgw,Pw.120_0fqg94m393jof3tu8hg0w5x729s49pfh}`

Comparing the unicode code points of the encrypted flag with `PUCTF24{...}`, we will notice that it isn't a Caesar Cipher. The first thing that came to my mind is Vigenère cipher.

Searching the challenge description 'Come Retribution' further confirmed my idea, as Vigenère Cipher was used to encrypt Confederate secrets during transmission.

![Vigenère Cipher](vigenere.png?raw=true "vigenere.png")

From the table, knowing that `PUCTF` encrypts to `RIOXW`,  we deduced that the first 5 characters of the key is `COMER` - which reminded us of `COMERETRIBUTION`. Using this key on an [online tool](https://cryptii.com/pipes/vigenere-cipher), we decrypted the cipher text and got the flag - `PUCTF24{Shermans_March_to_the_Sea_Special_Field_Orders,No.120_0ffb94e393fdc3fd8ec0f5f729f49bac}`