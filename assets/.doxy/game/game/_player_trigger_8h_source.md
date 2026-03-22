

# File PlayerTrigger.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**Player**](dir_c3d399ad73eabae4c9209488b7fe7035.md) **>** [**PlayerTrigger.h**](_player_trigger_8h.md)

[Go to the documentation of this file](_player_trigger_8h.md)


```C++
#pragma once

class PlayerTrigger
{
private:
        u32 mSensorTrigger;
        u32 mCollisionTrigger;

public:
        enum ESensorTrigger
        {
        };

        enum ECollisionTrigger
        {
        };

public:
        void set( PlayerTrigger::ESensorTrigger trigger );
        void set( PlayerTrigger::ECollisionTrigger trigger );
        bool isOn( PlayerTrigger::ESensorTrigger trigger ) const;
        bool isOn( PlayerTrigger::ECollisionTrigger trigger ) const;
        void clearSensorTrigger();
        void clearCollisionTrigger();

public:
        PlayerTrigger();
};
```


