# Reading from `stdio`

The standard library contains an io module which can be used to create an
instance of `std::io::Stdin` by calling the function `std::io::stdin()`. This
provides a handler for reading from the terminal input.  Specifically, reading
a line from the terminal input can be done by calling the `read_line(&mut
<arg>)` function on an instance of `std::io::Stdin` where the argument is a
reference to a variable that the line will be read into. Remember that since
the argument needs to be modified to contain the string, it must be explicitly
declared mutable.
