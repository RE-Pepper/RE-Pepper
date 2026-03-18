

# File alClippingActorInfoList.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Clipping**](dir_b42721b03f0382f09cda06110232e739.md) **>** [**alClippingActorInfoList.h**](al_clipping_actor_info_list_8h.md)

[Go to the documentation of this file](al_clipping_actor_info_list_8h.md)


```C++
#pragma once

#include <container/seadPtrArray.h>

namespace al
{

class ClippingActorInfo;

class ClippingActorInfoList
{
private:
        sead::PtrArray<ClippingActorInfo> mInfos;

public:
        ClippingActorInfoList( int );
};

} // namespace al
```


