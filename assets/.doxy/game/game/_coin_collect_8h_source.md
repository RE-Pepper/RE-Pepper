

# File CoinCollect.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**MapObj**](dir_2096800ae80e9b320e335490a6d8aa70.md) **>** [**CoinCollect.h**](_coin_collect_8h.md)

[Go to the documentation of this file](_coin_collect_8h.md)


```C++
#pragma once

#include <MapObj/alMapObjActor.h>

class Coin : public al::MapObjActor
{
private:
        void*          _60;
        void*          _64;
        sead::Vector3f _68;
        sead::Quatf    _74;
        int            mCoinNo;
        float          _88;
        float          _8C;
        sead::Vector3f _90;
        bool           _9C;
        sead::Vector3f _A0;
        sead::Vector3f _AC;

public:
        virtual void init( const al::ActorInitInfo& info );
        virtual void initAfterPlacement();
        virtual void makeActorAppeared();
        virtual bool receiveMsg( u32 msg, al::HitSensor* other, al::HitSensor* me );

public:
        Coin( const sead::SafeString& name );
};
```


