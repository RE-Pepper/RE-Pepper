

# File fs\_UserFileSystem.h

[**File List**](files.md) **>** [**CTR**](dir_5853bd49094b28a7d349f2c46e9e7b6c.md) **>** [**MPCore**](dir_0282a2f8222a067606e59c7197458110.md) **>** [**detail**](dir_3410765bedc74f99235d87f94afe527b.md) **>** [**fs\_UserFileSystem.h**](fs___user_file_system_8h.md)

[Go to the documentation of this file](fs___user_file_system_8h.md)


```C++
#pragma once

#include <nn/Handle.h>

namespace nn {
namespace fs {
    namespace CTR {
        namespace MPCore {
            namespace detail {
                class UserFileSystem {
                public:
                    static void Initialize(Handle handle);
                };
            } // namespace detail
        } // namespace MPCore
    } // namespace CTR

    void ForceDisableLatencyEmulation();
} // namespace fs
} // namespace nn
```


