class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        # Convert string into list of words
        words = s.split()

        # If lengths are different, pattern can never match
        if len(pattern) != len(words):
            return False

        # Dictionary for character -> word mapping
        char_to_word = {}

        # Dictionary for word -> character mapping
        # This helps maintain one-to-one relation
        word_to_char = {}

        # Traverse both pattern and words together
        for char, word in zip(pattern, words):

            # If character already has a mapping
            if char in char_to_word:

                # Check if mapped word is same
                if char_to_word[char] != word:
                    return False

            else:
                # Create new mapping
                char_to_word[char] = word

            # If word already has a mapping
            if word in word_to_char:

                # Check if mapped character is same
                if word_to_char[word] != char:
                    return False

            else:
                # Create new mapping
                word_to_char[word] = char

        # If all mappings are correct
        return True