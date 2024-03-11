class Solution:
    def customSortString(self, order: str, s: str) -> str:

        #create a dictionary to keep the 'order' order
        dict = {char: i for i, char in enumerate(order)}

        #create a custom order
        def new_order(char):
            return dict.get(char, float('inf'))

        #use sorted() function to sort 's' by a custom key
        sortS = sorted(s, key=new_order)

        return ''.join(sortS)
