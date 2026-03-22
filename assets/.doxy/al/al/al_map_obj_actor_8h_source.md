

# File alMapObjActor.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**MapObj**](dir_186204ddd6c634d60c0262be70e5b53c.md) **>** [**alMapObjActor.h**](al_map_obj_actor_8h.md)

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


