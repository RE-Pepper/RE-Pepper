

# File GhostPlayer.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**Player**](dir_c3d399ad73eabae4c9209488b7fe7035.md) **>** [**GhostPlayer.h**](_ghost_player_8h.md)

[Go to the documentation of this file](_ghost_player_8h.md)


```C++
#pragma once

#include <MapObj/alMapObjActor.h>

class GhostPlayer : public al::MapObjActor
{
private:
        void* _60;
        bool  _64;
        bool  _65;
        bool  _66;
        bool  _67;
        bool  _68;
        bool  _69;
        bool  _6A;
        bool  _6B;
        bool  _6C;
        int   _70;
        int   _74;
        int   _78;

public:
        void exeHide();
        void exeBegin();
        void exeNrv5();

public:
        virtual void init( const al::ActorInitInfo& info );
        virtual void kill();
        virtual void attackSensor( al::HitSensor* me, al::HitSensor* other );
        virtual bool receiveMsg( u32 msg, al::HitSensor* other, al::HitSensor* me );
        virtual void control();

public:
        GhostPlayer( const sead::SafeString& name );
};
```


