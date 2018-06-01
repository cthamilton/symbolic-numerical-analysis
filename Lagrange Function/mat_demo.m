x = [0 1 2];
y = [3 5 1];

f = lagrange_fn(x, y, "fun");
s = lagrange_fn(x, y, "sym", 7);
l = lagrange_fn(x, y, "lat", 7);