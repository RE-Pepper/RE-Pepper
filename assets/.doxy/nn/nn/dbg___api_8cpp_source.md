

# File dbg\_Api.cpp

[**File List**](files.md) **>** [**CtrSDK**](dir_a581c965070d8303a3ac233c6039c11a.md) **>** [**sources**](dir_6ad72fc0abbc32b2f59992fddd21f3c1.md) **>** [**dbg**](dir_34384f97eb7d7a0f4fb4ac7db3565ead.md) **>** [**dbg\_Api.cpp**](dbg___api_8cpp.md)

[Go to the documentation of this file](dbg___api_8cpp.md)


```C++
#include <nn/dbg/dbg_Api.h>
#include <nn/svc/svc_Api.h>

namespace nn {
namespace dbg {

    void Break(BreakReason reason)
    {
        nn::svc::Break(reason);
    }

} // namespace dbg
} // namespace nn
```


