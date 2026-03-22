

# File Bubble.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**Enemy**](dir_e35196509c323c9bb4cd921cf1b24d53.md) **>** [**Bubble.h**](_bubble_8h.md)

[Go to the documentation of this file](_bubble_8h.md)


```C++
#pragma once

#include <MapObj/alMapObjActor.h>

class Bubble : public al::MapObjActor
{
private:
        int            _60;
        int            _64;
        void*          _68;
        float          _6C;
        float          _70;
        sead::Vector3f _74;
        sead::Quatf    _80;
        int            _90;

public:
        virtual void init( const al::ActorInitInfo& info );
        virtual void attackSensor( al::HitSensor* me, al::HitSensor* other );
        virtual bool receiveMsg( u32 msg, al::HitSensor* other, al::HitSensor* me );

public:
        Bubble( const sead::SafeString& name );
};
```


