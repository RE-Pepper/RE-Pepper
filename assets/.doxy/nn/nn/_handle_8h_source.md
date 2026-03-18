

# File Handle.h

[**File List**](files.md) **>** [**CtrSDK**](dir_a581c965070d8303a3ac233c6039c11a.md) **>** [**include**](dir_af9254bf4d22366cfccd04cbaa9622aa.md) **>** [**nn**](dir_a185e92459882a1d3c4a0e5724303e75.md) **>** [**Handle.h**](_handle_8h.md)

[Go to the documentation of this file](_handle_8h.md)


```C++
#pragma once

#include <nn/types.h>

namespace nn {

struct Handle {
    u32 m_Handle;
    Handle()
        : m_Handle(0)
    {
    }
};

} // namespace nn
```


