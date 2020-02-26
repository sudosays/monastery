# Result types and Error handling

Rust uses Result types to encode error handling information. The Result type
itself is an enum with two variants Ok, and Err. Using Result types effectively
forces you to write error handling code as the compiler will complain at you
with warnings.

For a specific example, the `std::io::stdin().read_line(&mut <arg>)`
returns a Result value of a specific type `io::Result`. These Result
types may have methods defined on them and in this particular case the
`.expect(<String>)` method will print the given string argument if
the Result type is of an Err variant.

