

# File srv\_Service.h

[**File List**](files.md) **>** [**CtrSDK**](dir_a581c965070d8303a3ac233c6039c11a.md) **>** [**include**](dir_af9254bf4d22366cfccd04cbaa9622aa.md) **>** [**nn**](dir_a185e92459882a1d3c4a0e5724303e75.md) **>** [**srv**](dir_2f77558cefdcdd091fbae5ab2d60e6ab.md) **>** [**detail**](dir_102dcb73cc6fb1a3136e1728b868f8ae.md) **>** [**srv\_Service.h**](srv___service_8h.md)

[Go to the documentation of this file](srv___service_8h.md)


```C++
#pragma once

#include <nn/Handle.h>
#include <nn/Result.h>

namespace nn {
namespace srv {
    namespace detail {

        class Service {
        public:
            static Result GetServiceHandle(Handle* out, const char* service, s32, u32);
        };

    } // namespace detail
} // namespace srv
} // namespace nn
```


