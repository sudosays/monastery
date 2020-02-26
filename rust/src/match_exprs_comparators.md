# Match expressions and comparators}
Every type that can be compared has a `.cmp()` method that returns a
`std::cmp::Ordering` type. This can be one of three variants:
`Ordering::Less`, `Ordering::Greater`, and
`Ordering::Equal`.

A match expression is similar to a switch statement in other languages and will
check the value against its _arms_ and then execute the appropriate code.
For example:

```rust
match numbera.cmp(&numberb) {
    Ordering::Less => println!(``Number A < Number B''),
    Ordering::Greater => println!(``Number A > Number B''),
    Ordering::Equal => println!(``Number A = Number B''),
}
```
However, match expressions are much more powerful than simple switch statements
and can be used to ensure that you are handling a whole variety of situations
that can arise.

## Error handling with match expressions}

Since the `Result` type is an enum containing `Ok` and
`Err` types, you can use a `match` expression to replace an
`expect` method and do more fine-grained processing of errors. In
this case the arms of the expression become the types `Ok` and
`Err`.

For example, trying to parse a string into an integer you can use the
following:

```rust
let five = "a 5"
let five: u32 = match five.trim().parse() {
    Ok(num) => num,
    Err(_) => { //do something },
}
```

The underscore is a wildcard that will match any value, but not bind to it
(meaning you won't be able to use the underscore in an expression).


