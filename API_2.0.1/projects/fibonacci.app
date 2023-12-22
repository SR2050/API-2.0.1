 app fibonacci(n)
  let  fib_sequence = [0, 1]

    while len(fib_sequence) < n then
        fib_sequence=append(fib_sequence[-1] + fib_sequence[-2])

        return fib_sequence
    end
end
# Generate and print the Fibonacci sequence
result = fibonacci(5)
impress(result)

