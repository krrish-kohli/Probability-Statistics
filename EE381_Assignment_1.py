import numpy as np

# Function to get the exact answer using simple math
def exact_probability():
    total_outcomes = 5 ** 3       # 5 cans for each of 3 balls
    good_outcomes = 5 * 4 * 3     # each ball must go in a different can
    return good_outcomes / total_outcomes


# Function to simulate the experiment many times
def simulate(n_trials=1000000):
    range_ = np.random.default_rng()  # random number generator
    success = 0

    for _ in range(n_trials):
        # Toss 3 balls into 5 cans (numbers 0–4)
        balls = range_.integers(0, 5, 3)
        if len(set(balls)) == 3:   # check if all landed in different cans
            success += 1

    probability = success / n_trials
    return probability


# Main program
def main():
    exact = exact_probability()
    estimate = simulate(1000000)

    print("Exact probability:", round(exact, 4))
    print("Estimated probability from simulation:", round(estimate, 4))


# Run the program
if __name__ == "__main__":
    main()
