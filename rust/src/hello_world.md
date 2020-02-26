# Hello World

All Rust programs must feature a main function defined by

```rust
fn main() {}
```

## Compilation

Compiling is done using the rustc command and supplying the file containing the
main function

## Cargo

Cargo is a useful tool for project creation and dependency management.

### Starting new projects

Using `cargo new <name>` automatically creates a new dir and
initialises a git repo in it. In the new repo you will find the following:

* Cargo.toml
* .gitignore
* src
    - main.rs

### Cargo.toml

The Cargo.toml file is a configuration file for the project written in Toms
Obvious Minimal Language.

It specifies a Rust package or _crate_.

Cargo expects all code to live within the src directory and all of the
configuration, README, and licenses to live in the top-level directory.

### Building with Cargo

Cargo has three different commands to check, build, and run the Rust code
called `check`, `build`, and `run`.

Cargo check doesn't actually build a runnable executable, but does a quick
check to see if your code will compile. Build on the other hand actually
creates a binary executable and places it in the target/debug folder. Finally,
run builds and then runs the code from the target/debug folder.

Should you wish to release a binary executable, adding the flag
`--release` to the build command will build a release version that
has been optimised thoroughly.

### Adding Dependencies

With the Cargo.toml file you can easily add library crates to your project by
listing them under the "dependencies" section. It is necessary to specify the
crate name as well as providing a _semantic version_ number. For example,
if we were to add the `rand` library we could do it like this:

```
[dependencies]

rand = "0.3.14"
```

When this has been added to the Cargo.toml file, running build, check, or run
will cause cargo to automatically look up the rand library on the crates.io
registry. Then it'll pull the library as well as any of its dependencies before
compiling your crate.


### Updating dependency versions

Running `cargo update` will ignore the Cargo.lock file and attempt to
update the version number of the dependencies. However, it will only update the
patch versions and not the minor versions. For example, given a version 1.2.1
and there are two new versions 1.2.2 and 1.3.0. Cargo will update to 1.2.2 and
not 1.3.0 because it will not automatically bump the minor version number.
Therefore, you need to manually bump any dependencies if you wish to use a
newer minor/major version.

### Cargo.lock file

For people familiar with the Python Pip system, the Cargo.lock file works
similarly to a requirements.txt, but is created and maintained automatically by
cargo. When the crate is first built it will "lock" all of the versions for
the dependencies which ensures that the crate will always build regardless of
the dependencies updating with breaking changes. These versions will not update
unless you explicitly run `cargo update` or manually edit the
versions in the Cargo.toml file.



