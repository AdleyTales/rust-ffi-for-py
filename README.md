# rust-ffi-for-py

### 创建python的一个测试工程
```sh
python -m venv venv 
.\venv\Scripts\activate

 pip install cffi
```

### 创建一个rust的lib项目

```cpp
cargo new --lib pyrust
```

- lib.rs
```cpp

#[no_mangle]
pub extern "C" fn rust_add(x: i32, y: i32) -> i32 {
    x + y
}

```
- Cargo.toml
```cpp
[package]
name = "pyrust"
version = "0.1.0"
edition = "2021"

# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]

[lib]
name = "pyrust"
crate-type = ["cdylib"]
```

- 构建 
```cpp
cargo build --release
```

### python调用ffi
- .so for Linux 
- .dll for Windows
- .dylib for MacOS

```cpp
import cffi

ffi = cffi.FFI()

ffi.cdef(
  """
    int rust_add(int x, int y);
  """
)

C = ffi.dlopen('./pyrust/target/release/pyrust.dll')

res = C.rust_add(12, 5)
print(res)
```

- 

```cpp
python main.py
```
