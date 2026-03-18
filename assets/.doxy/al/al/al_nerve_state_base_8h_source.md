

# File alNerveStateBase.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**include**](dir_f7e8efec570a34efc8a6993e55383954.md) **>** [**Nerve**](dir_0d638fa675477dde0733aed9f19ea6f2.md) **>** [**alNerveStateBase.h**](al_nerve_state_base_8h.md)

[Go to the documentation of this file](al_nerve_state_base_8h.md)


```C++
#pragma once

#include <Nerve/alNerveExecutor.h>

namespace al
{

class NerveStateBase : public NerveExecutor
{
private:
        bool mIsDead;

public:
        inline bool isDead() const
        {
                return mIsDead;
        }

public:
        virtual void init();
        virtual void appear();
        virtual void kill();
        virtual bool update();
        virtual void control();

public:
        NerveStateBase( const char* name );
};

} // namespace al
```


