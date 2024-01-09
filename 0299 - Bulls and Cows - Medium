class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        guess = list(guess)
        secret = list(secret)
        bulls = 0
        cows = 0
        new_guess = []
        new_secret = []

        for i in range(len(guess)-1, -1, -1):
            if guess[i] == secret[i]:
                bulls += 1
            else:
                new_guess.append(guess[i])
                new_secret.append(secret[i])
        for i in range(len(new_guess)-1, -1, -1):
            if new_guess[i] in new_secret:
                cows += 1
                new_secret.remove(new_guess[i])
                new_guess.remove(new_guess[i])

        return f"{bulls}A{cows}B"
