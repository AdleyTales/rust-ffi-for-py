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