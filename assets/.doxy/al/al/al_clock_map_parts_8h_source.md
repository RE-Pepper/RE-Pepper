

# File alClockMapParts.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**MapObj**](dir_186204ddd6c634d60c0262be70e5b53c.md) **>** [**alClockMapParts.h**](al_clock_map_parts_8h.md)

[Go to the documentation of this file](al_clock_map_parts_8h.md)


```C++
#pragma once

#include <MapObj/alMapObjActor.h>

namespace al
{

class ClockMapParts : public MapObjActor
{
private:
        sead::Quatf _60;
        int         _70;
        float       _74;
        int         _78;
        int         _7C;
        int         _80;

public
        void exeStandBy();
        void exeRotateSign();
        void exeRotate();
        void exeWait();

public:
        virtual void init( const ActorInitInfo& info );

public:
        ClockMapParts( const sead::SafeString& name );
};

} // namespace al
```


