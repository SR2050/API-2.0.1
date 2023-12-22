
api calculetor()
        display("----------------------------")
        display("         Normal Calculetor  ")
        display("----------------------------")
        display("Enter Number Here: ")
        let n =scanf_int()
        display("Enter Number Here: ")
        let m = scanf_int()

        display("Select A Operator ->['+','-','*','/'] :")
        let op = scanf()



        if op == "+" then
                impress(n + m)
        else if op == "-" then
                impress(n - m)
        else if op == "*" then
                impress(n * m)
        else if op == "/" then
                impress(n/m)
        else
                impress("Math Error..!")
        end
end
calculetor()