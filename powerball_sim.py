import random
import time

def generate_ticket():
    white_balls = random.sample(range(1, 70), 5)
    red_ball = random.randint(1, 26)
    return white_balls, red_ball

attempts = 0
start_time = time.time()

print("Powerball Jackpot Simulator (Press Ctrl+C to quit)")
print("-----------------------------------------------------")

try:
    while True:
        attempts += 1
        cost = attempts * 2  # $2 per ticket
        elapsed_time = time.time() - start_time

        my_ticket = generate_ticket()
        winning_ticket = generate_ticket()

        if my_ticket == winning_ticket:
            print("JACKPOT! YOU WIN!")
            print(f"Your Ticket: {my_ticket}")
            print(f"Winning Ticket: {winning_ticket}")
            print(f"Attempts: {attempts:,}")
            print(f"Total Cost: ${cost:,}")
            print(f"Time Spent: {elapsed_time:.2f} seconds")
            break

        if attempts % 1000 == 0:
            print(f"Attempts: {attempts:,} | Cost: ${cost:,} | Time: {elapsed_time:.2f}s")

except KeyboardInterrupt:
    print("Stopped by user.")
