

# File alMapObjActor.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**MapObj**](dir_21193efef39fb5d321859f2312a01914.md) **>** [**alMapObjActor.h**](al_map_obj_actor_8h.md)

[Go to the documentation of this file](al_map_obj_actor_8h.md)


```C++
#pragma once

#include <LiveActor/alLiveActor.h>
#include <prim/seadSafeString.h>

namespace al
{

class MapObjActor : public LiveActor
{
public:
        MapObjActor( const sead::SafeString& name );
};

} // namespace al
```


