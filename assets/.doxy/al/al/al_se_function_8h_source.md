

# File alSeFunction.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Se**](dir_80eeee9f399bfcc1dc7c8bcc9010f301.md) **>** [**alSeFunction.h**](al_se_function_8h.md)

[Go to the documentation of this file](al_se_function_8h.md)


```C++
#pragma once

#include <prim/seadSafeString.h>

namespace al
{
class IUseAudioKeeper;

void startSe( IUseAudioKeeper* p, const sead::SafeString& name );
bool tryStartSe( IUseAudioKeeper* p, const sead::SafeString& name, int /* ? */ );

} // namespace al
```


