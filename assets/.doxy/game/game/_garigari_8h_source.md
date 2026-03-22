

# File Garigari.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**MapObj**](dir_2096800ae80e9b320e335490a6d8aa70.md) **>** [**Garigari.h**](_garigari_8h.md)

[Go to the documentation of this file](_garigari_8h.md)


```C++
#pragma once

#include <MapObj/alMapObjActor.h>

class Garigari : public al::MapObjActor
{
private:
        float _60;
        int   mSpeed;
        int   _68;
        int   _6C;
        int   _70;
        int   _74;

public:
        virtual void init( const al::ActorInitInfo& info );
        virtual void attackSensor( al::HitSensor* me, al::HitSensor* other );
        virtual bool receiveMsg( u32 msg, al::HitSensor* other, al::HitSensor* me );
        virtual void control();

public:
        Garigari( const sead::SafeString& name );
};
```


