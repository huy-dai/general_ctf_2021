# PicoMini 2022

This is a month-long event ran in January 2022 aimed at beginners wanting to get started in CTF. I wanted to take a crack at the problems to see their difficulty and consider how useful this mini-competition may be for TechSec club members.

## runme.py

Category: General Skills
Points: 5

Run the Python script

Flag: picoCTF{run_s4n1ty_run}

## ncme

Category: General Skills
Points: 10

Run the provided netcat command.

Flag: picoCTF{s4n1ty_c4t}

## convertme.py

Category: General Skills
Points: 15

The Python program ask for a decimal to binary conversion. Interestingly, the file uses an xor key encryption to hide the true value of the text until the user correctly answers the question. This process can be easily reversed, though it is not necessary for this question.

Flag: picoCTF{4ll_y0ur_b4535_722f6b39}

## Codebook

Category: General Skills
Points: 20

Same as last problem but this problem has an added text file.

Flag: picoCTF{c0d3b00k_455157_687087ee}

## fixme1.py

Category: General Skills
Points: 25

The identation was off in the python script.

Flag: picoCTF{1nd3nt1ty_cr1515_79fb5597}

## fixme2.py

Category: General Skills
Points: 25

The equality check needed an extra equal sign = .

Flag: picoCTF{3qu4l1ty_n0t_4551gnm3nt_f6a5aefc}

## PW Crack 1

Category: General Skills
Points: 25

The file was checking for user input equals "60ab"

Flag: picoCTF{545h_r1ng1ng_c26330ca}

## Glitch Cat

Category: General Skills
Points: 30

We just need to evaluate the Python expression

~~~py
res = 'picoCTF{gl17ch_m3_n07_' + chr(0x38) + chr(0x31) + chr(0x31) + chr(0x66) + chr(0x66) + chr(0x66) + chr(0x65) + chr(0x65) + '}'
print(res)
~~~

Flag: picoCTF{gl17ch_m3_n07_811fffee}

