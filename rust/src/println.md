# The `println!` Macro

The `println!` macro allows you to use placeholders in the form of
curly braces within the string. These placeholders then get replaced with the
value of the supplied variables in the order in which they appear. For example:

```rust
println!("This is placeholder {}, {}", 1, 2);
// outputs "This is placeholder 1, 2"
```

## Marco not function

The `println!` is not a function but a macro. Macros are specified with an
exclamation point "!".
