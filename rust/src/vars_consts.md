# Variables and Constants

## Variable Assignment and Referencing

Variables and references are immutable by default. Variable assignment is
achieved by using the `let` keyword. Should you want a mutable
variable you add the `mut` keyword after `let` but before
the variable name. For example:

```rust
let steadfast = true; //immutable

let mut wavering = true; //mutable
wavering = false;

```

Similarly, references are also immutable by default.

```rust
&wavering // immutable

&mut wavering // mutable
```

It is important in Rust to be judicious in the use of mutability. There are
trade-offs to be made with respect to efficiency, debugging, code legibility, and
maintenance. For example, it might be more efficient to modify a large data
structure in place than creating a new updated copy. On the other hand, if the
data is small enough, it would probably be easier to read by creating new
instances of the data structure that also avoids any unwanted mutability.

### Specifying type

A specific type for a variable can be denoted using the `:`
syntax. For example declaring a unsigned 32-bit integer looks something like
this:

```rust
let x: u32 = 1
```

## Variable Shadowing

Rust uses type inference to determine --- at compile time --- what the types
are of the variables. However, it also allows variable names to be reused even
in the same scope and "shadow" the other variable declarations and
assignments. This is useful when doing type conversions without having to
declare additional variable names.

## Type Conversions

### String to Unsigned 32-bit Integer

Strings in Rust feature a `parse` function to convert strings to
whatever the inferred type is. However, parsing strings can also result in
failure and as such you should use the `expect` method on the
`parse` method.

It is also wise to use `trim()` on strings to ensure that leading and
trailing whitespace is removed before attempting to parse an integer.

For example converting the string `five = "5"` to an integer you can
do the following.

```rust
let five: u32 = five.trim().parse()
    .expect("Failed to parse string!")
```

## Constants

While variables in Rust are immutable by default, there are also constants
which are always immutable. Furthermore, constants have the following
constraints:

- declared using `const` keyword
- type must be annotated
- may only be set to a constant expression

That last point means that the constant cannot be assigned to the result of a
function or another any value that is computed at runtime.

Rust convention is to name constants with all uppercase and underscores between
words.

```rust
const MAX_POINTS: u32 = 100_000;
```

### Scope \and Shadowing

Constants are valid for the entire time the program runs within their declared
scope. Furthermore, constants may be declared in the global scope so as to be
accessible to the entirety of the Rust program.

That also means that a constant, once declared, cannot be shadowed by another
variable. Instead the compiler will complain that the variable name was instead
interpreted as a constant pattern. This does not apply to shadowing a constant
with a constant in a different scope as can be seen below.

```rust
const MAX_POINTS: u32 = 100_000;

fn main() {
    
    const MAX_POINTS: u32 = 200_000;

    println!("{}", MAX_POINTS);

}
```

The following code will print `200000` although the compiler will warn
that the outer scoped `MAX_POINTS` is unused.

It should be noted however, that constants are used in the scope that they are
declared in. For example, if we had a function that makes use of our constant
and then call in in a scope where the constant was shadowed, it will use the
unshadowed constant. See the example below.

```rust
const MAX_POINTS: u32 = 100_000;

fn main() {
    
    const MAX_POINTS: u32 = 200_000;

    println!("{}", MAX_POINTS);

    print_points();
}

fn print_points() {

    println!("{}", MAX_POINTS);

}
```

The following will first print `200000` followed by
`100000` since the function `print_points` makes use of the
globally scoped constant and not the locally scoped constant.

