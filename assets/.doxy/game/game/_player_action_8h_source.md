

# File PlayerAction.h

[**File List**](files.md) **>** [**backup**](dir_70d69dea5d1e5ae3147e3b96d60a7ce1.md) **>** [**include**](dir_e05fb92cc301336445c4f62f6c4f58b8.md) **>** [**Player**](dir_c3d399ad73eabae4c9209488b7fe7035.md) **>** [**PlayerAction.h**](_player_action_8h.md)

[Go to the documentation of this file](_player_action_8h.md)


```C++
#pragma once

#include <prim/seadRuntimeTypeInfo.h>

class PlayerAction
{
        SEAD_RTTI_BASE( PlayerAction )
public:
        virtual ~PlayerAction();

        virtual void move();
        virtual void update();
        virtual void setup();
        virtual void teardown();
};
```


