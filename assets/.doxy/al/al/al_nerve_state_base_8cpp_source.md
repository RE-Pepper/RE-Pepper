

# File alNerveStateBase.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**backup**](dir_e950b0fd36f81e11534198fd855feab3.md) **>** [**src**](dir_6f98f21a57298fb921e921b3faae2f7d.md) **>** [**Nerve**](dir_8d6afa48c7513136f8b448a486977ca0.md) **>** [**alNerveStateBase.cpp**](al_nerve_state_base_8cpp.md)

[Go to the documentation of this file](al_nerve_state_base_8cpp.md)


```C++
#include <Nerve/alNerveStateBase.h>

namespace al
{

NerveStateBase::NerveStateBase( const char* name ) : NerveExecutor( name ), mIsDead( true )
{
}

void NerveStateBase::init()
{
}

void NerveStateBase::appear()
{
        mIsDead = false;
}

void NerveStateBase::kill()
{
        mIsDead = true;
}

bool NerveStateBase::update()
{
        updateNerve();
        if ( !mIsDead )
        {
                control();
                return false;
        }
        return true;
}

void NerveStateBase::control()
{
}

} // namespace al
```


