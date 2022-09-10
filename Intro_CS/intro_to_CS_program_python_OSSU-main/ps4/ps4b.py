# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" 4‘’!@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words("words.txt")

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        
        return self.valid_words[:]

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        
        all_letters_lower = string.ascii_lowercase
        all_letters_upper = string.ascii_uppercase
        all_letters = all_letters_lower + all_letters_upper
        
        list_letters = list()
        for letter in all_letters:
            list_letters.append(letter)
            
        letter_shift = dict()
        for letter in list_letters:
            if letter in all_letters_lower:
                indi = all_letters_lower.find(letter) + shift
                if indi >= 26:
                    indi = indi - 26
                    letter_shift[letter] = all_letters_lower[indi]
                else :
                    letter_shift[letter] = all_letters_lower[indi]
            else :
                indi = all_letters_upper.find(letter) + shift
                if indi >= 26:
                    indi = indi - 26
                    letter_shift[letter] = all_letters_upper[indi]
                else :
                    letter_shift[letter] = all_letters_upper[indi]
                
        return letter_shift

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''

        assert shift >= 0 or shift < 26, "Range: 0 <= shift < 26"
        letter_shift_dict = self.build_shift_dict(shift)
        text_shift =  ""
        
        for letter in self.message_text:
            if letter in " 4‘’!@#$%^&*()-_+={}[]|\:;'<>?,./\"":
                text_shift += letter
            else:
                text_shift += letter_shift_dict[letter] 
        
        return text_shift
        
        
class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        
        Message.__init__(self, text)
        self.shift = shift 
        self.encryption_dict = Message.build_shift_dict(self, shift)
        self.message_text_encrypted = Message.apply_shift(self, shift)


    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        
        return self.encryption_dict.copy()


    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        
        return self.message_text_encrypted


    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        assert shift >= 0 or shift < 26, "Range: 0 <= shift < 26"
        self.__init__(self.get_message_text(), shift)
        
        
class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        
        Message.__init__(self, text)
        
        
    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        
        # Transfer cipher message to list.
        text_list = self.get_message_text().split()
        # Take the first word in that list.
        letter_0 = text_list[0]
        best = 0
        shift = 1
        while True:
            # If the first word is in valid words, then break while loop.
            if is_word(self.valid_words, letter_0) :
                break
            
            # Otherwise, shift 1 character in 1st word until it's content with if condition.
            else :
                best += 1
                # Build a dict when shift 1 char.
                letter_shift_dict = self.build_shift_dict(shift)
                text_shift =  ""
                
                # Add the char shifted to text_shift 
                for letter in letter_0:
                    text_shift += letter_shift_dict[letter] 
                
                # Replace letter_0 with text_shift 
                letter_0 = text_shift
                
        a = self.apply_shift(best)
        return (26-best, a)

if __name__ == '__main__':

#    #Example test case (PlaintextMessage)
#    plaintext = PlaintextMessage('hello', 2)
#    print('Expected Output: jgnnq')
#    print('Actual Output:', plaintext.get_message_text_encrypted())
#
#    #Example test case (CiphertextMessage)
#    ciphertext = CiphertextMessage('jgnnq')
#    print('Expected Output:', (24, 'hello'))
#    print('Actual Output:', ciphertext.decrypt_message())

    #TODO: WRITE YOUR TEST CASES HERE
    
    text_test = "Write two test cases for PlaintextMessage and two test cases for CiphertextMessage in comments under if __name__ == ‘__main__’ . Each test case should display the input, expected output, and actual output. An example can be found in ps4b.py. Then, decode the file story.txt and write the best shift value used to decrypt the story, and unencrypted story in a comment underneath your test cases. "
    p = PlaintextMessage(text_test, 5)
    print(p.get_message_text_encrypted())
    
    text = get_story_string()
    text_2 = "Bwnyj ybt yjxy hfxjx ktw UqfnsyjcyRjxxflj fsi ybt yjxy hfxjx ktw HnumjwyjcyRjxxflj ns htrrjsyx zsijw nk __sfrj__ == ‘__rfns__’ . Jfhm yjxy hfxj xmtzqi inxuqfd ymj nsuzy, jcujhyji tzyuzy, fsi fhyzfq tzyuzy. Fs jcfruqj hfs gj ktzsi ns ux4g.ud. Ymjs, ijhtij ymj knqj xytwd.ycy fsi bwnyj ymj gjxy xmnky afqzj zxji yt ijhwduy ymj xytwd, fsi zsjshwduyji xytwd ns f htrrjsy zsijwsjfym dtzw yjxy hfxjx."
    a = CiphertextMessage(text_2)
    print(a.decrypt_message())

    #TODO: best shift value and unencrypted story 
    
    load_words("words.txt")
    