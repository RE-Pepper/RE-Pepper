

# File alFixMapParts.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**MapObj**](dir_21193efef39fb5d321859f2312a01914.md) **>** [**alFixMapParts.h**](al_fix_map_parts_8h.md)

[Go to the documentation of this file](al_fix_map_parts_8h.md)


```C++
#pragma once

#include <MapObj/alMapObjActor.h>

namespace al
{

class FixMapParts : public MapObjActor
{
public:
        FixMapParts( const sead::SafeString& name );

        virtual void init( const ActorInitInfo& info );
        virtual void appear();
};

} // namespace al
```


