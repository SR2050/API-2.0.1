api factorial(n)
    if n == 0 then
        return 1
    else
        return n * factorial(n - 1)
    end
end

let result = factorial(5)

impress(result)
