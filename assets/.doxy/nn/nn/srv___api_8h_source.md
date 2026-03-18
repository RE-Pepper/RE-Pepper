

# File srv\_Api.h

[**File List**](files.md) **>** [**CtrSDK**](dir_a581c965070d8303a3ac233c6039c11a.md) **>** [**include**](dir_af9254bf4d22366cfccd04cbaa9622aa.md) **>** [**nn**](dir_a185e92459882a1d3c4a0e5724303e75.md) **>** [**srv**](dir_2f77558cefdcdd091fbae5ab2d60e6ab.md) **>** [**srv\_Api.h**](srv___api_8h.md)

[Go to the documentation of this file](srv___api_8h.md)


```C++
#pragma once

#include <nn/Handle.h>
#include <nn/Result.h>

namespace nn {
namespace srv {

    Result Initialize();
    Result GetServiceHandle(Handle* out, const char* service, s32, u32);

} // namespace srv
} // namespace nn
```


