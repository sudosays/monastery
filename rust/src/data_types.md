# Data Types 

Rust is a statically typed language that is able to infer data types at compile
time. However, sometimes there is ambiguity as to what type should be inferred
and then it is required for the variable to be explicitly annotated with a
datatype. This is particularly true when parsing strings into numerical values
as they can be valid for multiple different types: integer, float, double etc.

## Scalar types

Scalar types, as the name suggests, represent a singular value. Rust has four
primary scalar types:

- integer
- floating-point
- boolean
- character


### Integers

Integers are numbers without a fractional component and Rust allows for a
varying number of integer lengths from 8-bit up to 128-bit or whatever the
architecture standard is (specified with `isize` and
`usize` for signed and unsigned respectively). These integers can
either be signed (allowing for negative numbers) or unsigned (positive numbers
only) by prefixing the integer length with `i` or
`u` respectively. A breakdown on integer lengths and their type
declarations can be found in Table \ref{tab:int_types}.

| Length  | Signed  | Unsigned |
|---------|---------|----------|
| 8-bit   | `i8`    | `u8`     |
| 16-bit  | `i16`   | `u16`    |
| 32-bit  | `i32`   | `u32`    |
| 64-bit  | `i64`   | `u64`    |
| 128-bit | `i128`  | `u128`   |
| arch    | `isize` | `usize`  |

Integer literals can be written in a variety of ways as well as supporting a
type suffix. The exception to this is the byte literal notation which will
always result in a `u8` type. Some examples of the different integer
literals can be found in the table below.

| Number literals  | Example       |
|------------------|---------------|
| Decimal          | `98_222`      |
| Hex              | `0xff`        |
| Octal            | `0o77`        |
| Binary           | `0b1001_1111` |
| Byte (`u8` only) | `b'A'`        |


Integer overflow in Rust is handled a bit strangely. When compiling in debug
mode, Rust will check for integer overflow and panic if it occurs by exiting
with an error. However, if it is compiled in release mode, Rust will instead
use two's complement wrapping to prevent panics. This is still considered
erroneous since the wrapped value might not have the intended value.

### Floating-Point Types

The default floating-point size in Rust is 64 bits. Thus, if it is left to the
compiler to infer a floating-point type it will default to a 64-bit float with
`f64`.  However, you may explicitly specify a 32-bit float
(`f32`) as well. In Rust, a 32-bit float is considered single
precision while a 64-bit float is considered double precision.



## Compound types


