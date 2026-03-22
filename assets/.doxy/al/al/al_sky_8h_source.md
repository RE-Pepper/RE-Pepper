

# File alSky.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Npc**](dir_43489f5cd47c3c88012e1bbb9faf90cc.md) **>** [**alSky.h**](al_sky_8h.md)

[Go to the documentation of this file](al_sky_8h.md)


```C++
#pragma once

#include <MapObj/alMapObjActor.h>

namespace al
{

class Sky : public MapObjActor
{
private:
        const sead::Vector3f* mCameraTransPtr;

public:
        virtual void init( const ActorInitInfo& info );
        virtual void calcAnim();

public:
        Sky( const char* name );
};

} // namespace al
```


