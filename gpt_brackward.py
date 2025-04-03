learning_rate = 0.0001  # Lower learning rate
max_iterations = 10000  # Prevent infinite loops
tolerance = 1e-6  # Smaller stopping condition
momentum = 0.9  # Momentum factor for smoother convergence
clip_value = 1e4  # Gradient clipping to prevent divergence

def f(x, a, b, c):
    return a * x ** 2 + b * x + c

def error_pente(a, b, c):
    points = [(2, 11), (5, 13), (7, 16)]
    n = len(points)

    # Initialize velocity for momentum
    v_a, v_b, v_c = 0, 0, 0

    for i in range(max_iterations):
        gradient_a = sum(2 * (f(x, a, b, c) - y) * (x ** 2) for x, y in points) / n
        gradient_b = sum(2 * (f(x, a, b, c) - y) * x for x, y in points) / n
        gradient_c = sum(2 * (f(x, a, b, c) - y) for x, y in points) / n

        # Gradient clipping to prevent explosion
        gradient_a = max(-clip_value, min(clip_value, gradient_a))
        gradient_b = max(-clip_value, min(clip_value, gradient_b))
        gradient_c = max(-clip_value, min(clip_value, gradient_c))

        # Debugging step
        print(f"Iteration {i}: a={a:.5f}, b={b:.5f}, c={c:.5f}, grad_a={gradient_a:.5f}, grad_b={gradient_b:.5f}, grad_c={gradient_c:.5f}")

        # Stop if gradients are NaN or infinite
        if any(map(lambda g: not (g == g and g != float('inf') and g != float('-inf')), [gradient_a, gradient_b, gradient_c])):
            print("NaN or Infinite value detected, stopping early.")
            break

        # Stopping condition
        if abs(gradient_a) + abs(gradient_b) + abs(gradient_c) < tolerance:
            break

        # Apply momentum update
        v_a = momentum * v_a - learning_rate * gradient_a
        v_b = momentum * v_b - learning_rate * gradient_b
        v_c = momentum * v_c - learning_rate * gradient_c

        a += v_a
        b += v_b
        c += v_c

    return a, b, c

# Initial guesses
best_a, best_b, best_c = error_pente(1.0, 1.0, 1.0)
print("Final values:", best_a, best_b, best_c)
