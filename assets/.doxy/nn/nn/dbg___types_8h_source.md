

# File dbg\_Types.h

[**File List**](files.md) **>** [**CtrSDK**](dir_a581c965070d8303a3ac233c6039c11a.md) **>** [**include**](dir_af9254bf4d22366cfccd04cbaa9622aa.md) **>** [**nn**](dir_a185e92459882a1d3c4a0e5724303e75.md) **>** [**dbg**](dir_8674e25a187048eae8b9b07d931da2b2.md) **>** [**dbg\_Types.h**](dbg___types_8h.md)

[Go to the documentation of this file](dbg___types_8h.md)


```C++
#pragma once

namespace nn {
namespace dbg {

    enum BreakReason {
        BreakReason_PANIC,
        BreakReason_ASSERT,
        BreakReason_USER,
        BreakReason_LOAD_RO,
        BreakReason_UNLOAD_RO,
    };

} // namespace dbg
} // namespace nn
```


