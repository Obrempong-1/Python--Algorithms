import random


def stone_game(piles):
    """Alice uses the winning strategy:
    - She computes total stones in even-index piles and odd-index piles.
    - She chooses the group with the larger total.
    - During the game she always tries to pick from that group."""

    even_total = sum(piles[i] for i in range(0, len(piles), 2))
    odd_total = sum(piles[i] for i in range(1, len(piles), 2))

    if even_total >= odd_total:
        target = "even"
    else:
        target = "odd"

    print(f"Alice chooses to collect all {target}-indexed piles.\n")

    left = 0
    right = len(piles) - 1

    alice_score = 0
    bob_score = 0
    turn_alice = True

    while left <= right:
        if turn_alice:
            print(f"Alice's turn. Piles left: {piles[left:right + 1]}")

            if target == "even":
                pick_left_is_even = (left % 2 == 0)
                pick_right_is_even = (right % 2 == 0)
            else:
                pick_left_is_even = (left % 2 == 1)
                pick_right_is_even = (right % 2 == 1)

            if pick_left_is_even:
                print(f"Alice takes LEFT pile = {piles[left]}")
                alice_score += piles[left]
                left += 1
            elif pick_right_is_even:
                print(f"Alice takes RIGHT pile = {piles[right]}")
                alice_score += piles[right]
                right -= 1
            else:
                if piles[left] >= piles[right]:
                    print(f"Alice takes LEFT pile = {piles[left]}")
                    alice_score += piles[left]
                    left += 1
                else:
                    print(f"Alice takes RIGHT pile = {piles[right]}")
                    alice_score += piles[right]
                    right -= 1

        else:
            print(f"Bob's turn. Piles left: {piles[left:right + 1]}")
            if piles[left] >= piles[right]:
                print(f"Bob takes LEFT pile = {piles[left]}")
                bob_score += piles[left]
                left += 1
            else:
                print(f"Bob takes RIGHT pile = {piles[right]}")
                bob_score += piles[right]
                right -= 1

        print()
        turn_alice = not turn_alice

    print("\nGAME OVER")
    print(f"Alice's total stones: {alice_score}")
    print(f"Bob's total stones: {bob_score}")

    if alice_score > bob_score:
        print("Alice wins (as she always should)")
    else:
        print("Something unexpected happened — Bob won!")


print("STONE GAME SIMULATION (Alice ALWAYS wins)\n")

n = 6
piles = [random.randint(1, 10) for _ in range(n)]
print("Initial piles:", piles, "\n")

stone_game(piles)

'''  The game has piles of stones in a straight line:
       [5, 3, 4, 5]
 Alice and Bob take turns picking from ONLY the left or right end.

 Alice always goes first.

 The trick: There are ALWAYS an even number of piles.
 Alice can add up stones in:
    even positions: 0, 2, 4...
    odd positions:  1, 3, 5...
One of these groups has more stones.
Alice chooses that group and plays in a way that she ends up taking all the piles from that group.
This is a guaranteed winning strategy.

 In this program:
 We randomly generate piles.
Alice calculates which group (even/odd) is bigger.
She always tries to take stones from that side.
Bob simply takes whatever is bigger on the ends.
Alice always wins.

Algorithm Type: Math / Game Theory

Time Complexity:
O(n) for summing the piles
O(n) for simulating the game
Overall: O(n)

Space Complexity: O(1) extra space  '''
