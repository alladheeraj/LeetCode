class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = 0
        cow = 0
        secret_count = [0] * 10
        guess_count = [0] * 10
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
            else:
                secret_count[int(secret[i])] += 1
                guess_count[int(guess[i])] += 1
                
        for i in range(10):
            cow += min(secret_count[i], guess_count[i])
                
        return f"{bull}A{cow}B"
