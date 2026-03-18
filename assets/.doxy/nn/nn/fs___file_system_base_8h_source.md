

# File fs\_FileSystemBase.h

[**File List**](files.md) **>** [**CtrSDK**](dir_a581c965070d8303a3ac233c6039c11a.md) **>** [**include**](dir_af9254bf4d22366cfccd04cbaa9622aa.md) **>** [**nn**](dir_a185e92459882a1d3c4a0e5724303e75.md) **>** [**fs**](dir_ebaeb7c8987009097a9882ca30046667.md) **>** [**detail**](dir_3f787ef9b8b1977a0717b3ad578e7e39.md) **>** [**fs\_FileSystemBase.h**](fs___file_system_base_8h.md)

[Go to the documentation of this file](fs___file_system_base_8h.md)


```C++
#pragma once

namespace nn {
namespace fs {
    namespace detail {

        class FileSystemBase {
            int* _0;

        public:
            FileSystemBase() { }
            FileSystemBase(int* a)
                : _0(a)
            {
            }
        };

        void RegisterGlobalFileSystemBase(FileSystemBase&);

    } // namespace detail
} // namespace fs
} // namespace nn
```


