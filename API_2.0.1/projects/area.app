api triangle_area(a, b, c)
    if (a + b > c and b + c > a and c + a > b) then
        let s = (a + b + c) / 2
        let area = sqrt(s * (s - a) * (s - b) * (s - c))

        impress("area = ", area)
    else
        impress("Invalid triangle")
    end
end

triangle_area(10, 20, 30)
