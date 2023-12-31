from MM1 import MM1QueueSimulator

# Simulate M/M/1 Queue for different values of rho
rhos = [0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85, 0.95]
average_packet_counts = []

# Simulation time
T = 1000
arrival_rate = 200.0
transmission_rate = 1000000
average_packet_length = 2000
# Infinite queue
K = None

print("MM1 Plot P(idle) vs. rho")

for rho in rhos:
    # Compute arrival rate for given rho
    arrival_rate = rho * transmission_rate / average_packet_length
    simulator = MM1QueueSimulator(T, arrival_rate, average_packet_length, transmission_rate, K)
    # Get Pidle from current simulator
    p_idle = simulator.run_simulation()[1]
    average_packet_counts.append(p_idle)
    print(f"rho = {rho}, P(idle) = {p_idle}")

if __name__ == "__main__":
    # Plot P(idle) vs. rho
    import matplotlib.pyplot as plt
    plt.plot(rhos, average_packet_counts)
    plt.xlabel('rho')
    plt.ylabel('P(idle)')
    plt.title('P(idle) in M/M/1 Queue')
    plt.show()
