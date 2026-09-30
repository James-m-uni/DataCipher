# Welcome to DataCipher

## What does this program allow you to do?
This program allows for the encryption/decryption of data using some unique ciphers, with the pros and cons of each cipher explained in detail.
When interacting with the GUI, you have the option to choose different ciphers. You can then enter your desired text and convert the input.

## What different ciphers are available?

### Time cipher
This cipher uses the current date (Year, month ,day) and creates a unique day key through the operation year * month * day. Each
character in the message to be encoded is converted into the numeric ascii code. The encoded character is then created through 
the operation (daykey - ascii code).

The first number of the cipher indicates how long the first encoded letter(phrase) is. For example

6######

The number after the first phrase is the length of the next phrase

6######6######...

Decryption looks at the markers indicating the length of each phrase to extract them

#### What are the advantages of this cipher?
- Because the current date is used as the key, the message can only be decoded on the same day it was encoded or if the date when the message was encoded is known
