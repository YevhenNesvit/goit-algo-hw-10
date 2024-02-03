from scipy.integrate import quad

from monte_carlo import monte_carlo, func, a, b


small_num_points = 1000
medium_num_points = 10000
large_num_points = 100000

small_quad_result, small_quad_error = quad(func, a, b)
medium_quad_result, medium_quad_error = quad(func, a, b)
large_quad_result, large_quad_error = quad(func, a, b)

small_monte_carlo_result = monte_carlo(func, a, b, small_num_points)
medium_monte_carlo_result = monte_carlo(func, a, b, medium_num_points)
large_monte_carlo_result = monte_carlo(func, a, b, large_num_points)

print(f"{'| Algorithm': <13} | {'Area small num_points': <17} | {'Area medium num_points': <17} | {'Area large num_points': <16}|")
print(f"| {'-'*11} | {'-'*21} | {'-'*22} | {'-'*20} |")
print(f"{'| Monte Carlo': <11} | {small_monte_carlo_result:<21.5f} | {medium_monte_carlo_result:<22.5f} | {large_monte_carlo_result:<21.5f}|")
print(f"{'| Quad': <13} | {small_quad_result:<21.5f} | {medium_quad_result:<22.5f} | {large_quad_result:<21.5f}|")
print(f"| {'-'*11} | {'-'*21} | {'-'*22} | {'-'*20} |")
