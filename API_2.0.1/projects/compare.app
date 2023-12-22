api compare_numbers(num1, num2, num3)
    if num1 == num2 == num3 then
        display("All three numbers are equal.")
    else if num1 > num2 and num1 > num3 then
        display("num1 is the largest number.")
    else if num2 > num1 and num2 > num3 then
        display("num2 is the largest number.")
    else if num3 > num1 and num3 > num2 then
       display("num3 is the largest number.")
    else
        display("There are at least two equal largest numbers.")
    end
end

compare_numbers(10, 20, 30)