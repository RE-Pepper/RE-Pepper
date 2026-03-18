

# File hid\_HidBase.h

[**File List**](files.md) **>** [**CTR**](dir_469c329f832ba112fcb0b93bb5878886.md) **>** [**hid\_HidBase.h**](hid___hid_base_8h.md)

[Go to the documentation of this file](hid___hid_base_8h.md)


```C++
#pragma once
#include "nn/os/os_EventBase.h"

namespace nn {
namespace hid {
namespace CTR {

    class HidBase : nn::os::EventBase {
        void *m_pResource;
    };

} // namespace CTR
} // namespace hid
} // namespace nn
```


