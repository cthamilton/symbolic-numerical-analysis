function fun_out = lagrange_fn (x_array, y_array, out_type, d)
%Inputs-
%x_array: x-evaluation points
%y_array: function values at evaluation points(associated with the x-value
%of the same index)
%out_type: 3 options - "fun" returns a function, "sym" returns symbolic
%math object, "lat" returns latex code for the function
%d: number of digits desired in printing, only needed for options "sym", "lat"

    %catch easy error
    if length(x_array) ~= length(y_array)
       error('arrays not same length'); 
    end
    
    %find length of array
    n = length(x_array);
    %create x
    x = sym('x');
    %create var
    expr = 0;
    
    for i = 1:n
       %reset term
       term = 1;
       for j = 1:n
           if i ~= j
               %Add factor
               term = term * ((x - x_array(j)) / (x_array(i) - x_array(j))); 
           end
       end
       %addend new term with forrect function value
       expr = expr + y_array(i) * term;
    end
    %simplify expression (effect will probably depend on terms)
    %Presumably will convert to the monomial basis(if you aren't a fan you
    %can comment this out)
    expr = simplify(expr);
    
    %Function case
    if out_type == "fun"
        fun_out = matlabFunction(expr);
        return
    end
    
    %symbolic math object case
    if out_type == "sym"
        %set digits
        digits(d);
        fun_out = simplify(vpa(expr));
        return
    end
    
    
    if out_type == "lat"
        %set digits
        digits(d);
        fun_out = latex(simplify(vpa(expr)));
        return
    end
    
      
    errror('bad type (need to set out_type as fun, sym, or lat)')

    
end
