import time

# Optional: ANSI color codes for terminal output
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def start_timer():
    """Start a timer and return the start time."""
    return time.time()

def stop_timer(start_time):
    """Return the elapsed time in seconds."""
    return round(time.time() - start_time, 2)

def print_results(results, elapsed_time):
    """Nicely prints the search results."""
    if results:
        print(f"\n{GREEN}✅ Found {len(results)} file(s) in {elapsed_time} seconds!{RESET}\n")
        for path in results:
            print(f"➡️  {path}")
    else:
        print(f"\n{RED}❌ File not found after {elapsed_time} seconds.{RESET}")
