

# File alSeFunction.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Se**](dir_9733ad7fb9946fedc1136e5aa2a73b9a.md) **>** [**alSeFunction.h**](al_se_function_8h.md)

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


