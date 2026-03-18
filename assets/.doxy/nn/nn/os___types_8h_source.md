

# File os\_Types.h

[**File List**](files.md) **>** [**CtrSDK**](dir_a581c965070d8303a3ac233c6039c11a.md) **>** [**include**](dir_af9254bf4d22366cfccd04cbaa9622aa.md) **>** [**nn**](dir_a185e92459882a1d3c4a0e5724303e75.md) **>** [**os**](dir_53922fdb85244c81a863dd6ad700ec31.md) **>** [**os\_Types.h**](os___types_8h.md)

[Go to the documentation of this file](os___types_8h.md)


```C++
#pragma once

namespace nn {
namespace os {

    enum ArbitrationType {
        ArbitrationType_SIGNAL = 0, 
        ArbitrationType_WAIT_IF_LESS_THAN = 1, 
        ArbitrationType_DECREMENT_AND_WAIT_IF_LESS_THAN = 2, 
        ArbitrationType_WAIT_IF_LESS_THAN_TIMEOUT = 3, 
        ArbitrationType_DECREMENT_AND_WAIT_IF_LESS_THAN_TIMEOUT = 4, 
    };

    enum ResetType {
        ResetType_ONESHOT = 0, 
        ResetType_STICKY = 1, 
        ResetType_PULSE = 2 
    };

} // namespace os
} // namespace nn
```


