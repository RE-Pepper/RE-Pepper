

# File alNerveStateBase.h

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**include**](dir_91c8f731c875b4f3e2ff146851e9524c.md) **>** [**Nerve**](dir_cea16a3cd0068aab539e5f3441822a40.md) **>** [**alNerveStateBase.h**](al_nerve_state_base_8h.md)

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


