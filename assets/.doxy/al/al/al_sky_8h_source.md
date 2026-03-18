

# File alSky.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Npc**](dir_e3d165b8bf399078b0d48c0aef5b9296.md) **>** [**alSky.h**](al_sky_8h.md)

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


