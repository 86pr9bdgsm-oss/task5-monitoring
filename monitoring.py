def monitor_ctr(previous_ctr, current_ctr, threshold=0.2):
    drop = (previous_ctr - current_ctr) / previous_ctr

    if drop > threshold:
        print("ALERT: CTR dropped significantly!")
    else:
        print("CTR is stable.")


if __name__ == "__main__":
    previous_ctr = 0.12
    current_ctr = 0.08
    monitor_ctr(previous_ctr, current_ctr)