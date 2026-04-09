from process_steps import PROCESS_STEPS

def calculate_total_cycle_time():
    return sum(PROCESS_STEPS.values())

if __name__ == "__main__":
    total_time = calculate_total_cycle_time()
    print(f"Total cycle time: {total_time} seconds")
