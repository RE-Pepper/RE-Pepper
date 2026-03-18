

# File alNerveStateBase.cpp

[**File List**](files.md) **>** [**al**](dir_06a57bfe438b90fdc9c94a1df001d5d7.md) **>** [**src**](dir_d8628e97cbd71936d4b5fb3774410590.md) **>** [**Nerve**](dir_32e08f09dddceca537f9274884ee9aa2.md) **>** [**alNerveStateBase.cpp**](al_nerve_state_base_8cpp.md)

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


