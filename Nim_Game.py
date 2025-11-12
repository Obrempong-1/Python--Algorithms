import random

class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0


print(" Nim Game (LeetCode #292)\n")
print("You can test the algorithm or play a quick interactive game.\n")
print("1. Test algorithm for multiple values")
print("2. Play against the computer\n")

choice = input("Choose (1 or 2): ").strip()

if choice == "1":
    solver = Solution()
    for i in range(1, 21):
        result = solver.canWinNim(i)
        print(f"{i} stones → {'Win' if result else 'Lose'}")

elif choice == "2":
    n = random.randint(10, 30)
    print(f"\nThere are {n} stones in the pile.")
    print("You and the computer take turns removing 1–3 stones.")
    print("Whoever removes the last stone wins!\n")

    player_turn = True

    while n > 0:
        if player_turn:
            try:
                take = int(input("Your turn! Take 1–3 stones: "))
                if take < 1 or take > 3 or take > n:
                    print("Invalid move. Try again.")
                    continue
            except ValueError:
                print("Please enter a valid number.")
                continue
            n -= take
            print(f"You took {take}. Stones left: {n}")
            if n == 0:
                print(" You win!")
                break
        else:
            take = n % 4 if n % 4 != 0 else random.randint(1, 3)
            n -= take
            print(f"\n Computer takes {take}. Stones left: {n}")
            if n == 0:
                print(" Computer wins!")
                break
        player_turn = not player_turn
else:
    print("Invalid choice. Exiting.")


''' This program implements the classic Nim Game and determines whether a player can win.

1. The game starts with a random number of stones (between 10–30).
2. Each player can remove 1, 2, or 3 stones per turn.
3. The player who removes the last stone wins.
4. The computer plays optimally using the rule:
   - If the number of stones (n) is not a multiple of 4, take (n % 4) stones.
   - Otherwise, take a random number (1–3).
5. The program also includes a LeetCode-style function (canWinNim) 
   which mathematically determines if a player can win given n stones.

Algorithm Type: Mathematical or Game Theory
- Time Complexity: O(1)
Because the winning condition is determined by a single modulus operation (n % 4).
- Space Complexity: O(1)
No extra data structures are used, only variables for count and turns. '''
