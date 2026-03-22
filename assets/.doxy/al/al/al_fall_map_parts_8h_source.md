

# File alFallMapParts.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**MapObj**](dir_186204ddd6c634d60c0262be70e5b53c.md) **>** [**alFallMapParts.h**](al_fall_map_parts_8h.md)

[Go to the documentation of this file](al_fall_map_parts_8h.md)


```C++
#pragma once

#include <MapObj/alMapObjActor.h>

namespace al
{

class FallMapParts : public MapObjActor
{
private:
        sead::Vector3f mStartTrans;
        int            mFallFrames;
        bool           _70;

public:
        void exeAppear();
        void exeWait();
        void exeFallSign();
        void exeFall();
        void exeEnd();

public:
        virtual void init( const ActorInitInfo& info );
        virtual bool receiveMsg( u32 msg, HitSensor* other, HitSensor* me );

public:
        FallMapParts( const sead::SafeString& name );
};

} // namespace al
```


