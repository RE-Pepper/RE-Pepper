

# File os\_KConfigMemory.h

[**File List**](files.md) **>** [**CtrSDK**](dir_a581c965070d8303a3ac233c6039c11a.md) **>** [**include**](dir_af9254bf4d22366cfccd04cbaa9622aa.md) **>** [**nn**](dir_a185e92459882a1d3c4a0e5724303e75.md) **>** [**os**](dir_53922fdb85244c81a863dd6ad700ec31.md) **>** [**os\_KConfigMemory.h**](os___k_config_memory_8h.md)

[Go to the documentation of this file](os___k_config_memory_8h.md)


```C++
#pragma once
#include "Types.h"

/* Info for this header file has been generated from https://www.3dbrew.org/wiki/Configuration_Memory */
namespace nn {
namespace os {

    /* ARM11 Kernel Configuration Memory - r-- */
    struct KConfigMemory {
        u8 kVersionUnk;
        u8 kVersionRev;
        u8 kVersionMinor;
        u8 kVersionMajor;
        u32 updateFlag;
        u64 nsTid;
        u32 sysCoreVer;
        u8 envInfo;
        u8 unitInfo;
        u8 prevFirm;
        u8 pad1;
        u32 kCtrSdkVer;
        u32 pad2;
        u32 firmLaunchFlags;
        u32 pad3[3];
        u32 appMemType;
        u32 pad4[3];
        u32 appMemAlloc;
        u32 sysMemAlloc;
        u32 baseMemAlloc;
        u32 pad5[5];
        u8 firmVerUnk;
        u8 firmVerRev;
        u8 firmVerMinor;
        u8 firmVerMajor;
        u32 firmSysCoreVer;
        u32 firmCtrSdkVer;
    };

    inline const KConfigMemory *GetKConfigMemory() {
        return reinterpret_cast<KConfigMemory*>(0x1FF80000);
    }

    #pragma no_inline
    u32 GetAppMemorySize() {
        return GetKConfigMemory()->appMemAlloc;
    }
}
}
```


