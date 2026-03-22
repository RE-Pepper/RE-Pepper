

# File PlayerTrigger.cpp

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**src**](dir_47d28cd3eb946f860e1fe0f4e720b9c2.md) **>** [**Player**](dir_9f791c72b7e31512581b67600bde1506.md) **>** [**PlayerTrigger.cpp**](_player_trigger_8cpp.md)

[Go to the documentation of this file](_player_trigger_8cpp.md)


```C++
#include "Player/PlayerTrigger.h"

PlayerTrigger::PlayerTrigger() : mSensorTrigger( 0 ), mCollisionTrigger( 0 )
{
}

void PlayerTrigger::set( PlayerTrigger::ESensorTrigger trigger )
{
        mSensorTrigger |= 1 << trigger;
}

void PlayerTrigger::set( PlayerTrigger::ECollisionTrigger trigger )
{
        mCollisionTrigger |= 1 << trigger;
}

bool PlayerTrigger::isOn( PlayerTrigger::ESensorTrigger trigger ) const
{
        return ( mSensorTrigger & ( 1 << trigger ) ) != 0;
}

bool PlayerTrigger::isOn( PlayerTrigger::ECollisionTrigger trigger ) const
{
        return ( mCollisionTrigger & ( 1 << trigger ) ) != 0;
}

void PlayerTrigger::clearSensorTrigger()
{
        mSensorTrigger = 0;
}

void PlayerTrigger::clearCollisionTrigger()
{
        mCollisionTrigger = 0;
}
```


